"""Local, dated, non-destructive evidence campaigns for kOA.

A campaign is a frozen snapshot of *reported observations* and *manual decisions*,
not a certificate. Nothing in this module writes to the source repositories or
GitHub.  The ZIP contains no source repository files or historical audit logs.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import tempfile
import uuid
import shutil
import stat
import zipfile
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

from . import profiles, qualification
from .windows_process import hidden_console_kwargs

FORMAT = "koa_certification.campaign.v1"
MANIFEST_FORMAT = "koa_certification.manifest.v1"
REPO_PATTERN = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\Z")
SHA_PATTERN = re.compile(r"[0-9a-fA-F]{40}\Z")
ID_PATTERN = re.compile(r"[0-9]{8}T[0-9]{6}Z-[0-9a-f]{12}\Z")
NAME_PATTERN = re.compile(r"[A-Za-z0-9_.-]{1,120}\Z")
PROFILE_NAMES = ("ENGINEERING_PROFILE.md", "ENGINEERING_METRICS.json", "SECURITY_PROFILE.md")
MAX_ATTACHMENT = 8_000_000
MAX_REPORT = 30_000_000
MAX_CAMPAIGN = 100_000_000
MAX_FILES = 500
MAX_ZIP_BYTES = 100_000_000


def root_path() -> Path:
    # Independent from the installed/extracted app, so upgrading the ZIP cannot
    # overwrite a past campaign. Do NOT put this in docs/ or a source checkout.
    home = Path(os.environ.get("LOCALAPPDATA") or (Path.home() / ".local" / "share"))
    return home / "kOA-GitHub-Audit" / "campaigns"


def _hash(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def _dump(record: Any) -> bytes:
    return (json.dumps(record, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def _read_json(path: Path, limit: int = MAX_REPORT) -> dict:
    if path.is_symlink() or not path.is_file() or path.stat().st_size > limit:
        raise ValueError("Document absent, lien symbolique ou trop volumineux")
    result = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(result, dict):
        raise ValueError("Le document JSON doit être un objet")
    return result


def _github_link(repo: str, sha: str) -> dict:
    if not REPO_PATTERN.fullmatch(repo) or not SHA_PATTERN.fullmatch(sha):
        return {}
    base = f"https://github.com/{repo}"
    return {"commit": f"{base}/commit/{sha.lower()}",
            "download_zip": f"{base}/archive/{sha.lower()}.zip"}


def _origin_matches(raw: str, expected: str) -> bool:
    """Accept only unambiguous credential-free GitHub remote identities."""
    name = raw.strip().removesuffix(".git")
    for pre in ("https://github.com/", "git@github.com:", "ssh://git@github.com/"):
        if name.casefold().startswith(pre.casefold()):
            target = name[len(pre):]
            return bool(REPO_PATTERN.fullmatch(target)) and target.casefold() == expected.casefold()
    return False


def _git_cmd(path: Path, *args: str) -> str | None:
    try:
        p = subprocess.run(["git", "-c", "core.fsmonitor=false", "-C", str(path), *args],
                           capture_output=True, text=True, encoding="utf-8", errors="replace",
                           timeout=15, env={**os.environ, "GIT_TERMINAL_PROMPT": "0", "GIT_OPTIONAL_LOCKS": "0"},
                           **hidden_console_kwargs())
        if p.returncode != 0:
            return None
        return p.stdout.strip()
    except (OSError, subprocess.TimeoutExpired):
        return None


def _git_observation(path: Path, repo: str) -> dict:
    """Read *only* Git metadata. No fetch, checkout, hooks, writes or network."""
    if not path.is_dir() or path.is_symlink():
        return {"status": "local_source_unavailable"}
    origin = _git_cmd(path, "remote", "get-url", "origin")
    sha = _git_cmd(path, "rev-parse", "--verify", "HEAD")
    if origin is None or sha is None:
        return {"status": "git_metadata_unavailable"}
    if not _origin_matches(origin, repo):
        return {"status": "origin_not_verified"}
    if not SHA_PATTERN.fullmatch(sha):
        return {"status": "commit_unavailable"}
    porcelain = _git_cmd(path, "status", "--porcelain", "--untracked-files=no")
    if porcelain is None:
        worktree = "unknown"
    elif porcelain:
        worktree = "tracked_changes_present"
    else:
        worktree = "tracked_files_clean_untracked_not_checked"
    return {"status": "verified_git_origin", "head": sha.lower(), "worktree": worktree,
            "links": _github_link(repo, sha), "checked_at": _now(),
            "note": "Les fichiers non suivis, les sous-modules et les fichiers ignores ne sont pas qualifies."}


def _audit_observations(audit: dict) -> dict:
    """Freeze only allowlisted audit data; do not preserve source paths/secrets."""
    fmt = audit.get("format")
    if fmt not in ("koa_audit.local_observation.v1", "koa_audit.observation.v1"):
        raise ValueError("Rapport non pris en charge : fournir audit.json (local ou GitHub)\u00a0")
    result: dict = {"format": fmt, "observed_at": str(audit.get("generated_at", ""))[:60]}
    if fmt == "koa_audit.local_observation.v1":
        repo_data = {}
        for item in audit.get("repositories") or []:
            if not isinstance(item, dict):
                continue
            repo = item.get("repository")
            if not isinstance(repo, str) or not REPO_PATTERN.fullmatch(repo):
                continue
            reported_git = item.get("git") or {}
            head = reported_git.get("head") if isinstance(reported_git, dict) else None
            recorded_remote = reported_git.get("remote_repository") if isinstance(reported_git, dict) else None
            provenance = {"status": "not_confirmed", "head": None, "links": {}}
            if isinstance(head, str) and SHA_PATTERN.fullmatch(head) and str(recorded_remote).casefold() == repo.casefold():
                provenance = {"status": "audit_reported_head_not_worktree_verified", "head": head.lower(),
                              "links": _github_link(repo, head),
                              "note": "Commit releve par le rapport ancien ; fichiers de travail non verifies a cette date."}
            counts = item.get("finding_counts") or {}
            if not isinstance(counts, dict):
                counts = {}
            repo_data[repo.casefold()] = {
                "observed_at": result["observed_at"],
                "status": str(item.get("status", "UNKNOWN"))[:60],
                "files_enumerated": _nonnegative(item.get("files_enumerated")),
                "files_inspected": _nonnegative(item.get("files_inspected")),
                "findings_total": sum(_nonnegative(n) for n in counts.values()),
                "recorded_git": provenance,
            }
        result["repositories"] = repo_data
    else:
        repo_data = {}
        for item in audit.get("repositories") or []:
            if isinstance(item, dict) and isinstance(item.get("repository"), str) and REPO_PATTERN.fullmatch(item["repository"]):
                metadata = item.get("repository_metadata") or {}
                head = metadata.get("head_sha") if isinstance(metadata, dict) else None
                if not isinstance(head, str) or not SHA_PATTERN.fullmatch(head):
                    head = None
                repo_data[item["repository"].casefold()] = {
                    "access": str(item.get("access", "unknown"))[:60],
                    "reported_head": head.lower() if head else None,
                    "links": _github_link(item["repository"], head) if head else {},
                    "note": "Metadonnees GitHub observees ; statut de qualification non deduit.",
                }
        result["repositories"] = repo_data
    return result


def _nonnegative(n: Any) -> int:
    return min(n, 10_000_000_000) if type(n) is int and n >= 0 else 0


def _kristal_capture(folder: Path | None, inventory: list[str]) -> tuple[dict, dict]:
    """Freeze only a semantic projection; never copy live Kristal catalogs."""
    from . import kristal_source
    root = Path(folder) if folder is not None else kristal_source.get_source_root()
    if not root.is_dir():
        return {"status": "unavailable", "notice": "Référentiel Kristal non disponible pour cette capture."}, {}
    try:
        view = kristal_source.build_local_kristal_view(root, inventory)
    except (OSError, ValueError, TypeError, KeyError):
        return {"status": "unavailable", "notice": "Catalogues Kristal non lisibles pour cette capture."}, {}
    fingerprints = {}
    for kind, rel, maximum in kristal_source.CATALOGS:
        path = root / rel
        if path.is_file() and not path.is_symlink() and path.stat().st_size <= maximum:
            fingerprints[kind] = _hash(path.read_bytes())
    allowed = ("catalog_repositories", "catalog_components", "catalog_relations", "catalog_contracts",
               "catalog_capabilities", "matched", "explicit_repositories", "candidate_repositories",
               "unlinked_repositories")
    snapshot = {"status": "frozen_local_projection", "captured_at": _now(),
                "counts": {key: view.get(key) for key in allowed},
                "source_catalog_sha256": fingerprints,
                "notice": "Associations sémantiques, pas des tests d'intégration ou certifications."}
    per_repo = {row["repo"]: {key: row.get(key) for key in
                 ("association", "name", "description", "role", "membership", "locator_status",
                  "components", "candidates", "relations", "candidate_relations")}
                for row in view["repositories"] if row.get("found") and row.get("repo") in inventory}
    return snapshot, per_repo


def _source_lookup(report: dict) -> dict[str, Path]:
    """Existing report can identify local folders; these paths are never stored."""
    paths = {}
    if report.get("format") == "koa_audit.local_observation.v1":
        for item in report.get("repositories") or []:
            if isinstance(item, dict) and isinstance(item.get("repository"), str) and isinstance(item.get("location"), str):
                paths[item["repository"].casefold()] = Path(item["location"])
    return paths


def _profile_payload(project: Path, repo: str, archived: dict[str, bytes]) -> dict:
    info = {"engineering": False, "security": False, "metrics": False,
            "source_model": "unknown", "source_snapshot_sha256": None}
    directory = profiles.profile_directory(project, repo)
    slug = repo.split("/", 1)[-1]
    for filename in PROFILE_NAMES:
        path = directory / filename
        if not path.is_file() or path.is_symlink() or path.stat().st_size > 2_000_000:
            continue
        data = path.read_bytes()
        # In the user's PRIVATE campaign only; no raw source files are included.
        archived[f"profiles/{slug}/{filename}"] = data
        if filename == "ENGINEERING_PROFILE.md":
            info["engineering"] = True
        elif filename == "SECURITY_PROFILE.md":
            info["security"] = True
        else:
            info["metrics"] = True
            try:
                metrics = json.loads(data)
                info["source_model"] = str((metrics.get("method") or {}).get("source_model", "unknown"))[:100]
                checksum = (metrics.get("snapshot") or {}).get("sha256")
                if isinstance(checksum, str) and re.fullmatch(r"[0-9a-f]{64}", checksum):
                    info["source_snapshot_sha256"] = checksum
            except (ValueError, TypeError, AttributeError):
                pass
    return info


def _manual_claims(claims: dict, repo: str) -> dict:
    original = claims.get(repo) or {}
    return {stage: {"status": str((original.get(stage) or {}).get("status", "Non évalué"))[:40],
                    "scope": str((original.get(stage) or {}).get("scope", ""))[:300],
                    "evidence": str((original.get(stage) or {}).get("evidence", ""))[:1500],
                    "reviewed_at": str((original.get(stage) or {}).get("reviewed_at", ""))[:50]}
            for stage in qualification.STAGE_IDS}


def _manual_practices(assessments: dict, repo: str, valid_ids: set[str]) -> dict:
    original = assessments.get(repo) or {}
    return {key: {"status": str(value.get("status", "Non évalué"))[:40],
                  "note": str(value.get("note", ""))[:2000],
                  "reviewed_at": str(value.get("reviewed_at", ""))[:50]}
            for key, value in original.items() if key in valid_ids and isinstance(value, dict)}


def version_alignment(record: dict) -> dict:
    """Compare *only verifiable Git identities*; never transfer SHA to profiles/proofs.

    An old audit SHA and current local HEAD are independent observations.  Even
    when they match, unrelated snapshots and supplied reports stay unbound.
    """
    git = record.get("observed_git") or {}
    audit = record.get("historical_audit") or {}
    old = audit.get("recorded_git") or {}
    historical = old.get("head") or audit.get("reported_head")
    current = git.get("head") if git.get("status") == "verified_git_origin" else None
    clean = git.get("worktree") == "tracked_files_clean_untracked_not_checked"
    if current and historical:
        status = "git_commit_same" if current == historical else "git_commit_different"
    elif current or historical:
        status = "single_git_reference"
    else:
        status = "unknown"
    return {"git_comparison": status, "historical_commit": historical,
            "current_local_commit": current, "tracked_worktree_clean": bool(clean),
            "profile_to_git": "unknown_independent_snapshot",
            "attached_proofs_to_git": "unknown_without_verified_provenance",
            "note": "Même commit Git ne prouve pas qu'un profil ou rapport importé mesure ce commit. "
                    "Fichiers ignorés, non suivis et sous-modules non contrôlés."}


def proof_version_relation(proof: dict, record: dict) -> str:
    """A Git SHA match is a metadata comparison, NOT proof of execution at SHA."""
    recorded = (record.get("historical_audit") or {}).get("recorded_git") or {}
    audit = record.get("historical_audit") or {}
    observed = record.get("observed_git") or {}
    pinned = recorded.get("head") or audit.get("reported_head") or observed.get("head")
    source = proof.get("source_commit")
    if not isinstance(source, str) or not SHA_PATTERN.fullmatch(source):
        return "unverified_report_not_bound_to_commit"
    if not pinned or not SHA_PATTERN.fullmatch(pinned):
        return "collector_sha_without_campaign_git_reference"
    if source.lower() != pinned.lower():
        return "collector_git_head_differs_from_reference"
    return "collector_git_head_matches_reference_not_artifact_attestation"


def _archive_limits(documents: dict[str, bytes]) -> None:
    """Match the reader's constraints *before* any persistent filesystem write."""
    if len(documents) > MAX_FILES:
        raise ValueError("Trop de documents dans la campagne (limite 500)")
    size = sum(len(value) for value in documents.values())
    if size > MAX_CAMPAIGN:
        raise ValueError(f"Campagne trop volumineuse : {size:,} octets décompressés (limite {MAX_CAMPAIGN:,})")
    if any(len(value) > MAX_ATTACHMENT for value in documents.values()):
        raise ValueError("Une preuve dépasse la limite de 8 Mo")
    if any(name.startswith("/") or ".." in name.split("/") or "\\" in name for name in documents):
        raise ValueError("Nom de preuve invalide")


def _stream_sha256(path: Path) -> str:
    sha = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            sha.update(block)
    return sha.hexdigest()


def describe_proof(path: Path, data: bytes) -> dict:
    """Read familiar report metadata, without running tests or asserting compliance."""
    ext = path.suffix.lower()
    report: dict = {"recognition": "document_only", "execution": "not_executed_by_campaign"}
    try:
        if ext == ".xml" and b"<!DOCTYPE" not in data.upper() and b"<!ENTITY" not in data.upper():
            root = ET.fromstring(data)
            kind = root.tag.split("}")[-1]
            if kind in ("testsuite", "testsuites"):
                suites = [root] if kind == "testsuite" else list(root.findall("testsuite"))
                if not suites:
                    suites = [root]
                totals = {key: sum(_nonnegative(int(s.attrib.get(key, "0"))) for s in suites)
                          for key in ("tests", "failures", "errors", "skipped")}
                report = {"recognition": "junit_xml_summary", "execution": "report_imported_not_rerun",
                          "totals": totals, "note": "Résultat déclare par le XML fourni; version Git et contexte d'exécution non verifies."}
            elif kind == "coverage":
                rate = root.attrib.get("line-rate")
                if rate is not None:
                    value = float(rate)
                    if 0 <= value <= 1:
                        report = {"recognition": "coverage_xml_summary", "execution": "report_imported_not_rerun",
                                  "line_coverage_pct": round(100 * value, 2),
                                  "note": "Rapport existant; sa fraîcheur et sa provenance ne sont pas automatiquement vérifiées."}
        elif ext in (".sarif", ".json"):
            obj = json.loads(data)
            if isinstance(obj, dict) and (obj.get("version") == "2.1.0" or obj.get("$schema", "").endswith("sarif-schema-2.1.0.json")):
                runs = obj.get("runs") or []
                report = {"recognition": "sarif_summary", "execution": "report_imported_not_rerun",
                          "runs": len(runs),
                          "results_observed": sum(len(x.get("results") or []) for x in runs if isinstance(x, dict)),
                          "note": "Résultats statiques observés; ne sont pas tous des vulnérabilités réelles."}
            elif isinstance(obj, dict) and obj.get("format") == "koa_evidence.static_metadata.v1":
                git = obj.get("git") or {}
                source_sha = git.get("head") if git.get("status") == "verified_git_origin" else None
                report = {"recognition":"koa_static_metadata_summary", "execution":"observed_readonly_git_and_optional_tools",
                          "tracked_files":_nonnegative(obj.get("tracked_files")),
                          "github_workflows":_nonnegative(obj.get("github_workflow_files")),
                          "source_commit_reported":source_sha if isinstance(source_sha,str) and SHA_PATTERN.fullmatch(source_sha) else None,
                          "tracked_worktree":str(git.get("worktree","unknown"))[:80],
                          "collector_reported_at":str(obj.get("captured_at", ""))[:50],
                          "note":"Révision Git observée au moment de la mesure; résultats de tests et validation de production non exécutés."}
            elif isinstance(obj, dict) and isinstance(obj.get("totals"), dict):
                value = obj["totals"].get("percent_covered")
                if isinstance(value, (int, float)) and 0 <= value <= 100:
                    report = {"recognition": "coverage_json_summary", "execution": "report_imported_not_rerun",
                              "line_coverage_pct": round(float(value), 2),
                              "note": "Couverture déclarée par le rapport existant, fraîcheur non garantie."}
    except (ET.ParseError, ValueError, OverflowError, TypeError, KeyError, AttributeError):
        pass
    return report


def create_campaign(project: Path, title: str, audit_file: Path | None = None,
                    *, store: Path | None = None, local_paths: dict[str, Path] | None = None,
                    extra_proofs: dict[str, list[Path]] | None = None,
                    git_probe: bool = True, kristal_folder: Path | None = None,
                    progress: Callable[[int, int, str], None] | None = None,
                    expected_proof_sha256: dict[Path, str] | None = None) -> Path:
    """Freeze a campaign ZIP. Never execute project code or change source repos.

    extra_proofs are explicit opt-in evidence files, not recursively discovered.
    """
    project = Path(project)
    title = title.strip()
    if not 3 <= len(title) <= 90 or any(ord(ch) < 32 for ch in title):
        raise ValueError("Choisir un titre entre 3 et 90 caracteres")
    store = Path(store) if store is not None else root_path()
    audit_raw = _read_json(Path(audit_file)) if audit_file else None
    if audit_raw is not None:
        audit_ref = _audit_observations(audit_raw)
        src_paths = _source_lookup(audit_raw)
        audit_provenance = {"file_sha256": _hash(Path(audit_file).read_bytes()),
                            "reported_at": audit_ref["observed_at"], "format": audit_ref["format"]}
    else:
        audit_ref, src_paths, audit_provenance = None, {}, None
    src_paths.update({k.casefold(): Path(v) for k, v in (local_paths or {}).items()})
    claims = qualification.load_state().get("claims", {})
    assessments = profiles.load_state().get("assessments", {})
    valid_ids = {item["id"] for item in profiles.catalog(project)}
    inventory = profiles.inventory(project)
    total_steps = len(inventory) + 4
    if progress:
        progress(0, total_steps, "Lecture des données et du catalogue Kristal")
    kristal_snapshot, kristal_repos = _kristal_capture(kristal_folder, inventory)
    repos = {}
    documents: dict[str, bytes] = {}
    for processed, repo in enumerate(inventory, 1):
        slug = repo.split("/", 1)[1]
        audit_entry = ((audit_ref or {}).get("repositories") or {}).get(repo.casefold())
        local = (src_paths.get(repo.casefold()) if git_probe else None)
        git = _git_observation(local, repo) if local else {"status": "not_checked"}
        record = {
            "repository": repo,
            "observed_git": git,
            "historical_audit": audit_entry,
            "profiles": _profile_payload(project, repo, documents),
            "qualification": _manual_claims(claims, repo),
            "practices": _manual_practices(assessments, repo, valid_ids),
            "kristal": kristal_repos.get(repo, {"association": "unavailable"}),
        }
        record["version_alignment"] = version_alignment(record)
        repos[slug] = record
        if progress:
            progress(processed, total_steps, f"Fiches conservées : {processed}/{len(inventory)}")
    if progress:
        progress(len(inventory), total_steps, "Intégration des preuves complémentaires")
    if extra_proofs:
        for repo_name, paths in extra_proofs.items():
            if repo_name not in inventory:
                raise ValueError("Preuve associee a un depot hors inventaire")
            if len(paths) > 15:
                raise ValueError("Trop de fichiers de preuve pour un depot")
            slug = repo_name.split("/", 1)[1]
            filelist = []
            for index, path in enumerate(paths):
                path = Path(path)
                if path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_ATTACHMENT:
                    raise ValueError("Preuve absente, lien symbolique ou trop volumineuse")
                if path.suffix.lower() not in (".json", ".md", ".txt", ".xml", ".sarif", ".pdf", ".html"):
                    raise ValueError("Type de preuve non pris en charge")
                member = f"proofs/{slug}/{index:02d}{path.suffix.lower()}"
                existing_total = sum(len(content) for content in documents.values())
                if existing_total + path.stat().st_size > MAX_CAMPAIGN or len(documents) + 2 > MAX_FILES:
                    raise ValueError("Limite totale de la campagne atteinte avant lecture de la preuve")
                raw = path.read_bytes()
                expected = (expected_proof_sha256 or {}).get(path)
                if expected is not None and _hash(raw) != expected:
                    raise ValueError("Rapport modifié depuis la découverte : refaire l'aperçu avant d'archiver")
                documents[member] = raw
                proof_summary = describe_proof(path, raw)
                proof_commit = None
                provenance = "file_imported_not_bound_to_git"
                if proof_summary.get("recognition") == "koa_static_metadata_summary":
                    try:
                        observed = json.loads(documents[member])
                        if observed.get("repository") == repo_name:
                            proof_commit=proof_summary.get("source_commit_reported")
                            provenance="koa_collector_report_declares_git_head_not_independent_attestation"
                        else:
                            provenance="koa_collector_repository_mismatch"
                    except (TypeError,ValueError):
                        pass
                filelist.append({"name": path.name[:140], "member": member, "sha256": _hash(documents[member]),
                                 "imported_at": _now(),
                                 "kind": path.suffix.lower().lstrip("."),
                                 "source_commit": proof_commit, "provenance": provenance,
                                 "summary": proof_summary})
            repos[slug]["attached_proofs"] = filelist
    for rec in repos.values():
        proofs = rec.get("attached_proofs") or []
        for proof in proofs:
            proof["version_relation"] = proof_version_relation(proof, rec)
        recorded = (rec.get("historical_audit") or {}).get("recorded_git") or {}
        pinned = recorded.get("head") or (rec.get("historical_audit") or {}).get("reported_head") or (rec.get("observed_git") or {}).get("head")
        source_shas = [p.get("source_commit") for p in proofs]
        if source_shas and all(source_shas) and pinned:
            rec["version_alignment"]["attached_proofs_to_git"] = ("collector_observed_same_head_not_source_attestation"
                if all(x==pinned for x in source_shas) else "collector_observed_different_head")
    # Preserve the owner-supplied historical review alongside any manual claim
    # that refers to it. This is a private, bounded attachment, not a validation.
    source_review = None
    from . import evidence_review
    if any(evidence_review.SOURCE_MARKER in str(v.get("evidence", ""))
           for claim in claims.values() if isinstance(claim, dict)
           for v in claim.values() if isinstance(v, dict)):
        review_file = evidence_review.archive_path(project)
        if not review_file.is_file() or review_file.is_symlink():
            raise ValueError("Revue historique référencée mais archive privée absente : campagne non créée")
        evidence_review.load_review(project)  # Check source index before freezing.
        raw = review_file.read_bytes()
        documents["private/historical_review_2026-10-30.zip"] = raw
        source_review = {"member": "private/historical_review_2026-10-30.zip",
                         "sha256": _hash(raw), "kind": "historical_owner_review_not_certification",
                         "scope": "49 repositories / 245 evidence cases, historical sources"}
    # Archive the exact historical spec review and its narrowly-scoped test
    # execution logs, independently of future application and Git revisions.
    # This is dated prior-source evidence, never attributed to the campaign HEAD.
    functional_review = None
    from . import specsheets, spec_tests
    if specsheets.load(project).get('state') == 'verified_index':
        index = (project / 'private_evidence' / specsheets.BUNDLE).read_bytes()
        member = 'private/snapshot_specs/functional-review-2026-10-30.json'
        documents[member] = index
        functional_review = {'member': member, 'sha256': _hash(index),
                             'source_date': '2026-10-30', 'linked_to_current_commit': False,
                             'targeted_unit_tests': 0, 'test_logs': []}
        runs = spec_tests.load(project)
        if runs:
            manifest_bytes = (project / 'private_evidence' / spec_tests.MANIFEST).read_bytes()
            test_member = 'private/snapshot_specs/targeted-test-runs-2026-10-30.json'
            documents[test_member] = manifest_bytes
            functional_review['test_manifest'] = {'member': test_member, 'sha256': _hash(manifest_bytes)}
            for r in runs.values():
                name = r['junit_link'].split('/')[-1]
                # Only two reviewed reports are supported; do not glob the filesystem.
                filename = 'KonnaxionDiag.junit.xml' if name == 'KonnaxionDiag' else (
                    'Capsule-Manager.junit.xml' if name == 'Konnaxion-Capsule-Manager' else None)
                if filename:
                    raw = (project / 'private_evidence' / 'test_reports' / filename).read_bytes()
                    dest = 'private/snapshot_specs/' + filename
                    documents[dest] = raw
                    functional_review['test_logs'].append({'member': dest, 'sha256': _hash(raw)})
                    functional_review['targeted_unit_tests'] += r['passed']
    if progress:
        progress(len(inventory) + 1, total_steps, "Calcul du manifeste et des empreintes")
    stamp = datetime.now(timezone.utc)
    cid = stamp.strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:12]
    captured = {"format": FORMAT, "campaign_id": cid, "title": title,
                "frozen_at": stamp.isoformat(timespec="microseconds").replace("+00:00", "Z"),
                "repository_count": len(inventory), "source_audit": audit_provenance,
                "kristal": kristal_snapshot,
                "historical_review": source_review,
                "functional_review": functional_review,
                "repository_profiles_snapshot": repos,
                "notice": "Capture historique privee; aucune qualification automatique, aucun scan ni test execute.",
                "availability_note": "Lien GitHub lie au SHA, non verifie en ligne; peut devenir indisponible si le commit disparait.",
                "worktree_note": "Des fichiers locaux modifies ou non suivis peuvent differer du commit affiche. Les profils issus de ZIP n'ont pas de SHA Git fiable."
                }
    documents["campaign.json"] = _dump(captured)
    manifest = {"format": MANIFEST_FORMAT, "campaign_id": cid,
                "sha256": {name: _hash(value) for name, value in sorted(documents.items())}}
    documents["manifest.json"] = _dump(manifest)
    # Check the same resource limits imposed during archive reading.  In addition,
    # enforce a hard compressed size so creation can never produce an unreadable ZIP.
    _archive_limits(documents)
    store.mkdir(parents=True, exist_ok=True)
    target = store / (cid + ".zip")
    checksum_path = store / (cid + ".zip.sha256")
    fd, tmp = tempfile.mkstemp(prefix="koa-campaign-", suffix=".tmp", dir=store)
    os.close(fd)
    staged_checksum = None
    published = False
    try:
        with zipfile.ZipFile(tmp, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
            for member, data in sorted(documents.items()):
                archive.writestr(member, data)
        if progress:
            progress(len(inventory) + 2, total_steps, "Archive écrite · vérification en cours")
        if Path(tmp).stat().st_size > MAX_ZIP_BYTES:
            raise ValueError("Archive ZIP trop volumineuse")
        digest = _stream_sha256(Path(tmp))
        # Fully validate BEFORE exposing as a completed campaign.
        with zipfile.ZipFile(tmp) as z:
            _validate_zip_contents(z, cid)
        if target.exists() or checksum_path.exists():
            raise FileExistsError("Une campagne porte deja cet identifiant")
        fd, staged_checksum = tempfile.mkstemp(prefix="koa-sha-", suffix=".tmp", dir=store)
        with os.fdopen(fd, "w", encoding="ascii") as f:
            f.write(digest + "  " + target.name + "\n")
            f.flush()
            os.fsync(f.fileno())
        if progress:
            progress(len(inventory) + 3, total_steps, "Intégrité validée · enregistrement final")
        # The ZIP appears atomically and exclusively; no replacing past captures.
        # The sidecar is staged first and then moved into place.  On failure,
        # clean up the freshly created ZIP, never a prior campaign.
        try:
            os.link(tmp, target)
        except OSError:
            if os.name == "nt" and not target.exists():
                # Windows rename refuses replacement of an existing file.
                os.rename(tmp, target)
            else:
                raise
        published = True
        os.replace(staged_checksum, checksum_path)
        staged_checksum = None
        if _stream_sha256(target) != digest:
            raise ValueError("Lecture de vérification de la nouvelle archive incorrecte")
    except Exception:
        if published:
            target.unlink(missing_ok=True)
            checksum_path.unlink(missing_ok=True)
        raise
    finally:
        Path(tmp).unlink(missing_ok=True)
        if staged_checksum:
            Path(staged_checksum).unlink(missing_ok=True)
    if progress:
        progress(total_steps, total_steps, "Campagne créée et vérifiée")
    return target


def _validate_zip_contents(archive: zipfile.ZipFile, cid: str) -> None:
    infos = archive.infolist()
    members = [item.filename for item in infos]
    if (len(members) > MAX_FILES or len(members) != len(set(members))
            or sum(item.file_size for item in infos) > MAX_CAMPAIGN
            or any(item.file_size > MAX_ATTACHMENT for item in infos)
            or any(item.filename.startswith("/") or ".." in item.filename.split("/")
                   or "\\" in item.filename for item in infos)):
        raise ValueError("Archive non conforme")
    if "manifest.json" not in members or "campaign.json" not in members:
        raise ValueError("Documents de campagne manquants")
    manifest = json.loads(archive.read("manifest.json"))
    if manifest.get("format") != MANIFEST_FORMAT or manifest.get("campaign_id") != cid:
        raise ValueError("Manifeste de campagne invalide")
    checksums = manifest.get("sha256", {})
    if not isinstance(checksums, dict) or set(checksums) != set(members) - {"manifest.json"}:
        raise ValueError("Liste de preuves non conforme")
    for member in members:
        if member == "manifest.json":
            continue
        if (not member.startswith(("profiles/", "proofs/"))
                and member not in ("campaign.json", "private/historical_review_2026-10-30.zip")
                and not member.startswith("private/snapshot_specs/")):
            raise ValueError("Membre interdit")
        content = archive.read(member)
        if len(content) > MAX_ATTACHMENT or _hash(content) != checksums[member]:
            raise ValueError("Preuve modifiee ou trop volumineuse")


def _validated_archive(cid: str, store: Path | None = None) -> zipfile.ZipFile:
    if not ID_PATTERN.fullmatch(cid):
        raise ValueError("Identifiant de campagne invalide")
    folder = Path(store) if store is not None else root_path()
    path = folder / (cid + ".zip")
    if path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_ZIP_BYTES:
        raise ValueError("Campagne absente ou trop volumineuse")
    expected_path = folder / (cid + ".zip.sha256")
    if expected_path.is_symlink() or not expected_path.is_file():
        raise ValueError("Empreinte externe absente")
    digest = expected_path.read_text(encoding="ascii").split(" ", 1)[0]
    if not re.fullmatch(r"[0-9a-f]{64}", digest) or _stream_sha256(path) != digest:
        raise ValueError("Empreinte SHA-256 du ZIP incorrecte")
    archive = zipfile.ZipFile(path)
    try:
        _validate_zip_contents(archive, cid)
        return archive
    except Exception:
        archive.close()
        raise


def read_archived_review(cid: str, store: Path | None = None) -> bytes:
    """Download the exact historical review ZIP frozen with an explicit claim."""
    with _validated_archive(cid, store) as z:
        data = json.loads(z.read("campaign.json"))
        ref = data.get("historical_review") or {}
        member = "private/historical_review_2026-10-30.zip"
        if ref.get("member") != member or member not in z.namelist():
            raise ValueError("Cette campagne ne contient aucune revue historique")
        raw = z.read(member)
        if _hash(raw) != ref.get("sha256"):
            raise ValueError("Empreinte de la revue historique invalide")
        return raw


def read_proof(cid: str, slug: str, index: int, store: Path | None = None) -> tuple[dict, bytes]:
    """Only ever retrieve a proof specifically declared by the frozen campaign."""
    if not NAME_PATTERN.fullmatch(slug) or not 0 <= index < 15:
        raise ValueError("Preuve ou dépôt invalide")
    with _validated_archive(cid, store) as z:
        data = json.loads(z.read("campaign.json"))
        repo = data.get("repository_profiles_snapshot", {}).get(slug)
        if not isinstance(repo, dict):
            raise ValueError("Dépôt absent")
        proofs = repo.get("attached_proofs") or []
        if index >= len(proofs):
            raise ValueError("Preuve absente")
        info = proofs[index]
        member = f"proofs/{slug}/{index:02d}.{info.get('kind', '')}"
        if info.get("member") != member or member not in z.namelist():
            raise ValueError("Référence de preuve incorrecte")
        raw = z.read(member)
        if _hash(raw) != info.get("sha256"):
            raise ValueError("Preuve altérée")
        return info, raw


def campaign_coverage(snapshot: dict) -> dict:
    records = snapshot.get("repository_profiles_snapshot") or {}
    stages = {}
    for key, title in qualification.STAGES:
        counts = {"Étayé par preuve":0,"À documenter":0,"Non applicable":0,"Non évalué":0}
        for record in records.values():
            state = (record.get("qualification") or {}).get(key, {}).get("status", "Non évalué")
            counts[state if state in counts else "Non évalué"] += 1
        stages[key] = {"title":title, "counts":counts}
    profiles_count = sum(bool((row.get("profiles") or {}).get("engineering")) for row in records.values())
    proof_count = sum(len(row.get("attached_proofs") or []) for row in records.values())
    practice_rows = sum(len([v for v in (row.get("practices") or {}).values()
                             if v.get("status", "Non évalué") != "Non évalué"]) for row in records.values())
    kinds = {}
    versions = {"collector_git_head_matches_reference_not_artifact_attestation": 0,
                "collector_git_head_differs_from_reference": 0,
                "collector_sha_without_campaign_git_reference": 0,
                "unverified_report_not_bound_to_commit": 0}
    for record in records.values():
        for proof in record.get("attached_proofs") or []:
            kind = (proof.get("summary") or {}).get("recognition", "document_only")
            kinds[kind] = kinds.get(kind, 0) + 1
            version = proof.get("version_relation") or proof_version_relation(proof, record)
            versions[version] = versions.get(version, 0) + 1
    return {"repository_count":len(records),"engineering_profiles":profiles_count,
            "attached_proofs":proof_count,"practice_reviews":practice_rows,"stages":stages,
            "proof_categories":kinds,"proof_version_relations":versions}


def compare_campaigns(older_id: str, newer_id: str, store: Path | None = None) -> dict:
    """Mechanical comparisons, no automatic promotion or retroactive judgement."""
    a = read_campaign(older_id, store)
    b = read_campaign(newer_id, store)
    previous = a["repository_profiles_snapshot"]
    current = b["repository_profiles_snapshot"]
    items = []
    totals = {"profiles_added": 0, "profiles_removed": 0, "stage_new_evidence": 0,
              "stage_evidence_revised": 0, "stage_evidence_withdrawn": 0,
              "practices_reviewed_added": 0, "commit_changed": 0,
              "proof_files_added": 0, "proof_files_removed": 0,
              "report_kinds_added": 0}
    for slug in sorted(set(previous) | set(current)):
        old, new = previous.get(slug, {}), current.get(slug, {})
        op, np = old.get("profiles") or {}, new.get("profiles") or {}
        old_engineering, new_engineering = bool(op.get("engineering")), bool(np.get("engineering"))
        if new_engineering and not old_engineering: totals["profiles_added"] += 1
        if old_engineering and not new_engineering: totals["profiles_removed"] += 1
        oc, nc = old.get("qualification") or {}, new.get("qualification") or {}
        incoming, revised, withdrawn = 0, 0, 0
        for stage in qualification.STAGE_IDS:
            before, after = oc.get(stage) or {}, nc.get(stage) or {}
            bef, aft = before.get("status") == "Étayé par preuve", after.get("status") == "Étayé par preuve"
            if aft and not bef: incoming += 1
            if bef and not aft: withdrawn += 1
            if aft and bef and (before.get("scope"), before.get("evidence")) != (after.get("scope"),after.get("evidence")):
                revised += 1
        totals["stage_new_evidence"] += incoming
        totals["stage_evidence_revised"] += revised
        totals["stage_evidence_withdrawn"] += withdrawn
        reviewed=lambda record: {k for k,v in (record.get("practices") or {}).items() if v.get("status") != "Non évalué"}
        added_reviews=len(reviewed(new)-reviewed(old))
        totals["practices_reviewed_added"] += added_reviews
        def sha(rec):
            obs=rec.get("observed_git") or {}
            oldaudit=rec.get("historical_audit") or {}
            return ((oldaudit.get("recorded_git") or {}).get("head") or oldaudit.get("reported_head") or obs.get("head"))
        commit_changed = bool(sha(old) and sha(new) and sha(old)!=sha(new))
        totals["commit_changed"] += commit_changed
        proof_set=lambda rec: {(p.get("sha256"), (p.get("summary") or {}).get("recognition"))
                              for p in (rec.get("attached_proofs") or []) if p.get("sha256")}
        old_files, new_files = proof_set(old), proof_set(new)
        files_added, files_removed = len(new_files-old_files),len(old_files-new_files)
        totals["proof_files_added"] += files_added
        totals["proof_files_removed"] += files_removed
        old_kinds = {(p.get("summary") or {}).get("recognition")
                     for p in (old.get("attached_proofs") or [])}
        new_kinds = {(p.get("summary") or {}).get("recognition")
                     for p in (new.get("attached_proofs") or [])}
        totals["report_kinds_added"] += len(new_kinds-old_kinds)
        items.append({"slug":slug,"proof_files_added":files_added,"proof_files_removed":files_removed,
                      "new_evidence":incoming,"revised":revised,"withdrawn":withdrawn,
                      "new_practice_reviews":added_reviews,"profile_added":new_engineering and not old_engineering,
                      "profile_removed":old_engineering and not new_engineering,"commit_changed":commit_changed})
    return {"older": {"id":older_id,"title":a["title"],"date":a["frozen_at"], "coverage":campaign_coverage(a)},
            "newer": {"id":newer_id,"title":b["title"],"date":b["frozen_at"], "coverage":campaign_coverage(b)},
            "totals":totals,"repositories":items,
            "notice":"Différences documentaires entre deux captures; ni verdict de qualité, ni promotion automatique."}


def read_campaign(cid: str, store: Path | None = None) -> dict:
    with _validated_archive(cid, store) as archive:
        data = json.loads(archive.read("campaign.json"))
    if data.get("format") != FORMAT or data.get("campaign_id") != cid:
        raise ValueError("Format de campagne incorrect")
    return data


def read_profile(cid: str, slug: str, store: Path | None = None) -> str | None:
    if not NAME_PATTERN.fullmatch(slug):
        raise ValueError("Nom de depot invalide")
    with _validated_archive(cid, store) as archive:
        member = f"profiles/{slug}/ENGINEERING_PROFILE.md"
        if member not in archive.namelist():
            return None
        return archive.read(member).decode("utf-8-sig", errors="replace")


_LIST_VERIFIED: dict[str, tuple[int, int, int, int]] = {}


def list_campaigns(store: Path | None = None) -> list[dict]:
    """Verify once per file version, then cache the integrity status in memory.

    Changes in ZIP or external checksum force re-verification.  Opening a
    campaign always rechecks the full SHA and all internal documents.
    """
    folder = Path(store) if store is not None else root_path()
    if not folder.is_dir():
        return []
    found=[]
    for p in sorted(folder.glob("*.zip"), reverse=True)[:200]:
        cid=p.stem
        if not ID_PATTERN.fullmatch(cid):
            continue
        try:
            checksum=folder/(cid+'.zip.sha256')
            zp, sp=p.stat(), checksum.stat()
            if p.is_symlink() or checksum.is_symlink() or zp.st_size > MAX_ZIP_BYTES:
                raise ValueError("Archive non conforme")
            token=(zp.st_size,zp.st_mtime_ns,sp.st_size,sp.st_mtime_ns)
            if _LIST_VERIFIED.get(str(p)) != token:
                data=read_campaign(cid,folder)
                _LIST_VERIFIED[str(p)]=token
            else:
                # Minimal metadata read only; full validation already cached.
                with zipfile.ZipFile(p) as z:
                    data=json.loads(z.read('campaign.json'))
            found.append({"id":cid,"title":data["title"],"frozen_at":data["frozen_at"],
                          "repositories":len(data["repository_profiles_snapshot"]),"integrity":"ok",
                          "created_ns":zp.st_mtime_ns})
        except (OSError,ValueError,KeyError,TypeError,zipfile.BadZipFile):
            _LIST_VERIFIED.pop(str(p),None)
            found.append({"id":cid,"title":"Campagne illisible","frozen_at":"","repositories":0,
                          "integrity":"failed"})
    found.sort(key=lambda row:(row.get("frozen_at", ""),row.get("created_ns",0)),reverse=True)
    return found


def latest_summary(store: Path | None = None) -> dict:
    """Private status-only summary for the *loopback* atlas (not GitHub Pages)."""
    rows = [r for r in list_campaigns(store) if r.get("integrity") == "ok"]
    output = {"format": "koa_certification.latest_summary.v1", "available": bool(rows)}
    if not rows:
        return output
    most_recent = rows[0]
    snapshot = read_campaign(most_recent["id"], store)
    coverage = campaign_coverage(snapshot)
    output["latest"] = {
        "id": most_recent["id"], "frozen_at": most_recent["frozen_at"],
        "repository_count": coverage["repository_count"],
        "engineering_profiles": coverage["engineering_profiles"],
        "proof_files": coverage["attached_proofs"],
        "practice_reviews": coverage["practice_reviews"],
        "stages_evidenced": {key: info["counts"]["Étayé par preuve"]
                            for key, info in coverage["stages"].items()},
        "proof_categories": coverage["proof_categories"],
        # Names only from the fixed inventory. No notes, proof contents, paths,
        # review scope or manual decisions are exposed by this endpoint.
        "repositories": {record["repository"]: {
            "engineering_profile": bool((record.get("profiles") or {}).get("engineering")),
            "proof_files": len(record.get("attached_proofs") or []),
            "manually_evidenced_stages": sum(1 for claim in (record.get("qualification") or {}).values()
                                              if isinstance(claim,dict) and claim.get("status")=="Étayé par preuve")
            } for record in snapshot["repository_profiles_snapshot"].values()},
    }
    if len(rows) >= 2:
        output["previous_id"] = rows[1]["id"]
    return output


def render_local_page(route: str, store: Path | None = None) -> str:
    """Build a private, click-through history view for the loopback preview only."""
    from html import escape
    from urllib.parse import quote

    css = """<style>
      :root{color-scheme:dark}*{box-sizing:border-box}body{margin:0;background:#0b1c1b;
      color:#e9f6f3;font:15px/1.5 system-ui,'Segoe UI',sans-serif}
      header{padding:22px 5vw;border-bottom:1px solid #284944;display:flex;gap:28px;align-items:center}
      main{max-width:1280px;margin:auto;padding:32px 5vw}
      h1{font-size:34px;margin-bottom:5px}h2{margin-top:30px}p,small{color:#acccc6}
      a{color:#72ccc3}a:hover{color:#b9faf0}
      table{width:100%;border-collapse:collapse;background:#132927;border:1px solid #31524d;border-radius:10px}
      th,td{text-align:left;vertical-align:top;padding:12px 14px;border-bottom:1px solid #2a4541}
      th{color:#86d7ca}strong{color:#f1fcf9}
      .chip{font-size:12px;white-space:nowrap;background:#1e6864;padding:5px 9px;border-radius:16px}
      .panel{border:1px solid #31524d;background:#132725;padding:20px;border-radius:14px;margin:18px 0}
      .grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
      .metric{margin:9px 0 20px}.metric label{display:flex;justify-content:space-between;gap:12px;margin-bottom:5px}
      .track{height:11px;background:#304743;overflow:hidden;border-radius:20px}
      .fill{height:100%;background:#68c4b7;border-radius:20px}
      .fill.prior{background:#9baeb4}.track+.track{margin-top:5px}
      pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#eef7f5;color:#162d29;padding:25px;border-radius:12px}
      @media(max-width:780px){.grid{grid-template-columns:1fr}table{display:block;overflow-x:auto}}
    </style>"""
    def page(title: str, body: str) -> str:
        return ("<!doctype html><html lang='fr'><head><meta charset='utf-8'><meta name='viewport' "
                "content='width=device-width,initial-scale=1'><title>"+escape(title)+" · kOA</title>"+css+
                "</head><body><header><a href='/index.html'>← Carte des applications</a>"
                "<a href='/local/campaigns'>Campagnes de conformité</a>"
                "<span class='chip'>Données privées · PC local seulement</span></header><main>"+body+"</main></body></html>")
    parts = route.strip("/").split("/")
    if parts == ["local", "campaigns"]:
        rows = list_campaigns(store)
        items = []
        for rec in rows:
            link = "/local/campaigns/" + rec["id"]
            items.append("<tr><td><a href='" + link + "'>"+escape(rec["title"])+"</a></td>"
                         "<td>"+escape(rec["frozen_at"])+"</td><td>"+str(rec["repositories"])+
                         "</td><td>"+("Empreinte vérifiée" if rec["integrity"] == "ok" else "Archive à vérifier")+"</td></tr>")
        timeline = []
        for rec in reversed([r for r in rows if r["integrity"] == "ok"][-12:]):
            try:
                coverage = campaign_coverage(read_campaign(rec["id"], store))
                total = max(1, coverage["repository_count"])
                ratio = round(100 * coverage["engineering_profiles"] / total, 1)
                described = str(coverage["engineering_profiles"]) + "/" + str(coverage["repository_count"])
                timeline.append("<div class='metric'><label><span><a href='/local/campaigns/"+
                                rec["id"]+"'>"+escape(rec["title"])+"</a> · "+escape(rec["frozen_at"][:10])+
                                "</span><strong>"+described+" profils · "+str(coverage["attached_proofs"])+
                                " rapports joints</strong></label><div class='track'><div class='fill' "
                                "style='width:"+str(ratio)+"%'></div></div></div>")
            except (OSError, ValueError, KeyError, TypeError, zipfile.BadZipFile):
                pass
        timeline_html = ("<div class='panel'><h2>Évolution de la couverture documentaire</h2>"
                         "<p>Barres : profils disponibles dans chaque campagne, pas taux de conformité ou de développement.</p>"+
                         "".join(timeline)+"</div>") if timeline else ""
        return page("Campagnes", "<h1>Campagnes de conformité</h1>"
                    "<p>Chaque campagne est une capture datée, indépendante des modifications futures des dépôts. "
                    "Aucun état « appliqué » n’est inféré d’un scan ou d’une taille de code.</p>"
                    "<table><thead><tr><th>Campagne</th><th>Date UTC</th><th>Dépôts</th><th>Intégrité</th></tr></thead><tbody>"
                    + ("".join(items) or "<tr><td colspan='4'>Aucune campagne figée pour le moment. Crée-en une dans le launcher Windows.</td></tr>")
                    + "</tbody></table>"+timeline_html+"<p>Les ZIP et empreintes restent dans ton dossier de campagnes local, jamais dans GitHub Pages.</p>")
    if len(parts) == 4 and parts[2] == "compare":
        comparison = compare_campaigns(parts[3].split("--")[0], parts[3].split("--")[-1], store) if "--" in parts[3] else None
        if comparison is None:
            raise ValueError("Sélectionner deux campagnes")
        totals = comparison["totals"]
        cards = "".join("<div class='panel'><strong>"+str(value)+"</strong><p>"+escape(key)+"</p></div>" for key,value in totals.items())
        old_coverage, new_coverage = comparison["older"]["coverage"], comparison["newer"]["coverage"]
        before_total=max(1,old_coverage["repository_count"]); after_total=max(1,new_coverage["repository_count"])
        charts=[]
        for key,label in qualification.STAGES:
            before=old_coverage["stages"][key]["counts"]["Étayé par preuve"]
            after=new_coverage["stages"][key]["counts"]["Étayé par preuve"]
            charts.append("<div class='metric'><label><span>"+escape(label)+"</span><strong>"+
                          str(before)+" → "+str(after)+" preuves étayées</strong></label>"
                          "<div class='track'><div class='fill prior' style='width:"+str(min(100,round(100*before/before_total,2)))+"%'></div></div>"
                          "<div class='track'><div class='fill' style='width:"+str(min(100,round(100*after/after_total,2)))+"%'></div></div></div>")
        chart_html=("<div class='panel'><h2>Évolution des cinq jalons · preuves validées manuellement</h2>"
                    "<p>Gris : campagne précédente · turquoise : campagne récente. "
                    "Non évalué n'est ni échec ni défaut.</p>"+"".join(charts)+"</div>")
        rows = "".join("<tr><td><a href='/local/campaigns/"+comparison["newer"]["id"]+
                       "/app/"+escape(row["slug"])+"'>"+escape(row["slug"])+"</a></td><td>"+
                       str(row["proof_files_added"])+" / "+str(row["proof_files_removed"])+
                       "</td><td>"+str(row["new_evidence"])+
                       "</td><td>"+str(row["withdrawn"])+"</td><td>"+str(row["new_practice_reviews"])+
                       "</td><td>"+("Oui" if row["commit_changed"] else "—")+"</td></tr>" for row in comparison["repositories"])
        return page("Comparaison des campagnes", "<h1>Comparaison documentaire</h1><p>"+
                    escape(comparison["older"]["title"])+" → "+escape(comparison["newer"]["title"])+
                    "</p><p>Aucune certification déduite automatiquement.</p><div class='grid'>"+cards+
                    "</div>"+chart_html+"<table><tr><th>Application</th><th>Rapports ajoutés / retirés</th><th>Nouveaux jalons étayés</th><th>Jalons non étayés depuis</th>"
                    "<th>Pratiques évaluées en plus</th><th>Commit différent</th></tr>"+rows+"</table>")
    if len(parts) < 3 or parts[:2] != ["local", "campaigns"] or not ID_PATTERN.fullmatch(parts[2]):
        raise ValueError("Route de campagne invalide")
    cid = parts[2]
    data = read_campaign(cid, store)
    records = data["repository_profiles_snapshot"]
    if len(parts) == 5 and parts[3] == "app":
        slug = parts[4]
        if slug not in records:
            raise ValueError("Fiche absente")
        record = records[slug]
        stages = record.get("qualification", {})
        rows = []
        for key, label in qualification.STAGES:
            item = stages.get(key, {})
            rows.append("<tr><td>"+escape(label)+"</td><td>"+escape(item.get("status", "Non évalué"))+
                        "</td><td>"+escape(item.get("scope", ""))+"</td><td>"+escape(item.get("evidence", ""))+
                        "</td><td>"+escape(item.get("reviewed_at", ""))+"</td></tr>")
        practice_rows = []
        for item_id, item in sorted((record.get("practices") or {}).items()):
            practice_rows.append("<tr><td>"+escape(item_id)+"</td><td>"+escape(item.get("status", ""))+
                                 "</td><td>"+escape(item.get("note", ""))+"</td></tr>")
        kristal = record.get("kristal") or {}
        assoc = kristal.get("association", "unavailable")
        linked = kristal.get("components") or []
        candidate = kristal.get("candidates") or []
        relation = kristal.get("relations") or []
        candidate_relation = kristal.get("candidate_relations") or []
        kdesc = ("<p>Statut documentaire : <strong>"+escape(assoc)+"</strong>. "
                 +str(len(linked))+" composant(s) explicite(s), "+str(len(candidate))+" proposition(s), "
                 +str(len(relation))+" relation(s) explicite(s) et "
                 +str(len(candidate_relation))+" relation(s) proposées. "
                 "Ces relations ne prouvent aucune qualification.</p>")
        def members(items):
            return "".join("<li>"+escape(str(e.get("label") or e.get("id") or e.get("subject") or ""))+" — "
                           +escape(str(e.get("evidence",e.get("status", ""))))+"</li>" for e in items[:25])
        kdesc += "<p>Composants explicitement reliés :</p><ul>"+members(linked)+"</ul>"
        kdesc += "<p>Correspondances proposées (non validées) :</p><ul>"+members(candidate)+"</ul>"
        prof = record.get("profiles") or {}
        plink = ("<p><a href='/local/campaigns/"+cid+"/engineering/"+quote(slug)+
                 "'>Lire le profil d’ingénierie figé</a></p>" if prof.get("engineering") else "<p>Profil d’ingénierie absent à cette date.</p>")
        audit = record.get("historical_audit") or {}
        github = (audit.get("recorded_git") or {})
        sha = github.get("head") or audit.get("reported_head") or (record.get("observed_git") or {}).get("head")
        urls = _github_link(record["repository"], sha) if sha else {}
        version = ("<p>Commit : <code>"+escape(sha)+"</code> — "
                   "<a href='"+urls["commit"]+"' rel='noopener noreferrer' target='_blank'>Ouvrir sur GitHub</a> · "
                   "<a href='"+urls["download_zip"]+"' rel='noopener noreferrer' target='_blank'>Télécharger ZIP</a>"
                   "</p>" if urls else "<p>Aucun commit Git SHA disponible pour cette capture.</p>")
        labels = {
            "collector_git_head_matches_reference_not_artifact_attestation": "SHA du collecteur concordant (exécution du rapport non attestée)",
            "collector_git_head_differs_from_reference": "SHA du collecteur différent de la version historique choisie",
            "collector_sha_without_campaign_git_reference": "SHA du collecteur seul, version historique non connue",
            "unverified_report_not_bound_to_commit": "Rapport importé, version Git non vérifiée",
        }
        proof_rows = []
        for index, proof in enumerate(record.get("attached_proofs") or []):
            link = "/local/campaigns/" + cid + "/proof/" + quote(slug) + "/" + str(index)
            proof_rows.append("<li><a href='"+link+"'>"+escape(proof.get("name", "Preuve"))+
                              "</a> — SHA-256 : "+escape(proof.get("sha256", ""))[:20]+"… — "
                              +escape(str((proof.get("summary") or {}).get("recognition", "document_only")))+
                              " — Git à la collecte : "+escape(str(proof.get("source_commit") or "non relié"))[:18]+
                              " · Relation au SHA : "+escape(labels.get(proof.get("version_relation") or proof_version_relation(proof,record),"Provenance inconnue"))+
                              " (rapport observé, non certifié)</li>")
        align = record.get("version_alignment") or version_alignment(record)
        alignment = ("<p>Comparaison des SHA Git : <strong>"+escape(align["git_comparison"])+
                     "</strong> · Profil ↔ commit : <strong>non vérifié (snapshot indépendant)</strong>. "
                     "Rapports joints ↔ commit : <strong>non vérifié</strong>.</p>")
        body = ("<h1>"+escape(slug)+"</h1><p>"+escape(record["repository"])+" — campagne "+escape(cid)+"</p>"
                +"<div class='panel'><h2>Version GitHub enregistrée</h2>"+version+alignment+"</div>"
                +"<div class='panel'><h2>Engineering Profile figé</h2>"+plink
                +"<p>Provenance : "+escape(str(prof.get("source_model", "unknown")))+
                " · SHA-256 du snapshot source : "+escape(str(prof.get("source_snapshot_sha256") or "non renseigné"))+
                ". Identité Git non prouvée par ce SHA.</p></div>"
                +"<div class='panel'><h2>Qualification manuelle figée</h2><table><tr><th>Jalon</th><th>État</th>"
                +"<th>Portée</th><th>Référence de preuve</th><th>Revu le</th></tr>"+"".join(rows)+"</table></div>"
                +"<div class='panel'><h2>Pratiques examinées</h2>"+
                ("<table><tr><th>ID</th><th>État</th><th>Justification</th></tr>"+"".join(practice_rows)+"</table>"
                 if practice_rows else "<p>Aucune pratique explicitement évaluée à cette date.</p>")+"</div>"
                +"<div class='panel'><h2>Kristal à la date de campagne</h2>"+kdesc+"</div>"
                +"<div class='panel'><h2>Pièces de preuve jointes</h2>"+
                ("<ul>"+"".join(proof_rows)+"</ul>" if proof_rows else "<p>Aucun rapport complémentaire joint.</p>")+"</div>")
        if data.get("historical_review"):
            body += ("<div class='panel'><h2>Revue historique figée</h2><p>"
                     "Les sources originales de la revue des 245 dossiers ont été archivées "
                     "avec cette campagne. Ce lot n'atteste pas le même SHA Git pour chaque preuve. "
                     "<a href='/local/campaigns/"+cid+"/review/download'>Télécharger la revue figée</a></p></div>")
        return page("Fiche historique · "+slug, body)
    if len(parts) == 5 and parts[3:] == ["review", "download"]:
        raise ValueError("La revue historique est téléchargeable via le serveur local")
    if len(parts) == 6 and parts[3] == "proof":
        slug = parts[4]
        if slug not in records or not parts[5].isdigit():
            raise ValueError("Preuve introuvable")
        info, raw = read_proof(cid, slug, int(parts[5]), store)
        label = escape(str(info.get("name", "Preuve")))
        kind = info.get("kind", "")
        if kind == "pdf":
            content = ("<h1>"+label+"</h1><p>Document PDF archivé, enregistré dans le ZIP privé. "
                       "Pour l'ouvrir, utiliser le bouton Télécharger ci-dessous.</p>"
                       "<p><a href='/local/campaigns/"+cid+"/download/"+quote(slug)+"/"+parts[5]+
                       "'>Télécharger la preuve PDF figée</a></p>")
        else:
            content = ("<h1>"+label+"</h1><p>Pièce figée · SHA-256 : <code>"+
                       escape(info.get("sha256", ""))+"</code> · source Git non attestée.</p>"
                       "<p><a href='/local/campaigns/"+cid+"/download/"+quote(slug)+"/"+parts[5]+
                       "'>Télécharger la pièce originale</a></p><pre>"+
                       escape(raw.decode("utf-8-sig",errors="replace"))+"</pre>")
        return page("Preuve · "+label, content)
    if len(parts) == 6 and parts[3] == "download":
        raise ValueError("Cette preuve doit être téléchargée via le serveur local")
    if len(parts) == 5 and parts[3] == "engineering":
        slug = parts[4]
        if slug not in records:
            raise ValueError("Profil absent de la campagne")
        text = read_profile(cid, slug, store)
        if text is None:
            raise ValueError("Document indisponible dans cette campagne")
        return page("Engineering Profile · " + slug, "<h1>Engineering Profile — " + escape(slug) +
                    "</h1><p>Document figé dans la campagne "+escape(cid)+". "
                    "Les mesures décrivent leur source propre et peuvent précéder le commit Git enregistré.</p><pre>"
                    +escape(text)+"</pre>")
    if len(parts) != 3:
        raise ValueError("Route de campagne invalide")
    items = []
    nprofiles = 0
    nverified = 0
    for slug, record in sorted(records.items(), key=lambda kv: kv[0].casefold()):
        git = record["observed_git"]
        audit = record.get("historical_audit") or {}
        old = audit.get("recorded_git") or {}
        historical = old if old.get("head") else ({"head": audit.get("reported_head"), "links": audit.get("links", {})} if audit else {})
        pinned = historical if historical.get("head") else (git if git.get("head") else {})
        sha = pinned.get("head")
        links = _github_link(record["repository"], sha) if sha else {}
        nverified += bool(git.get("status") == "verified_git_origin")
        profile = bool(record["profiles"].get("engineering"))
        nprofiles += profile
        profile_link = ("<a href='/local/campaigns/"+cid+"/engineering/"+quote(slug)+"'>Ouvrir le profil figé</a>" if profile else "—")
        stages = record.get("qualification", {})
        evidenced = sum(x.get("status") == "Étayé par preuve" for x in stages.values())
        versions = ("<a href='"+links["commit"]+"' target='_blank' rel='noopener noreferrer'>Commit</a> · "
                    "<a href='"+links["download_zip"]+"' target='_blank' rel='noopener noreferrer'>Télécharger le code ZIP</a>"
                    if links else "Pas de commit attesté")
        origin = "SHA de l’audit antérieur" if historical.get("head") else ("Git local actuel" if git.get("head") else "Aucun")
        items.append("<tr><td><strong><a href='/local/campaigns/"+cid+"/app/"+quote(slug)+"'>"+escape(slug)+"</a></strong><br><small>"+escape(origin)+"</small></td>"
                     "<td>"+profile_link+"</td><td>"+str(evidenced)+" / 5 jalons étayés</td>"
                     "<td>"+versions+"<br><small>"+escape((sha or "")[:12])+"</small></td>"
                     "<td><small>"+escape(git.get("worktree",git.get("status","Non vérifié")))+"</small></td></tr>")
    header = "<h1>"+escape(data["title"])+"</h1><p>Capture UTC : "+escape(data["frozen_at"])+" · ID : "+escape(cid)+"</p>"
    old_rows = [x for x in list_campaigns(store)
                if x["id"] != cid and x["integrity"] != "failed"
                and x["frozen_at"] < data["frozen_at"]]
    if old_rows:
        previous = max(old_rows,key=lambda x:(x["frozen_at"],x.get("created_ns",0)))["id"]
        header += ("<p><a href='/local/campaigns/compare/"+previous+"--"+cid+
                   "'>Comparer à la campagne précédente →</a></p>")
    coverage=campaign_coverage(data)
    summary = ("<div class='grid'>"+"".join("<div class='panel'><strong>"+v+"</strong><p>"+k+"</p></div>"
                for k,v in [("Dépôts documentés",str(len(records))), ("Engineering Profiles figés",str(nprofiles)),
                            ("Origines Git vérifiées localement",str(nverified)),
                            ("Pièces de preuves jointes",str(coverage["attached_proofs"])),
                            ("Pratiques examinées explicitement",str(coverage["practice_reviews"]))])+"</div>")
    visual=[]
    count=max(1,len(records))
    for key,title in qualification.STAGES:
        amounts=coverage["stages"][key]["counts"]
        validated=amounts["Étayé par preuve"]
        visual.append("<div class='metric'><label><span>"+escape(title)+"</span><strong>"+
                      str(validated)+" / "+str(len(records))+" étayés</strong></label>"
                      "<div class='track'><div class='fill' style='width:"+
                      str(round(100*validated/count,2))+"%'></div></div>"
                      "<small>À documenter : "+str(amounts["À documenter"])+
                      " · Non évalué : "+str(amounts["Non évalué"])+
                      " · Non applicable : "+str(amounts["Non applicable"])+"</small></div>")
    kinds = coverage.get("proof_categories") or {}
    relations = coverage.get("proof_version_relations") or {}
    rows = "".join("<tr><td>"+escape(str(kind))+"</td><td>"+str(count)+"</td></tr>"
                   for kind,count in sorted(kinds.items()))
    summary += ("<div class='panel'><h2>Rapports archivés et provenance Git</h2>"
                "<p>Rapports présents dans le ZIP, sans les réexécuter : " +str(coverage["attached_proofs"])+
                ". Une concordance de SHA ne prouve pas que le rapport a été généré à ce commit.</p>"
                +("<table><tr><th>Type de preuve importée</th><th>Nombre</th></tr>"+rows+"</table>" if rows else "<p>Aucun rapport complémentaire.</p>")+
                "<p>SHA collecteur concordant : "+str(relations.get("collector_git_head_matches_reference_not_artifact_attestation",0))+
                " · SHA différent : "+str(relations.get("collector_git_head_differs_from_reference",0))+
                " · Non relié / inconnu : "+str(relations.get("unverified_report_not_bound_to_commit",0))+".</p></div>")
    summary += "<div class='panel'><h2>Qualification documentée · 5 jalons indépendants</h2>"+"".join(visual)+"</div>"
    if data.get("historical_review"):
        summary += ("<div class='panel'><h2>Revue historique originale conservée</h2>"
                    "<p>245 dossiers de revue privés, archives de documents originaux et empreintes. "
                    "Leur présence ne signifie pas que 245 jalons sont étayés. "
                    "<a href='/local/campaigns/"+cid+"/review/download'>Télécharger la revue historique figée</a></p></div>")
    note = ("<div class='panel'><strong>Important</strong><p>Les liens de téléchargement ciblent un SHA, "
            "pas main. Leur disponibilité distante n’a pas été testée. "
            "Les anciens profils issus de snapshots peuvent provenir d’une autre version que le commit indiqué. "
            "Les champs Git et les résultats d'audit ne certifient aucun jalon.</p></div>")
    table = ("<table><thead><tr><th>Dépôt</th><th>Profil figé</th><th>Qualification manuelle</th>"
             "<th>Version GitHub (commit historique prioritaire)</th><th>État de la copie actuelle</th></tr></thead><tbody>"
             +"".join(items)+"</tbody></table>")
    return page("Campagne · " + data["title"],header+summary+note+table)
