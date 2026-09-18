"""Issue #40 follow-on: executable probe for identity-decision provenance.

These expected failures document the remaining model/validator seam after PR #41.
They are not production requirements yet. Removing an expectedFailure decorator
requires an earned contract and production repair, not merely making the test green.
"""
import json
from pathlib import Path
import tempfile
import unittest

import validate_operational as validator


class IdentityResolutionProvenanceProbe(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "records").mkdir()
        (self.root / "registry").mkdir()

        self.homer = "thr:entity:da243807-2e4e-44a5-86bc-aa8b8d4f23fb"
        self.other = "thr:entity:ccdb0a44-1893-448d-a7fc-631e18d829cf"
        self.source = "thr:source:fb6063f7-6e0d-4f87-9a9c-c5e5d001d724"
        self.observation = "thr:observation:28fb29f3-ba69-44b4-a96c-c87db4e11bbe"
        self.mention_id = "thr:mention:911dddc8-21ed-44e2-b6f2-58cff24c9fda"
        self.assertion_id = "thr:assertion:844f548d-80b8-4f25-a03b-d39e812f1ede"

        self.candidate = {
            "entity_id": self.homer,
            "state": "resolved_as",
            "basis": [
                "same literal creator name in the owner record and the existing specimen reconciliation"
            ],
            "conflicts": [],
        }
        self.mention = {
            "id": self.mention_id,
            "literal": "Winslow Homer",
            "source_id": self.source,
            "observation_id": self.observation,
            "record_id": "camp-fire-1880",
            "status": "resolved",
            "candidates": [self.candidate],
        }
        self.source_check = {
            "id": "thr:source-check:25463bdb-35a4-4744-a1ba-d0f047b2e482",
            "source_id": self.source,
            "checked_at": "2026-09-18",
            "locator": "https://example.org/met",
            "outcome": "live_locator_retrieved",
            "fingerprint": None,
            "record_evidence_promoted": False,
        }
        self.assertion = {
            "id": self.assertion_id,
            "subject": {"mention_id": self.mention_id},
            "predicate": "identity_resolution_basis",
            "object": {"entity_id": self.homer},
            "state": "inferred",
            "evidence": {
                "source_ids": [self.source],
                "observation_ids": [self.observation],
            },
            "scope": {
                "meaning": "synthetic proposed machine-addressable basis for this probe"
            },
            "record_links": [],
            "corrections": [],
        }
        self.write()

    def write(self):
        (self.root / "records/catalog.json").write_text(
            json.dumps({
                "mention_registry": "https://thehumanrecord.net/registry/mentions.json",
                "source_check_registry": "https://thehumanrecord.net/registry/source-checks.json",
                "records": [{"id": "camp-fire-1880"}],
            }),
            encoding="utf-8",
        )
        (self.root / "registry/entities.json").write_text(
            json.dumps({"entities": [{"id": self.homer}, {"id": self.other}]}),
            encoding="utf-8",
        )
        (self.root / "registry/sources.json").write_text(
            json.dumps({"sources": [{
                "id": self.source,
                "observations": [{"id": self.observation}],
            }]}),
            encoding="utf-8",
        )
        (self.root / "registry/mentions.json").write_text(
            json.dumps({"mentions": [self.mention]}),
            encoding="utf-8",
        )
        (self.root / "registry/source-checks.json").write_text(
            json.dumps({"checks": [self.source_check]}),
            encoding="utf-8",
        )
        # validate_operational does not currently read this registry. It is
        # present so proposed assertion-linked shapes are explicit in the probe.
        (self.root / "registry/assertions.json").write_text(
            json.dumps({"assertions": [self.assertion]}),
            encoding="utf-8",
        )

    def errors(self):
        self.write()
        return validator.validate(self.root)[0]

    def test_current_public_shape_still_passes(self):
        self.assertEqual(self.errors(), [])

    @unittest.expectedFailure
    def test_model_basis_is_not_yet_enforced(self):
        # IDENTITY_MODEL §5 says each proposed link should carry a basis.
        # Current operational validation accepts a decisive resolution without one.
        self.candidate.pop("basis")
        self.assertTrue(self.errors())

    @unittest.expectedFailure
    def test_candidate_evidence_state_is_not_a_supported_parallel_epistemology(self):
        # Issue #40 V6: a candidate-local direct-evidence word is ignored.
        # Desired direction is fail closed or route through the assertion model,
        # not invent a second evidence-state system here.
        self.candidate["evidence_state"] = "observed"
        self.assertTrue(self.errors())

    @unittest.expectedFailure
    def test_dangling_basis_assertion_reference_is_not_yet_checked(self):
        # Candidate -> assertion is a design hypothesis, not production syntax.
        # If this shape is adopted, a dangling reference must not validate.
        self.candidate["basis_assertion_ids"] = [
            "thr:assertion:11111111-1111-4111-8111-111111111111"
        ]
        self.assertTrue(self.errors())

    @unittest.expectedFailure
    def test_relevant_basis_assertion_is_not_yet_distinguished_from_free_text(self):
        # This is the positive half of the design hypothesis: a decisive
        # resolution could point at a separately evidence-bearing assertion
        # connecting this mention and candidate entity. Current validator ignores it.
        self.candidate["basis_assertion_ids"] = [self.assertion_id]
        # If/when the field is earned, a validator should at least recognise it
        # as typed structure rather than treating it exactly like its absence.
        before = self.errors()
        self.candidate.pop("basis_assertion_ids")
        after = self.errors()
        self.assertNotEqual(before, after)


if __name__ == "__main__":
    unittest.main()
