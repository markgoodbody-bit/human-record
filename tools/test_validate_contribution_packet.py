"""Contract checks for the optional portable contribution packet."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "contribution-packet.schema.json").read_text(encoding="utf-8"))
EXAMPLE = json.loads((ROOT / "examples" / "grok-flak-relay.packet.json").read_text(encoding="utf-8"))

class ContributionPacketTests(unittest.TestCase):
    def test_format_and_authentication_ceiling_are_fixed(self):
        self.assertEqual(SCHEMA["properties"]["format"]["const"], "human-record-contribution-packet/0.1")
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

    def test_checked_and_unchecked_sources_remain_distinct(self):
        states = {row["label"]: row["checked_by_contributor"] for row in EXAMPLE["evidence"]}
        self.assertTrue(states["Edward B. Westermann, Flak: German Anti-Aircraft Defenses, 1914–1945"])
        self.assertFalse(states["Bundesarchiv-Militärarchiv / personnel and unit-level flak casualty holdings"])

    def test_source_check_status_is_attributed_not_boolean(self):\n        allowed = set(SCHEMA[\"properties\"][\"evidence\"][\"items\"][\"properties\"][\"source_check_status\"][\"enum\"])\n        self.assertEqual(allowed, {\"reported_checked\", \"reported_not_checked\", \"unknown\"})\n        self.assertNotIn(\"checked_by_contributor\", SCHEMA[\"properties\"][\"evidence\"][\"items\"][\"properties\"])\n\n    def test_availability_is_time_bounded_to_receipt(self):\n        contributor = EXAMPLE[\"declared_contributor\"]\n        self.assertIn(\"availability_at_receipt\", contributor)\n        self.assertNotIn(\"availability\", contributor)\n\n    def test_unknowns_and_not_checked_are_not_empty(self):
        self.assertGreater(len(EXAMPLE["unknowns"]), 0)
        self.assertGreater(len(EXAMPLE["not_checked"]), 0)

    def test_packet_does_not_claim_private_transcript_is_public(self):
        self.assertFalse(EXAMPLE["rights_and_privacy"]["contains_private_personal_information"])
        self.assertIn("not the full private exchange", EXAMPLE["rights_and_privacy"]["notes"])

    def test_schema_does_not_make_packet_mandatory_for_contribution(self):
        # This packet is an optional relay surface, not part of the record schema.
        self.assertNotIn("contribution_packet", SCHEMA.get("required", []))

if __name__ == "__main__":
    unittest.main()
