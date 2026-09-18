"""Contract checks for the optional portable contribution packet."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "contribution-packet.schema.json").read_text(encoding="utf-8"))
EXAMPLE = json.loads((ROOT / "examples" / "grok-flak-relay.packet.json").read_text(encoding="utf-8"))


class ContributionPacketTests(unittest.TestCase):
    def test_format_and_authentication_ceiling_are_fixed(self):
        self.assertEqual(
            SCHEMA["properties"]["format"]["const"],
            "human-record-contribution-packet/0.1",
        )
        self.assertEqual(
            SCHEMA["properties"]["authentication_ceiling"]["const"],
            "packet_is_not_identity_or_source_authentication",
        )
        self.assertEqual(EXAMPLE["format"], SCHEMA["properties"]["format"]["const"])
        self.assertEqual(
            EXAMPLE["authentication_ceiling"],
            SCHEMA["properties"]["authentication_ceiling"]["const"],
        )

    def test_required_top_level_fields_exist_in_example(self):
        for key in SCHEMA["required"]:
            self.assertIn(key, EXAMPLE, key)

    def test_relay_provenance_is_explicit(self):
        self.assertTrue(EXAMPLE["relay"]["relayed"])
        self.assertTrue(EXAMPLE["relay"]["relayed_by"])
        self.assertTrue(EXAMPLE["relay"]["medium"])
        self.assertIn("not independently verified", EXAMPLE["relay"]["notes"])

    def test_source_check_status_is_attributed_not_boolean(self):
        evidence_schema = SCHEMA["properties"]["evidence"]["items"]
        allowed = set(evidence_schema["properties"]["source_check_status"]["enum"])
        self.assertEqual(
            allowed,
            {"reported_checked", "reported_not_checked", "unknown"},
        )
        self.assertNotIn("checked_by_contributor", evidence_schema["properties"])
        states = {
            row["label"]: row["source_check_status"]
            for row in EXAMPLE["evidence"]
        }
        self.assertEqual(
            states["Edward B. Westermann, Flak: German Anti-Aircraft Defenses, 1914–1945"],
            "reported_checked",
        )
        self.assertEqual(
            states["Bundesarchiv-Militärarchiv / personnel and unit-level flak casualty holdings"],
            "reported_not_checked",
        )

    def test_availability_is_time_bounded_to_receipt(self):
        contributor_schema = SCHEMA["properties"]["declared_contributor"]
        self.assertIn("availability_at_receipt", contributor_schema["properties"])
        self.assertNotIn("availability", contributor_schema["properties"])
        self.assertIn("availability_at_receipt", EXAMPLE["declared_contributor"])
        self.assertNotIn("availability", EXAMPLE["declared_contributor"])

    def test_unknowns_and_not_checked_are_not_empty(self):
        self.assertGreater(len(EXAMPLE["unknowns"]), 0)
        self.assertGreater(len(EXAMPLE["not_checked"]), 0)

    def test_packet_does_not_claim_private_transcript_is_public(self):
        self.assertFalse(
            EXAMPLE["rights_and_privacy"]["contains_private_personal_information"]
        )
        self.assertIn(
            "not the full private exchange",
            EXAMPLE["rights_and_privacy"]["notes"],
        )

    def test_schema_keeps_packet_optional_and_non_record(self):
        self.assertNotIn("contribution_packet", SCHEMA.get("required", []))
        self.assertIn("Optional relay envelope", SCHEMA["description"])

    def test_evidence_rows_keep_locator_nullable_for_lost_citations(self):
        locator_type = SCHEMA["properties"]["evidence"]["items"]["properties"]["locator"]["type"]
        self.assertIn("null", locator_type)
        self.assertIsNone(EXAMPLE["evidence"][0]["locator"])


if __name__ == "__main__":
    unittest.main()
