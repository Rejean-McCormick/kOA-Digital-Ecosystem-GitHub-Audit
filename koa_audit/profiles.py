"""Local-only engineering/security profile registry and manual pattern assessments.

Never infer compliance from audit findings, control presence, or a profile's absence.
The 86 patterns are source-indexed metadata, not automatically applied assertions.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import tempfile
from datetime import datetime, timezone
from pathlib import Path

CATALOG_FORMAT = "koa_profiles.catalog.v1"
STATE_FORMAT = "koa_profiles.assessments.v1"
STATUSES = ("Non évalué", "Pas applicable", "À améliorer", "Appliqué")
PROFILE_NAMES = ("ENGINEERING_PROFILE.md", "SECURITY_PROFILE.md")


def inventory(project: Path) -> list[str]:
    raw = json.loads((project / "data/initial_inventory.json").read_text(encoding="utf-8"))
    return sorted({str(x["github_repo"]) for x in raw if isinstance(x, dict) and x.get("github_repo")}, key=str.casefold)


def catalog(project: Path) -> list[dict]:
    p = project / "profiles/catalog.json"
    raw = json.loads(p.read_text(encoding="utf-8"))
    if raw.get("format") != CATALOG_FORMAT or not isinstance(raw.get("patterns"), list):
        raise ValueError("Catalogue de profils invalide")
    ids = set()
    patterns = []
    for item in raw["patterns"]:
        if not isinstance(item, dict) or not re.fullmatch(r"(?:ARCH|SEC)-\d\d", str(item.get("id", ""))):
            raise ValueError("Identifiant de pratique invalide")
        if item["id"] in ids:
            raise ValueError("Doublon dans le catalogue")
        if item.get("family") not in ("architecture", "security"):
            raise ValueError("Famille invalide")
        ids.add(item["id"])
        patterns.append({k: str(item[k]) for k in ("id", "family", "category", "title", "source")})
    return patterns


def repo_key(name: str, project: Path) -> str:
    lookup = {x.casefold(): x for x in inventory(project)}
    if name.casefold() not in lookup:
        raise ValueError("Dépôt absent de l'inventaire")
    return lookup[name.casefold()]


def profile_directory(project: Path, repo: str) -> Path:
    """The only approved repo-dependent path is a fixed inventory slug."""
    canonical = repo_key(repo, project)
    return project / "profiles" / "repositories" / canonical.split("/", 1)[-1]


def get_profile(project: Path, repo: str, kind: str) -> str | None:
    if kind not in PROFILE_NAMES:
        raise ValueError("Type de profil non autorisé")
    path = profile_directory(project, repo) / kind
    if not path.is_file():
        return None
    if path.is_symlink() or path.stat().st_size > 2_000_000:
        raise ValueError("Fichier de profil non autorisé")
    return path.read_text(encoding="utf-8-sig")


def install_profile(project: Path, repo: str, kind: str, source: Path) -> Path:
    """Copy a user-approved Markdown report into the project profile folder."""
    if kind not in PROFILE_NAMES:
        raise ValueError("Type de profil invalide")
    if not source.is_file() or source.is_symlink() or source.suffix.lower() != ".md":
        raise ValueError("Choisir un fichier Markdown ordinaire")
    if source.stat().st_size > 2_000_000:
        raise ValueError("Profil trop volumineux")
    text = source.read_text(encoding="utf-8-sig")
    if not text.strip():
        raise ValueError("Profil vide")
    folder = profile_directory(project, repo)
    folder.mkdir(parents=True, exist_ok=True)
    dest = folder / kind
    dest.write_text(text, encoding="utf-8")
    return dest


def get_pattern_text(project: Path, pattern_id: str) -> str:
    """Inspect a bundled, user-provided architecture/security pattern locally."""
    target = next((p for p in catalog(project) if p["id"] == pattern_id), None)
    if not target:
        raise ValueError("Pratique inconnue")
    root = (project / "profiles" / "library").resolve()
    src = (root / target["source"]).resolve()
    if not src.is_relative_to(root) or not src.is_file() or src.stat().st_size > 200_000:
        raise ValueError("Fiche de pratique manquante ou invalide")
    return src.read_text(encoding="utf-8-sig")


def state_path() -> Path:
    """User state survives replacing the app's extracted ZIP. No Git remote writes."""
    base = Path(os.environ.get("LOCALAPPDATA") or Path.home() / ".local" / "share")
    return base / "kOA-GitHub-Audit" / "profiles" / "assessments.json"


def load_state(path: Path | None = None) -> dict:
    path = path or state_path()
    if not path.exists():
        return {"format": STATE_FORMAT, "assessments": {}}
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict) or raw.get("format") != STATE_FORMAT or not isinstance(raw.get("assessments"), dict):
        raise ValueError("Évaluations locales invalides")
    return raw


def get_assessment(project: Path, repo: str, pattern_id: str, path: Path | None = None) -> dict:
    canonical = repo_key(repo, project)
    if pattern_id not in {p["id"] for p in catalog(project)}:
        raise ValueError("Pratique inconnue")
    state = load_state(path)
    record = state["assessments"].get(canonical, {}).get(pattern_id, {})
    status = record.get("status") if isinstance(record, dict) else None
    return {"status": status if status in STATUSES else STATUSES[0],
            "note": str(record.get("note", "")) if isinstance(record, dict) else "",
            "reviewed_at": record.get("reviewed_at", "") if isinstance(record, dict) else ""}


def set_assessment(project: Path, repo: str, pattern_id: str, status: str, note: str = "", path: Path | None = None) -> Path:
    canonical = repo_key(repo, project)
    if pattern_id not in {p["id"] for p in catalog(project)}:
        raise ValueError("Pratique inconnue")
    if status not in STATUSES:
        raise ValueError("Statut inconnu")
    if len(note) > 2000:
        raise ValueError("Note trop longue (2000 caractères max)")
    path = path or state_path()
    state = load_state(path)
    state["assessments"].setdefault(canonical, {})[pattern_id] = {
        "status": status, "note": note,
        "reviewed_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    # Atomic write; never write an assessment to Git repos under audit.
    fd, tmp_name = tempfile.mkstemp(prefix="koa-profiles-", suffix=".json", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(state, stream, ensure_ascii=False, indent=2, sort_keys=True)
            stream.write("\n")
        Path(tmp_name).replace(path)
    finally:
        Path(tmp_name).unlink(missing_ok=True)
    return path


def progress(project: Path, repo: str, path: Path | None = None) -> dict:
    canonical = repo_key(repo, project)
    records = load_state(path)["assessments"].get(canonical, {})
    counts = {s: 0 for s in STATUSES}
    for p in catalog(project):
        v = records.get(p["id"], {})
        s = v.get("status") if isinstance(v, dict) else None
        counts[s if s in counts else STATUSES[0]] += 1
    counts["total"] = sum(counts.values())
    counts["reviewed"] = counts["total"] - counts[STATUSES[0]]
    return counts


def audit_context(project: Path, repo: str, report_path: Path) -> dict | None:
    """Read the known local-audit JSON only; no scan and no remote calls."""
    canonical = repo_key(repo, project)
    if not report_path.is_file() or report_path.stat().st_size > 30_000_000:
        return None
    report = json.loads(report_path.read_text(encoding="utf-8-sig"))
    if report.get("format") != "koa_audit.local_observation.v1":
        return None
    for entry in report.get("repositories", []):
        if isinstance(entry, dict) and str(entry.get("repository", "")).casefold() == canonical.casefold():
            return {
                "status": str(entry.get("status", "UNKNOWN")),
                "files_enumerated": int(entry.get("files_enumerated") or 0),
                "files_inspected": int(entry.get("files_inspected") or 0),
                "findings": sum(int(v) for v in (entry.get("finding_counts") or {}).values()),
                "head": str((entry.get("git") or {}).get("head", ""))[:12],
            }
    return None
