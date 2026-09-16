import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import validate_operational as validator


class OperationalRegistryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "records").mkdir()
        (self.root / "registry").mkdir()
        self.entity = "thr:entity:da243807-2e4e-44a5-86bc-aa8b8d4f23fb"
        self.source = "thr:source:47f0817a-3cae-4ded-98eb-320332a72bd5"
        self.observation = "thr:observation:28fb29f3-ba69-44b4-a96c-c87db4e11bbe"
        self.mention = {
            "id": "thr:mention:911dddc8-21ed-44e2-b6f2-58cff24c9fda",
            "literal": "Example",
            "source_id": self.source,
            "observation_id": self.observation,
            "record_id": "r1",
            "status": "resolved",
            "candidates": [{"entity_id": self.entity, "state": "resolved_as"}],
        }
        self.check = {
            "id": "thr:source-check:25463bdb-35a4-4744-a1ba-d0f047b2e482",
            "source_id": self.source,
            "checked_at": "2026-09-16",
            "locator": "https://example.org/",
            "outcome": "live_locator_retrieved",
            "fingerprint": None,
            "record_evidence_promoted": False,
        }
        self.write()

    def write(self):
        (self.root / "records/catalog.json").write_text(json.dumps({"records": [{"id": "r1"}]}), encoding="utf-8")
        (self.root / "registry/entities.json").write_text(json.dumps({"entities": [{"id": self.entity}]}), encoding="utf-8")
        (self.root / "registry/sources.json").write_text(json.dumps({"sources": [{"id": self.source, "observations": [{"id": self.observation}]}]}), encoding="utf-8")
        (self.root / "registry/mentions.json").write_text(json.dumps({"mentions": [self.mention]}), encoding="utf-8")
        (self.root / "registry/source-checks.json").write_text(json.dumps({"checks": [self.check]}), encoding="utf-8")

    def test_valid_fixture(self):
        errors, counts = validator.validate(self.root)
        self.assertEqual(errors, [])
        self.assertEqual(counts, {"mentions": 1, "source_checks": 1})

    def test_unknown_entity_rejected(self):
        self.mention["candidates"][0]["entity_id"] = "thr:entity:11111111-1111-4111-8111-111111111111"
        self.write()
        self.assertTrue(validator.validate(self.root)[0])

    def test_resolved_requires_exactly_one_resolved_candidate(self):
        self.mention["candidates"] = []
        self.write()
        self.assertTrue(any("exactly one" in e for e in validator.validate(self.root)[0]))

    def test_unresolved_can_have_no_candidate(self):
        self.mention["status"] = "unresolved_not_required"
        self.mention["candidates"] = []
        self.write()
        self.assertEqual(validator.validate(self.root)[0], [])

    def test_unknown_source_rejected(self):
        self.check["source_id"] = "thr:source:11111111-1111-4111-8111-111111111111"
        self.write()
        self.assertTrue(validator.validate(self.root)[0])

    def test_promoted_evidence_requires_observation(self):
        self.check["record_evidence_promoted"] = True
        self.write()
        self.assertTrue(any("promoted evidence" in e for e in validator.validate(self.root)[0]))

    def test_bad_json_root_rejected(self):
        (self.root / "registry/mentions.json").write_text("[]", encoding="utf-8")
        self.assertTrue(validator.validate(self.root)[0])


if __name__ == "__main__":
    unittest.main()
