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


class VocabularyTests(unittest.TestCase):
    """The registries' controlled values are checked against the model documents themselves.
    Closed lists (preservation state) error on an unknown value; open lists warn; a model
    that no longer names its values fails loudly instead of passing everything."""

    MODEL = (
        "# model\n\n## 3. Observation\n\nPossible outcomes include:\n\n- `retrieved`\n- `not_retrieved`\n\n"
        "## 5. Source ancestry and relationships\n\n- `cites`\n\n"
        "## 6. Preservation state\n\nWorking preservation states:\n\n- `not_yet_checked`\n- `related_copy_observed`\n\n"
        "## 7. Next\n\n- `not_a_state_because_it_is_under_another_heading`\n"
    )

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.patch = patch.object(validator, "ROOT", self.root)
        self.patch.start()
        self.addCleanup(self.patch.stop)
        validator.errors.clear()
        validator.warnings.clear()
        validator._vocabulary_cache.clear()
        self.addCleanup(validator.errors.clear)
        self.addCleanup(validator.warnings.clear)
        self.addCleanup(validator._vocabulary_cache.clear)
        (self.root / "SOURCE_MODEL.md").write_text(self.MODEL, encoding="utf-8")

    def test_vocabulary_is_read_from_the_model_and_stops_at_the_next_heading(self):
        self.assertEqual(validator.model_vocabulary("SOURCE_MODEL.md", "## 6. Preservation state"),
                         {"not_yet_checked", "related_copy_observed"})
        self.assertEqual(validator.model_vocabulary("SOURCE_MODEL.md", "## 3. Observation"),
                         {"retrieved", "not_retrieved"})
        self.assertEqual(validator.errors, [])

    def test_closed_list_value_in_model_passes(self):
        validator.check_vocabulary("related_copy_observed", "SOURCE_MODEL.md", "## 6. Preservation state",
                                   "preservation.status", True, "src")
        self.assertEqual(validator.errors, [])
        self.assertEqual(validator.warnings, [])

    def test_closed_list_value_outside_model_errors(self):
        # the exact string that shipped on 2026-09-16 and passed the string-typed check
        validator.check_vocabulary("local_copy_legitimate", "SOURCE_MODEL.md", "## 6. Preservation state",
                                   "preservation.status", True, "src")
        self.assertTrue(any("local_copy_legitimate" in item and "not in SOURCE_MODEL.md" in item
                            for item in validator.errors))
        self.assertEqual(validator.warnings, [])

    def test_open_list_value_outside_model_warns_not_errors(self):
        validator.check_vocabulary("referenced_by_record", "SOURCE_MODEL.md", "## 3. Observation",
                                   "observation.outcome", False, "src")
        self.assertEqual(validator.errors, [])
        self.assertTrue(any("referenced_by_record" in item for item in validator.warnings))

    def test_missing_heading_is_an_error_not_a_pass(self):
        validator.check_vocabulary("anything", "SOURCE_MODEL.md", "## 99. Absent", "x", True, "src")
        self.assertTrue(any("not found" in item for item in validator.errors))

    def test_missing_model_document_is_an_error_not_a_pass(self):
        validator.check_vocabulary("anything", "ASSERTION_MODEL.md", "## 4. Assertion state", "x", False, "src")
        self.assertTrue(any("missing" in item for item in validator.errors))

    def test_empty_list_under_heading_is_an_error_not_a_pass(self):
        (self.root / "SOURCE_MODEL.md").write_text("## 6. Preservation state\n\nprose only\n\n## 7. Next\n", encoding="utf-8")
        for _ in range(3):
            validator.check_vocabulary("not_yet_checked", "SOURCE_MODEL.md", "## 6. Preservation state", "x", True, "src")
        hits = [item for item in validator.errors if "no backticked bullet values" in item]
        self.assertEqual(len(hits), 1, "a broken model is reported once, not once per row")


if __name__ == "__main__":
    unittest.main()
