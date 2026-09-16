"""Bounded regressions for false structural PASS; no source-record mutation."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import validate_integrity as validator


class IntegrityRegressionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.patch = patch.object(validator, "ROOT", self.root)
        self.patch.start()
        self.addCleanup(self.patch.stop)
        validator.errors.clear()
        validator.warnings.clear()
        self.addCleanup(validator.errors.clear)
        (self.root / "records").mkdir()
        for name in ("a.md", "a.json", "view.html", "contribute.md"):
            (self.root / name).write_text("{}", encoding="utf-8")
        self.record = {
            "id": "example",
            "human_view": "https://thehumanrecord.net/view.html",
            "full_human_record": "https://thehumanrecord.net/a.md",
            "machine_record": "https://thehumanrecord.net/a.json",
            "correction_route": "https://thehumanrecord.net/contribute.md",
            "view_basis": {"source_git_blobs": {
                name: validator.git_blob_sha(self.root / name) for name in ("a.md", "a.json")
            }},
        }

    def check_catalog(self):
        catalog = {field: "https://thehumanrecord.net/contribute.md" for field in (
            "record_contract", "human_explanation", "scale_architecture",
            "technical_scale_note", "identity_model", "source_model",
            "assertion_model", "entity_registry", "source_registry",
            "assertion_registry", "selection_orientation",
        )}
        catalog["records"] = [self.record]
        (self.root / "records/catalog.json").write_text(json.dumps(catalog), encoding="utf-8")
        validator.check_catalog()

    def test_valid_pair(self):
        self.check_catalog()
        self.assertEqual(validator.errors, [])

    def test_wrong_root_types(self):
        for value in (None, [], "text", 42):
            with self.subTest(value=value):
                validator.errors.clear()
                (self.root / "input.json").write_text(json.dumps(value), encoding="utf-8")
                self.assertIsNone(validator.load_json("input.json"))
                self.assertTrue(validator.errors)

    def test_omitted_pin(self):
        del self.record["view_basis"]["source_git_blobs"]["a.md"]
        self.check_catalog()
        self.assertTrue(validator.errors)

    def test_extra_pin(self):
        self.record["view_basis"]["source_git_blobs"]["view.html"] = validator.git_blob_sha(self.root / "view.html")
        self.check_catalog()
        self.assertTrue(validator.errors)

    def test_invalid_pin(self):
        self.record["view_basis"]["source_git_blobs"]["a.md"] = "not-a-blob-id"
        self.check_catalog()
        self.assertTrue(any("invalid Git blob ID" in item for item in validator.errors))

    def test_escaped_source(self):
        self.record["full_human_record"] = "https://thehumanrecord.net/../outside.md"
        self.check_catalog()
        self.assertTrue(any("escapes" in item for item in validator.errors))

    def test_stale_source(self):
        (self.root / "a.md").write_text("changed", encoding="utf-8")
        self.check_catalog()
        self.assertTrue(any("stale" in item for item in validator.errors))

    def test_external_record_route(self):
        self.record["machine_record"] = "https://other.example/a.json"
        self.check_catalog()
        self.assertTrue(validator.errors)

    def test_missing_source(self):
        (self.root / "a.md").unlink()
        self.check_catalog()
        self.assertTrue(validator.errors)


if __name__ == "__main__":
    unittest.main()
