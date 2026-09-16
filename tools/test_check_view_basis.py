import json
from pathlib import Path
import tempfile
import unittest
import subprocess
import sys
from check_view_basis import check, git_blob


class ViewBasisTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "records").mkdir()
        self.data = {"record.md": b"original\n", "record.json": b"{}\n"}
        for name, data in self.data.items():
            (self.root / name).write_bytes(data)
        self.record = {
            "id": "example",
            "full_human_record": "https://thehumanrecord.net/record.md",
            "machine_record": "https://thehumanrecord.net/record.json",
            "view_basis": {"source_git_blobs": {name: git_blob(data) for name, data in self.data.items()}},
        }
        self.save()

    def save(self):
        (self.root / "records/catalog.json").write_text(json.dumps({"records": [self.record]}), encoding="utf-8")

    def test_matching_pair(self):
        self.assertEqual(check(self.root), (2, []))

    def test_changed_source(self):
        (self.root / "record.md").write_bytes(b"changed\n")
        self.assertTrue(check(self.root)[1])

    def test_missing_source(self):
        (self.root / "record.md").unlink()
        self.assertTrue(check(self.root)[1])

    def test_omitted_pin(self):
        del self.record["view_basis"]["source_git_blobs"]["record.md"]
        self.save()
        self.assertTrue(check(self.root)[1])

    def test_invalid_catalogue(self):
        (self.root / "records/catalog.json").write_text("{}", encoding="utf-8")
        self.assertTrue(check(self.root)[1])

    def test_git_blob_known_vector(self):
        self.assertEqual(git_blob(b""), "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391")

    def test_cli_rejects_extra_arguments(self):
        script = Path(__file__).with_name("check_view_basis.py")
        result = subprocess.run([sys.executable, str(script), str(self.root), "extra"],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertNotIn("0 failures", result.stdout)

    def test_cli_checks_requested_directory(self):
        script = Path(__file__).with_name("check_view_basis.py")
        result = subprocess.run([sys.executable, str(script), str(self.root / "missing")],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("Cannot establish view basis", result.stdout)

    def test_source_path_cannot_escape_root(self):
        self.record["full_human_record"] = "https://thehumanrecord.net/../outside.md"
        pins = self.record["view_basis"]["source_git_blobs"]
        pins["../outside.md"] = pins.pop("record.md")
        self.save()
        self.assertIn("escapes checkout", check(self.root)[1][0])

    def test_invalid_pin(self):
        self.record["view_basis"]["source_git_blobs"]["record.md"] = "invalid"
        self.save()
        self.assertIn("invalid Git blob ID", check(self.root)[1][0])


if __name__ == "__main__":
    unittest.main()
