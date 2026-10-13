"""Flak reader source-access controls: historically inspected is not endorsed access."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PUBLISHER = "https://kansaspress.ku.edu/9780700614202/"
HISTORICAL = {
    "westermann-2001-selected-passage": "prussia.online",
    "westermann-2001-targeted-book-search": "murrellsmodels.co.uk",
}

class FlakHistoricalCarrierTests(unittest.TestCase):
    def test_current_human_routes_exclude_complete_copy_link_promotion(self):
        md = (ROOT / "cases/viral-flak-claim.md").read_text(encoding="utf-8")
        html = (ROOT / "records/flak-claim.html").read_text(encoding="utf-8")
        self.assertIn(PUBLISHER, md)
        self.assertIn(PUBLISHER, html)
        for host in HISTORICAL.values():
            self.assertIn(host, md)
            self.assertNotIn("https://" + host, md)
            self.assertNotIn("https://www." + host, md)
            self.assertNotIn("https://" + host, html)
            self.assertNotIn("https://www." + host, html)
        for s in (md, html):
            self.assertIn("UNKNOWN", s)
            self.assertIn("historical", s.lower())
            self.assertIn("not", s.lower())

    def test_machine_provenance_keeps_both_exact_original_carriers(self):
        j = json.loads((ROOT / "cases/viral-flak-claim.json").read_text(encoding="utf-8"))
        reg = json.loads((ROOT / "registry/sources.json").read_text(encoding="utf-8"))
        self.assertEqual(j["record_version"], "0.2.8")
        west = [x for x in reg["sources"] if x.get("title") == "Flak: German Anti-Aircraft Defenses, 1914–1945"]
        self.assertEqual(len(west), 1)
        source = west[0]
        self.assertEqual(source["locators"][0]["value"], PUBLISHER)
        self.assertIn("UNKNOWN", source["preservation"]["note"])
        locators = {x.get("value"): x for x in source["locators"]}
        for node_id, host in HISTORICAL.items():
            nodes = [x for x in j["nodes"] if x.get("id") == node_id]
            self.assertEqual(len(nodes), 1)
            node = nodes[0]
            self.assertIn(host, node["url"])
            self.assertIn("UNKNOWN", node["role"])
            self.assertIn(node["url"], locators)
            self.assertIn("rights_unknown", locators[node["url"]]["status"])
        self.assertEqual(j["historical_truth_status"], "unknown")
        self.assertEqual(j["status"], "unsupported_in_sources_checked")
        self.assertTrue(any("rights" in s.lower() or "authoris" in s.lower() for s in j["unknowns"]))
        self.assertIn("Revision 0.2.7", (ROOT / "cases/viral-flak-claim.md").read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
