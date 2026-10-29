"""Only aggregate dashboard data may be pushed by the one-click publisher."""
import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

from koa_audit.dashboard_sync import publish_to_github, latest_reports


def git(*args, cwd=None):
    proc = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True,
                          env={**os.environ, "GIT_AUTHOR_NAME": "Test User", "GIT_AUTHOR_EMAIL": "test@example.invalid",
                               "GIT_COMMITTER_NAME": "Test User", "GIT_COMMITTER_EMAIL": "test@example.invalid"})
    if proc.returncode:
        raise AssertionError((args, proc.stderr))
    return proc.stdout.strip()


class DashboardSyncTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.p = Path(self.temp.name)
        self.remote = self.p / "audit.git"
        self.seed = self.p / "seed"
        self.project = self.p / "project"
        self.project.mkdir()
        git("init", "--bare", str(self.remote))
        git("init", "-b", "main", str(self.seed))
        (self.seed / "docs/data").mkdir(parents=True)
        (self.seed / "docs/index.html").write_text("<h1>Dashboard</h1>")
        (self.seed / "docs/data/dashboard.json").write_text(json.dumps({
            "format": "koa_audit.dashboard.v1", "snapshots": [], "policy": "AGGREGATES_ONLY_NO_PATHS_NO_SECRETS"}))
        git("add", ".", cwd=self.seed)
        git("commit", "-m", "init", cwd=self.seed)
        git("remote", "add", "origin", str(self.remote), cwd=self.seed)
        git("push", "origin", "main", cwd=self.seed)
        git("symbolic-ref", "HEAD", "refs/heads/main", cwd=self.remote)
        (self.project / ".github/workflows").mkdir(parents=True)
        (self.project / ".github/workflows/dashboard-pages.yml").write_text("name: deployment\n")
        (self.project / "docs/data").mkdir(parents=True)
        (self.project / "docs/data/dashboard.json").write_text(json.dumps({
            "format": "koa_audit.dashboard.v1", "snapshots": [], "policy": "AGGREGATES_ONLY_NO_PATHS_NO_SECRETS"}))
        self.audit = self.project / "audit.json"
        self.audit.write_text(json.dumps({
            "format": "koa_audit.local_observation.v1", "generated_at": "2026-10-28T20:42:13Z",
            "declared_repositories": 49, "repositories_scanned": 47,
            "local_repositories_discovered": 142,
            "findings_by_type": {"PYTHON_TLS_BYPASS": 3},
            "repositories": [{"repository": "SENSITIVE_REPO", "location": "C:\\mycode\\SECRET_FILE",
                              "status": "REVIEW", "findings": [{"path": "backend/.env", "secret": "SECRET_987"}]}]
        }), encoding="utf-8")

    def test_publish_only_data_and_no_raw_secrets(self):
        result=publish_to_github(self.project, [self.audit], remote=str(self.remote), progress=lambda _: None)
        self.assertEqual(result["status"], "published")
        target=self.p / "inspect"
        git("clone", "--quiet", str(self.remote), str(target))
        data=(target / "docs/data/dashboard.json").read_text(encoding="utf-8")
        self.assertIn("PYTHON_TLS_BYPASS", data)
        for denied in ("SECRET_987", "SECRET_FILE", "SENSITIVE_REPO", "backend/.env", "mycode"):
            self.assertNotIn(denied, data)
        self.assertFalse((target / "audit.json").exists())
        self.assertEqual(set(git("diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD", cwd=target).splitlines()),
                         {"docs/data/dashboard.json", ".github/workflows/dashboard-pages.yml"})
        self.assertEqual(publish_to_github(self.project, [self.audit], remote=str(self.remote), progress=lambda _: None)["status"], "already_current")

    def test_auto_discover_latest_by_type(self):
        path=self.project/"reports/local";path.mkdir(parents=True)
        (path/"audit.json").write_text(self.audit.read_text())
        self.assertEqual(latest_reports(self.project),[path/"audit.json"])

    def test_invalid_report_does_not_publish(self):
        self.audit.write_text('{"format":"BAD", "secret": "HIDDEN"}')
        before=git("rev-parse", "main",cwd=self.seed)
        with self.assertRaises(ValueError):
            publish_to_github(self.project,[self.audit],remote=str(self.remote),progress=lambda _:None)
        self.assertEqual(git("rev-parse", "main",cwd=self.seed),before)


if __name__ == "__main__":
    unittest.main()
