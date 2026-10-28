"""Publishing tests use aggregate outputs only; no GitHub access."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from koa_audit.dashboard import publish_reports, _safe_ratio_data


class DashboardTest(unittest.TestCase):
    def local(self):
        return {
            "format": "koa_audit.local_observation.v1",
            "generated_at": "2026-10-28T18:56:09+00:00",
            "mode": "LOCAL_OBSERVE", "roots": ["C:\\mycode\\secret"],
            "declared_repositories": 49, "local_repositories_discovered": 142,
            "repositories_scanned": 47,
            "ambiguous_duplicates": ["owner/PrivateProject", "owner/AnotherProject"],
            "inventory_repositories_missing_locally": [],
            "findings_by_type": {"WORKFLOW_UNPINNED_ACTION": 98, "PYTHON_SSL_VERIFY_DISABLED": 6},
            "repositories": [{"repository": "owner/PrivateProject", "location": "C:\\mycode\\secret",
                              "status": "PARTIAL", "findings": [{"path": "backend/.env", "value": "SECRET_VALUE_EXAMPLE_987654"}]}]
        }

    def remote(self):
        return {
            "format": "koa_audit.observation.v1",
            "generated_at": "2026-10-28T22:15:19+00:00",
            "summary": {"repos_in_scope": 49, "repositories_observed": 15,
                        "repositories_without_metadata": 34,
                        "codeql_coverage": {"unknown": 49},
                        "security_alerts": {"dependabot": {"open_observed_lower_bound": 0, "complete_count": False}}},
            "repositories": [{"repository": "owner/PrivateProject", "ci": {
                "last_observed_default_branch_run": {"conclusion": "failure"}}}]
        }

    def test_public_projection_does_not_expose_paths_secrets_repos(self):
        with tempfile.TemporaryDirectory() as temp:
            t = Path(temp)
            p = t / "audit.json"
            p.write_text(json.dumps(self.local()), encoding="utf-8")
            output = t / "docs"
            result = publish_reports([p], output)
            self.assertEqual(result["local_snapshots"], 1)
            raw = (output / "data/dashboard.json").read_text(encoding="utf-8")
            for secret in ("mycode", "PrivateProject", "AnotherProject", "backend/.env", "SECRET_VALUE_EXAMPLE_987654", "roots", "location"):
                self.assertNotIn(secret, raw)
            sample = json.loads(raw)["snapshots"][0]
            self.assertEqual(sample["findings"]["WORKFLOW_UNPINNED_ACTION"], 98)
            self.assertEqual(sample["ambiguous"], 2)
            self.assertEqual(sample["statuses"]["PARTIAL"], 1)

    def test_persist_history_and_keep_modes_separate(self):
        with tempfile.TemporaryDirectory() as temp:
            t = Path(temp)
            src = t / "src.json"
            src.write_text(json.dumps(self.local()), encoding="utf-8")
            publish_reports([src], t / "docs")
            src.write_text(json.dumps(self.remote()), encoding="utf-8")
            publish_reports([src], t / "docs")
            publish_reports([src], t / "docs")  # dedup
            data = json.loads((t / "docs/data/dashboard.json").read_text())
            self.assertEqual(len(data["snapshots"]), 2)
            self.assertEqual({i["mode"] for i in data["snapshots"]}, {"LOCAL_OBSERVE", "OBSERVE"})
            remote = next(i for i in data["snapshots"] if i["mode"] == "OBSERVE")
            self.assertEqual(remote["ci"]["failure"], 1)
            self.assertFalse(remote["alerts"]["dependabot"]["complete"])

    def test_existing_dashboard_nested_values_are_sanitized(self):
        with tempfile.TemporaryDirectory() as temp:
            t=Path(temp)
            src=t / "audit.json"
            src.write_text(json.dumps(self.local()))
            out=t / "docs"
            publish_reports([src],out)
            data_path=out / "data/dashboard.json"
            payload=json.loads(data_path.read_text())
            payload["snapshots"][0]["findings"]["a-local-path"] = "C:\\mycode\\SECRET_ABC"
            payload["snapshots"][0]["statuses"]["PRIVATE_PROJECT"] = "TOPSECRET"
            payload["snapshots"][0]["notes"]="TOPSECRET"
            data_path.write_text(json.dumps(payload))
            publish_reports([src],out)
            raw=data_path.read_text()
            self.assertNotIn("TOPSECRET",raw)
            self.assertNotIn("mycode",raw)
            self.assertNotIn("PRIVATE_PROJECT",raw)

    def test_reject_unknown_format_without_writing(self):
        with tempfile.TemporaryDirectory() as temp:
            t = Path(temp)
            source=t / "bad.json"
            source.write_text('{"format":"bad"}')
            with self.assertRaises(ValueError):
                publish_reports([source],t / "docs")
            self.assertFalse((t / "docs/data/dashboard.json").exists())

    def test_reject_missing_zone_and_invalid_counts(self):
        data=self.local()
        data["generated_at"] = "2026-10-28T19:00:00"
        with self.assertRaises(ValueError):_safe_ratio_data(data)
        data["generated_at"] = "2026-10-28T19:00:00Z"
        data["findings_by_type"]["PYTHON_SSL_VERIFY_DISABLED"] = -100
        sample=_safe_ratio_data(data)
        self.assertEqual(sample["findings"]["PYTHON_SSL_VERIFY_DISABLED"],0)

if __name__ == "__main__": unittest.main()
