#!/usr/bin/env python3
"""Validate Human Record cross-record integrity without network access.

This script deliberately checks structure, identity uniqueness, local routing and byte
identity. It does not decide whether historical, provenance, identity or assertion claims
are true. HTML basis labels are compared to the catalogue, not assessed for rendered
visibility, summary accuracy or the truth of their alignment date.
"""

from __future__ import annotations

import hashlib
import argparse
from html.parser import HTMLParser
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse, unquote

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_ORIGIN = "https://thehumanrecord.net"
UUID = r"[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}"
ENTITY_RE = re.compile(rf"^thr:entity:{UUID}$")
SOURCE_RE = re.compile(rf"^thr:source:{UUID}$")
OBS_RE = re.compile(rf"^thr:observation:{UUID}$")
ASSERTION_RE = re.compile(rf"^thr:assertion:{UUID}$")

errors: list[str] = []
warnings: list[str] = []


def error(message: str) -> None:
    errors.append(message)


def warn(message: str) -> None:
    warnings.append(message)


def load_json(relative: str):
    path = ROOT / relative
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(value, dict):
            error(f"{relative}: JSON root must be an object")
            return None
        return value
    except FileNotFoundError:
        error(f"missing JSON file: {relative}")
    except json.JSONDecodeError as exc:
        error(f"invalid JSON in {relative}: {exc}")
    return None


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


# Vocabularies are read from the model documents, not copied into this file. On
# 2026-09-16 registry/sources.json shipped two preservation states the model does
# not define (one of them a rights conclusion SOURCE_MODEL.md §6 says not to draw)
# and this validator passed, because it checked that `status` was a string. A
# second copy of the list here would drift from the model the same way the
# registry did; the model is the mould, so read it.
#
# `closed` lists ("Working preservation states:") produce errors on an unknown
# value; `open` lists ("Possible outcomes include:", "Examples:") produce
# warnings, because the model itself leaves them extensible.
VOCABULARIES = (
    # (document, heading, key path, closed?)
    ("SOURCE_MODEL.md", "## 6. Preservation state", "preservation.status", True),
    ("SOURCE_MODEL.md", "## 3. Observation", "observation.outcome", False),
    ("SOURCE_MODEL.md", "## 5. Source ancestry and relationships", "relation.type", False),
    ("ASSERTION_MODEL.md", "## 4. Assertion state", "assertion.state", False),
)

DIRECT_EVIDENCE_STATES_MODEL = (
    "ASSERTION_MODEL.md",
    "## 4a. Direct-evidence implementation boundary",
)


_vocabulary_cache: dict[tuple[str, str], set[str] | None] = {}


def model_vocabulary(document: str, heading: str) -> set[str] | None:
    """The backticked bullet items under `heading` in `document`, up to the next heading.
    None (and one error, not one per row) if the document or heading is missing or the
    list is empty, so a model that stops naming its states fails loudly rather than passing."""
    key = (document, heading)
    if key not in _vocabulary_cache:
        _vocabulary_cache[key] = _read_model_vocabulary(document, heading)
    return _vocabulary_cache[key]


def _read_model_vocabulary(document: str, heading: str) -> set[str] | None:
    path = ROOT / document
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        error(f"{document}: missing; cannot read the vocabulary under {heading!r}")
        return None
    start = text.find(heading)
    if start < 0:
        error(f"{document}: heading {heading!r} not found; cannot read its vocabulary")
        return None
    section = text[start + len(heading):]
    end = re.search(r"^## ", section, re.M)
    section = section[: end.start()] if end else section
    values = set(re.findall(r"^- `([a-z_]+)`", section, re.M))
    if not values:
        error(f"{document}: no backticked bullet values under {heading!r}")
        return None
    return values


def check_vocabulary(value, document: str, heading: str, key: str, closed: bool, context: str) -> None:
    allowed = model_vocabulary(document, heading)
    if allowed is None or not isinstance(value, str):
        return
    if value in allowed:
        return
    message = f"{context}: {key} {value!r} is not in {document} {heading!r} ({', '.join(sorted(allowed))})"
    if closed:
        error(message)
    else:
        warn(message + "; the model calls this list open, so this is a warning")


def local_public_path(url: str) -> Path | None:
    try:
        parsed = urlparse(url)
    except ValueError:
        return None
    if (f"{parsed.scheme}://{parsed.netloc}" != PUBLIC_ORIGIN
            or parsed.query or parsed.fragment or parsed.params):
        return None
    rel = unquote(parsed.path).lstrip("/")
    if "\x00" in rel or "\\" in rel:
        return None
    if not rel:
        rel = "index.html"
    elif rel.endswith("/"):
        rel += "index.html"
    return ROOT / rel


def require_local_route(url: str, context: str) -> None:
    path = local_public_path(url)
    if path is None:
        error(f"{context}: expected a plain local public route: {url}")
    elif not path.resolve().is_relative_to(ROOT.resolve()):
        error(f"{context}: local public route escapes checkout: {url}")
    elif not path.is_file():
        error(f"{context}: local public route does not exist: {url} -> {path.relative_to(ROOT)}")


def check_catalog() -> set[str]:
    catalog = load_json("records/catalog.json")
    if not isinstance(catalog, dict):
        return set()

    for field in (
        "record_contract",
        "human_explanation",
        "scale_architecture",
        "technical_scale_note",
        "identity_model",
        "source_model",
        "assertion_model",
        "entity_registry",
        "source_registry",
        "assertion_registry",
        "selection_orientation",
    ):
        value = catalog.get(field)
        if isinstance(value, str):
            require_local_route(value, f"records/catalog.json.{field}")
        else:
            error(f"records/catalog.json: missing string field {field}")

    records = catalog.get("records")
    if not isinstance(records, list) or not records:
        error("records/catalog.json: records must be a non-empty list")
        return set()

    seen: set[str] = set()
    for i, record in enumerate(records):
        context = f"records/catalog.json records[{i}]"
        if not isinstance(record, dict):
            error(f"{context}: record must be an object")
            continue
        record_id = record.get("id")
        if not isinstance(record_id, str) or not record_id:
            error(f"{context}: missing non-empty id")
            continue
        if record_id in seen:
            error(f"{context}: duplicate record id {record_id}")
        seen.add(record_id)

        for field in ("human_view", "full_human_record", "machine_record", "correction_route"):
            value = record.get(field)
            if isinstance(value, str):
                require_local_route(value, f"{record_id}.{field}")
            else:
                error(f"{record_id}: missing string field {field}")

        basis = record.get("view_basis")
        if not isinstance(basis, dict):
            error(f"{record_id}: missing view_basis")
            continue
        pinned = basis.get("source_git_blobs")
        if not isinstance(pinned, dict) or not pinned:
            error(f"{record_id}: view_basis.source_git_blobs must be a non-empty object")
            continue
        required_paths: set[str] = set()
        for field in ("full_human_record", "machine_record"):
            value = record.get(field)
            path = local_public_path(value) if isinstance(value, str) else None
            if path is None:
                error(f"{record_id}: {field} must identify a local public source")
                continue
            resolved = path.resolve()
            if not resolved.is_relative_to(ROOT.resolve()):
                error(f"{record_id}: {field} escapes the checkout")
                continue
            required_paths.add(resolved.relative_to(ROOT.resolve()).as_posix())
        if len(required_paths) != 2 or set(pinned) != required_paths:
            error(f"{record_id}: source pins must cover exactly both record source routes")
            continue
        check_view_label(record)
        for rel, expected in pinned.items():
            path = (ROOT / rel).resolve()
            if not path.is_relative_to(ROOT.resolve()):
                error(f"{record_id}: pinned source escapes checkout: {rel}")
                continue
            if not isinstance(expected, str) or not re.fullmatch(r"[0-9a-f]{40}", expected):
                error(f"{record_id}: invalid Git blob ID: {rel}")
                continue
            if not path.exists():
                error(f"{record_id}: pinned source does not exist: {rel}")
                continue
            actual = git_blob_sha(path)
            if actual != expected:
                error(
                    f"{record_id}: stale human-view basis for {rel}: "
                    f"catalog={expected} working-tree={actual}"
                )

    return seen


class BasisParagraphs(HTMLParser):
    """Extract labels, not rendered visibility or semantic correctness."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.current = None
        self.paragraphs = []

    def handle_starttag(self, tag, attrs):
        if tag == "p":
            self.current = []

    def handle_data(self, data):
        if self.current is not None:
            self.current.append(data)

    def handle_endtag(self, tag):
        if tag == "p" and self.current is not None:
            text = "".join(self.current)
            if text.strip().startswith("View basis:"):
                self.paragraphs.append(text)
            self.current = None


def check_view_label(record):
    identity = record["id"]
    value = record.get("human_view")
    path = local_public_path(value) if isinstance(value, str) else None
    if path is None or not path.resolve().is_relative_to(ROOT.resolve()):
        error(f"{identity}: human view must be inside checkout")
        return
    try:
        parser = BasisParagraphs()
        parser.feed(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError) as exc:
        error(f"{identity}: cannot read human view: {exc}")
        return
    if len(parser.paragraphs) != 1:
        error(f"{identity}: expected one View basis paragraph")
        return
    text = parser.paragraphs[0]
    basis = record["view_basis"]
    for name, pin in basis["source_git_blobs"].items():
        matches = re.findall(re.escape(name) + r"@([0-9a-f]{7,40})(?:…|\.\.\.|(?=\s|[).,]|$))", text)
        if not isinstance(pin, str) or len(matches) != 1 or not pin.startswith(matches[0]):
            error(f"{identity}: stale or missing HTML source marker for {name}")
    if "source_record_version" in basis:
        versions = re.findall(r"record version\s+([0-9]+(?:\.[0-9]+)+)", text)
        if versions != [basis["source_record_version"]]:
            error(f"{identity}: HTML record version mismatch")
    elif isinstance(basis.get("source_record_format"), str):
        if basis["source_record_format"] not in text:
            error(f"{identity}: HTML record format mismatch")
    else:
        error(f"{identity}: missing record version or format")


def check_entities() -> set[str]:
    registry = load_json("registry/entities.json")
    if not isinstance(registry, dict):
        return set()
    entities = registry.get("entities")
    if not isinstance(entities, list):
        error("registry/entities.json: entities must be a list")
        return set()

    seen: set[str] = set()
    for i, entity in enumerate(entities):
        context = f"registry/entities.json entities[{i}]"
        if not isinstance(entity, dict):
            error(f"{context}: entity must be an object")
            continue
        entity_id = entity.get("id")
        if not isinstance(entity_id, str) or not ENTITY_RE.match(entity_id):
            error(f"{context}: invalid opaque entity id {entity_id!r}")
            continue
        if entity_id in seen:
            error(f"{context}: duplicate entity id {entity_id}")
        seen.add(entity_id)

        labels = entity.get("labels")
        if not isinstance(labels, list) or not labels:
            error(f"{entity_id}: labels must be a non-empty list")
        else:
            for j, label in enumerate(labels):
                if not isinstance(label, dict) or not isinstance(label.get("text"), str) or not label.get("text"):
                    error(f"{entity_id}: labels[{j}] must contain non-empty text")

        for rel in entity.get("record_links", []):
            if not isinstance(rel, str) or not (ROOT / rel).exists():
                error(f"{entity_id}: record_link does not exist: {rel!r}")

    return seen


def check_sources(record_ids: set[str]) -> tuple[set[str], set[str]]:
    registry = load_json("registry/sources.json")
    if not isinstance(registry, dict):
        return set(), set()
    sources = registry.get("sources")
    if not isinstance(sources, list):
        error("registry/sources.json: sources must be a list")
        return set(), set()

    source_ids: set[str] = set()
    observation_ids: set[str] = set()

    for i, source in enumerate(sources):
        context = f"registry/sources.json sources[{i}]"
        if not isinstance(source, dict):
            error(f"{context}: source must be an object")
            continue
        source_id = source.get("id")
        if not isinstance(source_id, str) or not SOURCE_RE.match(source_id):
            error(f"{context}: invalid opaque source id {source_id!r}")
            continue
        if source_id in source_ids:
            error(f"{context}: duplicate source id {source_id}")
        source_ids.add(source_id)

        locators = source.get("locators")
        if not isinstance(locators, list) or not locators:
            error(f"{source_id}: locators must be a non-empty list")

        observations = source.get("observations")
        if not isinstance(observations, list):
            error(f"{source_id}: observations must be a list")
        else:
            for j, observation in enumerate(observations):
                if not isinstance(observation, dict):
                    error(f"{source_id}: observations[{j}] must be an object")
                    continue
                obs_id = observation.get("id")
                if not isinstance(obs_id, str) or not OBS_RE.match(obs_id):
                    error(f"{source_id}: invalid observation id {obs_id!r}")
                elif obs_id in observation_ids:
                    error(f"{source_id}: duplicate observation id {obs_id}")
                else:
                    observation_ids.add(obs_id)
                if not isinstance(observation.get("observed_at"), str):
                    error(f"{source_id}: observation {obs_id!r} missing observed_at")
                if not isinstance(observation.get("outcome"), str):
                    error(f"{source_id}: observation {obs_id!r} missing outcome")
                else:
                    check_vocabulary(observation["outcome"], *VOCABULARIES[1][:3], VOCABULARIES[1][3],
                                     f"{source_id}: observation {obs_id!r}")

        preservation = source.get("preservation")
        if not isinstance(preservation, dict) or not isinstance(preservation.get("status"), str):
            error(f"{source_id}: preservation.status must be present")
        else:
            check_vocabulary(preservation["status"], *VOCABULARIES[0][:3], VOCABULARIES[0][3], source_id)

        for record_id in source.get("used_by_records", []):
            if record_id not in record_ids:
                error(f"{source_id}: used_by_records refers to unknown record id {record_id!r}")

    # Relations are checked after all source IDs are collected so forward references work.
    for source in sources:
        if not isinstance(source, dict):
            continue
        source_id = source.get("id", "<unknown>")
        for relation in source.get("relations", []):
            if not isinstance(relation, dict):
                error(f"{source_id}: source relation must be an object")
                continue
            target = relation.get("target")
            if isinstance(target, str) and target.startswith("thr:source:") and target not in source_ids:
                error(f"{source_id}: relation points to unknown source {target}")
            if isinstance(relation.get("type"), str):
                check_vocabulary(relation["type"], *VOCABULARIES[2][:3], VOCABULARIES[2][3], source_id)

    return source_ids, observation_ids


def check_assertions(
    record_ids: set[str],
    entity_ids: set[str],
    source_ids: set[str],
    observation_ids: set[str],
) -> set[str]:
    registry = load_json("registry/assertions.json")
    if not isinstance(registry, dict):
        return set()
    assertions = registry.get("assertions")
    if not isinstance(assertions, list):
        error("registry/assertions.json: assertions must be a list")
        return set()

    # Existence alone permits an assertion to borrow another source's observation.
    # Build ownership from the registry, never from the assertion being checked.
    source_registry = load_json("registry/sources.json")
    observation_sources: dict[str, str] = {}
    source_items = source_registry.get("sources", []) if isinstance(source_registry, dict) else []
    for source in source_items if isinstance(source_items, list) else []:
        if not isinstance(source, dict) or not isinstance(source.get("id"), str):
            continue
        observations = source.get("observations", [])
        for observation in observations if isinstance(observations, list) else []:
            if isinstance(observation, dict) and isinstance(observation.get("id"), str):
                observation_sources[observation["id"]] = source["id"]

    direct_evidence_states = model_vocabulary(*DIRECT_EVIDENCE_STATES_MODEL)
    if not direct_evidence_states:
        error(
            "direct-evidence boundary section missing or empty in ASSERTION_MODEL.md; "
            "fail-closed state guard cannot be evaluated"
        )
        direct_evidence_states = set()

    seen: set[str] = set()
    for i, assertion in enumerate(assertions):
        context = f"registry/assertions.json assertions[{i}]"
        if not isinstance(assertion, dict):
            error(f"{context}: assertion must be an object")
            continue
        assertion_id = assertion.get("id")
        if not isinstance(assertion_id, str) or not ASSERTION_RE.match(assertion_id):
            error(f"{context}: invalid opaque assertion id {assertion_id!r}")
            continue
        if assertion_id in seen:
            error(f"{context}: duplicate assertion id {assertion_id}")
        seen.add(assertion_id)

        if not isinstance(assertion.get("predicate"), str) or not assertion.get("predicate"):
            error(f"{assertion_id}: predicate must be a non-empty string")
        if not isinstance(assertion.get("state"), str) or not assertion.get("state"):
            error(f"{assertion_id}: state must be a non-empty string")
        else:
            check_vocabulary(assertion["state"], *VOCABULARIES[3][:3], VOCABULARIES[3][3], assertion_id)
            if assertion["state"] in direct_evidence_states:
                error(
                    f"{assertion_id}: state {assertion['state']!r} requires typed "
                    "observation/reconciliation target support; current source observations "
                    "record retrieval/inspection only"
                )

        for role in ("subject", "object"):
            value = assertion.get(role)
            if not isinstance(value, dict):
                error(f"{assertion_id}: {role} must be an object")
                continue
            entity_id = value.get("entity_id")
            if isinstance(entity_id, str) and entity_id not in entity_ids:
                error(f"{assertion_id}: {role} refers to unknown entity {entity_id}")
            record_id = value.get("record_id")
            if isinstance(record_id, str) and record_id not in record_ids:
                error(f"{assertion_id}: {role} refers to unknown record {record_id}")
            if not any(key in value for key in ("entity_id", "record_id", "literal", "assertion_id")):
                error(f"{assertion_id}: {role} has no recognised referent")

        evidence = assertion.get("evidence")
        if not isinstance(evidence, dict):
            error(f"{assertion_id}: evidence must be an object")
        else:
            for source_id in evidence.get("source_ids", []):
                if source_id not in source_ids:
                    error(f"{assertion_id}: evidence refers to unknown source {source_id!r}")
            for obs_id in evidence.get("observation_ids", []):
                if obs_id not in observation_ids:
                    error(f"{assertion_id}: evidence refers to unknown observation {obs_id!r}")
                elif observation_sources.get(obs_id) not in evidence.get("source_ids", []):
                    error(f"{assertion_id}: evidence observation belongs to a source not cited in source_ids: {obs_id!r}")

        for rel in assertion.get("record_links", []):
            if not isinstance(rel, str) or not (ROOT / rel).exists():
                error(f"{assertion_id}: record_link does not exist: {rel!r}")

    # Validate assertion-to-assertion references after all IDs are known.
    for assertion in assertions:
        if not isinstance(assertion, dict):
            continue
        assertion_id = assertion.get("id", "<unknown>")
        for role in ("subject", "object"):
            value = assertion.get(role)
            if not isinstance(value, dict):
                continue
            target = value.get("assertion_id")
            if isinstance(target, str) and target not in seen:
                error(f"{assertion_id}: {role} refers to unknown assertion {target}")

    return seen


def main() -> int:
    record_ids = check_catalog()
    entity_ids = check_entities()
    source_ids, observation_ids = check_sources(record_ids)
    assertion_ids = check_assertions(record_ids, entity_ids, source_ids, observation_ids)

    for message in warnings:
        print(f"WARN: {message}")
    if errors:
        for message in errors:
            print(f"ERROR: {message}")
        print(f"FAIL: {len(errors)} integrity error(s)")
        return 1

    print(
        "PASS: Human Record structural integrity checks passed "
        "(catalogue pins/routes and HTML basis labels; entity/source/observation/assertion IDs; cross-registry references)."
    )
    print(
        f"INDEX: {len(record_ids)} record(s), {len(entity_ids)} entity id(s), "
        f"{len(source_ids)} source id(s), {len(observation_ids)} observation id(s), "
        f"{len(assertion_ids)} assertion id(s)."
    )
    print("NOTE: structural PASS does not establish truth, identity certainty or preservation completeness.")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=ROOT,
                        help="checkout to inspect (defaults to this script's repository)")
    args = parser.parse_args()
    ROOT = args.root.resolve()
    if not ROOT.is_dir():
        parser.exit(1, f"ERROR: checkout directory does not exist: {ROOT}\n")
    sys.exit(main())
