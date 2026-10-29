"""Bounded, offline, read-only workspace inspection.

Never contacts GitHub, runs checked-out project code or records secret values.
All findings are heuristic; no CVE database, CodeQL engine, or CI execution is implied.
"""
from __future__ import annotations

import csv
import json
import os
import re
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from .inventory import bundled_inventory
from .report import safe_csv
from .python_tls import tls_verification_disabled_lines

FORMAT = "koa_audit.local_observation.v1"
EXCLUDED_DIRS = {".git", ".svn", ".hg", "node_modules", ".venv", "venv", "env", "__pycache__",
                 ".mypy_cache", ".pytest_cache", ".next", ".nuxt", "dist", "build", "coverage",
                 "target", "vendor", ".idea", ".vscode", ".tox", ".cache", "site-packages",
                 "reports", ".legacy", "out", ".gradle", ".terraform"}
SOURCE_EXT = {".py", ".pyw", ".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs", ".java",
              ".kt", ".go", ".rs", ".php", ".rb", ".sh", ".ps1", ".yml", ".yaml", ".toml",
              ".json", ".xml", ".ini", ".cfg", ".txt", ".env"}
MANIFESTS = {"package.json", "package-lock.json", "pnpm-lock.yaml", "yarn.lock", "requirements.txt",
             "pyproject.toml", "poetry.lock", "pdm.lock", "uv.lock", "Pipfile", "Pipfile.lock",
             "Cargo.toml", "Cargo.lock", "go.mod", "go.sum", "pom.xml", "build.gradle",
             "build.gradle.kts", "Gemfile", "Gemfile.lock", "composer.json", "composer.lock",
             "Dockerfile", "Dockerfile.lock"}
SECRET_RE = [
    ("PRIVATE_KEY_MATERIAL", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----")),
    ("GITHUB_TOKEN_PATTERN", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9_]{25,}|github_pat_[A-Za-z0-9_]{30,})\b")),
    ("AWS_ACCESS_KEY_PATTERN", re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
]
CODE_HEURISTICS = [
    ("PYTHON_SHELL_TRUE", re.compile(r"\bshell\s*=\s*True\b"), "review", "Review shell=True invocation"),
    ("PYTHON_PICKLE_LOAD", re.compile(r"\bpickle\.(?:load|loads)\s*\("), "review", "Review deserialization of untrusted data"),
]


def _git_info(folder: Path) -> dict:
    """Local Git metadata only; no fetch, hooks, checkout, network or mutations."""
    result = {"head": None, "remote_repository": None}
    if not (folder / ".git").exists():
        return result
    for name, arguments in (("head", ["rev-parse", "HEAD"]),
                            ("remote_repository", ["config", "--get", "remote.origin.url"])):
        try:
            env = os.environ.copy()
            env["GIT_TERMINAL_PROMPT"] = "0"
            p = subprocess.run(["git", "-C", str(folder), *arguments], capture_output=True,
                               text=True, errors="replace", timeout=4, env=env, check=False)
        except (OSError, subprocess.TimeoutExpired):
            continue
        if p.returncode != 0:
            continue
        value = p.stdout.strip()
        if name == "head":
            if re.fullmatch(r"[a-fA-F0-9]{40,64}", value):
                result[name] = value
        else:
            # Strictly extract owner/repository, never persist raw remote URL or credentials.
            value = value.replace("\\", "/").removesuffix(".git").rstrip("/")
            match = re.search(r"(?:github\.com[:/])([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)$", value, re.I)
            if match:
                result[name] = match.group(1)
    return result


def discover_repositories(roots: list[Path], *, max_depth: int = 4, max_dirs: int = 12000) -> tuple[list[Path], dict]:
    """Folder scan only. No traversal through symlinks or into discovered Git repositories."""
    if not 0 <= max_depth <= 10:
        raise ValueError("max_depth must be between 0 and 10")
    found: dict[str, Path] = {}
    visited: set[str] = set()
    inspected = 0
    truncated = False
    missing_roots: list[str] = []
    for starting in roots:
        root = starting.expanduser().resolve()
        if not root.is_dir():
            missing_roots.append(str(root))
            continue
        stack: list[tuple[Path, int]] = [(root, 0)]
        while stack:
            folder, depth = stack.pop()
            identifier = str(folder).casefold()
            if identifier in visited:
                continue
            visited.add(identifier)
            inspected += 1
            if inspected > max_dirs:
                truncated = True
                break
            if (folder / ".git").exists():
                found[identifier] = folder
                continue
            if depth >= max_depth:
                continue
            try:
                with os.scandir(folder) as iterator:
                    children = [Path(entry.path) for entry in iterator
                                if entry.is_dir(follow_symlinks=False)
                                and entry.name not in EXCLUDED_DIRS
                                and (not entry.name.startswith(".") or entry.name == ".github")]
            except OSError:
                continue
            stack.extend((p, depth + 1) for p in sorted(children, reverse=True))
        if truncated:
            break
    return sorted(found.values(), key=lambda p: str(p).casefold()), {
        "directories_visited": inspected, "discovery_truncated": truncated, "missing_roots": missing_roots,
    }


def _repo_members(folder: Path, *, max_files: int) -> tuple[list[Path], bool]:
    """Enumerate bounded set of local regular files, without following symlinks."""
    members: list[Path] = []
    stack = [folder]
    truncated = False
    while stack:
        current = stack.pop()
        try:
            with os.scandir(current) as iterator:
                entries = list(iterator)
        except OSError:
            continue
        dirs = []
        for entry in entries:
            try:
                if entry.is_symlink():
                    continue
                if entry.is_dir(follow_symlinks=False):
                    if entry.name not in EXCLUDED_DIRS and (not entry.name.startswith(".") or entry.name == ".github"):
                        dirs.append(Path(entry.path))
                elif entry.is_file(follow_symlinks=False):
                    # Do not read data from uncontrolled files beyond the budget.
                    if len(members) >= max_files:
                        truncated = True
                        break
                    members.append(Path(entry.path))
            except OSError:
                continue
        if truncated:
            break
        stack.extend(sorted(dirs, reverse=True))
    return sorted(members), truncated


def scan_repository(folder: Path, *, inventory_name: str | None = None, max_files: int = 6000) -> dict:
    if max_files < 1 or max_files > 100000:
        raise ValueError("max_files out of range")
    members, truncated = _repo_members(folder, max_files=max_files)
    git = _git_info(folder)
    findings: list[dict] = []
    counts: Counter = Counter()
    manifests: set[str] = set()
    workflows: list[str] = []
    source_files = 0
    scanned_bytes = 0
    max_read_bytes = 262144
    for p in members:
        rel = p.relative_to(folder).as_posix()
        name = p.name
        if name in MANIFESTS or re.match(r"requirements[-_].*\.txt$", name):
            manifests.add(name)
        is_workflow = rel.startswith(".github/workflows/") and p.suffix in (".yml", ".yaml")
        if is_workflow:
            workflows.append(rel)
        if name.startswith(".env") and name not in (".env.example", ".env.sample", ".env.template"):
            counts["SENSITIVE_FILENAME"] += 1
            if len(findings) < 100:
                findings.append({"id": "SENSITIVE_FILENAME", "severity": "info", "path": rel,
                                 "line": None, "message": "Environment-style filename observed; name alone is not an exposure"})
        if p.suffix.lower() not in SOURCE_EXT and not is_workflow and name not in ("Dockerfile", ".env"):
            continue
        try:
            size = p.stat().st_size
            if size > max_read_bytes:
                counts["LARGE_FILE_NOT_INSPECTED"] += 1
                continue
            data = p.read_bytes()
            if b"\0" in data[:4096]:
                continue
            content = data.decode("utf-8", errors="replace")
        except OSError:
            counts["READ_ERROR"] += 1
            continue
        source_files += 1
        scanned_bytes += len(data)
        tls_lines = (tls_verification_disabled_lines(content)
                     if p.suffix.lower() in {".py", ".pyw"} else set())
        for num, line in enumerate(content.splitlines(), start=1):
            for code, pattern in SECRET_RE:
                if pattern.search(line):
                    counts[code] += 1
                    if len(findings) < 100:
                        findings.append({"id": code, "severity": "high_review", "path": rel,
                                         "line": num, "message": "Potential credential material (value never recorded)"})
            if num in tls_lines:
                counts["PYTHON_SSL_VERIFY_DISABLED"] += 1
                if len(findings) < 100:
                    findings.append({"id": "PYTHON_SSL_VERIFY_DISABLED", "severity": "review",
                                     "path": rel, "line": num,
                                     "message": "Python HTTP/TLS API may disable certificate verification"})
            if p.suffix.lower() in {".py", ".pyw"}:
                for code, pattern, sev, message in CODE_HEURISTICS:
                    if pattern.search(line):
                        counts[code] += 1
                        if len(findings) < 100:
                            findings.append({"id": code, "severity": sev, "path": rel,
                                             "line": num, "message": message})
        if is_workflow:
            checks = (("WORKFLOW_UNPINNED_ACTION", re.compile(r"(?m)^\s*-?\s*uses:\s*[^#\s]+@(?![0-9a-fA-F]{40}\s*(?:#.*)?$)[^\s#]+"),
                       "Action reference not pinned to full commit SHA"),
                      ("WORKFLOW_PULL_REQUEST_TARGET", re.compile(r"(?m)^\s*pull_request_target\s*:|\bpull_request_target\b"),
                       "Review high-privilege pull_request_target use"),
                      ("WORKFLOW_WRITE_ALL", re.compile(r"(?m)^\s*permissions:\s*write-all\b"),
                       "Workflow requests write-all permissions"),
                      ("WORKFLOW_REMOTE_SCRIPT", re.compile(r"\b(?:curl|wget)\b[^\n|]{0,200}\|\s*(?:bash|sh)\b"),
                       "Review remote script execution"))
            for code, pattern, message in checks:
                for match in list(pattern.finditer(content))[:20]:
                    counts[code] += 1
                    if len(findings) < 100:
                        findings.append({"id": code, "severity": "info" if code == "WORKFLOW_UNPINNED_ACTION" else "review", "path": rel,
                                         "line": content.count("\n", 0, match.start()) + 1, "message": message})
    workflows.sort()
    has_codeql = any("codeql" in wf.lower() for wf in workflows)
    # Only identifying a codeql action in workflow content (not name) would be stronger;
    # the status explicitly remains declared/unknown, not executed/verified.
    if not has_codeql:
        for path in workflows:
            try:
                text = (folder / path).read_text(encoding="utf-8", errors="replace")[:131072]
                if "github/codeql-action" in text:
                    has_codeql = True
                    break
            except OSError:
                pass
    return {
        "repository": inventory_name or git["remote_repository"] or f"LOCAL/{folder.name}",
        "location": str(folder), "access": "local_observed", "git": git,
        "files_enumerated": len(members), "files_inspected": source_files, "bytes_inspected": scanned_bytes,
        "file_inventory_truncated": truncated, "finding_list_truncated": sum(counts.values()) > len(findings),
        "workflows": workflows, "ci_status": "CONFIG_PRESENT_NOT_EXECUTED" if workflows else "NOT_FOUND_LOCALLY",
        "codeql": "CONFIG_PRESENT_NOT_EXECUTED" if has_codeql else "NOT_DETERMINED",
        "dependabot_config": (folder / ".github" / "dependabot.yml").is_file() or
                              (folder / ".github" / "dependabot.yaml").is_file(),
        "dependency_files": sorted(manifests), "findings": findings, "finding_counts": dict(counts),
        "vulnerability_database_check": "NOT_PERFORMED_OFFLINE", "secrets_scan_kind": "HEURISTIC_PATTERN_ONLY",
        "status": "PARTIAL" if truncated or counts["LARGE_FILE_NOT_INSPECTED"] or counts["READ_ERROR"]
                  else ("REVIEW" if any(f.get("severity") in ("review", "high_review") for f in findings)
                        else ("OBSERVED_INFORMATIONAL" if findings else "INSPECTED_NO_PATTERN_MATCH")),
    }


def run_local_audit(roots: list[Path], *, inventory_path: Path, max_depth: int = 4,
                    max_files: int = 6000, include_unlisted: bool = True,
                    limit: int = 0, progress=None) -> dict:
    rows, origin = bundled_inventory(inventory_path)
    inventory = {r["github_repo"].lower(): r["github_repo"] for r in rows}
    by_short: dict[str, list[str]] = {}
    for repo in inventory.values():
        by_short.setdefault(repo.rsplit("/", 1)[1].lower(), []).append(repo)
    folders, discovery = discover_repositories(roots, max_depth=max_depth)
    # Prefer an exact GitHub remote mapping; fallback by unique directory name.
    associated: dict[str, list[tuple[Path, dict]]] = {}
    unlisted: list[tuple[Path, dict]] = []
    for folder in folders:
        git = _git_info(folder)
        remote_name = git["remote_repository"]
        if remote_name and remote_name.lower() in inventory:
            name = inventory[remote_name.lower()]
        elif remote_name:
            name = None  # Remote doesn't match inventory; never force-map by directory name.
        else:
            choices = by_short.get(folder.name.lower(), [])
            name = choices[0] if len(choices) == 1 else None
        if name:
            associated.setdefault(name.lower(), []).append((folder, git))
        else:
            unlisted.append((folder, git))
    results: list[dict] = []
    missing: list[str] = []
    duplicates: list[str] = []
    selected = 0
    for row in rows:
        name = row["github_repo"]
        candidates = associated.get(name.lower(), [])
        if not candidates:
            missing.append(name)
            continue
        if len(candidates) > 1:
            duplicates.append(name)
            continue
        if limit and selected >= limit:
            break
        if progress:
            progress(f"Scanning {name} …")
        results.append(scan_repository(candidates[0][0], inventory_name=name, max_files=max_files))
        selected += 1
    if include_unlisted:
        for folder, git in unlisted:
            if limit and selected >= limit:
                break
            if progress:
                progress(f"Scanning local {folder.name} …")
            results.append(scan_repository(folder, max_files=max_files))
            selected += 1
    total_findings = Counter()
    for r in results:
        total_findings.update(r["finding_counts"])
    return {
        "format": FORMAT, "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "mode": "LOCAL_OBSERVE", "network_required": False, "token_required": False,
        "source_repositories_mutated": False, "roots": [str(p.expanduser().resolve()) for p in roots],
        "inventory": origin, "discovery": discovery, "declared_repositories": len(rows),
        "local_repositories_discovered": len(folders), "inventory_repositories_missing_locally": missing,
        "ambiguous_duplicates": duplicates,
        "repositories_scanned": len(results), "findings_by_type": dict(total_findings),
        "repositories": results,
        "caveats": ["Offline heuristics only: not CodeQL, Dependabot, live GitHub API or an authoritative CVE scan.",
                    "No CI workflow was executed; presence of workflow files does not prove they pass.",
                    "Sensitive values are never included in the report; findings may require manual review.",
                    "Missing repositories may exist elsewhere; scan only searches selected local roots.",
                    "Local files, including untracked files, can be inspected; not equivalent to Git tracked contents.",
                    "No repository code executed, no Git remote contacted, no security authority transferred."],
    }


def write_local_reports(out: Path, report: dict) -> None:
    out.mkdir(parents=True, exist_ok=True)
    (out / "audit.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    columns = ["repository", "local_folder", "status", "files_inspected", "workflows", "codeql_configuration",
               "dependabot_configuration", "dependency_files", "potential_secrets", "review_findings", "git_head"]
    with (out / "audit.csv").open("w", newline="", encoding="utf-8-sig") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns)
        writer.writeheader()
        for r in report["repositories"]:
            counts = r["finding_counts"]
            item = {"repository": r["repository"], "local_folder": r["location"], "status": r["status"],
                    "files_inspected": r["files_inspected"], "workflows": len(r["workflows"]),
                    "codeql_configuration": r["codeql"], "dependabot_configuration": r["dependabot_config"],
                    "dependency_files": len(r["dependency_files"]),
                    "potential_secrets": sum(v for k, v in counts.items() if k.endswith("_PATTERN") or k == "PRIVATE_KEY_MATERIAL"),
                    "review_findings": sum(counts.values()), "git_head": r["git"]["head"] or ""}
            writer.writerow({k: safe_csv(v) for k, v in item.items()})
    lines = ["# kOA — Local repository audit", "", f"UTC: {report['generated_at']}",
             "", "**Mode: LOCAL_OBSERVE — offline, no token, no network.**", "",
             f"Repositories discovered: **{report['local_repositories_discovered']}**",
             f"Repositories scanned: **{report['repositories_scanned']}**",
             f"Declared inventory: **{report['declared_repositories']}**",
             f"Missing locally: **{len(report['inventory_repositories_missing_locally'])}**",
             f"Ambiguous local duplicates: **{len(report['ambiguous_duplicates'])}**", "",
             "## Observed pattern findings", ""]
    if report["findings_by_type"]:
        for k, v in sorted(report["findings_by_type"].items()):
            lines.append(f"- {k}: {v}")
    else:
        lines.append("No selected patterns matched. This is **not** a vulnerability-free verdict.")
    lines += ["", f"Historical records imported (separate, not current): **{len(report.get('historical_legacy', []))}**",
              "", "## Coverage", "", "| Repository | Inspection | Workflows | CodeQL config | Findings |",
              "| --- | --- | ---: | --- | ---: |"]
    for r in report["repositories"]:
        clean = lambda x: str(x).replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {clean(r['repository'])} | {r['status']} | {len(r['workflows'])} | {r['codeql']} | {sum(r['finding_counts'].values())} |")
    lines += ["", "## What cannot be concluded", "",
              "- No CVEs were checked against an offline or online vulnerability database.",
              "- No GitHub Actions were executed; CI status is unknown.",
              "- No full secret-scanning service was run; findings are heuristic.",
              "- No CodeQL analysis was executed; only local configuration could be observed.", ""]
    (out / "SUMMARY.md").write_text("\n".join(lines), encoding="utf-8")
