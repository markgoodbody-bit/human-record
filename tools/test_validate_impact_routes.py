import json
from pathlib import Path
import tempfile
import unittest

import impact_routes


class ImpactRouteTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "records").mkdir()
        (self.root / "registry").mkdir()

        self.source_id = "thr:source:11111111-1111-4111-8111-111111111111"
        self.other_source_id = "thr:source:22222222-2222-4222-8222-222222222222"

        self.catalog = {
            "records": [
                {
                    "id": "record-a",
                    "full_human_record": "https://thehumanrecord.net/cases/a.md",
                    "machine_record": "https://thehumanrecord.net/cases/a.json",
                    "human_view": "https://thehumanrecord.net/records/a.html",
                },
                {
                    "id": "record-b",
                    "full_human_record": "https://thehumanrecord.net/cases/b.md",
                    "machine_record": "https://thehumanrecord.net/cases/b.json",
                    "human_view": "https://thehumanrecord.net/records/b.html",
                },
            ]
        }
        self.sources = {
            "sources": [
                {
                    "id": self.source_id,
                    "title": "Fixture source",
                    "used_by_records": ["record-a"],
                },
                {
                    "id": self.other_source_id,
                    "title": "Other source",
                    "used_by_records": [],
                },
            ]
        }
        self.assertions = {"assertions": []}
        self.write()

    def write(self):
        (self.root / "records/catalog.json").write_text(
            json.dumps(self.catalog), encoding="utf-8"
        )
        (self.root / "registry/sources.json").write_text(
            json.dumps(self.sources), encoding="utf-8"
        )
        (self.root / "registry/assertions.json").write_text(
            json.dumps(self.assertions), encoding="utf-8"
        )

    def add_assertion(self, source_id, record_links, assertion_id="a1"):
        self.assertions["assertions"].append({
            "id": assertion_id,
            "predicate": "fixture_predicate",
            "evidence": {"source_ids": [source_id], "observation_ids": []},
            "record_links": record_links,
        })
        self.write()

    def test_direct_record_route_survives_without_assertion_edge(self):
        result = impact_routes.derive_impact_routes(self.root, self.source_id)
        self.assertEqual(result["assertion_routes"], [])
        self.assertEqual(result["affected_records"], ["record-a"])
        self.assertIn("NO_ASSERTION_EDGE != NO_RECORD_DEPENDENCY", result["ceilings"])

    def test_unknown_direct_record_is_visible_not_silently_dropped(self):
        self.sources["sources"][0]["used_by_records"].append("missing-record")
        self.write()
        result = impact_routes.derive_impact_routes(self.root, self.source_id)
        self.assertEqual(result["affected_records"], ["record-a"])
        self.assertEqual(result["unresolved_direct_used_by_records"], ["missing-record"])

    def test_malformed_direct_routes_fail_loudly(self):
        for value in ("record-b", None, ["record-a", 42], [""]):
            with self.subTest(value=value):
                self.sources["sources"][0]["used_by_records"] = value
                self.write()
                with self.assertRaises(ValueError):
                    impact_routes.derive_impact_routes(self.root, self.source_id)

    def test_assertion_route_adds_second_record(self):
        self.add_assertion(self.source_id, ["cases/b.md"])
        result = impact_routes.derive_impact_routes(self.root, self.source_id)
        self.assertEqual(result["direct_used_by_records"], ["record-a"])
        self.assertEqual(result["assertion_derived_records"], ["record-b"])
        self.assertEqual(result["affected_records"], ["record-a", "record-b"])

    def test_union_deduplicates_direct_and_assertion_route(self):
        self.add_assertion(self.source_id, ["cases/a.json"])
        result = impact_routes.derive_impact_routes(self.root, self.source_id)
        self.assertEqual(result["affected_records"], ["record-a"])

    def test_assertion_only_source_can_still_route_to_record(self):
        self.add_assertion(self.other_source_id, ["cases/b.json"])
        result = impact_routes.derive_impact_routes(self.root, self.other_source_id)
        self.assertEqual(result["direct_used_by_records"], [])
        self.assertEqual(result["affected_records"], ["record-b"])

    def test_unresolved_record_link_is_visible_not_silently_dropped(self):
        self.add_assertion(self.source_id, ["cases/missing.json"])
        result = impact_routes.derive_impact_routes(self.root, self.source_id)
        self.assertEqual(result["affected_records"], ["record-a"])
        self.assertEqual(result["unresolved_record_links"], [{
            "assertion_id": "a1",
            "record_link": "cases/missing.json",
        }])

    def test_malformed_assertion_record_links_fail_loudly(self):
        for value in ("cases/b.json", None, ["cases/b.json", 42], [""]):
            with self.subTest(value=value):
                self.assertions = {"assertions": []}
                self.add_assertion(self.source_id, value)
                with self.assertRaises(ValueError):
                    impact_routes.derive_impact_routes(self.root, self.source_id)

    def test_unknown_source_rejected(self):
        with self.assertRaises(KeyError):
            impact_routes.derive_impact_routes(
                self.root,
                "thr:source:99999999-9999-4999-8999-999999999999",
            )

    def test_public_url_and_repo_path_normalize_to_same_record(self):
        self.add_assertion(
            self.source_id,
            [
                "https://thehumanrecord.net/cases/b.md",
                "cases/b.json",
            ],
        )
        result = impact_routes.derive_impact_routes(self.root, self.source_id)
        self.assertEqual(result["assertion_derived_records"], ["record-b"])

    def test_foreign_origin_cannot_resolve_by_matching_path(self):
        self.add_assertion(
            self.source_id,
            ["https://unrelated.example/cases/b.json"],
        )
        result = impact_routes.derive_impact_routes(self.root, self.source_id)
        self.assertEqual(result["affected_records"], ["record-a"])
        self.assertEqual(result["unresolved_record_links"], [{
            "assertion_id": "a1",
            "record_link": "https://unrelated.example/cases/b.json",
        }])

    def test_public_origin_rejects_credentials_port_and_wrong_scheme(self):
        links = [
            "http://thehumanrecord.net/cases/b.json",
            "https://user@thehumanrecord.net/cases/b.json",
            "https://thehumanrecord.net:443/cases/b.json",
        ]
        for link in links:
            with self.subTest(link=link):
                self.assertions = {"assertions": []}
                self.add_assertion(self.source_id, [link])
                result = impact_routes.derive_impact_routes(self.root, self.source_id)
                self.assertEqual(result["affected_records"], ["record-a"])
                self.assertEqual(result["unresolved_record_links"][0]["record_link"], link)

    def test_query_and_fragment_policy_is_consistent(self):
        links = [
            "cases/b.json#part",
            "https://thehumanrecord.net/cases/b.json#part",
            "cases/b.json?version=2",
            "https://thehumanrecord.net/cases/b.json?version=2",
        ]
        for link in links:
            with self.subTest(link=link):
                self.assertions = {"assertions": []}
                self.add_assertion(self.source_id, [link])
                result = impact_routes.derive_impact_routes(self.root, self.source_id)
                self.assertEqual(result["affected_records"], ["record-a"])
                self.assertEqual(result["unresolved_record_links"][0]["record_link"], link)

    def test_duplicate_catalogue_path_across_records_is_rejected(self):
        self.catalog["records"][1]["machine_record"] = (
            "https://thehumanrecord.net/cases/a.json"
        )
        self.write()
        with self.assertRaises(ValueError):
            impact_routes.derive_impact_routes(self.root, self.source_id)

    def test_repeated_catalogue_path_within_same_record_is_safe(self):
        self.catalog["records"][0]["human_view"] = (
            "https://thehumanrecord.net/cases/a.json"
        )
        self.write()
        result = impact_routes.derive_impact_routes(self.root, self.source_id)
        self.assertEqual(result["affected_records"], ["record-a"])


if __name__ == "__main__":
    unittest.main()
