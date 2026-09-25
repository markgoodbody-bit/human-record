"""Both directions for the entity-admission check: it must pass the real checkout and fail
each way an entity could be admitted without a record. A check only run in the direction that
passes has not been tested."""
from __future__ import annotations

import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

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
    (root / "records" / "catalog.json").write_text(json.dumps({"records": [
        {"id": "x", "machine_record": "https://thehumanrecord.net/cases/x.json",
         "full_human_record": "https://thehumanrecord.net/cases/x.md",
         "human_view": "https://thehumanrecord.net/records/x.html"}]}), encoding="utf-8")
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


class CodexPostMergeFalsifier(unittest.TestCase):
    """Codex 5797126626 (THR #73, 2026-09-23), reproduced as reported: real checkout and real
    path checks; only load() is patched, in memory, to swap each entity's record_links. At
    main 0a8e537 all three returned 0/PASS. The registry on disk is never touched."""

    def run_with_links(self, links):
        real_load = vea.load

        def patched(root, rel):
            value = real_load(root, rel)
            if rel == "registry/entities.json":
                value = json.loads(json.dumps(value))
                for entity in value["entities"]:
                    entity["record_links"] = list(links)
            return value

        with mock.patch.object(vea, "load", side_effect=patched):
            return vea.main(ROOT)

    def test_a_readme_does_not_admit_an_entity(self):
        self.assertEqual(self.run_with_links(["README.md"]), 1)

    def test_b_a_registry_file_does_not_admit_an_entity(self):
        self.assertEqual(self.run_with_links(["registry/entities.json"]), 1)

    def test_c_an_absolute_path_outside_the_checkout_does_not_admit_an_entity(self):
        outside = Path(tempfile.mkdtemp(prefix="other-checkout-"))
        try:
            (outside / "README.md").write_text("another checkout", encoding="utf-8")
            self.assertEqual(self.run_with_links([str((outside / "README.md").resolve())]), 1)
        finally:
            shutil.rmtree(outside, ignore_errors=True)


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

    # --- containment and the record inventory (after Codex 5797126626) ---
    def set_links(self, links):
        value = load(self.root, "entities")
        value["entities"][0]["record_links"] = links
        write(self.root, "entities", value)

    def test_an_uncatalogued_json_inside_the_checkout_does_not_admit(self):
        (self.root / "cases" / "loose.json").write_text("{}", encoding="utf-8")
        self.set_links(["cases/loose.json"])
        self.assertEqual(vea.main(self.root), 1)

    def test_a_catalogued_machine_record_alone_admits(self):
        self.set_links(["cases/x.json"])
        self.assertEqual(vea.main(self.root), 0)

    def test_dot_dot_escape_fails_even_to_an_existing_file(self):
        (self.tmp / "escaped.json").write_text("{}", encoding="utf-8")
        self.set_links(["cases/x.json", "cases/../../escaped.json"])
        self.assertEqual(vea.main(self.root), 1)

    def test_symlink_escape_fails(self):
        (self.tmp / "target.md").write_text("outside", encoding="utf-8")
        try:
            os.symlink(self.tmp / "target.md", self.root / "cases" / "link.md")
        except (OSError, NotImplementedError) as exc:
            self.skipTest(f"cannot create a symlink here: {exc}")
        self.set_links(["cases/x.json", "cases/link.md"])
        self.assertEqual(vea.main(self.root), 1)

    def test_a_catalogue_entry_that_points_outside_does_not_count(self):
        (self.tmp / "outside.json").write_text("{}", encoding="utf-8")
        cat = json.loads((self.root / "records" / "catalog.json").read_text(encoding="utf-8"))
        cat["records"][0]["machine_record"] = "https://thehumanrecord.net/../outside.json"
        (self.root / "records" / "catalog.json").write_text(json.dumps(cat), encoding="utf-8")
        self.set_links(["cases/x.md"])          # still catalogued as full_human_record
        self.assertEqual(vea.main(self.root), 0)
        self.set_links(["../outside.json"])
        self.assertEqual(vea.main(self.root), 1)

    def test_unreadable_catalogue_is_not_a_pass(self):
        (self.root / "records" / "catalog.json").write_text("{not json", encoding="utf-8")
        self.assertEqual(vea.main(self.root), 1)


if __name__ == "__main__":
    unittest.main()
