"""Regression for issue #40: assertions may address an existing unresolved mention.

This is the smallest executable repair from the outside R. Vale identity probe.
It does not change candidate-link evidence/history semantics.
"""
import copy
from pathlib import Path
import unittest
from unittest.mock import patch

import validate_integrity as integrity


ROOT = Path(__file__).resolve().parents[1]
ASSERTION_ID = "thr:assertion:11111111-1111-4111-8111-111111111111"
MENTION_ID = "thr:mention:22222222-2222-4222-8222-222222222222"
UNKNOWN_MENTION_ID = "thr:mention:33333333-3333-4333-8333-333333333333"
MALFORMED_MENTION_ID = "mention-not-opaque"
SOURCE_ID = "thr:source:44444444-4444-4444-8444-444444444444"
OBS_ID = "thr:observation:55555555-5555-4555-8555-555555555555"


class AssertionMentionReferentTests(unittest.TestCase):
    def setUp(self):
        self.assertion = {
            "id": ASSERTION_ID,
            "subject": {"mention_id": MENTION_ID},
            "predicate": "reported_distinct_referents",
            "object": {"literal": "synthetic counterpart"},
            "state": "reported_by_source",
            "evidence": {
                "source_ids": [SOURCE_ID],
                "observation_ids": [OBS_ID],
            },
            "scope": {},
            "record_links": [],
            "corrections": [],
        }
        self.documents = {
            "registry/assertions.json": {"assertions": [self.assertion]},
            "registry/mentions.json": {
                "mentions": [{
                    "id": MENTION_ID,
                    "literal": "R. Vale — Harbour Study, 2024",
                    "source_id": SOURCE_ID,
                    "observation_id": OBS_ID,
                    "context": "synthetic issue #40 fixture",
                    "status": "unresolved",
                    "candidates": [],
                }]
            },
            "registry/sources.json": {
                "sources": [{
                    "id": SOURCE_ID,
                    "observations": [{
                        "id": OBS_ID,
                        "outcome": "partial",
                    }],
                }]
            },
        }
        integrity.errors.clear()
        integrity.warnings.clear()
        integrity._vocabulary_cache.clear()
        self.addCleanup(integrity.errors.clear)
        self.addCleanup(integrity.warnings.clear)
        self.addCleanup(integrity._vocabulary_cache.clear)

    def check(self):
        def loader(rel):
            if rel not in self.documents:
                raise AssertionError("unexpected load: " + rel)
            return copy.deepcopy(self.documents[rel])

        with patch.object(integrity, "ROOT", ROOT), patch.object(
            integrity, "load_json", side_effect=loader
        ):
            return integrity.check_assertions(
                record_ids=set(),
                entity_ids=set(),
                source_ids={SOURCE_ID},
                observation_ids={OBS_ID},
            )

    def test_existing_unresolved_mention_is_a_valid_assertion_referent(self):
        self.check()
        self.assertEqual(integrity.errors, [])

    def test_unknown_mention_is_rejected(self):
        self.assertion["subject"] = {"mention_id": UNKNOWN_MENTION_ID}
        self.check()
        self.assertEqual(
            integrity.errors,
            [ASSERTION_ID + ": subject refers to unknown mention " + UNKNOWN_MENTION_ID],
        )

    def test_non_string_mention_id_is_rejected(self):
        self.assertion["subject"] = {"mention_id": 42}
        self.check()
        self.assertEqual(
            integrity.errors,
            [ASSERTION_ID + ": subject.mention_id must be a non-empty string"],
        )

    def test_malformed_registry_mention_id_cannot_satisfy_reference(self):
        self.assertion["subject"] = {"mention_id": MALFORMED_MENTION_ID}
        self.documents["registry/mentions.json"]["mentions"][0]["id"] = MALFORMED_MENTION_ID
        self.check()
        self.assertEqual(
            integrity.errors,
            [
                "registry/mentions.json mentions[0]: invalid opaque mention id "
                + repr(MALFORMED_MENTION_ID),
                ASSERTION_ID + ": subject refers to unknown mention " + MALFORMED_MENTION_ID,
            ],
        )

    def test_duplicate_registry_mention_id_is_rejected(self):
        duplicate = copy.deepcopy(self.documents["registry/mentions.json"]["mentions"][0])
        self.documents["registry/mentions.json"]["mentions"].append(duplicate)
        self.check()
        self.assertEqual(
            integrity.errors,
            ["registry/mentions.json mentions[1]: duplicate mention id " + MENTION_ID],
        )


if __name__ == "__main__":
    unittest.main()
