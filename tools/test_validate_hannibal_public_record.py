"""Public record 4 contract checks for the Hannibal source-survival encounter."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
RECORD_ID = "hannibal-source-survival"
ENTITY_ID = "thr:entity:68be4504-74ab-48a5-81e3-95fb30242db0"
NEPOS_SOURCE = "thr:source:8d40b5c1-3eb6-47d3-86e2-48e95853e930"
POLYBIUS_SOURCE = "thr:source:7a1b2e15-a9b2-4af4-9e0b-2c44b10eb9d2"

class HannibalPublicRecordTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((ROOT / "records/catalog.json").read_text(encoding="utf-8"))
        cls.machine = json.loads((ROOT / "cases/hannibal-barca.json").read_text(encoding="utf-8"))
        cls.entities = json.loads((ROOT / "registry/entities.json").read_text(encoding="utf-8"))
        cls.sources = json.loads((ROOT / "registry/sources.json").read_text(encoding="utf-8"))
        cls.mentions = json.loads((ROOT / "registry/mentions.json").read_text(encoding="utf-8"))
        cls.assertions = json.loads((ROOT / "registry/assertions.json").read_text(encoding="utf-8"))
        cls.checks = json.loads((ROOT / "registry/source-checks.json").read_text(encoding="utf-8"))

    def test_catalogue_has_exactly_four_public_records_and_hannibal_route(self):
        self.assertEqual(len(self.catalog["records"]), 4)
        row = next(r for r in self.catalog["records"] if r["id"] == RECORD_ID)
        self.assertEqual(row["machine_record"], "https://thehumanrecord.net/cases/hannibal-barca.json")
        self.assertEqual(row["human_view"], "https://thehumanrecord.net/records/hannibal.html")

    def test_machine_record_keeps_two_source_mentions_separate(self):
        self.assertEqual(self.machine["record_id"], RECORD_ID)
        self.assertEqual(self.machine["record_version"], "0.1.2")
        self.assertEqual(len(self.machine["mentions"]), 2)
        self.assertEqual({m["literal"] for m in self.machine["mentions"]}, {"Hannibal"})
        self.assertEqual({m["source_id"] for m in self.machine["mentions"]}, {NEPOS_SOURCE, POLYBIUS_SOURCE})
        self.assertEqual({m["status"] for m in self.machine["mentions"]}, {"candidate"})
        for mention in self.machine["mentions"]:
            self.assertEqual(len(mention["candidates"]), 1)
            self.assertEqual(mention["candidates"][0]["entity_id"], ENTITY_ID)
            self.assertEqual(mention["candidates"][0]["state"], "candidate")
            self.assertTrue(mention["candidates"][0]["basis"])

    def test_all_historical_assertions_remain_source_attributed(self):
        self.assertEqual(len(self.machine["assertions"]), 5)
        self.assertEqual({a["state"] for a in self.machine["assertions"]}, {"reported_by_source"})
        self.assertTrue(all(a["evidence"]["source_ids"] for a in self.machine["assertions"]))
        self.assertTrue(all(a["evidence"]["observation_ids"] for a in self.machine["assertions"]))

    def test_registry_copies_match_public_machine_objects(self):
        entity = next(e for e in self.entities["entities"] if e["id"] == ENTITY_ID)
        self.assertEqual(entity, self.machine["entity"])
        for item in self.machine["sources"]:
            self.assertEqual(next(s for s in self.sources["sources"] if s["id"] == item["id"]), item)
        for item in self.machine["mentions"]:
            self.assertEqual(next(m for m in self.mentions["mentions"] if m["id"] == item["id"]), item)
        for item in self.machine["assertions"]:
            self.assertEqual(next(a for a in self.assertions["assertions"] if a["id"] == item["id"]), item)

    def test_fresh_source_checks_do_not_claim_record_evidence_promotion(self):
        relevant = [c for c in self.checks["checks"] if c["source_id"] in {NEPOS_SOURCE, POLYBIUS_SOURCE}]
        self.assertEqual(len(relevant), 2)
        self.assertEqual({c["outcome"] for c in relevant}, {"live_locator_retrieved"})
        self.assertEqual({c["record_evidence_promoted"] for c in relevant}, {False})

    def test_human_page_is_public_not_proposal_and_has_view_basis(self):
        page = (ROOT / "records/hannibal.html").read_text(encoding="utf-8")
        self.assertIn('content="index,follow"', page)
        self.assertIn("Historical-person source survival · Record 4", page)
        self.assertIn("View basis:", page)
        self.assertNotIn("not public record 4", page.lower())
        self.assertNotIn("noindex,nofollow", page)

if __name__ == "__main__":
    unittest.main()
