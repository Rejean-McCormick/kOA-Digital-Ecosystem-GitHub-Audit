"""Observe GitHub metadata and *existing* analyses. Never start or modify a scan."""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
from typing import Any
from urllib.parse import quote

from .github_client import ApiError, GitHubClient
from .inventory import check_repo


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def parse_time(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        date = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return date if date.tzinfo else date.replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def feature_error(err: ApiError) -> dict:
    return {"status": "unknown", "reason": err.category, "http_status": err.status}


def guarded_list(client: GitHubClient, path: str, *, key: str | None = None,
                 pages: int = 10, params: dict | None = None) -> tuple[list[dict] | None, dict]:
    try:
        rows, truncated = client.list_items(path, key, max_pages=pages, params=params)
        return rows, {"status": "partial" if truncated else "ok",
                      "truncated": truncated, "observed_count": len(rows)}
    except ApiError as exc:
        return None, feature_error(exc)


def count_alerts(client: GitHubClient, repo: str, category: str) -> dict:
    path = f"/repos/{repo}/{category}/alerts"
    rows, state = guarded_list(client, path, params={"state": "open"}, pages=10)
    if rows is None:
        return state
    result = {**state, "open_observed": len(rows)}
    if category == "dependabot":
        severity: dict[str, int] = {}
        for alert in rows:
            level = (alert.get("security_advisory") or {}).get("severity") or "unknown"
            level = str(level).lower()
            severity[level] = severity.get(level, 0) + 1
        result["severity"] = severity
    elif category == "code-scanning":
        severity = {}
        for alert in rows:
            rule = alert.get("rule") or {}
            level = rule.get("security_severity_level") or rule.get("severity") or "unknown"
            level = str(level).lower()
            severity[level] = severity.get(level, 0) + 1
        result["severity"] = severity
    # Secrets: only count, never include alert attributes or token values.
    return result


def codeql_coverage(client: GitHubClient, repo: str, branch: str, max_age_days: int) -> dict:
    rows, state = guarded_list(client, f"/repos/{repo}/code-scanning/analyses", pages=1)
    if rows is None:
        return state
    ref = "refs/heads/" + branch
    codeql = [x for x in rows if x.get("ref") == ref and
              "codeql" in str((x.get("tool") or {}).get("name", x.get("tool_name", ""))).lower()]
    latest = max(codeql, key=lambda x: str(x.get("created_at", "")), default=None)
    if latest is None:
        return {**state, "coverage": "unknown" if state["truncated"] else "not_observed",
                "latest_default_branch_codeql": None,
                "note": "Only the most recent 100 analyses are inspected"}
    timestamp = latest.get("created_at")
    at = parse_time(timestamp)
    freshness = "unknown"
    if at:
        freshness = "recent" if at >= datetime.now(timezone.utc) - timedelta(days=max_age_days) else "stale"
    if latest.get("error"):
        freshness = "analysis_error"
    return {**state, "coverage": freshness,
            "latest_default_branch_codeql": timestamp,
            "analysis_commit": latest.get("commit_sha"),
            "note": "Latest observed CodeQL analysis, not complete language coverage"}


def ci_observation(client: GitHubClient, repo: str, branch: str) -> dict:
    workflows, wf_state = guarded_list(client, f"/repos/{repo}/actions/workflows", key="workflows", pages=5)
    runs, run_state = guarded_list(client, f"/repos/{repo}/actions/runs", key="workflow_runs",
                                   pages=1, params={"branch": branch})
    result = {"workflows_status": wf_state, "runs_status": run_state}
    if workflows is not None:
        result["workflows_observed"] = len(workflows)
        result["workflows"] = [{"name": str(x.get("name", ""))[:160],
                                 "path": str(x.get("path", ""))[:200],
                                 "state": str(x.get("state", "unknown"))}
                                for x in workflows]
    if runs is not None:
        result["default_branch_recent_runs_observed"] = len(runs)
        if runs:
            # GitHub returns latest first, but explicitly sort to avoid assumptions.
            latest = max(runs, key=lambda x: str(x.get("created_at", "")))
            result["last_observed_default_branch_run"] = {
                "created_at": latest.get("created_at"),
                "status": latest.get("status"),
                "conclusion": latest.get("conclusion"),
                "head_sha": latest.get("head_sha"),
            }
            result["successful_runs_in_sample"] = sum(x.get("conclusion") == "success" for x in runs)
        else:
            result["last_observed_default_branch_run"] = None
    return result


def audit_one(client: GitHubClient, repo: str, max_age_days: int) -> dict:
    repo = check_repo(repo)
    item: dict = {"repository": repo, "checked_at": now_iso(), "access": "unknown"}
    try:
        info, _ = client.get("/repos/" + repo)
    except ApiError as exc:
        item["repository_metadata"] = feature_error(exc)
        return item
    item["access"] = "observed"
    branch = info.get("default_branch") or ""
    item["repository_metadata"] = {
        "status": "ok", "default_branch": branch, "archived": bool(info.get("archived")),
        "disabled": bool(info.get("disabled")), "private": bool(info.get("private")),
        "pushed_at": info.get("pushed_at"),
        "head_sha": None,
        "security_features": {
            name: (info.get("security_and_analysis") or {}).get(name, {}).get("status", "unknown")
            for name in ("advanced_security", "dependabot_security_updates", "secret_scanning", "secret_scanning_push_protection")
        },
    }
    if branch:
        try:
            commit, _ = client.get(f"/repos/{repo}/commits/{quote(branch, safe='')}")
            item["repository_metadata"]["head_sha"] = commit.get("sha")
        except ApiError:
            pass
    if branch:
        item["ci"] = ci_observation(client, repo, branch)
        item["codeql"] = codeql_coverage(client, repo, branch, max_age_days)
    else:
        item["ci"] = {"status": "unknown", "reason": "missing_default_branch"}
        item["codeql"] = {"status": "unknown", "reason": "missing_default_branch"}
    item["alerts"] = {
        "code_scanning": count_alerts(client, repo, "code-scanning"),
        "dependabot": count_alerts(client, repo, "dependabot"),
        "secret_scanning": count_alerts(client, repo, "secret-scanning"),
    }
    return item


def run_audit(client: GitHubClient, repos: list[dict], *, workers: int = 3,
              max_age_days: int = 30) -> list[dict]:
    if workers < 1 or workers > 6:
        raise ValueError("workers must be between 1 and 6")
    if max_age_days < 1 or max_age_days > 365:
        raise ValueError("max_age_days out of range")
    results: list[dict] = []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        future_map = {pool.submit(audit_one, client, x["github_repo"], max_age_days): x for x in repos}
        for future in as_completed(future_map):
            inventory_entry = future_map[future]
            try:
                result = future.result()
            except Exception:
                # Internal failures are visible, not silently interpreted as clean.
                result = {"repository": inventory_entry["github_repo"],
                          "checked_at": now_iso(), "access": "unknown",
                          "internal_error": "collector_failure"}
            result["inventory_scope"] = inventory_entry.get("scope", "UNSPECIFIED")
            result["inventory_status"] = inventory_entry.get("source_status", "unspecified")
            results.append(result)
    return sorted(results, key=lambda x: x["repository"].lower())
