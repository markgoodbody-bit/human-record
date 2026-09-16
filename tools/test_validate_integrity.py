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
            "view_basis": {"source_record_version": "0.1", "source_git_blobs": {
                name: validator.git_blob_sha(self.root / name) for name in ("a.md", "a.json")
            }},
        }
        markers = " and ".join(f"{name}@{pin[:7]}…" for name, pin in self.record["view_basis"]["source_git_blobs"].items())
        self.label = f"<p><strong>View basis:</strong> record version <code>0.1</code>, {markers}.</p>"
        self.view = self.root / "view.html"
        self.view.write_text(self.label, encoding="utf-8")

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

    def test_stale_html_pin(self):
        pin = self.record["view_basis"]["source_git_blobs"]["a.md"][:7]
        self.view.write_text(self.label.replace(pin, "0000000"), encoding="utf-8")
        self.check_catalog()
        self.assertTrue(any("HTML source marker" in item for item in validator.errors))

    def test_stale_html_version(self):
        self.view.write_text(self.label.replace("0.1", "0.2"), encoding="utf-8")
        self.check_catalog()
        self.assertTrue(any("version mismatch" in item for item in validator.errors))

    def test_missing_html_label(self):
        self.view.write_text("<p>No basis</p>", encoding="utf-8")
        self.check_catalog()
        self.assertTrue(any("expected one" in item for item in validator.errors))

    def test_duplicate_html_label(self):
        self.view.write_text(self.label * 2, encoding="utf-8")
        self.check_catalog()
        self.assertTrue(any("expected one" in item for item in validator.errors))

    def test_html_format(self):
        basis = self.record["view_basis"]
        del basis["source_record_version"]
        basis["source_record_format"] = "example/0.1"
        self.view.write_text(self.label.replace("record version <code>0.1</code>", "example/0.1"), encoding="utf-8")
        self.check_catalog()
        self.assertEqual(validator.errors, [])
        basis["source_record_format"] = "example/0.2"
        self.check_catalog()
        self.assertTrue(any("format mismatch" in item for item in validator.errors))

    def test_git_blob_known_vector(self):
        (self.root / "empty").write_bytes(b"")
        self.assertEqual(validator.git_blob_sha(self.root / "empty"), "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391")


if __name__ == "__main__":
    unittest.main()
