import unittest
from koa_audit.audit import audit_one, codeql_coverage, count_alerts, run_audit
from koa_audit.github_client import ApiError
from koa_audit.report import summarize, scalar_count, safe_csv


class StubClient:
    def __init__(self, deny=None, truncate=None):
        self.deny = deny or set()
        self.truncate = truncate or set()
    def get(self, path, params=None):
        if path in self.deny: raise ApiError(403, "access_denied_or_feature_unavailable")
        if path == "/repos/o/r":
            return {"default_branch": "main", "archived": False, "security_and_analysis": {}}, {}
        if path.endswith("/commits/main"): return {"sha": "f"*40}, {}
        return {}, {}
    def list_items(self, path, key=None, *, max_pages=10, params=None):
        if path in self.deny: raise ApiError(403, "access_denied_or_feature_unavailable")
        if path.endswith("/code-scanning/analyses"):
            return [{"ref": "refs/heads/main", "tool": {"name": "CodeQL"},
                     "created_at": "2020-01-01T01:00:00Z", "commit_sha": "c"*40, "error": ""}], False
        if path.endswith("/actions/workflows"):
            return [{"name": "CI", "path": ".github/workflows/ci.yml", "state": "active"}], False
        if path.endswith("/actions/runs"):
            return [{"created_at": "2026-10-20T01:00:00Z", "conclusion": "success", "status": "completed"}], False
        return [], path in self.truncate


class AuditTest(unittest.TestCase):
    def test_existing_codeql_stale(self):
        result = audit_one(StubClient(), "o/r", 30)
        self.assertEqual(result["codeql"]["coverage"], "stale")
        self.assertEqual(result["ci"]["workflows_observed"], 1)
        self.assertEqual(result["alerts"]["secret_scanning"]["open_observed"], 0)

    def test_unknown_not_zero(self):
        p = "/repos/o/r/secret-scanning/alerts"
        result = audit_one(StubClient(deny={p}), "o/r", 30)
        self.assertEqual(result["alerts"]["secret_scanning"]["status"], "unknown")
        self.assertEqual(scalar_count(result["alerts"]["secret_scanning"]), "UNKNOWN_OR_PARTIAL")

    def test_truncated_count_not_complete(self):
        x = count_alerts(StubClient(truncate={"/repos/o/r/dependabot/alerts"}), "o/r", "dependabot")
        self.assertEqual(x["status"], "partial")
        self.assertEqual(scalar_count(x), "UNKNOWN_OR_PARTIAL")

    def test_codeql_none_and_truncation(self):
        class Empty(StubClient):
            def list_items(self,*args,**kwargs): return [], True
        x = codeql_coverage(Empty(), "o/r", "main", 30)
        self.assertEqual(x["coverage"], "unknown")

    def test_summarize_does_not_call_unknown_zero(self):
        results = [audit_one(StubClient(deny={"/repos/o/r/dependabot/alerts"}), "o/r", 30)]
        s = summarize(results, [])
        self.assertFalse(s["security_alerts"]["dependabot"]["complete_count"])

    def test_csv_formula_guard(self):
        self.assertEqual(safe_csv("=cmd()"), "'=cmd()")

    def test_workers_validation(self):
        with self.assertRaises(ValueError): run_audit(StubClient(), [], workers=20)


if __name__ == "__main__": unittest.main()
