"""Read-only adapter for the user's local Kristal-kOA-Ecosystem canonical catalogs.

We never ingest generated .kristal states or private/local paths into a website.
Only a small, explicitly allowlisted semantic projection is returned to the
loopback dashboard; no files in the source repository are ever changed.
"""
from __future__ import annotations

import json
import os
import re
import tempfile
import unicodedata
from collections import Counter
from pathlib import Path
from typing import Any

FORMAT = "koa_audit.kristal_local.v1"
DEFAULT_WINDOWS_ROOT = r"C:\mycode\Kristal\locals\Kristal-kOA-Ecosystem"
CATALOGS = (
    ("repositories", "knowledge-base/sources/repositories.json", 4_000_000),
    ("components", "knowledge-base/sources/components.json", 2_000_000),
    ("relations", "knowledge-base/sources/relations.json", 4_000_000),
    ("contracts", "knowledge-base/sources/contracts.json", 2_000_000),
    ("capabilities", "knowledge-base/sources/capabilities.json", 2_000_000),
    ("sources", "knowledge-base/sources/source-registry/source-registry.json", 2_000_000),
)
RELATIONS = {"koa:part_of", "koa:connects_to", "koa:uses_contract", "koa:conforms_to", "koa:participates_in", "koa:realizes_or_supports"}
_ALLOWED_STATE = {"sourced", "claimed"}


def settings_path() -> Path:
    folder = os.environ.get("LOCALAPPDATA") or tempfile.gettempdir()
    return Path(folder) / "kOA-GitHub-Audit" / "kristal-source.json"


def get_source_root() -> Path:
    override = os.environ.get("KOA_KRISTAL_SOURCE", "").strip()
    if override:
        return Path(override).expanduser()
    state = settings_path()
    if state.is_file() and not state.is_symlink() and state.stat().st_size < 8192:
        try:
            saved = json.loads(state.read_text(encoding="utf-8"))
            if isinstance(saved, dict) and isinstance(saved.get("folder"), str) and saved["folder"].strip():
                return Path(saved["folder"]).expanduser()
        except (OSError, ValueError):
            pass
    return Path(DEFAULT_WINDOWS_ROOT)


def save_source_root(folder: Path) -> None:
    """Save only the chosen root location, outside the project; never publish."""
    target = settings_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    payload = {"format": "koa_audit.kristal_source_settings.v1", "folder": str(folder)}
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def _read_catalog(folder: Path, rel: str, max_bytes: int) -> list[dict]:
    path = folder / rel
    if path.is_symlink() or not path.is_file():
        raise FileNotFoundError(f"Catalogue Kristal manquant : {rel}")
    size = path.stat().st_size
    if size <= 0 or size > max_bytes:
        raise ValueError(f"Catalogue Kristal hors limites : {rel}")
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    name = "sources" if rel.endswith("source-registry.json") else Path(rel).stem
    rows = data.get(name) if isinstance(data, dict) else None
    if not isinstance(rows, list) or len(rows) > 100_000:
        raise ValueError(f"Structure du catalogue Kristal invalide : {rel}")
    return [r for r in rows if isinstance(r, dict)]


def _text(value: Any, limit: int = 240) -> str:
    if not isinstance(value, str):
        return ""
    # Catalog descriptions may contain internal paths. Never surface local
    # Windows or POSIX paths as part of public-looking projected summaries.
    value = value.strip().replace("\x00", "")
    value = re.sub(r"[A-Za-z]:[\\/][^\s,;\])]+", "[chemin local]", value)
    return value[:limit]


def _safe_identity(value: Any) -> str:
    if isinstance(value, str) and re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", value):
        return value
    return ""


def _canonical_name(value: Any) -> str:
    """Compare exact normalized identities, not fuzzy substring similarities."""
    if not isinstance(value, str):
        return ""
    plain = unicodedata.normalize("NFKD", value).casefold()
    return "".join(c for c in plain if c.isascii() and c.isalnum())


def _source_refs(value: Any) -> list[str]:
    """References are used internally to corroborate candidates, never returned."""
    if not isinstance(value, list):
        return []
    return [ref for ref in value if isinstance(ref, str) and len(ref) <= 180
            and re.fullmatch(r"src:[A-Za-z0-9_.:/-]+", ref)]


def _candidate_view(c: dict, reason: str, shared_count: int) -> dict:
    return {"id": _text(c.get("id"), 150), "label": _text(c.get("label"), 110),
            "kind": _text(c.get("kind"), 75),
            "evidence": c.get("assertion_status") if c.get("assertion_status") in _ALLOWED_STATE else "unknown",
            "reason": reason,
            "source_count": min(len(_source_refs(c.get("source_refs"))), 100),
            "shared_source_count": min(shared_count, 4),
            "status": "CANDIDATE_NOT_VALIDATED"}


def build_local_kristal_view(folder: Path, inventory: list[str]) -> dict:
    """Match repositories by exact full_name; do not guess membership or certification."""
    folder = Path(folder)
    if not folder.is_dir():
        raise FileNotFoundError("Dossier Kristal introuvable")
    repo_items = _read_catalog(folder, CATALOGS[0][1], CATALOGS[0][2])
    component_items = _read_catalog(folder, CATALOGS[1][1], CATALOGS[1][2])
    relation_items = _read_catalog(folder, CATALOGS[2][1], CATALOGS[2][2])
    # Additional catalogs are informative aggregates; older/minimal source trees
    # may not have them and should still be supported without inventing counts.
    optional_counts = {}
    for key, relative, limit in CATALOGS[3:]:
        try:
            optional_counts[key] = len(_read_catalog(folder, relative, limit))
        except FileNotFoundError:
            optional_counts[key] = None
    by_full = {}
    for item in repo_items:
        name = _safe_identity(item.get("full_name"))
        if name:
            by_full.setdefault(name.casefold(), item)
    chosen = {name.casefold():name for name in inventory if _safe_identity(name)}
    by_id = {item['id']: item for item in component_items
             if isinstance(item.get('id'),str) and len(item['id']) < 160}
    mapped = {repo.get('id'):chosen[key] for key,repo in by_full.items()
              if key in chosen and isinstance(repo.get('id'),str)}
    # A specific shared source is only a suggestion, never an implicit mapping.
    source_usage = Counter(ref for repo in repo_items for ref in _source_refs(repo.get('source_refs')))
    components_by_repo = {}
    for component in component_items:
        owner = mapped.get(component.get('repository_ref'))
        if owner:
            components_by_repo.setdefault(owner, []).append(component)
    # Use only components without repository_ref as candidates. Exact normalized
    # name/canonical ID matches; source matches require a rare specific GitHub ref.
    candidate_by_repo: dict[str, list[dict]] = {}
    candidate_ids_by_repo: dict[str, set[str]] = {}
    for official in inventory:
        source = by_full.get(official.casefold())
        if not source:
            continue
        normal = _canonical_name(official.split('/')[-1])
        refs = set(_source_refs(source.get('source_refs')))
        found=[]
        for comp in component_items:
            if comp.get('repository_ref'):
                continue
            comp_id=comp.get('id')
            if not isinstance(comp_id,str) or len(comp_id) > 150:
                continue
            same_name = len(normal)>3 and normal in (
                _canonical_name(comp.get('label')),
                _canonical_name(comp_id.rsplit(':', 1)[-1]),
            )
            shared = [ref for ref in _source_refs(comp.get('source_refs'))
                      if ref in refs and ref.startswith('src:github-') and source_usage[ref] <= 2]
            if same_name or shared:
                reason = 'EXACT_NAME_OR_CANONICAL_ID' if same_name else 'SHARED_SPECIFIC_GITHUB_SOURCE'
                found.append(_candidate_view(comp, reason, len(shared)))
        if found:
            candidate_by_repo[official]=found[:20]
            candidate_ids_by_repo[official]={c['id'] for c in found[:20]}
    edges_by_repo = {}
    candidate_edges_by_repo: dict[str, list[dict]] = {}
    for rel in relation_items:
        pred=rel.get('predicate')
        if pred not in RELATIONS or rel.get('assertion_status') not in _ALLOWED_STATE:
            continue
        sid=rel.get('subject'); oid=rel.get('object')
        sub=by_id.get(sid); obj=by_id.get(oid)
        if not sub or not obj:
            continue
        owners={mapped.get(sub.get('repository_ref')),mapped.get(obj.get('repository_ref'))}-{None}
        # Relation to a proposed component stays explicitly separate from
        # relations anchored by a canonical repository_ref.
        for candidate_repo, ids in candidate_ids_by_repo.items():
            if sid not in ids and oid not in ids:
                continue
            arr = candidate_edges_by_repo.setdefault(candidate_repo, [])
            if len(arr) < 16:
                arr.append({"subject":_text(sub.get('label'),90),
                            "predicate":pred.rsplit(':',1)[-1],
                            "object":_text(obj.get('label'),90),
                            "evidence":rel.get('assertion_status'),
                            "status":"CANDIDATE_NOT_VALIDATED"})
        if not owners:continue
        edge={"subject":_text(sub.get('label'),90),"predicate":pred.rsplit(':',1)[-1],
              "object":_text(obj.get('label'),90),"evidence":rel.get('assertion_status'),
              "source_count":min(len(rel.get('source_refs') or []),100)}
        for owner in owners:
            arr=edges_by_repo.setdefault(owner,[])
            if len(arr) < 24:arr.append(edge)
    rows=[]
    for official in inventory:
        source=by_full.get(official.casefold())
        if source is None:
            rows.append({"repo":official,"found":False,"components":[],"relations":[],
                         "candidates":[],"candidate_relations":[],"association":"unknown"})
            continue
        components=[]
        for c in components_by_repo.get(official,[])[:20]:
            components.append({"label":_text(c.get('label'),100),
                               "kind":_text(c.get('kind'),80),
                               "description":_text(c.get('description'),320),
                               "evidence":c.get('assertion_status') if c.get('assertion_status') in _ALLOWED_STATE else 'unknown'})
        rows.append({"repo":official,"found":True,
            "name":_text(source.get('name'),110),
            "description":_text(source.get('description'),400),
            "membership":_text(source.get('architectural_membership'),80),
            "role":_text(source.get('repository_role'),80),
            "locator_status":_text(source.get('repository_locator_status'),80),
            "components":components,
            "candidates":candidate_by_repo.get(official,[]),
            "candidate_relations":candidate_edges_by_repo.get(official,[]),
            "association":"explicit" if components else ("candidate" if candidate_by_repo.get(official) else "unlinked"),
            "relations":edges_by_repo.get(official,[]),
        })
    matched=sum(1 for r in rows if r['found'])
    return {"format":FORMAT,"state":"ready","catalog_repositories":len(repo_items),
            "catalog_components":len(component_items),"catalog_relations":len(relation_items),
            "catalog_contracts":optional_counts.get('contracts'),
            "catalog_capabilities":optional_counts.get('capabilities'),
            "catalog_sources":optional_counts.get('sources'),
            "inventory":len(inventory),"matched":matched,
            "mapped_components":sum(len(r.get('components') or []) for r in rows),
            "explicit_repositories":sum(bool(r.get('components')) for r in rows),
            "candidate_repositories":sum(bool(r.get('candidates')) and not bool(r.get('components')) for r in rows),
            "unlinked_repositories":sum(bool(r.get('found')) and not r.get('components') and not r.get('candidates') for r in rows),
            "repositories":rows,
            "provenance":"Kristal local — knowledge-base/sources/; rapprochement exact du registre kOA",
            "notice":"Cartographie sémantique, pas preuve de tests, de déploiement ou de certification."}
