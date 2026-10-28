"""Historical diagnostic summary import (metadata only, no re-execution)."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from zipfile import ZipFile

from .inventory import check_repo

SCHEMAS = {
    "KonnaxionDiag": "konnaxiondiag.campaign-summary.v4",
    "KorDiag": "kordiag.summary.v1",
    "KristalDiag": "kristaldiag.summary.v1",
    "LevelUpDiag-Orgo": "levelupdiag.campaign-summary.v2",
    "LevelUpDiag-SemantiK": "levelupdiag.campaign-summary.v2",
    "LevelUpDiag-Skope": "levelupdiag.campaign-summary.v2",
}
VERDICTS = {"PASS", "WARN", "FAIL", "SKIP", "BLOCKED", "PARTIAL", "ERROR", "INFRA_ERROR", "CONFIG_ERROR"}
FORMAT = "koa_audit.legacy_record.v1"
MAX_BYTES = 5_000_000


def load_source(path: Path, member: str | None = None) -> bytes:
    if member is not None:
        if path.suffix.lower() != ".zip" or member.startswith("/") or ".." in member.split("/"):
            raise ValueError("Invalid ZIP member")
        with ZipFile(path) as z:
            info = z.getinfo(member)
            if info.file_size > MAX_BYTES:
                raise ValueError("Legacy JSON too large")
            contents = z.read(info)
    else:
        if path.suffix.lower() != ".json" or path.stat().st_size > MAX_BYTES:
            raise ValueError("Expected a small JSON file, or a ZIP with explicit --member")
        contents = path.read_bytes()
    if len(contents) > MAX_BYTES:
        raise ValueError("Legacy JSON too large")
    return contents


def normalize_legacy(tool: str, repo: str, data: bytes, *, label: str) -> dict:
    check_repo(repo)
    if tool not in SCHEMAS:
        raise ValueError("Unsupported diagnostic family")
    original = json.loads(data)
    if not isinstance(original, dict) or original.get("schema") != SCHEMAS[tool]:
        raise ValueError("Unexpected or missing legacy schema")
    verdict = original.get("verdict")
    if verdict not in VERDICTS:
        raise ValueError("Unrecognized legacy verdict")
    levels = original.get("levels")
    if not isinstance(levels, list):
        raise ValueError("Legacy campaign is missing levels")
    # Retain only narrowly selected metadata. No findings, paths, personal data,
    # free-text messages, or signed authorization payloads are imported.
    compact_levels = []
    for level in levels:
        if not isinstance(level, dict):
            continue
        name = str(level.get("id", level.get("level_id", "unknown")))[:50]
        level_verdict = level.get("verdict", "UNKNOWN")
        findings = level.get("findings")
        count = len(findings) if isinstance(findings, list) else (findings if isinstance(findings, int) and findings >= 0 else None)
        compact_levels.append({"id": name,
                               "verdict": level_verdict if level_verdict in VERDICTS else "UNKNOWN",
                               "findings_count": count})
    subject = original.get("subject") or {}
    git = subject.get("git") or {} if isinstance(subject, dict) else {}
    commit = git.get("commit") if isinstance(git, dict) else None
    record = {
        "format": FORMAT, "source_kind": "historical_legacy",
        "tool": tool, "repository": repo, "source_schema": original["schema"],
        "run_id": str(original.get("run_id", "unknown"))[:120],
        "campaign": str(original.get("campaign", original.get("selection", "unknown")))[:120],
        "verdict": verdict, "levels": compact_levels,
        "reported_finished_at": original.get("ended_at"),
        "subject_commit_declared": commit,
        "subject_digest_declared": subject.get("subject_digest") if isinstance(subject, dict) else None,
        "evidence_digest_declared": original.get("evidence_digest"),
        "evidence_integrity_section_present": isinstance(original.get("evidence_integrity"), dict),
        "evidence_independently_verified": False,
        "source_sha256": hashlib.sha256(data).hexdigest(),
        "source_label": Path(label).name[:150],
        "ingested_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "current_security_conclusion": "NOT_ASSESSED",
        "authority": "non_authoritative_observation",
    }
    return record


def ingest(tool: str, repo: str, source: Path, *, member: str | None = None) -> dict:
    content = load_source(source, member)
    return normalize_legacy(tool, repo, content, label=(member or source.name))


def load_normalized_directory(folder: Path) -> tuple[list[dict], list[str]]:
    if not folder.is_dir():
        raise ValueError("Legacy directory not found")
    records = []
    errors = []
    for path in sorted(folder.glob("*.json")):
        try:
            if path.stat().st_size > MAX_BYTES:
                raise ValueError("oversized")
            record = json.loads(path.read_text(encoding="utf-8"))
            if record.get("format") != FORMAT or record.get("source_kind") != "historical_legacy":
                raise ValueError("not normalized")
            check_repo(record["repository"])
            if record.get("current_security_conclusion") != "NOT_ASSESSED":
                raise ValueError("unexpected security conclusion")
            records.append(record)
        except (ValueError, KeyError, OSError, json.JSONDecodeError, TypeError):
            errors.append(path.name)
    return records, errors
