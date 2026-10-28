"""Offline triage must never include raw secrets/source or scan outside root."""
from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
import zipfile
from pathlib import Path

from koa_audit.triage import build_triage, write_triage_zip, _safe_file
from koa_audit.launcher_support import make_triage_args


class LocalTriageTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.repo = self.root / "project"
        self.repo.mkdir()
        subprocess.run(["git", "init", "-q", str(self.repo)], check=True)
        subprocess.run(["git", "-C", str(self.repo), "config", "user.name", "Fixture"], check=True)
        subprocess.run(["git", "-C", str(self.repo), "config", "user.email", "fixture@example.invalid"], check=True)
        subprocess.run(["git", "-C", str(self.repo), "remote", "add", "origin", "https://github.com/test/sample.git"], check=True)
        (self.repo / ".github" / "workflows").mkdir(parents=True)
        (self.repo / ".github" / "workflows" / "ci.yml").write_text(
            "name: CI\nsteps:\n  - uses: actions/checkout@v4\n", encoding="utf-8")
        (self.repo / "app.py").write_text(
            'import requests\n# REMOVED SECRET TEST VALUE: DONT_COPY_STRING_123\n'
            'requests.get("SENSITIVE_URL_NOT_FOR_ZIP", verify=False)\n', encoding="utf-8")
        (self.repo / ".env").write_text("PASSWORD=NEVER_INCLUDE_THIS_SECRET\n", encoding="utf-8")
        (self.repo / "oversize.py").write_text("#" + "a" * 262144, encoding="utf-8")
        subprocess.run(["git", "-C", str(self.repo), "add", ".github", "app.py", "oversize.py"], check=True)
        subprocess.run(["git", "-C", str(self.repo), "commit", "-q", "-m", "test"], check=True)
        self.audit = self.root / "audit.json"
        self.report = {
            "format": "koa_audit.local_observation.v1", "generated_at": "2026-10-28T18:56:09Z",
            "repositories": [{
                "repository": "test/sample", "location": str(self.repo),
                "git": {"head": "oldhead"},
                "findings": [
                    {"id": "PYTHON_SSL_VERIFY_DISABLED", "path": "app.py", "line": 3},
                    {"id": "WORKFLOW_UNPINNED_ACTION", "path": ".github/workflows/ci.yml", "line": 3},
                    {"id": "SENSITIVE_FILENAME", "path": ".env", "line": None},
                    {"id": "PYTHON_SSL_VERIFY_DISABLED", "path": "../outside.py", "line": 1},
                ],
            }],
        }
        self.audit.write_text(json.dumps(self.report), encoding="utf-8")

    def test_structured_rechecks_and_zip_redaction(self):
        data = build_triage(self.root, self.audit)
        self.assertEqual(data["counts"]["repositories_rechecked"], 1)
        findings = data["repository_checks"][0]["finding_reviews"]
        self.assertEqual(findings[0]["recheck"], "TLS_BYPASS_API_STILL_PRESENT")
        self.assertEqual(findings[1]["recheck"], "REFERENCE_REQUIRES_REVIEW")
        self.assertEqual(findings[2]["git_tracked"], False)
        self.assertEqual(findings[3]["presence"], "INVALID_PATH")
        self.assertEqual(data["workflow_references"][0]["action"], "actions/checkout@v4")
        self.assertTrue(any(x["path"] == "oversize.py" for x in data["large_tracked_source_files"]))
        self.assertEqual(data["tracked_sensitive_names"], [])
        path = write_triage_zip(data, self.root / "bundle.zip")
        with zipfile.ZipFile(path) as archive:
            self.assertEqual(len(archive.namelist()), 6)
            contents = b"\n".join(archive.read(n) for n in archive.namelist())
            self.assertNotIn(b"NEVER_INCLUDE_THIS_SECRET", contents)
            self.assertNotIn(b"SENSITIVE_URL_NOT_FOR_ZIP", contents)
            self.assertNotIn(b"DONT_COPY_STRING_123", contents)
        with self.assertRaises(FileExistsError):
            write_triage_zip(data, path)

    def test_legacy_false_tls_report_is_reclassified_without_a_full_scan(self):
        (self.repo / "capsule.py").write_text(
            'warnings.append("capsule verification skipped by options.verify=False")\n'
            '# remote import with verify=False\n'
            'options = CapsuleImportOptions(verify=False)\n', encoding="utf-8")
        self.report["repositories"][0]["findings"] = [
            {"id": "PYTHON_SSL_VERIFY_DISABLED", "path": "capsule.py", "line": 1},
            {"id": "PYTHON_SSL_VERIFY_DISABLED", "path": "capsule.py", "line": 2},
            {"id": "PYTHON_SSL_VERIFY_DISABLED", "path": "capsule.py", "line": 3},
        ]
        self.audit.write_text(json.dumps(self.report), encoding="utf-8")
        data = build_triage(self.root, self.audit)
        rows = data["repository_checks"][0]["finding_reviews"]
        self.assertEqual([r["recheck"] for r in rows], ["NOT_A_TLS_BYPASS_API"] * 3)

    def test_only_within_root_and_no_follow_symlinks(self):
        outside = self.root.parent / "sensitive-outside-file.txt"
        path, reason = _safe_file(self.repo, "../sensitive-outside-file.txt")
        self.assertIsNone(path)
        self.assertEqual(reason, "INVALID_PATH")
        self.report["repositories"][0]["location"] = str(outside)
        self.audit.write_text(json.dumps(self.report), encoding="utf-8")
        data = build_triage(self.root, self.audit)
        self.assertEqual(data["repository_checks"][0]["status"], "OUTSIDE_SELECTED_ROOT")

    def test_duplicate_repositories_found_by_remote(self):
        another = self.root / "other"
        another.mkdir()
        subprocess.run(["git", "init", "-q", str(another)], check=True)
        subprocess.run(["git", "-C", str(another), "remote", "add", "origin", "git@github.com:test/sample.git"], check=True)
        data = build_triage(self.root, self.audit)
        self.assertEqual(len(data["duplicate_git_remotes"]), 1)
        self.assertEqual(len(data["duplicate_git_remotes"][0]["candidates"]), 2)

    def test_bad_report_rejected(self):
        self.audit.write_text('{"format": "wrong", "repositories": []}', encoding="utf-8")
        with self.assertRaises(ValueError):
            build_triage(self.root, self.audit)

    def test_argument_builder(self):
        cmd = make_triage_args(root=self.root, audit_json=self.audit, out_dir=self.root / "out", depth="4")
        self.assertEqual(cmd[2], "local-triage")
        self.assertTrue(cmd[cmd.index("--out") + 1].endswith(".zip"))
        self.assertNotIn("--apply", cmd)
        with self.assertRaises(ValueError):
            make_triage_args(root=self.root, audit_json=self.audit, out_dir=self.root, depth="100")


if __name__ == "__main__":
    unittest.main()
