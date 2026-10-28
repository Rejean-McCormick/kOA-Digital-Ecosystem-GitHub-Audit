"""Offline evidence ZIP for existing LOCAL_OBSERVE reports.

The bundle contains only structured metadata. Never archive raw code, secret
values, .env contents, arbitrary excerpts, or authenticated Git remotes.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import tempfile
import zipfile
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

from .local_scan import discover_repositories, _git_info, SECRET_RE, CODE_HEURISTICS

FORMAT = "koa_audit.local_triage.v1"
MAX_INPUT = 16 * 1024 * 1024
MAX_REPOSITORIES = 500
MAX_FINDINGS_PER_REPO = 700
MAX_TOTAL_FINDINGS = 15000
MAX_WORKFLOW_BYTES = 512 * 1024
MAX_SOURCE_BYTES = 512 * 1024
SAFE_ACTION = re.compile(r"^[a-zA-Z0-9_.-]+/[a-zA-Z0-9_./-]+@[a-zA-Z0-9_.-]+$")
SAFE_LOCAL_ACTION = re.compile(r"^\./[a-zA-Z0-9_./-]+$")
SENSITIVE_NAME = re.compile(r"(^|/)(?:\.env(?:\..*)?|[^/]+\.(?:pem|key|p12|pfx)|id_(?:rsa|ed25519|ecdsa))$", re.I)
TEST_PATH = re.compile(r"(^|/)(?:tests?|fixtures?|examples?|docs?)(/|$)|(^|/)test_[^/]+", re.I)
SAFE_FINDING_IDS = {name for name, *_ in [*SECRET_RE, *CODE_HEURISTICS]} | {
    "WORKFLOW_UNPINNED_ACTION", "WORKFLOW_PULL_REQUEST_TARGET", "WORKFLOW_WRITE_ALL",
    "WORKFLOW_REMOTE_SCRIPT", "SENSITIVE_FILENAME", "LARGE_FILE_NOT_INSPECTED", "READ_ERROR"
}


def _git(folder: Path, *args: str) -> bytes | None:
    env = os.environ.copy()
    env["GIT_TERMINAL_PROMPT"] = "0"
    try:
        p = subprocess.run(["git", "-C", str(folder), *args], stdout=subprocess.PIPE,
                           stderr=subprocess.DEVNULL, env=env, timeout=12, check=False)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return p.stdout if p.returncode == 0 else None


def _tracked_files(folder: Path) -> set[str] | None:
    raw = _git(folder, "ls-files", "--cached", "-z")
    if raw is None:
        return None
    return {os.fsdecode(v).replace("\\", "/") for v in raw.split(b"\0") if v}


def _safe_file(repo: Path, relative: object) -> tuple[Path | None, str]:
    """Reject traversal, symlinks and .git (including symlink ancestors)."""
    if not isinstance(relative, str) or not relative or "\x00" in relative:
        return None, "INVALID_PATH"
    raw = relative.replace("\\", "/")
    if raw.startswith("/") or re.match(r"^[a-zA-Z]:", raw):
        return None, "INVALID_PATH"
    parts = raw.split("/")
    if any(x in ("", ".", "..") for x in parts) or parts[0].lower() == ".git":
        return None, "INVALID_PATH"
    candidate = repo
    for element in parts:
        candidate = candidate / element
        if candidate.is_symlink():
            return None, "SYMLINK_SKIPPED"
    try:
        if not candidate.resolve().is_relative_to(repo.resolve()):
            return None, "OUTSIDE_REPOSITORY"
        if not candidate.is_file():
            return None, "MISSING_FILE"
    except OSError:
        return None, "READ_ERROR"
    return candidate, "OK"


def _safe_uses(content: str, relative: str) -> list[dict]:
    result = []
    for number, line in enumerate(content.splitlines(), 1):
        match = re.match(r"\s*(?:-\s*)?uses\s*:\s*([^#\s]+)", line)
        if match is None:
            continue
        action = match.group(1).strip("'\"")
        if SAFE_ACTION.fullmatch(action):
            status = "PINNED_SHA" if re.fullmatch(r"[0-9a-fA-F]{40}", action.rsplit("@", 1)[1]) else "TAG_OR_BRANCH"
        elif SAFE_LOCAL_ACTION.fullmatch(action):
            status, action = "LOCAL_ACTION", action
        else:
            status, action = "NONSTANDARD_REDACTED", "[REDACTED]"
        result.append({"workflow": relative, "line": number, "action": action, "pinning": status})
    return result


def _matching_signal(file: Path, line_number: object, finding_id: str) -> str:
    """Validate only the rule pattern at the reported line; never expose line text."""
    if finding_id == "SENSITIVE_FILENAME":
        return "FILE_EXISTS"
    if not isinstance(line_number, int) or isinstance(line_number, bool) or line_number <= 0:
        return "NOT_LINE_BASED"
    try:
        if file.stat().st_size > MAX_SOURCE_BYTES:
            return "TOO_LARGE_TO_RECHECK"
        content = file.read_text(encoding="utf-8", errors="replace").splitlines()
        if line_number > len(content):
            return "LINE_NO_LONGER_PRESENT"
        line = content[line_number - 1]
    except OSError:
        return "UNREADABLE"
    for ident, regex in SECRET_RE:
        if ident == finding_id:
            return "PATTERN_STILL_PRESENT" if regex.search(line) else "PATTERN_NOT_AT_REPORTED_LINE"
    for ident, regex, *_ in CODE_HEURISTICS:
        if ident == finding_id:
            return "PATTERN_STILL_PRESENT" if regex.search(line) else "PATTERN_NOT_AT_REPORTED_LINE"
    if finding_id == "WORKFLOW_UNPINNED_ACTION":
        found = re.search(r"\buses\s*:\s*([^\s#]+)", line)
        if not found:
            return "PATTERN_NOT_AT_REPORTED_LINE"
        ref = found.group(1).strip("'\"")
        if SAFE_ACTION.fullmatch(ref) and re.fullmatch(r"[0-9a-fA-F]{40}", ref.rsplit("@", 1)[1]):
            return "NOW_PINNED_SHA"
        return "REFERENCE_REQUIRES_REVIEW"
    return "MANUAL_REVIEW_REQUIRED"


def _validate_report(report: object) -> dict:
    if not isinstance(report, dict) or report.get("format") != "koa_audit.local_observation.v1":
        raise ValueError("Le fichier sélectionné n'est pas un audit LOCAL_OBSERVE v1.")
    repos = report.get("repositories")
    if not isinstance(repos, list) or len(repos) > MAX_REPOSITORIES:
        raise ValueError("Liste de dépôts invalide ou trop volumineuse.")
    return report


def build_triage(root: Path, audit_json: Path, *, max_depth: int = 4, progress=None) -> dict:
    root = root.expanduser().resolve()
    if not root.is_dir():
        raise ValueError("La racine des projets n'existe pas.")
    if audit_json.stat().st_size > MAX_INPUT:
        raise ValueError("audit.json dépasse la limite de 16 Mio.")
    report = _validate_report(json.loads(audit_json.read_text(encoding="utf-8-sig")))
    folders, discovery = discover_repositories([root], max_depth=max_depth)
    by_remote = defaultdict(list)
    for folder in folders:
        info = _git_info(folder)
        if info["remote_repository"]:
            by_remote[info["remote_repository"].casefold()].append({
                "location": str(folder), "git_head": info["head"]})
    duplicates = []
    for repo, instances in sorted(by_remote.items()):
        if len(instances) > 1:
            duplicates.append({"repository": repo, "candidates": instances})

    found_rows, flagged_counts, outcomes = [], Counter(), Counter()
    workflow_rows, sensitive_rows, large_rows = [], [], []
    seen = 0
    for entry in report["repositories"]:
        if not isinstance(entry, dict):
            continue
        name, location = entry.get("repository"), entry.get("location")
        if not isinstance(name, str) or not isinstance(location, str):
            continue
        # Never inspect arbitrary directories from untrusted reports outside chosen root.
        repo = Path(location).expanduser().resolve()
        item = {"repository": name, "local_location": str(repo), "audit_head": (entry.get("git") or {}).get("head"),
                "status": None, "current_head": None, "head_changed_since_audit": None, "finding_reviews": []}
        if not repo.is_relative_to(root):
            item["status"] = "OUTSIDE_SELECTED_ROOT"
        elif not (repo / ".git").exists():
            item["status"] = "GIT_REPOSITORY_MISSING"
        else:
            info = _git_info(repo)
            item["current_head"] = info["head"]
            if isinstance(item["audit_head"], str) and isinstance(info["head"], str):
                item["head_changed_since_audit"] = item["audit_head"] != info["head"]
            if info["remote_repository"] and info["remote_repository"].casefold() != name.casefold() and not name.startswith("LOCAL/"):
                item["status"] = "REMOTE_ID_MISMATCH"
            else:
                item["status"] = "RECHECKED"
        if item["status"] != "RECHECKED":
            outcomes[item["status"]] += 1
            found_rows.append(item)
            continue
        if progress:
            progress(f"Vérification locale : {name}")
        tracked = _tracked_files(repo)
        if tracked is None:
            item["status"] = "GIT_INDEX_UNAVAILABLE"
            outcomes[item["status"]] += 1
            found_rows.append(item)
            continue
        # Inspect only Git-tracked workflow files; never archive raw workflow content.
        for relative in sorted(p for p in tracked if p.startswith(".github/workflows/") and p.endswith((".yml", ".yaml"))):
            wf, why = _safe_file(repo, relative)
            if wf is not None and wf.stat().st_size <= MAX_WORKFLOW_BYTES:
                try:
                    refs = _safe_uses(wf.read_text(encoding="utf-8", errors="replace"), relative)
                    workflow_rows.extend({"repository": name, **row} for row in refs[:250])
                except OSError:
                    pass
        # All tracked names resembling sensitive files, without reading them.
        for relative in sorted(p for p in tracked if SENSITIVE_NAME.search(p))[:150]:
            file, reason = _safe_file(repo, relative)
            sensitive_rows.append({"repository": name, "path": relative,
                                   "tracked": True, "presence": reason})
        # Large Git-tracked sources the previous scanner may have skipped.
        for relative in sorted(tracked):
            if len(large_rows) >= 400:
                break
            file, reason = _safe_file(repo, relative)
            if file is None:
                continue
            try:
                size = file.stat().st_size
            except OSError:
                continue
            if size > 262144 and file.suffix.lower() in {".py", ".pyw", ".js", ".ts", ".tsx", ".json", ".yml", ".yaml", ".toml", ".rs", ".go", ".java", ".sh", ".ps1"}:
                large_rows.append({"repository": name, "path": relative, "bytes": size,
                                   "note": "Git-tracked candidate above original 256 KiB inspection ceiling"})
        findings = entry.get("findings")
        aggregate = entry.get("finding_counts")
        if isinstance(aggregate, dict):
            try:
                total_reported = sum(v for v in aggregate.values() if isinstance(v, int) and not isinstance(v, bool) and v >= 0)
                item["historical_aggregate_findings"] = total_reported
                item["historical_list_limit"] = max(0, total_reported - len(findings or [])) if isinstance(findings, list) else total_reported
            except (TypeError, ValueError):
                pass
        if not isinstance(findings, list):
            findings = []
        for finding in findings[:MAX_FINDINGS_PER_REPO]:
            if seen >= MAX_TOTAL_FINDINGS:
                break
            if not isinstance(finding, dict):
                continue
            ident, relative = finding.get("id"), finding.get("path")
            if not isinstance(ident, str) or ident not in SAFE_FINDING_IDS:
                continue
            seen += 1
            path, presence = _safe_file(repo, relative)
            checked = {"finding_id": ident, "path": relative if isinstance(relative, str) else "[INVALID]",
                       "audit_line": finding.get("line") if isinstance(finding.get("line"), int) else None,
                       "presence": presence, "git_tracked": relative in tracked if isinstance(relative, str) else False,
                       "git_ignored": (_git(repo, "check-ignore", "-q", "--", relative) is not None)
                                      if isinstance(relative, str) and ident == "SENSITIVE_FILENAME" and presence != "INVALID_PATH" else None,
                       "likely_test_or_docs": bool(TEST_PATH.search(relative)) if isinstance(relative, str) else None,
                       "recheck": _matching_signal(path, finding.get("line"), ident) if path is not None else presence}
            item["finding_reviews"].append(checked)
            flagged_counts[ident] += 1
            outcomes[checked["recheck"]] += 1
        found_rows.append(item)
    return {
        "format": FORMAT, "created_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "mode": "LOCAL_OBSERVE", "source_audit_generated_at": report.get("generated_at"),
        "selected_root": str(root), "network_required": False, "token_required": False,
        "source_repositories_mutated": False, "raw_source_files_included": False,
        "repository_checks": found_rows, "duplicate_git_remotes": duplicates,
        "discovery": {**discovery, "local_git_repositories_discovered": len(folders)},
        "workflow_references": workflow_rows, "tracked_sensitive_names": sensitive_rows,
        "large_tracked_source_files": large_rows,
        "counts": {"repositories_in_report": len(report["repositories"]), "repositories_rechecked": sum(x["status"] == "RECHECKED" for x in found_rows),
                   "findings_rechecked": seen, "by_finding_id": dict(flagged_counts), "by_recheck_status": dict(outcomes)},
        "limitations": [
            "No secrets or raw source files are included. The ZIP still contains local file paths and Git metadata.",
            "Rule matches at historical line numbers are not proofs of exploitable vulnerabilities; manual review is required.",
            "An unmatched historical finding may have moved to a different line rather than being fixed.",
            "Workflow references are parsed from local files only. CI execution results, CodeQL and CVEs remain unknown offline.",
            "Historical report capped its findings list: aggregate counts may exceed individually rechecked findings.",
        ],
    }


def write_triage_zip(payload: dict, path: Path) -> Path:
    path = path.expanduser().resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise FileExistsError(f"Le ZIP existe déjà : {path}")
    summary = (
        "# kOA — contre-vérification locale\n\n"
        f"Dépôts revérifiés : **{payload['counts']['repositories_rechecked']}**\n\n"
        f"Signalements revérifiés : **{payload['counts']['findings_rechecked']}**\n\n"
        f"Copies Git en doublon : **{len(payload['duplicate_git_remotes'])}**\n\n"
        f"Références GitHub Actions relevées : **{len(payload['workflow_references'])}**\n\n"
        "**Aucun code brut, fichier .env, clé ou secret copié.**\n\n"
        "Les correspondances de motifs ne sont pas des vulnérabilités confirmées.\n"
    )
    files = {
        "SUMMARY.md": summary.encode("utf-8"),
        "TRIAGE.json": json.dumps(payload, indent=2, ensure_ascii=False).encode("utf-8"),
        "workflows.json": json.dumps(payload["workflow_references"], indent=2, ensure_ascii=False).encode("utf-8"),
        "duplicates.json": json.dumps(payload["duplicate_git_remotes"], indent=2, ensure_ascii=False).encode("utf-8"),
        "sensitive_tracked_names.json": json.dumps(payload["tracked_sensitive_names"], indent=2, ensure_ascii=False).encode("utf-8"),
        "large_files.json": json.dumps(payload["large_tracked_source_files"], indent=2, ensure_ascii=False).encode("utf-8"),
    }
    temp_name = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, suffix=".tmp", delete=False) as f:
            temp_name = Path(f.name)
        with zipfile.ZipFile(temp_name, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
            for member, data in files.items():
                z.writestr(member, data)
        temp_name.replace(path)
    finally:
        if temp_name and temp_name.exists():
            temp_name.unlink()
    return path
