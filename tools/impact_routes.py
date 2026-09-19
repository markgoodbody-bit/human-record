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
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def repo_path(value):
    """Convert a public THR URL or repository-relative path into a repository path."""
    if not isinstance(value, str) or not value.strip():
        return None
    value = value.strip()
    parsed = urlparse(value)
    if parsed.scheme and parsed.netloc:
        return parsed.path.lstrip("/") or None
    return value.lstrip("/")


def catalog_path_index(catalog):
    """Map current record files/routes to their catalogue record IDs."""
    index = {}
    for record in catalog.get("records", []):
        record_id = record.get("id")
        if not isinstance(record_id, str) or not record_id:
            continue
        for field in ("full_human_record", "machine_record", "human_view"):
            path = repo_path(record.get(field))
            if path:
                index[path] = record_id
    return index


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

    direct_records = sorted({
        record_id
        for record_id in source.get("used_by_records", [])
        if isinstance(record_id, str) and record_id in valid_record_ids
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

        resolved_records = set()
        unresolved = []
        for raw_link in assertion.get("record_links", []):
            path = repo_path(raw_link)
            record_id = path_index.get(path) if path else None
            if record_id:
                resolved_records.add(record_id)
                assertion_records.add(record_id)
            elif isinstance(raw_link, str) and raw_link:
                unresolved.append(raw_link)
                unresolved_record_links.append({
                    "assertion_id": assertion.get("id"),
                    "record_link": raw_link,
                })

        assertion_routes.append({
            "assertion_id": assertion.get("id"),
            "predicate": assertion.get("predicate"),
            "record_links": assertion.get("record_links", []),
            "resolved_records": sorted(resolved_records),
            "unresolved_record_links": unresolved,
        })

    affected_records = sorted(set(direct_records) | assertion_records)

    return {
        "source_id": source_id,
        "source_title": source.get("title"),
        "direct_used_by_records": direct_records,
        "assertion_routes": assertion_routes,
        "assertion_derived_records": sorted(assertion_records),
        "affected_records": affected_records,
        "unresolved_record_links": unresolved_record_links,
        "ceilings": [
            "AFFECTED_RECORD != FALSE_RECORD",
            "REVIEW_ROUTE != CORRECTION",
            "NO_ASSERTION_EDGE != NO_RECORD_DEPENDENCY",
            "ROUTE_DERIVED != COMPLETE_DEPENDENCY PROOF",
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

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
