"""Synthetic regressions for cross-record assertion semantics.

These tests exercise validator structure only. They do not encode any historical
claim, research fixture, or truth judgment.
"""
import copy
from pathlib import Path
import unittest
from unittest.mock import patch

import validate_integrity as integrity

ROOT = Path(__file__).resolve().parents[1]

ENTITY = "thr:entity:11111111-1111-4111-8111-111111111111"
SOURCE_A = "thr:source:22222222-2222-4222-8222-222222222222"
SOURCE_B = "thr:source:33333333-3333-4333-8333-333333333333"
OBS_A = "thr:observation:44444444-4444-4444-8444-444444444444"
OBS_B = "thr:observation:55555555-5555-4555-8555-555555555555"
ASSERTION = "thr:assertion:66666666-6666-4666-8666-666666666666"


class AssertionSemanticGuardTests(unittest.TestCase):
    def setUp(self):
        self.sources = {
            "sources": [
                {
                    "id": SOURCE_A,
                    "observations": [{"id": OBS_A, "outcome": "partial"}],
                },
                {
                    "id": SOURCE_B,
                    "observations": [{"id": OBS_B, "outcome": "partial"}],
                },
            ]
        }
        self.assertion = {
            "id": ASSERTION,
            "subject": {"entity_id": ENTITY},
            "predicate": "synthetic_test_predicate",
            "object": {"literal": "synthetic test value"},
            "state": "reported_by_source",
            "evidence": {
                "source_ids": [SOURCE_A],
                "observation_ids": [OBS_A],
            },
            "scope": {},
            "record_links": [],
            "corrections": [],
        }
        self.documents = {
            "registry/sources.json": self.sources,
            "registry/assertions.json": {"assertions": [self.assertion]},
        }
        integrity.errors.clear()
        integrity.warnings.clear()
        integrity._vocabulary_cache.clear()
        self.addCleanup(integrity.errors.clear)
        self.addCleanup(integrity.warnings.clear)
        self.addCleanup(integrity._vocabulary_cache.clear)

    def check(self):
        with patch.object(integrity, "ROOT", ROOT), patch.object(
            integrity,
            "load_json",
            side_effect=lambda rel: copy.deepcopy(self.documents[rel]),
        ):
            return integrity.check_assertions(
                {"example-record"},
                {ENTITY},
                {SOURCE_A, SOURCE_B},
                {OBS_A, OBS_B},
            )

    def observation(self, source_id, observation_id):
        for source in self.sources["sources"]:
            if source["id"] == source_id:
                for observation in source["observations"]:
                    if observation["id"] == observation_id:
                        return observation
        raise AssertionError("synthetic observation missing")

    def test_reported_by_source_baseline_passes(self):
        self.check()
        self.assertEqual(integrity.errors, [])

    def test_source_only_evidence_remains_allowed_for_reported_state(self):
        self.assertion["evidence"]["observation_ids"] = []
        self.check()
        self.assertEqual(integrity.errors, [])

    def test_foreign_observation_is_rejected(self):
        self.assertion["evidence"]["observation_ids"] = [OBS_B]
        self.check()
        self.assertEqual(integrity.errors, [
            ASSERTION + ": evidence observation belongs to a source not cited in source_ids: " + repr(OBS_B)
        ])

    def test_observed_state_fails_closed_without_typed_target(self):
        self.assertion["state"] = "observed"
        self.check()
        self.assertEqual(integrity.errors, [
            ASSERTION + ": state 'observed' requires typed observation/reconciliation "
            "target support; current source observations record retrieval/inspection only"
        ])

    def test_reconciled_state_fails_closed_without_typed_target(self):
        self.assertion["state"] = "reconciled"
        self.check()
        self.assertEqual(integrity.errors, [
            ASSERTION + ": state 'reconciled' requires typed observation/reconciliation "
            "target support; current source observations record retrieval/inspection only"
        ])

    def test_direct_evidence_guard_cannot_disappear_silently(self):
        with patch.object(
            integrity,
            "DIRECT_EVIDENCE_STATES_MODEL",
            ("ASSERTION_MODEL.md", "## 99. Missing direct-evidence boundary"),
        ):
            self.check()
        self.assertTrue(any(
            "direct-evidence boundary section missing or empty" in item
            for item in integrity.errors
        ))

    def test_unsupported_checked_rejects_empty_aperture(self):
        self.assertion["state"] = "unsupported_in_sources_checked"
        self.assertion["evidence"] = {"source_ids": [], "observation_ids": []}
        self.check()
        self.assertIn(
            ASSERTION + ": unsupported_in_sources_checked requires a non-empty evidence.source_ids list",
            integrity.errors,
        )
        self.assertIn(
            ASSERTION + ": unsupported_in_sources_checked requires a non-empty evidence.observation_ids list",
            integrity.errors,
        )

    def test_unsupported_checked_rejects_failed_retrieval(self):
        self.assertion["state"] = "unsupported_in_sources_checked"
        self.observation(SOURCE_A, OBS_A)["outcome"] = "failed"
        self.check()
        self.assertEqual(integrity.errors, [
            ASSERTION + ": unsupported_in_sources_checked counts source(s) without an inspected "
            "evidence observation as checked: " + repr([SOURCE_A])
        ])

    def test_unsupported_checked_rejects_citation_only_observation(self):
        self.assertion["state"] = "unsupported_in_sources_checked"
        self.observation(SOURCE_A, OBS_A)["outcome"] = "referenced_by_record"
        self.check()
        self.assertEqual(integrity.errors, [
            ASSERTION + ": unsupported_in_sources_checked counts source(s) without an inspected "
            "evidence observation as checked: " + repr([SOURCE_A])
        ])

    def test_unsupported_checked_accepts_bounded_partial_inspection(self):
        self.assertion["state"] = "unsupported_in_sources_checked"
        self.check()
        self.assertEqual(integrity.errors, [])

    def test_unsupported_checked_requires_each_counted_source_inspected(self):
        self.assertion["state"] = "unsupported_in_sources_checked"
        self.assertion["evidence"]["source_ids"].append(SOURCE_B)
        self.check()
        self.assertEqual(integrity.errors, [
            ASSERTION + ": unsupported_in_sources_checked counts source(s) without an inspected "
            "evidence observation as checked: " + repr([SOURCE_B])
        ])


if __name__ == "__main__":
    unittest.main()
