"""Synthetic regressions for assertion evidence container shape.

These tests exercise production validator structure only. They do not depend on
historical research fixtures or alter public records.
"""
import copy
import unittest
from unittest.mock import patch

import validate_integrity as integrity


ASSERTION_ID = "thr:assertion:11111111-1111-4111-8111-111111111111"
ENTITY_ID = "thr:entity:22222222-2222-4222-8222-222222222222"
SOURCE_ID = "thr:source:33333333-3333-4333-8333-333333333333"
OBS_ID = "thr:observation:44444444-4444-4444-8444-444444444444"


class AssertionEvidenceContainerShapeTests(unittest.TestCase):
    def setUp(self):
        integrity.errors.clear()
        integrity.warnings.clear()
        integrity._vocabulary_cache.clear()
        self.addCleanup(integrity.errors.clear)
        self.addCleanup(integrity.warnings.clear)
        self.addCleanup(integrity._vocabulary_cache.clear)

        self.assertion_registry = {
            "assertions": [{
                "id": ASSERTION_ID,
                "subject": {"entity_id": ENTITY_ID},
                "predicate": "synthetic_test_predicate",
                "object": {"literal": "synthetic object"},
                "state": "reported_by_source",
                "evidence": {
                    "source_ids": [SOURCE_ID],
                    "observation_ids": [OBS_ID],
                },
                "record_links": [],
            }]
        }
        self.source_registry = {
            "sources": [{
                "id": SOURCE_ID,
                "observations": [{
                    "id": OBS_ID,
                    "outcome": "partial",
                }],
            }]
        }

    def run_check(self):
        def loader(rel):
            if rel == "registry/assertions.json":
                return copy.deepcopy(self.assertion_registry)
            if rel == "registry/sources.json":
                return copy.deepcopy(self.source_registry)
            raise AssertionError("unexpected load: " + rel)

        with patch.object(integrity, "load_json", side_effect=loader):
            integrity.check_assertions(
                record_ids=set(),
                entity_ids={ENTITY_ID},
                source_ids={SOURCE_ID},
                observation_ids={OBS_ID},
            )

    def test_valid_lists_pass_shape_check(self):
        self.run_check()
        self.assertEqual(integrity.errors, [])

    def test_missing_optional_lists_default_to_empty(self):
        evidence = self.assertion_registry["assertions"][0]["evidence"]
        evidence.pop("source_ids")
        evidence.pop("observation_ids")
        self.run_check()
        self.assertEqual(integrity.errors, [])

    def test_malformed_source_id_containers_are_rejected_without_exception(self):
        for malformed in ("made-up-id", None, {}, [{}], [None], [""]):
            with self.subTest(malformed=malformed):
                integrity.errors.clear()
                self.assertion_registry["assertions"][0]["evidence"]["source_ids"] = copy.deepcopy(malformed)
                self.assertion_registry["assertions"][0]["evidence"]["observation_ids"] = []
                self.run_check()
                self.assertIn(
                    ASSERTION_ID + ": evidence.source_ids must be a list of non-empty strings",
                    integrity.errors,
                )

    def test_malformed_observation_id_containers_are_rejected_without_exception(self):
        for malformed in ("made-up-id", None, {}, [{}], [None], [""]):
            with self.subTest(malformed=malformed):
                integrity.errors.clear()
                self.assertion_registry["assertions"][0]["evidence"]["source_ids"] = [SOURCE_ID]
                self.assertion_registry["assertions"][0]["evidence"]["observation_ids"] = copy.deepcopy(malformed)
                self.run_check()
                self.assertIn(
                    ASSERTION_ID + ": evidence.observation_ids must be a list of non-empty strings",
                    integrity.errors,
                )


if __name__ == "__main__":
    unittest.main()
