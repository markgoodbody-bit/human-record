#!/usr/bin/env python3
"""Validate that every registered THR entity was admitted by a record, not by a mention.

`IDENTITY_MODEL.md` already states `MENTION != ENTITY`. This makes that sentence enforceable
against regression: an entity-first registry grows by mention unless something structural
stops it, and a statement of intent is not a structure. The check is narrow and its scope is
stated rather than implied.

WHAT IT CHECKS

1. every entity carries at least one `record_links` entry;
2. every `record_links` target exists in the checkout;
3. at least one target is a record-bearing file rather than only a rendered page, so an
   entity cannot be admitted by an HTML view alone;
4. every entity id referenced by `registry/mentions.json` candidates is registered, so a
   mention cannot conjure a referent by naming one.

WHAT IT DOES NOT CHECK

It does not decide whether a record should exist, whether an entity is the right referent,
whether a record's contents are minimal or proportionate, or whether publication was
appropriate. A pass here is a statement about admission route only.

    AN_ENTITY_STORE_GROWS_BY_MENTION UNLESS_ADMISSION_IS_A_PRECONDITION
    STRUCTURAL_PASS != APPROPRIATE_TO_HOLD
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UUID = r"[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}"
ENTITY_RE = re.compile(rf"^thr:entity:{UUID}$")
# A record-bearing file states claims with evidence; a rendered page presents them.
RECORD_SUFFIXES = (".json", ".md")


def load(root: Path, rel: str) -> dict:
    value = json.loads((root / rel).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{rel}: JSON root must be an object")
    return value


def main(root: Path = ROOT) -> int:
    root = Path(root).resolve()
    errors: list[str] = []
    try:
        entities = load(root, "registry/entities.json").get("entities")
        mentions = load(root, "registry/mentions.json").get("mentions")
    except (OSError, ValueError) as exc:
        # A checker that cannot read its inputs must not report a pass.
        print(f"ERROR: entity admission check could not read the registries: {exc}")
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
        missing = [str(link) for link in links if not (root / str(link)).is_file()]
        if missing:
            errors.append(f"{eid}: record_links target(s) not in the checkout: {', '.join(missing)}")
        bearing = [str(link) for link in links if str(link).endswith(RECORD_SUFFIXES)]
        if not bearing:
            errors.append(f"{eid}: record_links contains no record-bearing file "
                          f"({' or '.join(RECORD_SUFFIXES)}); a rendered page alone does not admit an entity")

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
    print(f"PASS: {len(entities)} entity record(s) each admitted by an existing record-bearing "
          f"file; {len(mentions)} mention(s) name only registered entities.")
    print("ADMISSION ROUTE CHECKED != CONTENTS PROPORTIONATE != APPROPRIATE TO HOLD")
    return 0


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT))
