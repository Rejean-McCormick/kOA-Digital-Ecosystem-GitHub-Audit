"""Offline tests for Windows launcher command preparation (no display required)."""
from __future__ import annotations

import tempfile
import unittest
from datetime import datetime
from pathlib import Path

from koa_audit.launcher_support import make_plan_args, make_audit_args, make_legacy_args


class LauncherSupportTest(unittest.TestCase):
    def test_plan_bundled_offline(self):
        self.assertEqual(make_plan_args(source="bundled", limit="0"),
                         ["-m", "koa_audit", "plan", "--inventory-source", "bundled", "--limit", "0"])

    def test_audit_safe_flags(self):
        with tempfile.TemporaryDirectory() as directory:
            cmd = make_audit_args(source="github", limit="49", workers="3",
                                  max_age_days="30", out=Path(directory), require_auth=True,
                                  discover_public_owner=True, legacy_dir=None)
            self.assertEqual(cmd[2], "audit")
            self.assertIn("--require-auth", cmd)
            self.assertIn("--discover-public-owner", cmd)
            self.assertNotIn("--apply", cmd)
            self.assertNotIn("workflow_dispatch", cmd)
            self.assertEqual(cmd[cmd.index("--workers") + 1], "3")

    def test_reject_bad_numbers_and_inventory(self):
        for source, count in (("bundled", "-2"), ("oops", "0"), ("github", "x")):
            with self.subTest(source=source, count=count):
                with self.assertRaises(ValueError):
                    make_plan_args(source=source, limit=count)
        with self.assertRaises(ValueError):
            make_audit_args(source="bundled", limit=0, workers=0,
                            max_age_days=30, out=Path("reports"), require_auth=False,
                            discover_public_owner=False, legacy_dir=None)
        with self.assertRaises(ValueError):
            make_audit_args(source="bundled", limit=0, workers=2,
                            max_age_days=0, out=Path("reports"), require_auth=False,
                            discover_public_owner=False, legacy_dir=None)

    def test_optional_legacy_must_exist(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                make_audit_args(source="bundled", limit=0, workers=2,
                                max_age_days=30, out=Path(directory), require_auth=False,
                                discover_public_owner=False, legacy_dir=Path(directory) / "missing")

    def test_import_json_and_zip_member(self):
        with tempfile.TemporaryDirectory() as directory:
            directory = Path(directory)
            source = directory / "report.json"
            source.write_text("{}", encoding="utf-8")
            archive = directory / "report.zip"
            archive.write_bytes(b"NOT A REAL ZIP")  # only path/extension checked by the GUI
            when = datetime(2026, 10, 28, 12, 0, 0)
            cmd = make_legacy_args(tool="KorDiag", repo="Example/Repo", source_path=source,
                                   member="", out_dir=directory, now=when)
            self.assertIn("--repo", cmd)
            self.assertNotIn("--member", cmd)
            self.assertTrue(cmd[cmd.index("--out") + 1].endswith(".json"))
            cmd_zip = make_legacy_args(tool="LevelUpDiag-Orgo", repo="Example/Repo",
                                       source_path=archive, member="verification/embedded/summary.json",
                                       out_dir=directory, now=when)
            self.assertEqual(cmd_zip[cmd_zip.index("--member") + 1],
                             "verification/embedded/summary.json")

    def test_import_prevents_path_traversal_and_ambiguous_binding(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "report.zip"
            source.touch()
            for repo, member in (("invalid", "a.json"), ("owner/repo", "../a.json"),
                                 ("owner/repo", "")):
                with self.subTest(repo=repo, member=member):
                    with self.assertRaises(ValueError):
                        make_legacy_args(tool="KorDiag", repo=repo, source_path=source,
                                         member=member, out_dir=Path(directory))

    def test_import_no_accidental_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            directory = Path(directory)
            source = directory / "report.json"
            source.write_text("{}", encoding="utf-8")
            when = datetime(2026, 10, 28, 12, 0, 0)
            cmd = make_legacy_args(tool="KorDiag", repo="owner/repo", source_path=source,
                                   member="", out_dir=directory, now=when)
            Path(cmd[cmd.index("--out") + 1]).write_text("existing", encoding="utf-8")
            with self.assertRaises(ValueError):
                make_legacy_args(tool="KorDiag", repo="owner/repo", source_path=source,
                                 member="", out_dir=directory, now=when)


if __name__ == "__main__":
    unittest.main()
