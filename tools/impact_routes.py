#!/usr/bin/env python3
"""Derive bounded THR review routes from existing source/assertion/catalog relations.

This is a read-only query helper. It does not change record state and it does not imply
that an affected record is false, corrected, stale, or required to change.

Core rule:

    DIRECT SOURCE USE
    UNION
    ASSERTION-DERIVED RECORD USE
    -> REVIEW CANDIDATES

No assertion edge must not mean no affected record.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
CANONICAL_PUBLIC_SCHEME = "https"
CANONICAL_PUBLIC_HOST = "thehumanrecord.net"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def repo_path(value):
    """Return a safe repository path for a THR public URL or repository-relative path.

    Absolute URLs are accepted only for the canonical HTTPS THR origin, with no
    credentials, port, query or fragment. Relative paths with query/fragment markers are
    rejected rather than normalised because those components can change resource
    identity. Unsupported/foreign values return None so callers can surface them as
    unresolved instead of falsely resolving by pathname.
    """
    if not isinstance(value, str) or not value.strip():
        return None

    value = value.strip()
    parsed = urlsplit(value)

    if parsed.scheme or parsed.netloc:
        if parsed.scheme != CANONICAL_PUBLIC_SCHEME:
            return None
        if parsed.hostname != CANONICAL_PUBLIC_HOST:
            return None
        if parsed.username is not None or parsed.password is not None:
            return None
        try:
            if parsed.port is not None:
                return None
        except ValueError:
            return None
        if parsed.query or parsed.fragment:
            return None
        path = parsed.path.lstrip("/")
    else:
        if value.startswith("//"):
            return None
        if parsed.query or parsed.fragment:
            return None
        path = parsed.path.lstrip("/")

    if not path:
        return None

    parts = path.split("/")
    if any(part in ("", ".", "..") for part in parts):
        return None

    return path


def catalog_path_index(catalog):
    """Map current record files/routes to catalogue record IDs, rejecting ambiguity."""
    index = {}
    for record in catalog.get("records", []):
        record_id = record.get("id")
        if not isinstance(record_id, str) or not record_id:
            continue

        for field in ("full_human_record", "machine_record", "human_view"):
            raw_value = record.get(field)
            if raw_value is None:
                continue

            path = repo_path(raw_value)
            if path is None:
                raise ValueError(
                    f"{record_id}: unsupported catalogue {field} route: {raw_value!r}"
                )

            previous = index.get(path)
            if previous is not None and previous != record_id:
                raise ValueError(
                    f"catalogue path {path!r} maps to multiple records: "
                    f"{previous!r}, {record_id!r}"
                )
            index[path] = record_id

    return index


def _strict_string_list(container, field, context):
    if field not in container:
        return []
    value = container[field]
    if not isinstance(value, list):
        raise ValueError(f"{context}.{field} must be a list")
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            raise ValueError(
                f"{context}.{field}[{index}] must be a non-empty string"
            )
    return value


def derive_impact_routes(root: Path, source_id: str):
    sources = load_json(root / "registry/sources.json").get("sources", [])
    assertions = load_json(root / "registry/assertions.json").get("assertions", [])
    catalog = load_json(root / "records/catalog.json")

    source = next((item for item in sources if item.get("id") == source_id), None)
    if source is None:
        raise KeyError(source_id)

    path_index = catalog_path_index(catalog)
    valid_record_ids = {
        item.get("id")
        for item in catalog.get("records", [])
        if isinstance(item.get("id"), str) and item.get("id")
    }

    raw_direct_records = _strict_string_list(
        source, "used_by_records", source_id
    )
    direct_records = sorted({
        record_id
        for record_id in raw_direct_records
        if record_id in valid_record_ids
    })
    unresolved_direct_records = sorted({
        record_id
        for record_id in raw_direct_records
        if record_id not in valid_record_ids
    })

    assertion_routes = []
    assertion_records = set()
    unresolved_record_links = []

    for assertion in assertions:
        evidence = assertion.get("evidence")
        if not isinstance(evidence, dict):
            continue
        source_ids = evidence.get("source_ids")
        if not isinstance(source_ids, list) or source_id not in source_ids:
            continue

        assertion_id = assertion.get("id", "<unknown>")
        raw_links = _strict_string_list(
            assertion, "record_links", assertion_id
        )

        resolved_records = set()
        unresolved = []
        for raw_link in raw_links:
            path = repo_path(raw_link)
            record_id = path_index.get(path) if path else None
            if record_id:
                resolved_records.add(record_id)
                assertion_records.add(record_id)
            else:
                unresolved.append(raw_link)
                unresolved_record_links.append({
                    "assertion_id": assertion.get("id"),
                    "record_link": raw_link,
                })

        assertion_routes.append({
            "assertion_id": assertion.get("id"),
            "predicate": assertion.get("predicate"),
            "record_links": raw_links,
            "resolved_records": sorted(resolved_records),
            "unresolved_record_links": unresolved,
        })

    affected_records = sorted(set(direct_records) | assertion_records)

    return {
        "source_id": source_id,
        "source_title": source.get("title"),
        "direct_used_by_records": direct_records,
        "unresolved_direct_used_by_records": unresolved_direct_records,
        "assertion_routes": assertion_routes,
        "assertion_derived_records": sorted(assertion_records),
        "affected_records": affected_records,
        "unresolved_record_links": unresolved_record_links,
        "ceilings": [
            "AFFECTED_RECORD != FALSE_RECORD",
            "REVIEW_ROUTE != CORRECTION",
            "NO_ASSERTION_EDGE != NO_RECORD_DEPENDENCY",
            "ROUTE_DERIVED != COMPLETE_DEPENDENCY_PROOF",
            "UNKNOWN_DIRECT_RECORD_ID != SILENTLY_IGNORED",
            "REGISTERED_SOURCE_QUERY != ALL_RECORD_LOCAL_DEPENDENCIES",
        ],
    }


def main():
    parser = argparse.ArgumentParser(
        description="Derive review candidates for one THR source from existing public relations."
    )
    parser.add_argument("source_id", help="registered thr:source:<uuid> identifier")
    parser.add_argument(
        "--root",
        type=Path,
        default=ROOT,
        help="THR checkout root (defaults to this repository)",
    )
    args = parser.parse_args()

    try:
        result = derive_impact_routes(args.root.resolve(), args.source_id)
    except KeyError:
        parser.error(f"unknown source_id: {args.source_id}")
    except ValueError as exc:
        parser.error(str(exc))

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
