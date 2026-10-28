"""Minimal, redacted aggregate reports. Never publish full alert payloads."""
from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


def summarize(results: list[dict], legacy: list[dict]) -> dict:
    coverage = Counter(x.get("codeql", {}).get("coverage", "unknown") for x in results)
    alert_classes = ("dependabot", "code_scanning", "secret_scanning")
    alert_summary = {}
    for category in alert_classes:
        states = Counter(x.get("alerts", {}).get(category, {}).get("status", "unknown") for x in results)
        observed = sum(x.get("alerts", {}).get(category, {}).get("open_observed", 0) for x in results)
        alert_summary[category] = {"states": dict(states),
                                   "open_observed_lower_bound": observed,
                                   "complete_count": all(x.get("alerts", {}).get(category, {}).get("status") == "ok" for x in results)}
    return {
        "repos_in_scope": len(results),
        "repositories_observed": sum(x.get("access") == "observed" for x in results),
        "repositories_without_metadata": sum(x.get("access") != "observed" for x in results),
        "codeql_coverage": dict(coverage),
        "security_alerts": alert_summary,
        "historical_records": len(legacy),
        "note": "Observed alerts are not a full security assessment. Unknown/partial never means zero.",
    }


def scalar_count(feature: dict) -> str:
    return str(feature.get("open_observed")) if feature.get("status") == "ok" else "UNKNOWN_OR_PARTIAL"


def safe_csv(value: object) -> str:
    text = str(value) if value is not None else ""
    # Spreadsheet formula injection hardening.
    return "'" + text if text.lstrip().startswith(("=", "+", "-", "@")) else text


def write_reports(out: Path, report: dict) -> None:
    out.mkdir(parents=True, exist_ok=True)
    (out / "audit.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    columns = ["repository", "metadata", "branch", "ci_workflows", "ci_latest_conclusion",
               "codeql_coverage", "last_codeql", "dependabot_alerts", "code_scanning_alerts",
               "secret_scanning_alerts", "legacy_records"]
    historical_by_repo = Counter(x.get("repository") for x in report.get("historical_legacy", []))
    with (out / "audit.csv").open("w", newline="", encoding="utf-8-sig") as fd:
        writer = csv.DictWriter(fd, fieldnames=columns)
        writer.writeheader()
        for item in report["repositories"]:
            ci = item.get("ci", {})
            alerts = item.get("alerts", {})
            row = {
                "repository": item["repository"],
                "metadata": item.get("access", "unknown"),
                "branch": item.get("repository_metadata", {}).get("default_branch", ""),
                "ci_workflows": ci.get("workflows_observed", "UNKNOWN"),
                "ci_latest_conclusion": (ci.get("last_observed_default_branch_run") or {}).get("conclusion", "UNKNOWN"),
                "codeql_coverage": item.get("codeql", {}).get("coverage", "unknown"),
                "last_codeql": item.get("codeql", {}).get("latest_default_branch_codeql", ""),
                "dependabot_alerts": scalar_count(alerts.get("dependabot", {})),
                "code_scanning_alerts": scalar_count(alerts.get("code_scanning", {})),
                "secret_scanning_alerts": scalar_count(alerts.get("secret_scanning", {})),
                "legacy_records": historical_by_repo[item["repository"]],
            }
            writer.writerow({key: safe_csv(value) for key, value in row.items()})
    summary = report["summary"]
    lines = ["# kOA GitHub Audit — observation report", "",
             f"Generated (UTC): {report['generated_at']}", "",
             f"Inventory source: `{report['inventory']['kind']}`",
             f"Inventory SHA-256: `{report['inventory']['sha256']}`",
             f"Inventory git commit: `{report['inventory'].get('git_commit') or 'snapshot only'}`", "",
             f"Repositories observed: **{summary['repositories_observed']}/{summary['repos_in_scope']}**", "",
             "## CodeQL default-branch coverage", ""]
    for status, count in sorted(summary["codeql_coverage"].items()):
        lines.append(f"- `{status}`: {count}")
    lines += ["", "## Open alerts (observed lower bounds)", ""]
    for category, values in summary["security_alerts"].items():
        qualifier = "complete API responses" if values["complete_count"] else "partial/unknown API coverage"
        lines.append(f"- {category}: **{values['open_observed_lower_bound']}** observed ({qualifier})")
    lines += ["", f"Historical diagnostic records imported: **{summary['historical_records']}**", "",
              "Historical verdicts are never promoted to current GitHub security verdicts.", "",
              "**This report is observational only:** no owner authorization, release gate, or production security certification.", ""]
    (out / "SUMMARY.md").write_text("\n".join(lines), encoding="utf-8")
