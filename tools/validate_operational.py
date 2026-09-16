#!/usr/bin/env python3
"""Validate THR mention-resolution and source-currentness receipts without network access.

This checks identifier shape and cross-registry references only. It does not decide whether an
identity resolution is historically correct, whether a source is unchanged, or whether a
preservation route is adequate.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UUID = r"[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}"
ENTITY_RE = re.compile(rf"^thr:entity:{UUID}$")
SOURCE_RE = re.compile(rf"^thr:source:{UUID}$")
OBS_RE = re.compile(rf"^thr:observation:{UUID}$")
MENTION_RE = re.compile(rf"^thr:mention:{UUID}$")
CHECK_RE = re.compile(rf"^thr:source-check:{UUID}$")

MENTION_STATES = {"resolved", "candidate", "unresolved", "unresolved_not_required"}
CANDIDATE_STATES = {"resolved_as", "candidate", "excluded"}
CHECK_OUTCOMES = {
    "live_locator_retrieved",
    "partial",
    "metadata_only",
    "failed",
    "access_restricted",
    "redirected",
    "not_retrieved",
}


def load_object(root: Path, rel: str) -> dict:
    value = json.loads((root / rel).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{rel}: JSON root must be an object")
    return value


def validate(root: Path = ROOT) -> tuple[list[str], dict[str, int]]:
    root = Path(root).resolve()
    errors: list[str] = []
    counts = {"mentions": 0, "source_checks": 0}

    try:
        catalog = load_object(root, "records/catalog.json")
        entities = load_object(root, "registry/entities.json")
        sources = load_object(root, "registry/sources.json")
        mentions = load_object(root, "registry/mentions.json")
        checks = load_object(root, "registry/source-checks.json")
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        return [str(exc)], counts

    expected_routes = {
        "mention_registry": "https://thehumanrecord.net/registry/mentions.json",
        "source_check_registry": "https://thehumanrecord.net/registry/source-checks.json",
    }
    for field, expected in expected_routes.items():
        if catalog.get(field) != expected:
            errors.append(f"records/catalog.json: {field} must be {expected}")

    record_ids = {r.get("id") for r in catalog.get("records", []) if isinstance(r, dict) and isinstance(r.get("id"), str)}
    entity_ids = {e.get("id") for e in entities.get("entities", []) if isinstance(e, dict) and isinstance(e.get("id"), str)}
    source_ids: set[str] = set()
    observation_ids: set[str] = set()
    for source in sources.get("sources", []):
        if not isinstance(source, dict):
            continue
        sid = source.get("id")
        if isinstance(sid, str):
            source_ids.add(sid)
        for obs in source.get("observations", []):
            if isinstance(obs, dict) and isinstance(obs.get("id"), str):
                observation_ids.add(obs["id"])

    seen_mentions: set[str] = set()
    mention_items = mentions.get("mentions")
    if not isinstance(mention_items, list):
        errors.append("registry/mentions.json: mentions must be a list")
    else:
        for i, mention in enumerate(mention_items):
            context = f"mentions[{i}]"
            if not isinstance(mention, dict):
                errors.append(f"{context}: mention must be an object")
                continue
            mid = mention.get("id")
            if not isinstance(mid, str) or not MENTION_RE.fullmatch(mid):
                errors.append(f"{context}: invalid mention id {mid!r}")
                continue
            if mid in seen_mentions:
                errors.append(f"{context}: duplicate mention id {mid}")
            seen_mentions.add(mid)
            counts["mentions"] += 1
            if not isinstance(mention.get("literal"), str) or not mention["literal"]:
                errors.append(f"{mid}: literal must be non-empty")
            sid = mention.get("source_id")
            if sid not in source_ids:
                errors.append(f"{mid}: unknown source_id {sid!r}")
            oid = mention.get("observation_id")
            if oid is not None and oid not in observation_ids:
                errors.append(f"{mid}: unknown observation_id {oid!r}")
            rid = mention.get("record_id")
            if rid not in record_ids:
                errors.append(f"{mid}: unknown record_id {rid!r}")
            status = mention.get("status")
            if status not in MENTION_STATES:
                errors.append(f"{mid}: invalid status {status!r}")
            candidates = mention.get("candidates")
            if not isinstance(candidates, list):
                errors.append(f"{mid}: candidates must be a list")
                continue
            resolved_count = 0
            for j, candidate in enumerate(candidates):
                if not isinstance(candidate, dict):
                    errors.append(f"{mid}: candidates[{j}] must be an object")
                    continue
                eid = candidate.get("entity_id")
                if eid not in entity_ids:
                    errors.append(f"{mid}: candidate refers to unknown entity {eid!r}")
                state = candidate.get("state")
                if state not in CANDIDATE_STATES:
                    errors.append(f"{mid}: invalid candidate state {state!r}")
                if state == "resolved_as":
                    resolved_count += 1
            if status == "resolved" and resolved_count != 1:
                errors.append(f"{mid}: resolved mention must have exactly one resolved_as candidate")
            if status != "resolved" and resolved_count:
                errors.append(f"{mid}: non-resolved mention cannot contain resolved_as candidate")

    seen_checks: set[str] = set()
    check_items = checks.get("checks")
    if not isinstance(check_items, list):
        errors.append("registry/source-checks.json: checks must be a list")
    else:
        for i, check in enumerate(check_items):
            context = f"checks[{i}]"
            if not isinstance(check, dict):
                errors.append(f"{context}: source check must be an object")
                continue
            cid = check.get("id")
            if not isinstance(cid, str) or not CHECK_RE.fullmatch(cid):
                errors.append(f"{context}: invalid source-check id {cid!r}")
                continue
            if cid in seen_checks:
                errors.append(f"{context}: duplicate source-check id {cid}")
            seen_checks.add(cid)
            counts["source_checks"] += 1
            sid = check.get("source_id")
            if sid not in source_ids:
                errors.append(f"{cid}: unknown source_id {sid!r}")
            if not isinstance(check.get("checked_at"), str) or not check["checked_at"]:
                errors.append(f"{cid}: checked_at must be non-empty")
            if not isinstance(check.get("locator"), str) or not check["locator"]:
                errors.append(f"{cid}: locator must be non-empty")
            if check.get("outcome") not in CHECK_OUTCOMES:
                errors.append(f"{cid}: invalid outcome {check.get('outcome')!r}")
            if not isinstance(check.get("record_evidence_promoted"), bool):
                errors.append(f"{cid}: record_evidence_promoted must be boolean")
            promoted = check.get("promoted_observation_id")
            if check.get("record_evidence_promoted") is True and promoted not in observation_ids:
                errors.append(f"{cid}: promoted evidence must name a known observation_id")
            fingerprint = check.get("fingerprint")
            if fingerprint is not None:
                if not isinstance(fingerprint, dict) or not isinstance(fingerprint.get("algorithm"), str) or not isinstance(fingerprint.get("value"), str):
                    errors.append(f"{cid}: fingerprint must be null or algorithm/value object")

    return errors, counts


def main() -> int:
    errors, counts = validate()
    for item in errors:
        print(f"ERROR: {item}")
    if errors:
        print(f"FAIL: operational registry integrity failed with {len(errors)} error(s).")
        return 1
    print(
        "PASS: operational registry structure is coherent "
        f"({counts['mentions']} mention(s), {counts['source_checks']} source check(s))."
    )
    print("STRUCTURAL PASS != IDENTITY TRUTH != SOURCE UNCHANGED != PRESERVATION")
    return 0


if __name__ == "__main__":
    sys.exit(main())
