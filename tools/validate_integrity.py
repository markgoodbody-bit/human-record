#!/usr/bin/env python3
"""Validate Human Record cross-record integrity without network access.

This script deliberately checks structure, identity uniqueness, local routing and byte
identity. It does not decide whether historical, provenance or identity claims are true.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_ORIGIN = "https://thehumanrecord.net"
ENTITY_RE = re.compile(r"^thr:entity:[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$")
SOURCE_RE = re.compile(r"^thr:source:[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$")
OBS_RE = re.compile(r"^thr:observation:[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$")

errors: list[str] = []
warnings: list[str] = []


def error(message: str) -> None:
    errors.append(message)


def warn(message: str) -> None:
    warnings.append(message)


def load_json(relative: str):
    path = ROOT / relative
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        error(f"missing JSON file: {relative}")
    except json.JSONDecodeError as exc:
        error(f"invalid JSON in {relative}: {exc}")
    return None


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def local_public_path(url: str) -> Path | None:
    parsed = urlparse(url)
    if f"{parsed.scheme}://{parsed.netloc}" != PUBLIC_ORIGIN:
        return None
    rel = parsed.path.lstrip("/")
    if not rel:
        rel = "index.html"
    elif rel.endswith("/"):
        rel += "index.html"
    return ROOT / rel


def require_local_route(url: str, context: str) -> None:
    path = local_public_path(url)
    if path is not None and not path.exists():
        error(f"{context}: local public route does not exist: {url} -> {path.relative_to(ROOT)}")


def check_catalog() -> set[str]:
    catalog = load_json("records/catalog.json")
    if not isinstance(catalog, dict):
        return set()
    records = catalog.get("records")
    if not isinstance(records, list):
        error("records/catalog.json: records must be a list")
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
        for rel, expected in pinned.items():
            path = ROOT / rel
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


def check_entities() -> None:
    registry = load_json("registry/entities.json")
    if not isinstance(registry, dict):
        return
    entities = registry.get("entities")
    if not isinstance(entities, list):
        error("registry/entities.json: entities must be a list")
        return

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



def check_sources(record_ids: set[str]) -> None:
    registry = load_json("registry/sources.json")
    if not isinstance(registry, dict):
        return
    sources = registry.get("sources")
    if not isinstance(sources, list):
        error("registry/sources.json: sources must be a list")
        return

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

        preservation = source.get("preservation")
        if not isinstance(preservation, dict) or not isinstance(preservation.get("status"), str):
            error(f"{source_id}: preservation.status must be present")

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


def main() -> int:
    record_ids = check_catalog()
    check_entities()
    check_sources(record_ids)

    for message in warnings:
        print(f"WARN: {message}")
    if errors:
        for message in errors:
            print(f"ERROR: {message}")
        print(f"FAIL: {len(errors)} integrity error(s)")
        return 1

    print(
        "PASS: Human Record structural integrity checks passed "
        "(catalogue pins, local routes, entity/source/observation IDs and registry references)."
    )
    print("NOTE: structural PASS does not establish truth, identity certainty or preservation completeness.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
