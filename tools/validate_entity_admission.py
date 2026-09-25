#!/usr/bin/env python3
"""Validate that every registered THR entity was admitted by a record, not by a mention.

`IDENTITY_MODEL.md` already states `MENTION != ENTITY`. This makes that sentence enforceable
against regression: an entity-first registry grows by mention unless something structural
stops it, and a statement of intent is not a structure. The check is narrow and its scope is
stated rather than implied.

WHAT IT CHECKS

1. every entity carries at least one `record_links` entry;
2. every `record_links` target is a relative path that resolves, symlinks included, to an
   existing file inside this checkout;
3. at least one target is a catalogued record file: the `machine_record` or
   `full_human_record` of an entry in `records/catalog.json`, the record inventory that
   `validate_integrity.py` already checks. A rendered page, a README or a registry file does
   not admit an entity;
4. every entity id referenced by `registry/mentions.json` candidates is registered, so a
   mention cannot conjure a referent by naming one.

WHAT IT DOES NOT CHECK

It does not check that the catalogued record is *about* the entity: record ownership is not
yet modelled, so a pass means "linked to some catalogued record", not "admitted by its own
record". It does not decide whether a record should exist, whether an entity is the right
referent, whether a record's contents are minimal or proportionate, or whether publication
was appropriate. A pass here is a statement about admission route only.

2026-09-23: Codex (THR #73, 5797126626) showed checks 2 and 3 as first written passed a
README, a registry file and an absolute path into another checkout: a suffix test plus
`is_file()` established neither record-bearing nor inside-this-checkout.

    AN_ENTITY_STORE_GROWS_BY_MENTION UNLESS_ADMISSION_IS_A_PRECONDITION
    STRUCTURAL_PASS != APPROPRIATE_TO_HOLD
    A_SUFFIX_IS_NOT_A_RECORD; IS_FILE_IS_NOT_INSIDE
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import validate_integrity as integrity  # noqa: E402  (its public-route rules, not a copy of them)

ROOT = Path(__file__).resolve().parents[1]
UUID = r"[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}"
ENTITY_RE = re.compile(rf"^thr:entity:{UUID}$")
RECORD_FIELDS = ("machine_record", "full_human_record")


def load(root: Path, rel: str) -> dict:
    value = json.loads((root / rel).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{rel}: JSON root must be an object")
    return value


def inside(root: Path, link: str) -> Path | None:
    """The resolved file a link names, or None if it is absolute, escapes the checkout
    (by `..` or by a symlink) or is not a file."""
    if not link or Path(link).is_absolute() or "\\" in link or "\x00" in link:
        return None
    target = (root / link).resolve()
    if not target.is_relative_to(root) or not target.is_file():
        return None
    return target


def catalogued_record_files(root: Path) -> set[Path]:
    """Resolved machine/full record files named by records/catalog.json, mapped to paths with
    validate_integrity's own local_public_path rules and rebased onto `root`."""
    records = load(root, "records/catalog.json").get("records")
    if not isinstance(records, list) or not records:
        raise ValueError("records/catalog.json: records must be a non-empty list")
    files: set[Path] = set()
    for record in records:
        for field in RECORD_FIELDS:
            url = record.get(field) if isinstance(record, dict) else None
            path = integrity.local_public_path(url) if isinstance(url, str) else None
            if path is None:
                continue
            rel = path.relative_to(integrity.ROOT).as_posix()
            target = inside(root, rel)
            if target is not None:
                files.add(target)
    return files


def main(root: Path = ROOT) -> int:
    root = Path(root).resolve()
    errors: list[str] = []
    try:
        entities = load(root, "registry/entities.json").get("entities")
        mentions = load(root, "registry/mentions.json").get("mentions")
        record_files = catalogued_record_files(root)
    except (OSError, ValueError) as exc:
        # A checker that cannot read its inputs must not report a pass.
        print(f"ERROR: entity admission check could not read the registries or the record catalogue: {exc}")
        return 1
    if not isinstance(entities, list) or not isinstance(mentions, list):
        print("ERROR: registry/entities.json or registry/mentions.json has no list to check")
        return 1

    registered = set()
    for index, entity in enumerate(entities):
        eid = entity.get("id") if isinstance(entity, dict) else None
        label = eid or f"entities[{index}]"
        if not isinstance(eid, str) or not ENTITY_RE.match(eid):
            errors.append(f"{label}: entity id is missing or not an opaque thr:entity:<UUID>")
            continue
        registered.add(eid)
        links = entity.get("record_links")
        if not isinstance(links, list) or not links:
            errors.append(f"{eid}: no record_links; an entity must be admitted by a record, "
                          f"not by a mention (IDENTITY_MODEL.md: MENTION != ENTITY)")
            continue
        resolved = {str(link): inside(root, str(link)) for link in links}
        outside = [link for link, target in resolved.items() if target is None]
        if outside:
            errors.append(f"{eid}: record_links target(s) not a file inside this checkout "
                          f"(absolute, escaping or missing): {', '.join(outside)}")
        if not any(target in record_files for target in resolved.values() if target is not None):
            errors.append(f"{eid}: record_links names no catalogued record file (a machine_record or "
                          f"full_human_record in records/catalog.json); a rendered page, README or "
                          f"registry file does not admit an entity")

    for index, mention in enumerate(mentions):
        if not isinstance(mention, dict):
            errors.append(f"mentions[{index}]: mention is not an object")
            continue
        mid = mention.get("id") or f"mentions[{index}]"
        for candidate in mention.get("candidates") or []:
            if not isinstance(candidate, dict):
                errors.append(f"{mid}: candidate is not an object")
                continue
            cid = candidate.get("entity_id")
            if cid is None:
                continue
            if cid not in registered:
                errors.append(f"{mid}: candidate names unregistered entity {cid}; "
                              f"a mention may propose a referent, it may not create one")

    for message in errors:
        print(f"FAIL: {message}")
    if errors:
        print(f"FAIL: {len(errors)} entity-admission problem(s) in {len(entities)} entity "
              f"record(s) and {len(mentions)} mention(s).")
        return 1
    print(f"PASS: {len(entities)} entity record(s) each linked to a catalogued record file inside "
          f"this checkout; {len(mentions)} mention(s) name only registered entities.")
    print("LINKED TO A CATALOGUED RECORD != ADMITTED BY ITS OWN RECORD (ownership not modelled)")
    print("ADMISSION ROUTE CHECKED != CONTENTS PROPORTIONATE != APPROPRIATE TO HOLD")
    return 0


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT))
