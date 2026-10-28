"""Public-safe, offline publication of aggregate kOA audit reports to GitHub Pages.

Never copy audit.json, source filenames, repository identifiers, secrets or filesystem
paths into the published directory. The only output is an allowlisted summary.
"""
from __future__ import annotations

import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

FORMAT = "koa_audit.dashboard.v1"
LOCAL = "koa_audit.local_observation.v1"
REMOTE = "koa_audit.observation.v1"
MAX_HISTORY = 100
INVENTORY_PATH = Path(__file__).resolve().parent.parent / "data" / "initial_inventory.json"
# Only these known rule IDs can appear in public aggregates. New IDs must be
# deliberately reviewed for disclosure risk before adding them to this list.
RULES = (
    "WORKFLOW_UNPINNED_ACTION", "PYTHON_SHELL_TRUE", "SENSITIVE_FILENAME",
    "LARGE_FILE_NOT_INSPECTED", "PRIVATE_KEY_MATERIAL",
    "PYTHON_SSL_VERIFY_DISABLED", "PYTHON_PICKLE_LOAD", "PYTHON_TLS_BYPASS",
)
RULE_SET = frozenset(RULES)
STATUS_KEYS = ("PARTIAL", "REVIEW", "INSPECTED_NO_PATTERN_MATCH", "UNKNOWN")


def _number(value: Any) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        return 0
    return min(value, 1_000_000)


def _utc(value: Any) -> str:
    if not isinstance(value, str) or len(value) > 50:
        raise ValueError("Date de rapport invalide")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as e:
        raise ValueError("Date de rapport invalide") from e
    if parsed.tzinfo is None:
        raise ValueError("Date sans fuseau horaire")
    return parsed.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def _safe_ratio_data(report: dict) -> dict:
    """Project only vetted counts, never input identities or paths."""
    if not isinstance(report, dict):
        raise ValueError("Le rapport doit être un objet JSON")
    fmt = report.get("format")
    if fmt not in (LOCAL, REMOTE):
        raise ValueError("Rapport non pris en charge (local_observation / observation v1 seulement)")
    generated = _utc(report.get("generated_at"))
    if fmt == LOCAL:
        repos = report.get("repositories") or []
        if not isinstance(repos, list):
            raise ValueError("Liste de dépôts invalide")
        counts = Counter()
        for repo in repos:
            if isinstance(repo, dict):
                key = repo.get("status", "UNKNOWN")
                counts[key if key in STATUS_KEYS else "UNKNOWN"] += 1
        # Numerator for the 49-repo inventory must not count unrelated local repos.
        try:
            inventory = {str(item["github_repo"]).casefold() for item in
                         json.loads(INVENTORY_PATH.read_text(encoding="utf-8"))}
        except (OSError, ValueError, KeyError, TypeError) as error:
            raise ValueError("Inventaire de référence indisponible") from error
        observed = {str(item.get("repository", "")).casefold()
                    for item in repos if isinstance(item, dict)}
        inventory_scanned = len(observed & inventory)
        findings = report.get("findings_by_type") or {}
        if not isinstance(findings, dict):
            raise ValueError("Résultats invalides")
        cleaned = {k: _number(findings[k]) for k in RULES if k in findings}
        unknown_rule_count = len([k for k in findings if k not in RULE_SET])
        sample = {
            "mode": "LOCAL_OBSERVE", "at": generated,
            "declared": _number(report.get("declared_repositories")),
            "scanned": _number(report.get("repositories_scanned")),
            "inventory_scanned": inventory_scanned,
            "discovered": _number(report.get("local_repositories_discovered")),
            "missing": _number(len(report.get("inventory_repositories_missing_locally") or [])),
            "ambiguous": _number(len(report.get("ambiguous_duplicates") or [])),
            "findings": cleaned,
            "other_rule_categories": unknown_rule_count,
            "statuses": {k: counts.get(k, 0) for k in STATUS_KEYS},
            "coverage_truncated": bool((report.get("discovery") or {}).get("discovery_truncated")),
            "historical_records": _number(len(report.get("historical_legacy") or [])),
        }
        return sample
    summary = report.get("summary") or {}
    if not isinstance(summary, dict):
        raise ValueError("Résumé distant invalide")
    ci = Counter()
    for repo in report.get("repositories") or []:
        if not isinstance(repo, dict):
            continue
        info = repo.get("ci") or {}
        last = (info.get("last_observed_default_branch_run") or {}) if isinstance(info, dict) else {}
        conclusion = last.get("conclusion", "unknown") if isinstance(last, dict) else "unknown"
        if conclusion == "success":
            ci["success"] += 1
        elif conclusion in ("failure", "timed_out", "cancelled", "action_required"):
            ci["failure"] += 1
    alerts = summary.get("security_alerts") or {}
    safe_alerts = {}
    for kind in ("dependabot", "code_scanning", "secret_scanning"):
        v = alerts.get(kind) or {}
        safe_alerts[kind] = {
            "observed_minimum": _number(v.get("open_observed_lower_bound")),
            "complete": bool(v.get("complete_count")),
        }
    return {
        "mode": "OBSERVE", "at": generated,
        "declared": _number(summary.get("repos_in_scope")),
        "observed": _number(summary.get("repositories_observed")),
        "unknown": _number(summary.get("repositories_without_metadata")),
        "ci": {"success": ci["success"], "failure": ci["failure"]},
        "alerts": safe_alerts,
        "codeql_unknown": _number((summary.get("codeql_coverage") or {}).get("unknown")),
        "historical_records": _number(summary.get("historical_records")),
    }


def _sanitize_previous(snap: dict) -> dict:
    """Allowlist even persisted snapshots, including nested values."""
    mode = snap.get("mode")
    at = _utc(snap.get("at"))
    if mode == "LOCAL_OBSERVE":
        findings = snap.get("findings") or {}
        statuses = snap.get("statuses") or {}
        if not isinstance(findings, dict) or not isinstance(statuses, dict):
            raise ValueError("Historique local invalide")
        return {
            "mode": mode, "at": at,
            **{key: _number(snap.get(key)) for key in
               ("declared", "scanned", "inventory_scanned", "discovered", "missing", "ambiguous", "historical_records", "other_rule_categories")},
            "findings": {key: _number(findings[key]) for key in RULES if key in findings},
            "statuses": {key: _number(statuses.get(key)) for key in STATUS_KEYS},
            "coverage_truncated": bool(snap.get("coverage_truncated")),
        }
    if mode == "OBSERVE":
        ci = snap.get("ci") or {}
        alerts = snap.get("alerts") or {}
        if not isinstance(ci, dict) or not isinstance(alerts, dict):
            raise ValueError("Historique distant invalide")
        return {
            "mode": mode, "at": at,
            **{key: _number(snap.get(key)) for key in
               ("declared", "observed", "unknown", "codeql_unknown", "historical_records")},
            "ci": {key: _number(ci.get(key)) for key in ("success", "failure")},
            "alerts": {key: {
                "observed_minimum": _number((alerts.get(key) or {}).get("observed_minimum")),
                "complete": bool((alerts.get(key) or {}).get("complete")),
            } for key in ("dependabot", "code_scanning", "secret_scanning")},
        }
    raise ValueError("Mode d'historique inconnu")


def load_published(path: Path) -> list[dict]:
    if not path.exists():
        return []
    content = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(content, dict) or content.get("format") != FORMAT:
        raise ValueError("Le dashboard existant n'est pas au format attendu")
    samples = content.get("snapshots", [])
    if not isinstance(samples, list):
        raise ValueError("Historique de dashboard invalide")
    return [_sanitize_previous(p) for p in samples if isinstance(p, dict)]


def publish_reports(input_paths: list[Path], output: Path) -> dict:
    """Merge sanitized snapshots; no remote calls, no target repository writes."""
    if not input_paths:
        raise ValueError("Au moins un fichier audit.json est requis")
    output = Path(output)
    data_file = output / "data" / "dashboard.json"
    # Read everything before writing anything, so invalid input is non-destructive.
    samples = []
    for src in input_paths:
        if not src.is_file() or src.stat().st_size > 30_000_000:
            raise ValueError(f"Rapport introuvable ou trop volumineux : {src}")
        try:
            raw = json.loads(src.read_text(encoding="utf-8-sig"))
        except (ValueError, UnicodeError) as error:
            raise ValueError("Rapport JSON illisible") from error
        samples.append(_safe_ratio_data(raw))
    # Rebuild existing history only from allowlisted generated keys.
    old = load_published(data_file)
    indexed = {(s["mode"], s["at"]): s for s in old + samples}
    chosen = sorted(indexed.values(), key=lambda a: (a["at"], a["mode"]))
    chosen = chosen[-MAX_HISTORY:]
    payload = {
        "format": FORMAT,
        "policy": "AGGREGATES_ONLY_NO_PATHS_NO_SECRETS",
        "snapshots": chosen,
    }
    data_file.parent.mkdir(parents=True, exist_ok=True)
    data_file.write_text(json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    return {"snapshots": len(chosen),
            "local_snapshots": sum(v["mode"] == "LOCAL_OBSERVE" for v in chosen),
            "github_snapshots": sum(v["mode"] == "OBSERVE" for v in chosen),
            "output": str(data_file)}
