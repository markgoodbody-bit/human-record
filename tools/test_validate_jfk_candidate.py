"""Contested-event probe; real bounded report attributions, synthetic mutations.

No production object is written. Passing syntax does not adjudicate JFK.
"""
import copy
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import validate_integrity as integrity
import validate_operational as operational

ROOT = Path(__file__).resolve().parents[1]


class JFKCandidateProbe(unittest.TestCase):
    def setUp(self):
        self.fixture = json.loads((ROOT / "tools/fixtures/jfk-contested-candidate.json").read_text(encoding="utf-8"))
        self.documents = {rel: json.loads((ROOT / rel).read_text(encoding="utf-8")) for rel in (
            "records/catalog.json", "registry/entities.json", "registry/sources.json",
            "registry/mentions.json", "registry/source-checks.json", "registry/assertions.json")}
        for kind in ("entities", "sources", "assertions"):
            self.documents[f"registry/{kind}.json"][kind].extend(copy.deepcopy(self.fixture[kind]))
        self.documents["registry/mentions.json"]["mentions"].append(copy.deepcopy(self.fixture["mention"]))
        integrity.errors.clear()
        integrity.warnings.clear()
        integrity._vocabulary_cache.clear()
        self.addCleanup(integrity.errors.clear)
        self.addCleanup(integrity.warnings.clear)
        self.addCleanup(integrity._vocabulary_cache.clear)

    def check_integrity(self):
        with patch.object(integrity, "ROOT", ROOT), patch.object(
                integrity, "load_json", side_effect=lambda rel: copy.deepcopy(self.documents[rel])):
            records = integrity.check_catalog()
            entities = integrity.check_entities()
            sources, observations = integrity.check_sources(records)
            return integrity.check_assertions(records, entities, sources, observations)

    def test_reports_shared_referent_and_custody_fit_existing_envelopes(self):
        assertions = self.check_integrity()
        self.assertEqual(integrity.errors, [])
        self.assertTrue({a["id"] for a in self.fixture["assertions"]} <= assertions)
        a, b, film_a, film_b, custody, materials = self.fixture["assertions"]
        self.assertEqual(a["subject"], b["subject"])
        self.assertNotEqual(a["object"], b["object"])
        self.assertNotEqual(a["evidence"], b["evidence"])
        self.assertEqual(film_a["object"], film_b["object"])
        self.assertEqual({x["state"] for x in self.fixture["assertions"]}, {"reported_by_source"})
        self.assertEqual(len(self.fixture["sources"]), 4)  # Report pages only, no fake film observation.

    def test_unpublished_mention_has_same_catalogue_failure_as_hannibal(self):
        with patch.object(operational, "load_object", side_effect=lambda root, rel: copy.deepcopy(self.documents[rel])):
            errors, _ = operational.validate(ROOT)
        self.assertEqual(errors, [
            self.fixture["mention"]["id"] + ": unknown record_id 'jfk-candidate-not-published'"])

    def test_foreign_observation_is_rejected(self):
        target = self.documents["registry/assertions.json"]["assertions"][-6]
        target["evidence"]["observation_ids"] = [self.fixture["sources"][2]["observations"][0]["id"]]
        self.check_integrity()
        self.assertEqual(integrity.errors, [
            target["id"] + ": evidence observation belongs to a source not cited in source_ids: "
            + repr(target["evidence"]["observation_ids"][0])])

    def test_unresolved_source_mention_without_public_record(self):
        mention = self.documents["registry/mentions.json"]["mentions"][-1]
        del mention["record_id"]
        with patch.object(operational, "load_object", side_effect=lambda root, rel: copy.deepcopy(self.documents[rel])):
            errors, _ = operational.validate(ROOT, allow_uncatalogued_mentions=True)
        self.assertEqual(errors, [])
        self.assertEqual(mention["candidates"], [])
        self.assertEqual(mention["status"], "unresolved_not_required")

    def test_multiple_cited_sources_may_supply_observations(self):
        target = self.documents["registry/assertions.json"]["assertions"][-6]
        target["evidence"]["source_ids"].append(self.fixture["sources"][2]["id"])
        target["evidence"]["observation_ids"].append(self.fixture["sources"][2]["observations"][0]["id"])
        self.check_integrity()
        self.assertEqual(integrity.errors, [])

    def test_observation_without_cited_owner_is_rejected(self):
        target = self.documents["registry/assertions.json"]["assertions"][-6]
        target["evidence"]["source_ids"] = []
        self.check_integrity()
        self.assertEqual(len(integrity.errors), 1)
        self.assertIn("source not cited", integrity.errors[0])

    def test_source_only_evidence_remains_allowed(self):
        target = self.documents["registry/assertions.json"]["assertions"][-6]
        target["evidence"]["observation_ids"] = []
        self.check_integrity()
        self.assertEqual(integrity.errors, [])

    def test_unsupported_in_sources_checked_rejects_empty_checked_set(self):
        target = self.documents["registry/assertions.json"]["assertions"][-6]
        target["state"] = "unsupported_in_sources_checked"
        target["evidence"]["source_ids"] = []
        target["evidence"]["observation_ids"] = []
        self.check_integrity()
        self.assertEqual(integrity.errors, [
            target["id"] + ": unsupported_in_sources_checked requires a non-empty evidence.source_ids list",
            target["id"] + ": unsupported_in_sources_checked requires a non-empty evidence.observation_ids list",
        ])

    def test_unsupported_in_sources_checked_requires_observation_for_every_counted_source(self):
        target = self.documents["registry/assertions.json"]["assertions"][-6]
        target["state"] = "unsupported_in_sources_checked"
        second_source = self.fixture["sources"][2]
        target["evidence"]["source_ids"].append(second_source["id"])
        # Deliberately do not add second_source's observation.
        self.check_integrity()
        self.assertEqual(integrity.errors, [
            target["id"] + ": unsupported_in_sources_checked counts source(s) without an owned "
            "evidence observation as checked: " + repr([second_source["id"]])
        ])

    def test_unsupported_in_sources_checked_accepts_bounded_observed_source_set(self):
        target = self.documents["registry/assertions.json"]["assertions"][-6]
        target["state"] = "unsupported_in_sources_checked"
        second_source = self.fixture["sources"][2]
        target["evidence"]["source_ids"].append(second_source["id"])
        target["evidence"]["observation_ids"].append(second_source["observations"][0]["id"])
        self.check_integrity()
        self.assertEqual(integrity.errors, [])


if __name__ == "__main__":
    unittest.main()
