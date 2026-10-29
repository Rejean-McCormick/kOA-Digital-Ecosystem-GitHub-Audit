"""Publish *only* allowlisted aggregate dashboard data to the dedicated audit repo.

This is the one explicit remote-writing operation in the application. It never
scans/pushes source repositories, never force-pushes, never copies raw reports.
"""
from __future__ import annotations

import json
import os
import subprocess
import tempfile
from pathlib import Path
from typing import Callable

from .dashboard import _sanitize_previous, publish_reports, load_published, FORMAT, MAX_HISTORY

AUDIT_REPO = "Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit"
GITHUB_REMOTE = "https://github.com/" + AUDIT_REPO + ".git"


def latest_reports(folder: Path, downloads: Path | None = None) -> list[Path]:
    """Find the newest known raw report of *each* mode (never rescan)."""
    roots = [folder / "reports" / "local", folder / "reports" / "github"]
    if downloads is not None:
        roots.append(downloads)
    newest: dict[str, tuple[str, Path]] = {}
    for directory in roots:
        if not directory.is_dir():
            continue
        # Bounds scanning to a few JSON candidates. Do not traverse the repo.
        for path in list(directory.glob("audit*.json"))[:100]:
            try:
                if path.stat().st_size > 30_000_000:
                    continue
                report = json.loads(path.read_text(encoding="utf-8-sig"))
                mode = report.get("format")
                at = report.get("generated_at", "")
                if (mode not in ("koa_audit.local_observation.v1", "koa_audit.observation.v1")
                        or not isinstance(at, str)):
                    continue
                if mode not in newest or at > newest[mode][0]:
                    newest[mode] = (at, path)
            except (OSError, UnicodeError, ValueError, TypeError):
                continue
    return [v[1] for v in newest.values()]


def _run_git(git: str, *args: str, cwd: Path | None = None) -> str:
    cmd = [git, *args]
    try:
        proc = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True,
                              encoding="utf-8", errors="replace", timeout=180,
                              env={**os.environ, "GIT_TERMINAL_PROMPT": "0"})
    except FileNotFoundError as e:
        raise RuntimeError("Git n'est pas installé ou n'est pas dans PATH") from e
    except subprocess.TimeoutExpired as e:
        raise RuntimeError("Git a pris trop de temps; publication non confirmée") from e
    if proc.returncode:
        # Do not surface raw stderr: credential helpers might echo sensitive URLs.
        raise RuntimeError(
            "La commande Git a échoué (" + args[0] + "). "
            "Vérifier la connexion GitHub de Git pour Windows, les droits d'écriture "
            "et que main n'est pas protégée. Aucun push forcé n'a été tenté."
        )
    return proc.stdout.strip()


def _merge_history(data_path: Path, local_published: Path | None) -> None:
    # First sanitize all prior values, regardless of their source.
    existing = load_published(data_path)
    extra = load_published(local_published) if local_published and local_published.is_file() else []
    snapshots = {(entry["mode"], entry["at"]): _sanitize_previous(entry)
                 for entry in existing + extra}
    payload = {"format": FORMAT,
               "policy": "AGGREGATES_ONLY_NO_PATHS_NO_SECRETS",
               "snapshots": sorted(snapshots.values(), key=lambda i: (i["at"], i["mode"]))[-MAX_HISTORY:]}
    data_path.parent.mkdir(parents=True, exist_ok=True)
    data_path.write_text(json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")


def publish_to_github(
    project: Path,
    sources: list[Path] | None = None,
    *,
    remote: str = GITHUB_REMOTE,
    git: str = "git",
    progress: Callable[[str], None] = print,
) -> dict:
    """Clone audit repo into a temp dir and push only safe aggregates + Pages workflow.

    Remote parameter is intended for local-bare-repository tests only; launcher
    always uses the fixed audit repository URL. This call modifies GitHub.
    """
    project = Path(project)
    chosen = list(sources) if sources is not None else latest_reports(project, Path.home() / "Downloads")
    # Fail early rather than producing empty history or silently discarding data.
    for src in chosen:
        if not src.is_file():
            raise ValueError("Rapport JSON introuvable : " + str(src))
    local_published = project / "docs" / "data" / "dashboard.json"
    if not local_published.is_file() and not chosen:
        raise ValueError("Aucun bilan à publier. Fournir un rapport ou générer un tableau de bord local.")
    progress("Publication du bilan agrégé uniquement (pas de nouvel audit, aucun .env).")
    with tempfile.TemporaryDirectory(prefix="koa-dashboard-") as temporary:
        folder = Path(temporary) / "audit_repo"
        # We do not use a person's source-repository checkout, ever.
        _run_git(git, "clone", "--quiet", "--depth", "1", "--branch", "main", "--single-branch", "--", remote, str(folder))
        destination = folder / "docs" / "data" / "dashboard.json"
        if not (folder / "docs" / "index.html").is_file():
            raise RuntimeError("Le dépôt distant ne contient pas le site docs/index.html. Rien n'a été publié.")
        # Bootstrap GitHub Pages deployment in the same normal push; source is
        # the reviewed, packaged application workflow, not a user-supplied file.
        packaged_workflow = project / ".github" / "workflows" / "dashboard-pages.yml"
        if not packaged_workflow.is_file():
            raise RuntimeError("Workflow GitHub Pages manquant dans l'application")
        remote_workflow = folder / ".github" / "workflows" / "dashboard-pages.yml"
        remote_workflow.parent.mkdir(parents=True, exist_ok=True)
        remote_workflow.write_bytes(packaged_workflow.read_bytes())
        _merge_history(destination, local_published)
        if chosen:
            publish_reports(chosen, folder / "docs")
        status = _run_git(git, "status", "--porcelain", "--", "docs/data/dashboard.json", ".github/workflows/dashboard-pages.yml", cwd=folder)
        if not status:
            progress("Le tableau de bord GitHub est déjà à jour.")
            return {"status": "already_current", "reports_used": len(chosen), "repository": AUDIT_REPO}
        _run_git(git, "add", "--", "docs/data/dashboard.json", ".github/workflows/dashboard-pages.yml", cwd=folder)
        # Stable app identity if user has not configured git globally.
        _run_git(git, "-c", "user.name=kOA Audit Dashboard", "-c",
                 "user.email=koa-audit@users.noreply.github.com", "commit", "--quiet",
                 "-m", "dashboard: publish aggregate audit results", cwd=folder)
        # Normal fast-forward-only push. If someone updates main concurrently,
        # report a conflict and stop rather than overwrite another commit.
        _run_git(git, "push", "--quiet", "origin", "HEAD:refs/heads/main", cwd=folder)
        progress("Bilan publié dans le dépôt d'audit. GitHub Pages déploiera le site si activé.")
        return {"status": "published", "reports_used": len(chosen), "repository": AUDIT_REPO}
