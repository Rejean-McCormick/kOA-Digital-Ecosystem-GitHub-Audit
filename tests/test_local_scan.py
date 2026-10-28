"""Offline local workspace fixtures; no GitHub token or network permitted."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from koa_audit.local_scan import discover_repositories, run_local_audit, scan_repository, write_local_reports
from koa_audit.launcher_support import make_local_args

INVENTORY = Path(__file__).resolve().parents[1] / "data" / "initial_inventory.json"


class LocalAuditTests(unittest.TestCase):
    def test_find_workflows_and_potential_secret_without_leaking_value(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp) / "Arketype"
            (repo / ".git").mkdir(parents=True)
            (repo / ".github" / "workflows").mkdir(parents=True)
            (repo / "src").mkdir()
            (repo / ".github" / "workflows" / "ci.yml").write_text(
                "on: [push]\npermissions: write-all\njobs:\n  run:\n    steps:\n"
                "      - uses: actions/checkout@v4\n", encoding="utf-8")
            token = "ghp_" + "B" * 38
            (repo / "src" / "script.py").write_text(f'example = "{token}"\n'
                                                   'subprocess.run("pwd", shell=True)\n', encoding="utf-8")
            (repo / "requirements.txt").write_text("requests==2.31.0\n", encoding="utf-8")
            result = scan_repository(repo, inventory_name="Rejean-McCormick/Arketype")
            self.assertEqual(result["access"], "local_observed")
            self.assertEqual(result["ci_status"], "CONFIG_PRESENT_NOT_EXECUTED")
            self.assertIn("WORKFLOW_UNPINNED_ACTION", result["finding_counts"])
            self.assertIn("GITHUB_TOKEN_PATTERN", result["finding_counts"])
            self.assertIn("requirements.txt", result["dependency_files"])
            self.assertNotIn(token, json.dumps(result))
            self.assertEqual(result["vulnerability_database_check"], "NOT_PERFORMED_OFFLINE")
            self.assertEqual(result["codeql"], "NOT_DETERMINED")

    def test_inventory_mapping_missing_local_and_unlisted(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in ("Arketype", "ExtraProject"):
                (root / name / ".git").mkdir(parents=True)
                (root / name / "main.py").write_text("print('safe')\n")
            result = run_local_audit([root], inventory_path=INVENTORY)
            self.assertEqual(result["local_repositories_discovered"], 2)
            self.assertEqual(result["repositories_scanned"], 2)
            self.assertIn("Rejean-McCormick/Arketype", [r["repository"] for r in result["repositories"]])
            self.assertIn("LOCAL/ExtraProject", [r["repository"] for r in result["repositories"]])
            self.assertEqual(result["token_required"], False)
            self.assertTrue(result["inventory_repositories_missing_locally"])
            output = root / "reports"
            write_local_reports(output, result)
            self.assertTrue((output / "audit.json").exists())
            self.assertIn("offline", (output / "SUMMARY.md").read_text())

    def test_no_traversal_into_symlinks_and_limit(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            repo = root / "repo"
            (repo / ".git").mkdir(parents=True)
            (repo / "a.py").write_text("pass\n")
            (repo / "b.py").write_text("pass\n")
            found, meta = discover_repositories([root], max_depth=2)
            self.assertEqual(found, [repo])
            self.assertFalse(meta["discovery_truncated"])
            partial = scan_repository(repo, max_files=1)
            self.assertTrue(partial["file_inventory_truncated"])
            self.assertEqual(partial["status"], "PARTIAL")

    def test_builder_no_token_and_invalid_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            args = make_local_args(command="local-audit", root=base, depth="4",
                                   limit="0", out=base / "out", max_files="6000")
            self.assertIn("local-audit", args)
            self.assertNotIn("--require-auth", args)
            self.assertNotIn("--source-repo", args)
            with self.assertRaises(ValueError):
                make_local_args(command="local-audit", root=base / "missing", depth=4,
                                limit=0, out=base / "out")


if __name__ == "__main__":
    unittest.main()

class TlsRegressionTests(unittest.TestCase):
    def test_capsule_verification_is_not_tls(self):
        from koa_audit.python_tls import tls_verification_disabled_lines
        code = '''
from dataclasses import dataclass
@dataclass
class CapsuleImportOptions:
    verify: bool = True
warnings.append("capsule verification skipped by options.verify=False")
# remote Agent should import with verify=False
payload["verify"] = False
options = CapsuleImportOptions(verify=False)
request = DropletDeployRequest(verify=False, plan_only=True)
'''
        self.assertEqual(tls_verification_disabled_lines(code), set())

    def test_http_clients_are_detected_without_line_regex_false_positives(self):
        from koa_audit.python_tls import tls_verification_disabled_lines
        code = '''
import requests as rq
import httpx as hx
import ssl
from requests import get as get_url
rq.get("https://example.invalid", verify=False)
hx.Client(verify=False)
get_url("https://example.invalid", verify=False)
session = rq.Session()
session.verify = False
# get_url("https://example.invalid", verify=False)
message = "verify=False"
ssl._create_unverified_context()
'''
        self.assertEqual(tls_verification_disabled_lines(code), {6, 7, 8, 10, 13})

    def test_explicit_tls_flag_is_reported(self):
        from koa_audit.python_tls import tls_verification_disabled_lines
        code = """
from kx_agent.runtime.healthchecks import run_healthchecks
run_healthchecks("prod", scheme="https", verify_tls=False)
options = CapsuleImportOptions(verify=False)
"""
        self.assertEqual(tls_verification_disabled_lines(code), {3})

    def test_snapshot_tls_false_positives(self):
        # Historical reproduction of the six misclassified snapshot lines.
        from koa_audit.python_tls import tls_verification_disabled_lines
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp) / "repo"
            repo.mkdir()
            targets = {
                "kx_agent/capsules/importer.py": 'warnings.append("capsule verification skipped by options.verify=False")\n',
                "kx_manager/services/deploy.py": '# remote Agent to import capsule with verify=False\n',
                "tests/test_capsule_verify.py": 'options = CapsuleImportOptions(verify=False)\n',
            }
            for relative, contents in targets.items():
                path = repo / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(contents, encoding="utf-8")
                self.assertEqual(tls_verification_disabled_lines(contents), set())
            result = scan_repository(repo)
            self.assertNotIn("PYTHON_SSL_VERIFY_DISABLED", result["finding_counts"])
