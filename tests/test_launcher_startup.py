"""Regression checks: pythonw startup should not silently import a missing project."""
from __future__ import annotations

import os
import runpy
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "kOA_GitHub_Audit_Launcher.pyw"


class LauncherBootstrapTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.launcher = runpy.run_path(str(SCRIPT))

    def test_project_is_valid_when_extracted(self):
        root = SCRIPT.parent
        self.assertTrue(self.launcher["_valid_project_dir"](root))
        self.assertFalse(self.launcher["_valid_project_dir"](root / "missing-directory"))

    def test_alone_file_does_not_need_project_import_on_load(self):
        # Loading the source must NOT import koa_audit. The import happens after
        # choosing a verified project root, so a standalone .pyw can show help.
        source = SCRIPT.read_text(encoding="utf-8")
        self.assertNotIn("from koa_audit.launcher_support import (\n    make_plan_args", source)
        self.assertIn("def _choose_project_root", source)
        self.assertIn("def _initialize_project", source)
        self.assertIn("def _fatal_dialog", source)

    def test_startup_failures_create_log(self):
        with tempfile.TemporaryDirectory() as tmp:
            with patch.dict(os.environ, {"LOCALAPPDATA": tmp}):
                path = self.launcher["diagnostic_log"](RuntimeError("startup-test"))
                self.assertIsNotNone(path)
                self.assertTrue(path.exists())
                self.assertIn("startup-test", path.read_text(encoding="utf-8"))

    def test_project_loads_after_resolution(self):
        self.launcher["_initialize_project"](SCRIPT.parent)
        self.assertEqual(self.launcher["ROOT"], SCRIPT.parent)


if __name__ == "__main__":
    unittest.main()
