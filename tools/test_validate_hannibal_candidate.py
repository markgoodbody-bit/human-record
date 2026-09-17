"""Run one unpromoted historical-person fixture through existing validators.

Production registries/catalogue are read only. No new schema or pass override.
"""
import copy
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import validate_integrity as integrity
import validate_operational as operational

ROOT = Path(__file__).resolve().parents[1]


class HannibalCandidateProbe(unittest.TestCase):
    def setUp(self):
        fixture = json.loads((ROOT / "tools/fixtures/hannibal-candidate.json").read_text(encoding="utf-8"))
        self.documents = {rel: json.loads((ROOT / rel).read_text(encoding="utf-8")) for rel in (
            "records/catalog.json", "registry/entities.json", "registry/sources.json",
            "registry/mentions.json", "registry/source-checks.json", "registry/assertions.json")}
        for rel, key, item in (
            ("registry/entities.json", "entities", "entity"),
            ("registry/sources.json", "sources", "source"),
            ("registry/mentions.json", "mentions", "mention"),
            ("registry/assertions.json", "assertions", "assertion")):
            self.documents[rel][key].append(fixture[item])
        self.fixture = fixture
        integrity.errors.clear()
        integrity.warnings.clear()
        integrity._vocabulary_cache.clear()
        self.addCleanup(integrity.errors.clear)
        self.addCleanup(integrity.warnings.clear)
        self.addCleanup(integrity._vocabulary_cache.clear)

    def test_entity_source_assertion_fit_without_new_vocabulary(self):
        with patch.object(integrity, "ROOT", ROOT), \
             patch.object(integrity, "load_json", side_effect=lambda rel: copy.deepcopy(self.documents[rel])):
            records = integrity.check_catalog()
            entities = integrity.check_entities()
            sources, observations = integrity.check_sources(records)
            assertions = integrity.check_assertions(records, entities, sources, observations)
        self.assertEqual(integrity.errors, [])
        self.assertIn(self.fixture["assertion"]["id"], assertions)

    def test_unpublished_mention_exposes_catalogue_dependency(self):
        with patch.object(operational, "load_object", side_effect=lambda root, rel: copy.deepcopy(self.documents[rel])):
            errors, _ = operational.validate(ROOT)
        self.assertEqual(errors, [
            self.fixture["mention"]["id"] + ": unknown record_id 'hannibal-candidate-not-published'"
        ])

    def test_no_false_resolution_to_make_fixture_pass(self):
        self.assertEqual(self.fixture["mention"]["status"], "candidate")
        self.assertEqual(self.fixture["assertion"]["state"], "reported_by_source")
        self.assertNotIn(self.fixture["mention"]["record_id"],
                         {record["id"] for record in self.documents["records/catalog.json"]["records"]})

    def test_source_anchored_candidate_without_public_record(self):
        mention = self.documents["registry/mentions.json"]["mentions"][-1]
        del mention["record_id"]
        with patch.object(operational, "load_object", side_effect=lambda root, rel: copy.deepcopy(self.documents[rel])):
            errors, _ = operational.validate(ROOT)
        self.assertEqual(errors, [])
        self.assertEqual(mention["status"], "candidate")
        self.assertEqual(len(self.documents["records/catalog.json"]["records"]),
                         len(json.loads((ROOT / "records/catalog.json").read_text(encoding="utf-8"))["records"]))


if __name__ == "__main__":
    unittest.main()
