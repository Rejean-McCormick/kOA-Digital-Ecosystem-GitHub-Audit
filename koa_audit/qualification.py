"""Evidence-scoped maturity and qualification registry for kOA.

There is no live audit and no inference from filenames, code size, CI presence,
static patterns, or engineering profiles. The separately reviewed 2026-10-30
documentary adjudication can be imported once at the owner's explicit request.
Each claim is scoped to one repository and one qualification stage.
"""
from __future__ import annotations

import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from . import profiles

SCHEMA = "koa_qualification.evidence.v1"
STAGES = (
    ("specified", "Spécifié / architecturé"),
    ("implemented", "Implémenté"),
    ("qualified", "Testé / qualifié"),
    ("integrated", "Intégré entre systèmes"),
    ("production", "Éprouvé en production"),
)
STAGE_IDS = tuple(item[0] for item in STAGES)
STATES = ("Non évalué", "Non applicable", "À documenter", "Étayé par preuve")


def state_path() -> Path:
    root = Path(os.environ.get("LOCALAPPDATA") or (Path.home() / ".local" / "share"))
    return root / "kOA-GitHub-Audit" / "profiles" / "qualification.json"


def _validate_repo(project: Path, name: str) -> str:
    return profiles.repo_key(name, project)


def load_state(path: Path | None = None) -> dict:
    path = path or state_path()
    if not path.exists():
        return {"format": SCHEMA, "claims": {}}
    raw = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(raw, dict) or raw.get("format") != SCHEMA or not isinstance(raw.get("claims"), dict):
        raise ValueError("Registre de qualification non valide")
    return raw


def get_claim(project: Path, repo: str, stage: str, path: Path | None = None) -> dict:
    name = _validate_repo(project, repo)
    if stage not in STAGE_IDS:
        raise ValueError("Jalon de qualification inconnu")
    record = load_state(path)["claims"].get(name, {}).get(stage, {})
    if not isinstance(record, dict):
        record = {}
    status = record.get("status")
    return {
        "status": status if status in STATES else STATES[0],
        "evidence": str(record.get("evidence", ""))[:1500],
        "scope": str(record.get("scope", ""))[:300],
        "reviewed_at": str(record.get("reviewed_at", ""))[:50],
    }


def set_claim(project: Path, repo: str, stage: str, status: str,
              evidence: str = "", scope: str = "", path: Path | None = None) -> Path:
    """Persist an explicit, reviewed claim; no GitHub or source mutations."""
    canonical = _validate_repo(project, repo)
    if stage not in STAGE_IDS or status not in STATES:
        raise ValueError("Jalon ou statut inconnu")
    if len(evidence) > 1500 or len(scope) > 300:
        raise ValueError("Description de preuve ou de portée trop longue")
    if status == "Étayé par preuve" and (len(evidence.strip()) < 8 or not scope.strip()):
        raise ValueError("Un statut étayé exige une référence de preuve et une portée explicite")
    path = path or state_path()
    state = load_state(path)
    state["claims"].setdefault(canonical, {})[stage] = {
        "status": status,
        "evidence": evidence.strip(),
        "scope": scope.strip(),
        "reviewed_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix="koa-qualification-", suffix=".json", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(state, stream, ensure_ascii=False, indent=2, sort_keys=True)
            stream.write("\n")
        Path(tmp_name).replace(path)
    finally:
        Path(tmp_name).unlink(missing_ok=True)
    return path


def progress(project: Path, repo: str, path: Path | None = None) -> dict:
    """Independent stage states; NEVER reduce them to one global readiness grade."""
    records = {stage: get_claim(project, repo, stage, path) for stage in STAGE_IDS}
    return {
        "stages": records,
        "evidenced": sum(v["status"] == "Étayé par preuve" for v in records.values()),
        "assessed": sum(v["status"] != "Non évalué" for v in records.values()),
        "total": len(STAGE_IDS),
    }


def ecosystem_board(project: Path, qualification_path: Path | None = None,
                    practice_path: Path | None = None) -> list[dict]:
    """Private evidence board for the authoritative 49-repository inventory.

    Never merge the separate five maturity axes into one rank or grade.
    Supplemental repositories are intentionally not added to the official board.
    """
    claims = load_state(qualification_path)["claims"]
    review = profiles.load_state(practice_path)["assessments"]
    pattern_ids = [p["id"] for p in profiles.catalog(project)]
    entries: list[dict] = []
    for repo in profiles.inventory(project):
        stages = claims.get(repo, {})
        assessments = review.get(repo, {})
        statuses = {}
        for key in STAGE_IDS:
            rec = stages.get(key, {})
            state = rec.get("status") if isinstance(rec, dict) else None
            statuses[key] = state if state in STATES else STATES[0]
        practice_counts = {key: 0 for key in profiles.STATUSES}
        for pattern_id in pattern_ids:
            rec = assessments.get(pattern_id, {})
            state = rec.get("status") if isinstance(rec, dict) else None
            practice_counts[state if state in practice_counts else profiles.STATUSES[0]] += 1
        measured = (profiles.profile_directory(project, repo) / "ENGINEERING_METRICS.json").is_file()
        entries.append({
            "repository": repo,
            "stages": statuses,
            "practice_counts": practice_counts,
            "engineering_profile": measured,
        })
    return entries
