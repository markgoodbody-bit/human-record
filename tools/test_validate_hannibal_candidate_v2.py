"""Bounded historical-human candidate against current production validators.

No production registry or catalogue object is written by these tests.
"""
import copy
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import validate_integrity as integrity
import validate_operational as operational

ROOT = Path(__file__).resolve().parents[1]


class HannibalCandidateV2Probe(unittest.TestCase):
    def setUp(self):
        self.fixture = json.loads(
            (ROOT / "tools/fixtures/hannibal-candidate-v2.json").read_text(encoding="utf-8")
        )
        self.documents = {
            rel: json.loads((ROOT / rel).read_text(encoding="utf-8"))
            for rel in (
                "records/catalog.json",
                "registry/entities.json",
                "registry/sources.json",
                "registry/mentions.json",
                "registry/source-checks.json",
                "registry/assertions.json",
            )
        }
        self.documents["registry/entities.json"]["entities"].append(copy.deepcopy(self.fixture["entity"]))
        self.documents["registry/sources.json"]["sources"].extend(copy.deepcopy(self.fixture["sources"]))
        self.documents["registry/mentions.json"]["mentions"].append(copy.deepcopy(self.fixture["mention"]))
        self.documents["registry/assertions.json"]["assertions"].extend(copy.deepcopy(self.fixture["assertions"]))

        integrity.errors.clear()
        integrity.warnings.clear()
        integrity._vocabulary_cache.clear()
        self.addCleanup(integrity.errors.clear)
        self.addCleanup(integrity.warnings.clear)
        self.addCleanup(integrity._vocabulary_cache.clear)

    def check_integrity(self):
        with patch.object(integrity, "ROOT", ROOT), patch.object(
            integrity, "load_json", side_effect=lambda rel: copy.deepcopy(self.documents[rel])
        ):
            records = integrity.check_catalog()
            entities = integrity.check_entities()
            sources, observations = integrity.check_sources(records)
            return integrity.check_assertions(records, entities, sources, observations)

    def test_current_envelopes_accept_candidate_without_new_vocabulary(self):
        assertions = self.check_integrity()
        self.assertEqual(integrity.errors, [])
        self.assertTrue({a["id"] for a in self.fixture["assertions"]} <= assertions)

    def test_every_candidate_assertion_stays_source_reported(self):
        self.assertEqual(
            {a["state"] for a in self.fixture["assertions"]},
            {"reported_by_source"},
        )

    def test_uninspected_attested_historians_are_not_fake_source_objects(self):
        titles = {s["title"] for s in self.fixture["sources"]}
        self.assertFalse(any("Sosylus" in title or "Silenus" in title for title in titles))
        self.assertEqual(
            self.fixture["inspection_boundary"]["sosylus_complete_work"],
            "not_inspected_and_not_represented_as_a_source_object",
        )

    def test_default_public_validation_rejects_unpublished_record_id(self):
        with patch.object(
            operational, "load_object", side_effect=lambda root, rel: copy.deepcopy(self.documents[rel])
        ):
            errors, _ = operational.validate(ROOT)
        self.assertEqual(errors, [
            self.fixture["mention"]["id"] + ": unknown record_id 'hannibal-candidate-not-published'"
        ])

    def test_explicit_isolated_research_mode_accepts_recordless_source_anchored_mention(self):
        mention = self.documents["registry/mentions.json"]["mentions"][-1]
        del mention["record_id"]
        with patch.object(
            operational, "load_object", side_effect=lambda root, rel: copy.deepcopy(self.documents[rel])
        ):
            errors, _ = operational.validate(ROOT, allow_uncatalogued_mentions=True)
        self.assertEqual(errors, [])
        self.assertEqual(mention["status"], "candidate")

    def test_candidate_does_not_change_public_catalogue_count(self):
        public_count = len(json.loads((ROOT / "records/catalog.json").read_text(encoding="utf-8"))["records"])
        self.assertEqual(
            len(self.documents["records/catalog.json"]["records"]),
            public_count,
        )
        self.assertEqual(public_count, 3)


if __name__ == "__main__":
    unittest.main()
