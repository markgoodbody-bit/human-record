from contextlib import redirect_stdout
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import validate_all as runner


class UnifiedValidationTests(unittest.TestCase):
    def test_selected_root_and_state_restoration(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            previous = runner.validate_integrity.ROOT
            def integrity():
                self.assertEqual(runner.validate_integrity.ROOT, root)
                return 0
            with patch.object(runner.validate_integrity, "main", side_effect=integrity), patch.object(runner.validate_operational, "main", return_value=0) as operational, redirect_stdout(io.StringIO()):
                self.assertEqual(runner.run(root), 0)
                operational.assert_called_once_with(root)
            self.assertEqual(runner.validate_integrity.ROOT, previous)

    def test_failure_and_exception_do_not_skip_second_stage(self):
        for exception in (False, True):
            with self.subTest(exception=exception), tempfile.TemporaryDirectory() as directory:
                output = io.StringIO()
                with patch.object(runner.validate_integrity, "main", return_value=1, side_effect=ValueError("fixture") if exception else None), patch.object(runner.validate_operational, "main", return_value=0) as operational, redirect_stdout(output):
                    self.assertEqual(runner.run(directory), 1)
                    operational.assert_called_once()
                self.assertNotIn("PASS: both", output.getvalue())

    def test_operational_failure_propagates(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(runner.validate_integrity, "main", return_value=0), patch.object(runner.validate_operational, "main", return_value=1), redirect_stdout(io.StringIO()):
            self.assertEqual(runner.run(directory), 1)

    def test_missing_root_runs_neither(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(runner.validate_integrity, "main") as integrity, patch.object(runner.validate_operational, "main") as operational, redirect_stdout(io.StringIO()):
            self.assertEqual(runner.run(Path(directory) / "missing"), 1)
            integrity.assert_not_called()
            operational.assert_not_called()
