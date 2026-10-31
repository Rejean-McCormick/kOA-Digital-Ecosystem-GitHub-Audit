"""Offline documentation index for owner-supplied repository ZIP bundles.

Metadata-only by design. No extraction, network, Git calls, code execution,
publication or source content in the output. An archive folder is not Git proof.
"""
from __future__ import annotations

import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path, PurePosixPath
from zipfile import BadZipFile, ZipFile, ZipInfo

FORMAT = "koa.documentation_graph_source.v1"
MAX_MEMBERS = 20000
MAX_ARCHIVE_BYTES = 1_000_000_000
MAX_DOC_BYTES = 2_000_000
MAX_TOTAL_DOC_BYTES = 150_000_000
DOC_EXTENSIONS = {".md", ".mdx", ".rst", ".adoc"}
ROOT_NAMES = {"readme.md", "contributing.md", "architecture.md", "security.md", "agents.md"}
HEX_SUFFIX = re.compile(r"^(?P<base>.+)-[0-9a-f]{8}$", re.IGNORECASE)
REPO_NAME = re.compile(r"^[A-Za-z0-9_.-]{1,120}$")


def _valid_path(name: str) -> tuple[str, str] | None:
    """Accept only repos/<repository>/<path> without navigation or ambiguity."""
    if "\\" in name or "\x00" in name or name.startswith("/") or ":" in name:
        return None
    parts = PurePosixPath(name).parts
    if (len(parts) < 3 or parts[0] != "repos" or
            any(p in ("", ".", "..") for p in name.split("/")) or
            not REPO_NAME.fullmatch(parts[1])):
        return None
    rel = "/".join(parts[2:])
    if not rel or name.endswith("/"):
        return None
    return parts[1], rel


def _document_kind(rel: str) -> str | None:
    parts = PurePosixPath(rel).parts
    if len(parts) == 1 and parts[0].casefold() in ROOT_NAMES:
        return "root"
    if PurePosixPath(rel).suffix.casefold() not in DOC_EXTENSIONS:
        return None
    if parts[0].casefold() == "docs":
        return "docs"
    if parts[0].casefold() == "wiki":
        return "wiki"
    return None


def _symlink(info: ZipInfo) -> bool:
    return (info.create_system == 3 and ((info.external_attr >> 16) & 0o170000) == 0o120000)


def _inventory_repos(inventory_path: Path) -> dict[str, str]:
    rows = json.loads(Path(inventory_path).read_text(encoding="utf-8"))
    if not isinstance(rows, list):
        raise ValueError("Expected inventory list")
    names: dict[str, str] = {}
    for item in rows:
        full = item.get("github_repo", "") if isinstance(item, dict) else ""
        if not isinstance(full, str) or "/" not in full:
            raise ValueError("Malformed repository in inventory")
        owner, name = full.split("/", 1)
        if not REPO_NAME.fullmatch(owner) or not REPO_NAME.fullmatch(name):
            raise ValueError("Malformed GitHub repository name")
        key = name.casefold()
        if key in names and names[key] != full:
            raise ValueError("Ambiguous inventory names across owners")
        names[key] = full
    return names


def collect_zip(archive: Path, inventory_path: Path) -> dict:
    """Inspect a repos/ bundle, returning a private, reproducible metadata index.

    Refuses path collisions and suspicious paths. Limits resource consumption.
    Never treats unseen code, repo identity or documentation as qualification.
    """
    archive = Path(archive)
    if not archive.is_file() or archive.is_symlink():
        raise ValueError("ZIP absent ou lien symbolique")
    if archive.stat().st_size > MAX_ARCHIVE_BYTES:
        raise ValueError("ZIP trop volumineux")
    official = _inventory_repos(inventory_path)
    records: dict[str, list[dict]] = defaultdict(list)
    discarded = defaultdict(int)
    bytes_read = 0
    with ZipFile(archive, "r") as z:
        infos = z.infolist()
        if len(infos) > MAX_MEMBERS:
            raise ValueError("ZIP trop volumineux : trop d'entrées")
        seen: set[str] = set()
        roots: set[str] = set()
        for info in infos:
            parsed = _valid_path(info.filename)
            if parsed is None:
                if not info.is_dir():
                    discarded["invalid_or_outside_repo"] += 1
                continue
            repo, rel = parsed
            roots.add(repo)
            if _symlink(info):
                discarded["symlink"] += 1
                continue
            key = (repo + "/" + rel).casefold()
            if key in seen:
                raise ValueError("Collision de chemins dans ZIP : " + key)
            seen.add(key)
            kind = _document_kind(rel)
            if kind is None:
                continue
            if info.file_size > MAX_DOC_BYTES or info.file_size < 0:
                discarded["oversized_document"] += 1
                continue
            if bytes_read + info.file_size > MAX_TOTAL_DOC_BYTES:
                raise ValueError("Volume documentaire supérieur à la limite")
            with z.open(info) as source:
                raw = source.read(MAX_DOC_BYTES + 1)
            if len(raw) != info.file_size or len(raw) > MAX_DOC_BYTES:
                raise ValueError("Taille documentaire non conforme : " + rel)
            bytes_read += len(raw)
            records[repo].append({"path": rel, "kind": kind,
                                  "size_bytes": len(raw),
                                  "sha256": hashlib.sha256(raw).hexdigest()})
    # Observe all roots, including code-only bundles without docs.
    for root in roots:
        records.setdefault(root, [])
    repos = []
    for root, entries in sorted(records.items(), key=lambda kv: kv[0].casefold()):
        entries.sort(key=lambda e: e["path"].casefold())
        suffix = HEX_SUFFIX.fullmatch(root)
        base = suffix.group("base") if suffix else None
        duplicate = bool(base and (base.casefold() in official or base in roots))
        status = ("inventory_match" if root.casefold() in official else
                  "snapshot_copy_candidate" if duplicate else "unregistered_candidate")
        # Only construct external URLs from official owner/repo identities.
        # Never assume GitHub README or wiki availability from ZIP contents.
        full_name = official.get(root.casefold())
        repository_url = "https://github.com/" + full_name if full_name else None
        github_links = ({"repository": repository_url,
                         "documentation": repository_url + "#readme",
                         "wiki": repository_url + "/wiki",
                         "availability_verified": False} if full_name else None)
        repos.append({"snapshot_folder": root,
                      "discovery_status": status,
                      "github_links": github_links,
                      "possible_base_repository": base if duplicate else None,
                      "documentation_count": len(entries),
                      "documentation_by_kind": {k: sum(d["kind"] == k for d in entries)
                                                for k in ("root", "docs", "wiki")},
                      "documents": entries})
    digest = hashlib.sha256()
    with archive.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return {"format": FORMAT, "source": {"type": "owner_supplied_zip",
            "name": archive.name, "sha256": digest.hexdigest(),
            "git_revision_verified": False},
            "inventory_baseline_count": len(official), "repositories_observed": len(repos),
            "registered_observed": sum(r["discovery_status"] == "inventory_match" for r in repos),
            "new_candidates": [r["snapshot_folder"] for r in repos
                               if r["discovery_status"] == "unregistered_candidate"],
            "discarded": dict(sorted(discarded.items())), "repositories": repos,
            "limitations": ["Les noms de dossiers ZIP ne prouvent ni l'identité de leur remote Git ni leur commit GitHub.",
                            "Aucun contenu documentaire n'est exporté ; seuls chemins, tailles et SHA-256 sont indexés.",
                            "Les doublons et nouveaux candidats requièrent une revue avant admission au registre.",
                            "Aucune qualification, preuve de test ou maturité n'est inférée.",
                            "Ce rapport est local/privé et ne doit pas être publié dans docs/ ou sur Pages."]}


def write_private_index(report: dict, destination: Path) -> Path:
    """Never overwrite evidence or publish beneath GitHub Pages docs/."""
    destination = Path(destination)
    if destination.suffix.lower() != ".json" or "docs" in (p.casefold() for p in destination.parts):
        raise ValueError("Rapport local JSON uniquement, hors docs/")
    destination.parent.mkdir(parents=True, exist_ok=True)
    payload = (json.dumps(report, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    with destination.open("xb") as f:
        f.write(payload)
    return destination
