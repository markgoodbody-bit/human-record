import json
from pathlib import Path
import tempfile
import unittest
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
            "candidates": [{
                "entity_id": self.entity,
                "state": "resolved_as",
                "basis": ["bounded fixture identity basis"],
                "conflicts": [],
            }],
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
        catalog = {
            "mention_registry": "https://thehumanrecord.net/registry/mentions.json",
            "source_check_registry": "https://thehumanrecord.net/registry/source-checks.json",
            "records": [{"id": "r1"}],
        }
        (self.root / "records/catalog.json").write_text(json.dumps(catalog), encoding="utf-8")
        (self.root / "registry/entities.json").write_text(json.dumps({"entities": [{"id": self.entity}]}), encoding="utf-8")
        (self.root / "registry/sources.json").write_text(json.dumps({"sources": [{"id": self.source, "observations": [{"id": self.observation}]}]}), encoding="utf-8")
        (self.root / "registry/mentions.json").write_text(json.dumps({"mentions": [self.mention]}), encoding="utf-8")
        (self.root / "registry/source-checks.json").write_text(json.dumps({"checks": [self.check]}), encoding="utf-8")

    def test_valid_fixture(self):
        errors, counts = validator.validate(self.root)
        self.assertEqual(errors, [])
        self.assertEqual(counts, {"mentions": 1, "source_checks": 1})

    def make_research_mention(self):
        del self.mention["record_id"]
        self.mention["context"] = "Report, section 4, named-subject paragraph"

    def test_source_anchored_mention_does_not_require_public_record(self):
        self.make_research_mention()
        self.write()
        self.assertEqual(validator.validate(self.root, allow_uncatalogued_mentions=True)[0], [])

    def test_public_validator_rejects_uncatalogued_research(self):
        self.make_research_mention()
        self.write()
        self.assertEqual(validator.validate(self.root)[0], [
            self.mention["id"] + ": public registry mention requires record_id"])

    def test_research_mention_requires_observation(self):
        self.make_research_mention()
        del self.mention["observation_id"]
        self.write()
        self.assertTrue(any("requires observation_id" in e for e in validator.validate(self.root, allow_uncatalogued_mentions=True)[0]))

    def test_research_mention_requires_locator_context(self):
        self.make_research_mention()
        for context in (None, "", "   ", {}, 42):
            with self.subTest(context=context):
                self.mention["context"] = context
                self.write()
                self.assertTrue(any("requires non-empty context" in e for e in validator.validate(self.root, allow_uncatalogued_mentions=True)[0]))

    def test_research_mention_rejects_foreign_observation(self):
        self.make_research_mention()
        self.mention["observation_id"] = "thr:observation:11111111-1111-4111-8111-111111111111"
        self.write()
        self.add_unrelated_observation()
        self.assertTrue(any("different source" in e for e in validator.validate(self.root, allow_uncatalogued_mentions=True)[0]))

    def test_explicit_bad_record_is_not_treated_as_omitted(self):
        self.mention["context"] = "Report, section 4"
        for record in (None, "", "missing", [], {}):
            with self.subTest(record=record):
                self.mention["record_id"] = record
                self.write()
                self.assertTrue(any("unknown record_id" in e for e in validator.validate(self.root)[0]))

    def test_research_mention_rejects_unknown_source(self):
        self.make_research_mention()
        self.mention["source_id"] = "thr:source:11111111-1111-4111-8111-111111111111"
        self.write()
        self.assertTrue(any("unknown source_id" in e for e in validator.validate(self.root, allow_uncatalogued_mentions=True)[0]))

    def test_unknown_entity_rejected(self):
        self.mention["candidates"][0]["entity_id"] = "thr:entity:11111111-1111-4111-8111-111111111111"
        self.write()
        self.assertTrue(validator.validate(self.root)[0])

    def test_candidate_requires_non_empty_basis(self):
        candidate = self.mention["candidates"][0]
        for basis in (None, [], [""], ["   "], "prose", [42]):
            with self.subTest(basis=basis):
                if basis is None:
                    candidate.pop("basis", None)
                else:
                    candidate["basis"] = basis
                self.write()
                self.assertTrue(any(
                    "basis must be a non-empty list" in e
                    for e in validator.validate(self.root)[0]
                ))
                candidate["basis"] = ["bounded fixture identity basis"]

    def test_candidate_rejects_parallel_evidence_semantics(self):
        candidate = self.mention["candidates"][0]
        for field, value in (
            ("evidence_state", "observed"),
            ("evidence", {"source_ids": [self.source]}),
            ("history", [{"state": "candidate"}]),
        ):
            with self.subTest(field=field):
                candidate[field] = value
                self.write()
                self.assertTrue(any(
                    f"unsupported field {field!r}" in e
                    for e in validator.validate(self.root)[0]
                ))
                candidate.pop(field)

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

    def test_missing_catalog_route_rejected(self):
        catalog = {"records": [{"id": "r1"}]}
        (self.root / "records/catalog.json").write_text(json.dumps(catalog), encoding="utf-8")
        self.assertTrue(validator.validate(self.root)[0])

    def add_unrelated_observation(self):
        other = "thr:observation:11111111-1111-4111-8111-111111111111"
        path = self.root / "registry/sources.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["sources"].append({
            "id": "thr:source:22222222-2222-4222-8222-222222222222",
            "observations": [{"id": other}],
        })
        path.write_text(json.dumps(data), encoding="utf-8")
        return other

    def test_mention_observation_must_belong_to_source(self):
        self.mention["observation_id"] = "thr:observation:11111111-1111-4111-8111-111111111111"
        self.write()
        self.add_unrelated_observation()
        self.assertTrue(any("different source" in e for e in validator.validate(self.root)[0]))

    def test_promoted_observation_must_belong_to_source(self):
        self.check["record_evidence_promoted"] = True
        self.check["promoted_observation_id"] = "thr:observation:11111111-1111-4111-8111-111111111111"
        self.write()
        self.add_unrelated_observation()
        self.assertTrue(any("different source" in e for e in validator.validate(self.root)[0]))

    def test_promoted_observation_from_same_source(self):
        self.check["record_evidence_promoted"] = True
        self.check["promoted_observation_id"] = self.observation
        self.write()
        self.assertEqual(validator.validate(self.root)[0], [])

    def test_duplicate_observation_id_rejected(self):
        self.add_unrelated_observation()
        path = self.root / "registry/sources.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["sources"][1]["observations"][0]["id"] = self.observation
        path.write_text(json.dumps(data), encoding="utf-8")
        self.assertTrue(any("duplicate observation" in e for e in validator.validate(self.root)[0]))


if __name__ == "__main__":
    unittest.main()
