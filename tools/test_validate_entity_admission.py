"""Both directions for the entity-admission check: it must pass the real checkout and fail
each way an entity could be admitted without a record. A check only run in the direction that
passes has not been tested."""
from __future__ import annotations

import json
import shutil
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import validate_entity_admission as vea

ROOT = Path(__file__).resolve().parents[1]


def sandbox(tmp: Path) -> Path:
    root = tmp / "thr"
    root.mkdir()
    (root / "registry").mkdir()
    (root / "cases").mkdir()
    (root / "records").mkdir()
    (root / "cases" / "x.json").write_text("{}", encoding="utf-8")
    (root / "cases" / "x.md").write_text("x", encoding="utf-8")
    (root / "records" / "x.html").write_text("<p>x</p>", encoding="utf-8")
    eid = "thr:entity:a9730018-62ab-4ccd-9882-eec34134c526"
    write(root, "entities", {"entities": [
        {"id": eid, "type": "person", "status": "current",
         "record_links": ["cases/x.json", "cases/x.md", "records/x.html"]}]})
    write(root, "mentions", {"mentions": [
        {"id": "thr:mention:11111111-1111-4111-8111-111111111111",
         "candidates": [{"entity_id": eid, "status": "resolved_as"}]}]})
    return root


def write(root: Path, name: str, value: dict) -> None:
    (root / "registry" / f"{name}.json").write_text(json.dumps(value, indent=1), encoding="utf-8")


def load(root: Path, name: str) -> dict:
    return json.loads((root / "registry" / f"{name}.json").read_text(encoding="utf-8"))


class EntityAdmission(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(__file__).resolve().parent / "_tmp_admission"
        if self.tmp.exists():
            shutil.rmtree(self.tmp)
        self.tmp.mkdir()
        self.root = sandbox(self.tmp)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_real_checkout_passes(self):
        self.assertEqual(vea.main(ROOT), 0, "the live THR checkout should satisfy the check")

    def test_sandbox_passes(self):
        self.assertEqual(vea.main(self.root), 0)

    def test_entity_with_no_record_links_fails(self):
        value = load(self.root, "entities")
        value["entities"][0].pop("record_links")
        write(self.root, "entities", value)
        self.assertEqual(vea.main(self.root), 1)

    def test_entity_with_empty_record_links_fails(self):
        value = load(self.root, "entities")
        value["entities"][0]["record_links"] = []
        write(self.root, "entities", value)
        self.assertEqual(vea.main(self.root), 1)

    def test_record_link_pointing_at_a_missing_file_fails(self):
        value = load(self.root, "entities")
        value["entities"][0]["record_links"] = ["cases/absent.json"]
        write(self.root, "entities", value)
        self.assertEqual(vea.main(self.root), 1)

    def test_entity_admitted_by_a_rendered_page_alone_fails(self):
        value = load(self.root, "entities")
        value["entities"][0]["record_links"] = ["records/x.html"]
        write(self.root, "entities", value)
        self.assertEqual(vea.main(self.root), 1)

    def test_mention_naming_an_unregistered_entity_fails(self):
        value = load(self.root, "mentions")
        value["mentions"][0]["candidates"][0]["entity_id"] = \
            "thr:entity:ffffffff-ffff-4fff-8fff-ffffffffffff"
        write(self.root, "mentions", value)
        self.assertEqual(vea.main(self.root), 1)

    def test_mention_with_no_candidate_entity_is_allowed(self):
        # An unresolved mention is the normal case and must not be forced into a referent.
        value = load(self.root, "mentions")
        value["mentions"][0]["candidates"] = []
        write(self.root, "mentions", value)
        self.assertEqual(vea.main(self.root), 0)

    def test_unreadable_registry_is_not_a_pass(self):
        (self.root / "registry" / "entities.json").write_text("{not json", encoding="utf-8")
        self.assertEqual(vea.main(self.root), 1)


if __name__ == "__main__":
    unittest.main()
