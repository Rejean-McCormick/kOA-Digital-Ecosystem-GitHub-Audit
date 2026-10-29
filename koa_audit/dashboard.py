"""Public-safe, offline publication of aggregate kOA audit reports to GitHub Pages.

Never copy audit.json, source filenames, repository identifiers, secrets or filesystem
paths into the published directory. The only output is an allowlisted summary.
"""
from __future__ import annotations

import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from statistics import median
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
STATUS_KEYS = ("PARTIAL", "REVIEW", "INSPECTED_NO_PATTERN_MATCH", "OBSERVED_INFORMATIONAL", "UNKNOWN")
LOCAL_INSIGHT_KEYS = (
    "controls", "size", "quality", "structuring", "flows",
)
REMOTE_INSIGHT_KEYS = (
    "visibility", "flows", "quality",
)


def _number(value: Any) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        return 0
    return min(value, 10_000_000_000)


def _safe_dict_numbers(data: dict[str, Any], keys: tuple[str, ...]) -> dict[str, int]:
    return {key: _number(data.get(key)) for key in keys}


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


def _codeql_present(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    return value not in {"", "NOT_DETERMINED", "UNKNOWN", "NOT_PRESENT"}


def _local_size_bucket(files_enumerated: Any) -> str:
    n = _number(files_enumerated)
    if n < 100:
        return "micro"
    if n < 300:
        return "medium"
    if n < 1000:
        return "large"
    return "xlarge"


def _local_structuring_bucket(repo: dict[str, Any]) -> str:
    score = 0
    if repo.get("workflows"):
        score += 1
    if repo.get("dependency_files"):
        score += 1
    if bool(repo.get("dependabot_config")):
        score += 1
    if _codeql_present(repo.get("codeql")):
        score += 1
    if score <= 1:
        return "initial"
    if score <= 2:
        return "structured"
    return "tooled"


def _sum_findings(repo: dict[str, Any]) -> int:
    counts = repo.get("finding_counts") or {}
    if not isinstance(counts, dict):
        return 0
    return sum(_number(v) for v in counts.values())


def _local_quality_bucket(repo: dict[str, Any]) -> str:
    n = _sum_findings(repo)
    if n == 0:
        return "clean"
    if n <= 2:
        return "light"
    if n <= 5:
        return "moderate"
    return "heavy"


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
        structuring = Counter()
        quality = Counter()
        size_buckets = Counter()
        controls = Counter()
        total_files_enumerated = 0
        total_files_inspected = 0
        total_bytes_inspected = 0
        all_repo_sizes: list[int] = []
        for repo in repos:
            if not isinstance(repo, dict):
                continue
            key = repo.get("status", "UNKNOWN")
            counts[key if key in STATUS_KEYS else "UNKNOWN"] += 1
            total_files_enumerated += _number(repo.get("files_enumerated"))
            total_files_inspected += _number(repo.get("files_inspected"))
            total_bytes_inspected += _number(repo.get("bytes_inspected"))
            all_repo_sizes.append(_number(repo.get("files_enumerated")))
            size_buckets[_local_size_bucket(repo.get("files_enumerated"))] += 1
            structuring[_local_structuring_bucket(repo)] += 1
            quality[_local_quality_bucket(repo)] += 1
            if repo.get("workflows"):
                controls["workflows"] += 1
            if repo.get("dependency_files"):
                controls["dependency_manifests"] += 1
            if bool(repo.get("dependabot_config")):
                controls["dependabot"] += 1
            if _codeql_present(repo.get("codeql")):
                controls["codeql"] += 1
        # Numerator for the 49-repo inventory must not count unrelated local repos.
        try:
            inventory = {str(item["github_repo"]).casefold() for item in
                         json.loads(INVENTORY_PATH.read_text(encoding="utf-8"))}
        except (OSError, ValueError, KeyError, TypeError) as error:
            raise ValueError("Inventaire de référence indisponible") from error
        observed = {str(item.get("repository", "")).casefold()
                    for item in repos if isinstance(item, dict)}
        inventory_scanned = len(observed & inventory)
        # A profile is evidence coverage, not a certificate or a maturity grade.
        # Count only recognized registry entries with a measured profile; no names
        # or raw profile content are published.
        profile_root = INVENTORY_PATH.parent.parent / "profiles" / "repositories"
        measured_folders = {
            folder.name.casefold() for folder in profile_root.iterdir()
            if folder.is_dir() and (folder / "ENGINEERING_METRICS.json").is_file()
        } if profile_root.is_dir() else set()
        engineering_profiles = sum(key.split("/", 1)[-1] in measured_folders for key in inventory)
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
            "engineering_profiles": engineering_profiles,
            "discovered": _number(report.get("local_repositories_discovered")),
            "missing": _number(len(report.get("inventory_repositories_missing_locally") or [])),
            "ambiguous": _number(len(report.get("ambiguous_duplicates") or [])),
            "findings": cleaned,
            "other_rule_categories": unknown_rule_count,
            "statuses": {k: counts.get(k, 0) for k in STATUS_KEYS},
            "coverage_truncated": bool((report.get("discovery") or {}).get("discovery_truncated")),
            "historical_records": _number(len(report.get("historical_legacy") or [])),
            "controls": {
                "workflows": controls.get("workflows", 0),
                "dependency_manifests": controls.get("dependency_manifests", 0),
                "dependabot": controls.get("dependabot", 0),
                "codeql": controls.get("codeql", 0),
            },
            "size": {
                "files_enumerated": total_files_enumerated,
                "files_inspected": total_files_inspected,
                "bytes_inspected": total_bytes_inspected,
                "median_repo_files": int(median(all_repo_sizes)) if all_repo_sizes else 0,
                "size_buckets": {
                    "micro": size_buckets.get("micro", 0),
                    "medium": size_buckets.get("medium", 0),
                    "large": size_buckets.get("large", 0),
                    "xlarge": size_buckets.get("xlarge", 0),
                },
            },
            "quality": {
                "clean": quality.get("clean", 0),
                "light": quality.get("light", 0),
                "moderate": quality.get("moderate", 0),
                "heavy": quality.get("heavy", 0),
            },
            "structuring": {
                "initial": structuring.get("initial", 0),
                "structured": structuring.get("structured", 0),
                "tooled": structuring.get("tooled", 0),
            },
            "flows": {
                "inspected_bytes_mb": round(total_bytes_inspected / 1_000_000),
            },
        }
        return sample
    summary = report.get("summary") or {}
    if not isinstance(summary, dict):
        raise ValueError("Résumé distant invalide")
    ci = Counter()
    visibility = Counter()
    flows = Counter()
    for repo in report.get("repositories") or []:
        if not isinstance(repo, dict):
            continue
        access = repo.get("access")
        if access == "observed":
            visibility["observed"] += 1
        else:
            visibility["unknown"] += 1
        info = repo.get("ci") or {}
        last = (info.get("last_observed_default_branch_run") or {}) if isinstance(info, dict) else {}
        conclusion = last.get("conclusion", "unknown") if isinstance(last, dict) else "unknown"
        if conclusion == "success":
            ci["success"] += 1
        elif conclusion in ("failure", "timed_out", "cancelled", "action_required"):
            ci["failure"] += 1
        if (info.get("workflows_observed") or 0) > 0:
            flows["workflows_visible"] += 1
        if (info.get("default_branch_recent_runs_observed") or 0) > 0:
            flows["runs_visible"] += 1
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
        "visibility": {
            "observed": visibility.get("observed", 0),
            "unknown": visibility.get("unknown", 0),
        },
        "flows": {
            "workflows_visible": flows.get("workflows_visible", 0),
            "runs_visible": flows.get("runs_visible", 0),
        },
        "quality": {
            "alerts_complete": sum(1 for key in ("dependabot", "code_scanning", "secret_scanning") if safe_alerts[key]["complete"]),
            "alerts_partial": sum(1 for key in ("dependabot", "code_scanning", "secret_scanning") if not safe_alerts[key]["complete"]),
        },
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
        cleaned = {
            "mode": mode, "at": at,
            **{key: _number(snap.get(key)) for key in
               ("declared", "scanned", "inventory_scanned", "engineering_profiles", "discovered", "missing", "ambiguous", "historical_records", "other_rule_categories")},
            "findings": {key: _number(findings[key]) for key in RULES if key in findings},
            "statuses": {key: _number(statuses.get(key)) for key in STATUS_KEYS},
            "coverage_truncated": bool(snap.get("coverage_truncated")),
        }
        controls = snap.get("controls") or {}
        size = snap.get("size") or {}
        quality = snap.get("quality") or {}
        structuring = snap.get("structuring") or {}
        flows = snap.get("flows") or {}
        if isinstance(controls, dict):
            cleaned["controls"] = _safe_dict_numbers(controls, ("workflows", "dependency_manifests", "dependabot", "codeql"))
        if isinstance(size, dict):
            buckets = size.get("size_buckets") or {}
            cleaned["size"] = {
                **_safe_dict_numbers(size, ("files_enumerated", "files_inspected", "bytes_inspected", "median_repo_files")),
                "size_buckets": _safe_dict_numbers(buckets, ("micro", "medium", "large", "xlarge")),
            }
        if isinstance(quality, dict):
            cleaned["quality"] = _safe_dict_numbers(quality, ("clean", "light", "moderate", "heavy"))
        if isinstance(structuring, dict):
            cleaned["structuring"] = _safe_dict_numbers(structuring, ("initial", "structured", "tooled"))
        if isinstance(flows, dict):
            cleaned["flows"] = _safe_dict_numbers(flows, ("inspected_bytes_mb",))
        return cleaned
    if mode == "OBSERVE":
        ci = snap.get("ci") or {}
        alerts = snap.get("alerts") or {}
        if not isinstance(ci, dict) or not isinstance(alerts, dict):
            raise ValueError("Historique distant invalide")
        cleaned = {
            "mode": mode, "at": at,
            **{key: _number(snap.get(key)) for key in
               ("declared", "observed", "unknown", "codeql_unknown", "historical_records")},
            "ci": {key: _number(ci.get(key)) for key in ("success", "failure")},
            "alerts": {key: {
                "observed_minimum": _number((alerts.get(key) or {}).get("observed_minimum")),
                "complete": bool((alerts.get(key) or {}).get("complete")),
            } for key in ("dependabot", "code_scanning", "secret_scanning")},
        }
        visibility = snap.get("visibility") or {}
        flows = snap.get("flows") or {}
        quality = snap.get("quality") or {}
        if isinstance(visibility, dict):
            cleaned["visibility"] = _safe_dict_numbers(visibility, ("observed", "unknown"))
        if isinstance(flows, dict):
            cleaned["flows"] = _safe_dict_numbers(flows, ("workflows_visible", "runs_visible"))
        if isinstance(quality, dict):
            cleaned["quality"] = _safe_dict_numbers(quality, ("alerts_complete", "alerts_partial"))
        return cleaned
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
