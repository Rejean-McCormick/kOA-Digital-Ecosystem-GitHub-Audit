"""Private, metadata-only adapter for Diagnostic du kOA Digital Ecosystem.

Reads a completed LevelUpDiag campaign, never runs the diagnostic, never reads target
repositories and never promotes a diagnostic observation into an audit certification.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

SOURCE_SCHEMA = "levelupdiag.campaign-summary.v2"
LEVEL_SCHEMA = "levelupdiag.report.v2"
SUITE = "Diagnostic du kOA Digital Ecosystem"
RECORD_FORMAT = "koa_audit.ecosystem_diag_observation.v1"
VERDICTS = frozenset({"PASS", "WARN", "FAIL", "SKIP", "BLOCKED", "PARTIAL", "ERROR", "INFRA_ERROR", "CONFIG_ERROR"})
RUN_ID = re.compile(r"[A-Za-z0-9._-]{1,120}\Z")
LEVEL_ID = re.compile(r"N[0-9]{2,3}\Z")
MAX_JSON = 5_000_000
MAX_ZIP_SIZE = 50_000_000
MAX_ZIP_FILES = 400
MAX_RECORDS = 200


def private_store() -> Path:
    home = Path(os.environ.get("LOCALAPPDATA") or Path.home() / ".local" / "share")
    return home / "kOA-GitHub-Audit" / "ecosystem-diag"


def _parse(raw: bytes, purpose: str) -> dict:
    if len(raw) > MAX_JSON:
        raise ValueError(f"{purpose}: taille excessive")
    try:
        data = json.loads(raw.decode("utf-8-sig"))
    except (UnicodeError, json.JSONDecodeError) as e:
        raise ValueError(f"{purpose}: JSON invalide") from e
    if not isinstance(data, dict):
        raise ValueError(f"{purpose}: objet JSON attendu")
    return data


def _load(root: Path) -> tuple[bytes, dict[str, bytes]]:
    """Return summary and strictly relevant level results; reject ambiguous runs."""
    members: dict[str, bytes] = {}
    if root.is_dir():
        if root.is_symlink():
            raise ValueError("Dossier symbolique non autorise")
        summary_path = root / "summary.json"
        if not summary_path.is_file() or summary_path.is_symlink():
            raise ValueError("summary.json absent dans le dossier de campagne")
        if summary_path.stat().st_size > MAX_JSON:
            raise ValueError("summary.json trop volumineux")
        summary_bytes = summary_path.read_bytes()
        levels_dir = root / "levels"
        if levels_dir.is_dir() and not levels_dir.is_symlink():
            for file in sorted(levels_dir.glob("N*/result.json")):
                if file.is_symlink() or file.stat().st_size > MAX_JSON:
                    raise ValueError("Resultat de niveau symbolique ou trop volumineux")
                name = file.parent.name
                if LEVEL_ID.fullmatch(name):
                    members[name] = file.read_bytes()
        return summary_bytes, members
    if not root.is_file() or root.is_symlink():
        raise ValueError("Campagne introuvable")
    if root.suffix.casefold() == ".json":
        if root.stat().st_size > MAX_JSON:
            raise ValueError("summary.json trop volumineux")
        return root.read_bytes(), members
    if root.suffix.casefold() != ".zip":
        raise ValueError("Attendu: dossier de campagne, summary.json ou ZIP")
    with zipfile.ZipFile(root) as archive:
        infos = archive.infolist()
        if len(infos) > MAX_ZIP_FILES or sum(i.file_size for i in infos) > MAX_ZIP_SIZE:
            raise ValueError("Archive trop volumineuse")
        paths: set[str] = set()
        for info in infos:
            name = info.filename
            posix = PurePosixPath(name)
            if name.startswith(("/", "\\")) or "\\" in name or ".." in posix.parts or posix.is_absolute():
                raise ValueError("Chemin ZIP non sur")
            if name in paths:
                raise ValueError("Doublon ZIP")
            paths.add(name)
            if (info.external_attr >> 16) & 0o170000 == 0o120000:
                raise ValueError("Lien symbolique ZIP non autorise")
        summaries = [i for i in infos if not i.is_dir() and PurePosixPath(i.filename).name == "summary.json"]
        if len(summaries) != 1:
            raise ValueError("ZIP: exactement un summary.json requis")
        summary_info = summaries[0]
        if summary_info.file_size > MAX_JSON:
            raise ValueError("summary.json trop volumineux")
        prefix = PurePosixPath(summary_info.filename).parent
        summary_bytes = archive.read(summary_info)
        for info in infos:
            if info.is_dir():
                continue
            path = PurePosixPath(info.filename)
            try:
                relative = path.relative_to(prefix)
            except ValueError:
                continue
            if len(relative.parts) == 3 and relative.parts[0] == "levels" and relative.parts[2] == "result.json" and LEVEL_ID.fullmatch(relative.parts[1]):
                if info.file_size > MAX_JSON:
                    raise ValueError("Resultat de niveau trop volumineux")
                members[relative.parts[1]] = archive.read(info)
        return summary_bytes, members


def _count(value: object) -> int | None:
    return value if type(value) is int and 0 <= value <= 1_000_000 else None


def _counts(source: object, fields: tuple[str, ...]) -> dict[str, int | None]:
    value = source if isinstance(source, dict) else {}
    return {key: _count(value.get(key)) for key in fields}


def _utc(value: object) -> str | None:
    if not isinstance(value, str) or len(value) > 60:
        return None
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if dt.tzinfo is None:
        return None
    return dt.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def normalize(source: Path) -> dict:
    raw, level_bytes = _load(Path(source))
    summary = _parse(raw, "summary")
    if summary.get("schema") != SOURCE_SCHEMA or summary.get("suite") != SUITE:
        raise ValueError("Cette campagne ne provient pas du Diagnostic du kOA Digital Ecosystem")
    run_id = summary.get("run_id")
    if not isinstance(run_id, str) or not RUN_ID.fullmatch(run_id):
        raise ValueError("Identifiant de campagne invalide")
    verdict = summary.get("verdict")
    if verdict not in VERDICTS:
        raise ValueError("Verdict de campagne non reconnu")
    levels = summary.get("levels")
    if not isinstance(levels, list) or not levels or len(levels) > 100:
        raise ValueError("Liste de niveaux absente ou invalide")
    normalized_levels = []
    seen = set()
    integrity_issues = []
    hashes = {}
    for level in levels:
        if not isinstance(level, dict):
            raise ValueError("Niveau invalide")
        lid = level.get("id")
        if not isinstance(lid, str) or not LEVEL_ID.fullmatch(lid) or lid in seen:
            raise ValueError("ID de niveau invalide ou duplique")
        seen.add(lid)
        lverdict = level.get("verdict")
        if lverdict not in VERDICTS:
            raise ValueError("Verdict de niveau invalide")
        reported = level_bytes.get(lid)
        detail = "missing"
        if reported is not None:
            hashes[lid] = hashlib.sha256(reported).hexdigest()
            parsed = _parse(reported, lid)
            if (parsed.get("schema") != LEVEL_SCHEMA or parsed.get("suite") != SUITE or
                parsed.get("run_id") != run_id or parsed.get("level_id") != lid or parsed.get("verdict") != lverdict):
                integrity_issues.append(lid)
                detail = "mismatch"
            else:
                detail = "consistent"
        normalized_levels.append({"id": lid, "verdict": lverdict, "detail": detail})
    if any(key not in seen for key in level_bytes):
        integrity_issues.append("extra_level")
    if integrity_issues:
        raise ValueError("Des niveaux ne correspondent pas au resume: " + ", ".join(integrity_issues))
    reported_counts = summary.get("counts")
    if isinstance(reported_counts, dict):
        for name in VERDICTS:
            count = reported_counts.get(name)
            if count is not None and count != sum(x["verdict"] == name for x in normalized_levels):
                raise ValueError("Comptes de verdict incoherents")
    coverage = summary.get("coverage")
    if not isinstance(coverage, dict):
        raise ValueError("Couverture de campagne absente")
    inv = coverage.get("inventory")
    if not isinstance(inv, dict):
        raise ValueError("Couverture d'inventaire absente")
    journeys = coverage.get("journeys") or {}
    traces = coverage.get("traces") or {}
    api = coverage.get("api") or {}
    global_e2e = coverage.get("global_end_to_end") or {}
    global_status = global_e2e.get("status") if isinstance(global_e2e, dict) else None
    if not isinstance(global_status, str) or len(global_status) > 80:
        global_status = "NON_DETERMINE"
    # Import only bounded numeric metadata and standardized verdicts. Never copy
    # target_repo_root, artifacts, findings, free text, paths, identifiers or traces.
    out = {
        "format": RECORD_FORMAT,
        "source_kind": "ecosystem_interrepo_observation",
        "source_suite": SUITE,
        "source_schema": SOURCE_SCHEMA,
        "source_version": str(summary.get("suite_version") or "unknown")[:32],
        "run_id": run_id,
        "campaign": str(summary.get("selection") or "unknown")[:80],
        "started_at": _utc(summary.get("started_at")),
        "ended_at": _utc(summary.get("ended_at")),
        "reported_verdict": verdict,
        "levels": normalized_levels,
        "coverage": {
            "inventory": _counts(inv, ("present", "declared", "truncated")),
            "inventory_complete_reported": inv.get("complete") if type(inv.get("complete")) is bool else None,
            "relations": _count(coverage.get("relations")),
            "api": _counts(api, ("static_calls", "routes_matched", "routes_inbound", "declared", "declared_matched", "live_checks_ok")),
            "traces": _counts(traces, ("correlated_pairs", "ik_receipts")),
            "journeys": _counts(journeys, ("declared", "evidence_complete", "not_proven")),
            "global_e2e_reported": global_status,
        },
        "integrity": {
            "summary_sha256": hashlib.sha256(raw).hexdigest(),
            "level_result_sha256": hashes,
            "consistent_level_results": sum(x["detail"] == "consistent" for x in normalized_levels),
            "missing_level_results": sum(x["detail"] == "missing" for x in normalized_levels),
            "independent_signature_verified": False,
        },
        "qualification": {
            "current_repository_security": "NOT_ASSESSED",
            "current_repository_integration": "NOT_ASSESSED",
            "ecosystem_e2e_certification": "NOT_ESTABLISHED",
            "scope": "cross_repository_only",
            "local_revision_binding": "NOT_VERIFIED",
            "auditor_authority": "non_authoritative_observation",
            "inventory_identity_reconciliation": "NOT_PERFORMED",
        },
        "ingested_at": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
    }
    return out


def save(record: dict, out: Path | None = None) -> Path:
    folder = private_store()
    output = Path(out) if out else folder / "records" / (record["run_id"] + ".json")
    # Do not allow writing to any public Pages area.
    if "docs" in {part.casefold() for part in output.resolve().parts}:
        raise ValueError("Refus d'ecrire des preuves dans docs/ (GitHub Pages)")
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = (json.dumps(record, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")
    if output.exists():
        existing = json.loads(output.read_text(encoding="utf-8"))
        if existing.get("integrity", {}).get("summary_sha256") != record["integrity"]["summary_sha256"]:
            raise ValueError("Campagne existante avec empreinte differente")
        return output
    # Exclusive create. A concurrent import cannot silently replace an existing record.
    with output.open("xb") as stream:
        stream.write(payload)
    return output


def import_campaign(path: Path, out: Path | None = None) -> tuple[dict, Path]:
    result = normalize(path)
    return result, save(result, out)


def recent_records(folder: Path | None = None) -> list[dict]:
    directory = folder or private_store() / "records"
    if not directory.is_dir():
        return []
    rows = []
    for path in sorted(directory.glob("*.json"), reverse=True)[:MAX_RECORDS]:
        try:
            if path.is_symlink() or path.stat().st_size > MAX_JSON:
                continue
            value = _parse(path.read_bytes(), path.name)
            if value.get("format") == RECORD_FORMAT and value.get("source_kind") == "ecosystem_interrepo_observation":
                rows.append(value)
        except (ValueError, OSError):
            continue
    return rows


def local_summary() -> dict:
    rows = recent_records()
    if not rows:
        return {"format": "koa_audit.ecosystem_diag_view.v1", "state": "not_imported", "count": 0}
    recent = max(rows, key=lambda r: (r.get("ended_at") or "", r.get("run_id") or ""))
    # A trusted local-only view, still metadata-only. Never send to Pages.
    return {"format": "koa_audit.ecosystem_diag_view.v1", "state": "observed_not_certified", "count": len(rows),
            "latest": {key: recent.get(key) for key in ("run_id", "campaign", "ended_at", "reported_verdict", "coverage", "integrity", "qualification")}}
