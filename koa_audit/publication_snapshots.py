"""Opt-in, dated public documentation snapshots. No audit/certification inference.

The network reader only runs in an explicit publishing workflow. Local tests can inject
captures without network access; published HTML contains frozen source text.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from datetime import datetime, timezone
import hashlib
import html
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import tempfile
from typing import Callable
from urllib.parse import quote

from .graph_public import compile_public_graph
from .focus_graph import compile_focused_paths

REPO_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
RELEASE_RE = re.compile(r"^[0-9]{8}T[0-9]{6}Z(?:-[0-9]+(?:-[0-9]+)?)?$")
DOC_EXT = {".md", ".mdx", ".markdown", ".rst", ".txt", ".adoc"}
MAX_DOCS = 150
MAX_DOC_BYTES = 256 * 1024
MAX_REPO_BYTES = 4 * 1024 * 1024


@dataclass
class Capture:
    repo: str
    revision: str
    documents: dict[str, str] = field(default_factory=dict)
    wiki_revision: str | None = None
    wiki: dict[str, str] = field(default_factory=dict)
    notes: list[str] = field(default_factory=list)
    graph_registry_text: str | None = None
    graph_inventory_text: str | None = None
    graph_focus_text: str | None = None


def _run(args: list[str], *, timeout: int = 180) -> str:
    result = subprocess.run(args, capture_output=True, text=True, check=False,
                            timeout=timeout, env={**os.environ, "GIT_TERMINAL_PROMPT": "0"})
    if result.returncode != 0:
        raise RuntimeError((result.stderr or result.stdout or "git failed").strip()[-500:])
    return result.stdout.strip()


def allowed_repositories(inventory: Path, additions: Path) -> list[str]:
    """Explicit PUBLIC allowlist. Folder names found in ZIPs are not trusted URLs."""
    entries = json.loads(inventory.read_text(encoding="utf-8"))
    extras = json.loads(additions.read_text(encoding="utf-8"))
    names: set[str] = set()
    for entry in [*entries, *extras]:
        if entry.get("scope") != "PUBLIC":
            continue
        name = entry.get("github_repo", "")
        if not REPO_RE.fullmatch(name):
            raise ValueError(f"Invalid repository identity: {name!r}")
        names.add(name)
    return sorted(names, key=str.casefold)


def selected_repositories(allowlist: list[str], mode: str, selected: str) -> list[str]:
    if mode == "all":
        return allowlist
    if mode != "selected":
        raise ValueError(f"Unsupported mode: {mode}")
    tokens = [x.strip() for x in re.split(r"[,;\n]+", selected) if x.strip()]
    if not tokens:
        raise ValueError("Selected mode requires at least one repository")
    by_full = {r.casefold(): r for r in allowlist}
    by_short = {}
    for r in allowlist:
        by_short.setdefault(r.split("/", 1)[1].casefold(), []).append(r)
    out = []
    for token in tokens:
        if token.casefold() in by_full:
            match = by_full[token.casefold()]
        elif len(by_short.get(token.casefold(), [])) == 1:
            match = by_short[token.casefold()][0]
        else:
            raise ValueError(f"Unknown or ambiguous repository: {token}. Update the explicit allowlist first.")
        if match not in out:
            out.append(match)
    return out


def _is_document(path: PurePosixPath, wiki: bool) -> bool:
    if path.suffix.lower() not in DOC_EXT:
        return False
    if any(part.startswith(".") or part.lower() in {"node_modules", "vendor", "build", "dist", "_site"} for part in path.parts):
        return False
    if wiki:
        return True
    return (len(path.parts) == 1 and path.name.lower().startswith("readme")) or (
        path.parts[0].lower() in {"docs", "doc", "documentation", "wiki"})


def _collect_tree(folder: Path, wiki: bool) -> tuple[dict[str, str], list[str]]:
    files, notes = {}, []
    used = 0
    for file in sorted(folder.rglob("*")):
        if not file.is_file() or file.is_symlink():
            continue
        rel = PurePosixPath(file.relative_to(folder).as_posix())
        if not _is_document(rel, wiki):
            continue
        if len(files) >= MAX_DOCS:
            notes.append(f"Document cap reached ({MAX_DOCS}); partial copy")
            break
        size = file.stat().st_size
        if size > MAX_DOC_BYTES or size + used > MAX_REPO_BYTES:
            notes.append(f"Skipped oversized file: {rel}")
            continue
        raw = file.read_bytes()
        if b"\x00" in raw:
            continue
        files[str(rel)] = raw.decode("utf-8", errors="replace")
        used += size
    return files, notes


def capture_public_repository(repo: str) -> Capture:
    """Read only. Shallow sparse clone of docs and a separate optional wiki clone."""
    if not REPO_RE.fullmatch(repo):
        raise ValueError("Invalid repository name")
    with tempfile.TemporaryDirectory(prefix="koa-publication-") as temp:
        tmp = Path(temp)
        root = tmp / "source"
        url = f"https://github.com/{repo}.git"
        _run(["git", "clone", "--quiet", "--depth", "1", "--filter=blob:none", "--sparse", "--single-branch", url, str(root)])
        _run(["git", "-C", str(root), "sparse-checkout", "set", "--no-cone", "/*README*", "/*readme*", "/docs/", "/doc/", "/documentation/", "/wiki/"])
        revision = _run(["git", "-C", str(root), "rev-parse", "HEAD"])
        documents, notes = _collect_tree(root, wiki=False)
        captured = Capture(repo=repo, revision=revision, documents=documents, notes=notes)
        if repo == "Rejean-McCormick/kOA-Digital-Ecosystem":
            registry_file = root / "docs/inventory/graph-registry.v1.json"
            inventory_file = root / "docs/inventory/repositories.json"
            if registry_file.is_file() and inventory_file.is_file():
                for f in (registry_file, inventory_file):
                    if f.is_symlink() or f.stat().st_size > 512_000:
                        raise ValueError("Unsafe graph source file")
                captured.graph_registry_text = registry_file.read_text(encoding="utf-8")
                captured.graph_inventory_text = inventory_file.read_text(encoding="utf-8")
                focus_file = root / "docs/inventory/graph-focus.v1.json"
                if focus_file.is_file():
                    if focus_file.is_symlink() or focus_file.stat().st_size > 512_000:
                        raise ValueError("Unsafe focused graph source file")
                    captured.graph_focus_text = focus_file.read_text(encoding="utf-8")
        wikidir = tmp / "wiki"
        try:
            _run(["git", "clone", "--quiet", "--depth", "1", f"https://github.com/{repo}.wiki.git", str(wikidir)], timeout=90)
            captured.wiki_revision = _run(["git", "-C", str(wikidir), "rev-parse", "HEAD"])
            captured.wiki, wiki_notes = _collect_tree(wikidir, wiki=True)
            captured.notes.extend(wiki_notes)
        except (RuntimeError, subprocess.TimeoutExpired):
            captured.notes.append("Wiki inaccessible, disabled or empty; no wiki copy")
        if not captured.documents and not captured.wiki:
            captured.notes.append("No README, docs or wiki text found")
        return captured


def _e(s: object) -> str:
    return html.escape(str(s), quote=True)


def _page(title: str, body: str) -> str:
    return ("<!doctype html><html lang='fr'><head><meta charset='utf-8'>"
            "<meta name='viewport' content='width=device-width,initial-scale=1'>"
            f"<title>{_e(title)}</title><style>body{{font:16px system-ui;max-width:1000px;margin:auto;padding:25px;"
            "background:#f4f8f6;color:#173733}}a{color:#1e6864}pre{white-space:pre-wrap;overflow-wrap:anywhere;"
            "background:white;border:1px solid #d4e3dd;border-radius:12px;padding:22px;line-height:1.6}"
            "small{color:#596c68}.meta{margin:14px 0 25px}</style></head><body>"
            f"{body}</body></html>")


def _write_doc(dest: Path, title: str, raw: str, repo: str, revision: str, source: str) -> tuple[str, str]:
    dest.parent.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()
    body = (f"<p><a href='../../../../index.html'>← Publications</a></p><h1>{_e(title)}</h1>"
            f"<p class='meta'><small>{_e(repo)} · {_e(revision[:12])} · SHA-256 {_e(digest[:16])}</small>"
            f"<br><a href='{_e(source)}' rel='noopener noreferrer'>Source GitHub / GitHub source</a></p>"
            f"<pre>{_e(raw)}</pre>")
    dest.write_text(_page(title, body), encoding="utf-8")
    return digest, source


def _document_path(repo: str, rel: str, wiki: bool) -> str:
    # Hash means paths cannot collide or escape destination, even if the source is malicious.
    key = hashlib.sha256((repo + "\0" + ("wiki/" if wiki else "") + rel).encode()).hexdigest()[:20]
    name = PurePosixPath(rel).name
    safe_name = re.sub(r"[^A-Za-z0-9_.-]", "-", name)[:60] or "doc"
    return f"repos/{repo.replace('/', '--')}/{key}-{safe_name}.html"


def _source_url(repo: str, revision: str, rel: str, wiki: bool) -> str:
    if wiki:
        # Source wiki URL is a convenience; the immutable wiki SHA is recorded separately.
        return f"https://github.com/{repo}/wiki/{quote(PurePosixPath(rel).stem)}"
    return f"https://github.com/{repo}/blob/{revision}/{quote(rel, safe='/')}"


def _load_previous(docs: Path) -> dict:
    pointer = docs / "data" / "publication-current.json"
    if not pointer.exists():
        return {"repos": []}
    payload = json.loads(pointer.read_text(encoding="utf-8"))
    release = payload.get("release_id", "")
    if not RELEASE_RE.fullmatch(release):
        raise ValueError("Invalid published release pointer")
    manifest = docs / "publications" / "releases" / release / "manifest.json"
    return json.loads(manifest.read_text(encoding="utf-8"))


def _l(fr: str, en: str) -> str:
    return f"<span class='fr'>{_e(fr)}</span><span class='en'>{_e(en)}</span>"


def _generate_index(manifest: dict, prefix: str) -> str:
    """Reuse the local dashboard's directory/detail layout for frozen publications.

    The viewer fetches ONLY this release's immutable manifest (or the dated pointer
    for the current publication). It never reads live GitHub while presenting.
    """
    archived = bool(prefix)
    assets = prefix + "../assets/"
    home = prefix + "../index.html"
    pointer = "" if archived else "../data/publication-current.json"
    manifest_url = "manifest.json" if archived else ""
    stamp = _e(manifest.get("published_at", ""))
    count = len(manifest.get("repos", []))
    chosen = len(manifest.get("selected", []))
    return ("<!doctype html><html lang='fr'><head><meta charset='utf-8'>"
            "<meta name='viewport' content='width=device-width,initial-scale=1'>"
            "<meta name='description' content='kOA Graph — publications documentaires datées'>"
            "<title>kOA Graph · Publications datées</title>"
            f"<link rel='stylesheet' href='{_e(assets)}atlas.css'>"
            "</head><body><div class='layout'>"
            "<nav class='rail' aria-label='Navigation principale'>"
            f"<a class='brand' href='{_e(home)}#apps' aria-label='kOA'><img src='{_e(assets)}logo.svg' alt='kOA'></a>"
            f"<a class='workspace-nav' href='{_e(home)}#validations'><span aria-hidden='true'>✓</span> Validations</a>"
            f"<a class='workspace-nav' href='{_e(home)}#apps'><span aria-hidden='true'>▦</span> Applications</a>"
            "<a class='workspace-nav active' href='#publication-viewer' aria-current='page'><span aria-hidden='true'>◷</span> Publications</a>"
            "<div class='rail-foot'>kOA</div></nav>"
            "<div class='content'><header class='topbar'>"
            f"<div class='brandline'><img src='{_e(assets)}logo.svg' alt=''><div><strong>kOA Digital Ecosystem</strong>"
            "<small>Centre de pilotage · Publications documentaires</small></div></div>"
            "<div class='topactions'><div class='lang-switch' role='group' aria-label='Langue / Language'>"
            "<button type='button' data-lang='fr' aria-pressed='true'>FR</button>"
            "<button type='button' data-lang='en' aria-pressed='false'>EN</button></div>"
            "<span class='indicator'></span><span id='published-load'>Chargement de la publication</span>"
            "</div></header><main>"
            "<section class='explorer section' id='publication-viewer'"
            f" data-pointer-url='{_e(pointer)}' data-manifest-url='{_e(manifest_url)}'"
            f" data-pages-prefix='{_e(prefix)}'>"
            "<div class='heading'><div><div class='eyebrow'>PUBLICATIONS · SOURCES FIGÉES</div>"
            "<h2>Les applications et leurs documents.</h2>"
            "<p>Sélectionne un dépôt pour consulter ses documents datés. La publication reste stable si le dépôt source change.</p>"
            "</div><div class='results-label'><span id='published-count'>" + str(count) + "</span> dépôts</div></div>"
            "<div class='publication-summary'>"
            "<span>Version : <code id='published-id'>" + _e(manifest['release_id']) + "</code></span>"
            "<span>Publiée (UTC) : <strong id='published-date'>" + stamp + "</strong></span>"
            "<span>Dépôts : <strong id='published-total'>" + str(count) + "</strong></span>"
            "<span>Actualisés : <strong id='published-selected'>" + str(chosen) + "</strong></span>"
            "</div><div class='explorer-grid'>"
            "<div class='directory'><div class='search-wrap'>"
            "<label for='published-repo-search'>Rechercher une application ou un document</label>"
            "<input type='search' id='published-repo-search' placeholder='Kolor, Karacter, README…' autocomplete='off'>"
            "</div><div class='filters' id='published-filters' role='group' aria-label='Filtrer les dépôts'></div>"
            "<div class='repo-list' id='published-repo-list' aria-label='Dépôts publiés'></div></div>"
            "<aside class='detail publication-detail' id='published-detail' aria-live='polite'>"
            "<div class='detail-placeholder'>Sélectionne un dépôt pour voir ses documents figés.</div>"
            "</aside></div></section>"
            "<section class='method-section'><div class='method-icon'>i</div>"
            "<div><strong>Documentation datée, sans certification implicite.</strong>"
            "<p>Cette page consulte une copie approuvée. Les dépôts GitHub peuvent évoluer indépendamment."
            " Les contrôles, tests et qualifications restent distincts des documents publiés.</p></div></section>"
            "</main><footer><span>kOA Digital Ecosystem · kOA Graph</span>"
            "<span>Version figée · publication contrôlée</span></footer></div></div>"
            f"<script defer src='{_e(assets)}i18n.js'></script>"
            f"<script defer src='{_e(assets)}publication-viewer.js'></script></body></html>")


def _publish_from_captures(docs: Path, selection: list[str], mode: str,
                           collector: Callable[[str], Capture], publication_id: str,
                           published_at: str) -> dict:
    if not RELEASE_RE.fullmatch(publication_id):
        raise ValueError("Invalid publication ID")
    releases = docs / "publications" / "releases"
    target = releases / publication_id
    if target.exists():
        raise FileExistsError(f"Release already exists: {publication_id}")
    previous = _load_previous(docs)
    current = {r["repo"]: dict(r) for r in previous["repos"]}
    new_successes = 0
    compiled_graph = None
    compiled_focus = None
    target.mkdir(parents=True)
    try:
        for repo in selection:
            try:
                capture = collector(repo)
                if not capture.documents and not capture.wiki:
                    raise ValueError("No public documentation to publish")
                if capture.repo != repo or not re.fullmatch(r"[0-9a-f]{40}", capture.revision):
                    raise ValueError("Invalid capture provenance")
                docs_list = []
                for kind, collection, rev in (("repo", capture.documents, capture.revision), ("wiki", capture.wiki, capture.wiki_revision)):
                    for rel, text in collection.items():
                        relpath = PurePosixPath(rel)
                        if not _is_document(relpath, wiki=kind == "wiki") or relpath.is_absolute() or ".." in relpath.parts:
                            continue
                        page = _document_path(repo, rel, kind == "wiki")
                        source = _source_url(repo, rev or capture.revision, rel, kind == "wiki")
                        sha, _ = _write_doc(target / page, f"{repo} · {rel}", text, repo, rev or capture.revision, source)
                        docs_list.append({"kind":kind, "path":rel, "page":f"releases/{publication_id}/{page}", "source":source, "sha256":sha})
                        gitbook_file = target / "gitbook" / Path(page).with_suffix(".md")
                        gitbook_file.parent.mkdir(parents=True, exist_ok=True)
                        gitbook_file.write_text(f"<!-- Frozen source: {source} | commit: {rev or capture.revision} | SHA-256: {sha} -->\n\n" + text, encoding="utf-8")
                if repo == "Rejean-McCormick/kOA-Digital-Ecosystem":
                    if capture.graph_registry_text and capture.graph_inventory_text:
                        # Both files are read from the exact same immutable repository SHA.
                        compiled_graph = compile_public_graph(capture.graph_registry_text,
                                                              capture.graph_inventory_text,
                                                              capture.revision)
                    else:
                        # Do not fabricate a graph if owner data was not available.
                        capture.notes.append("Owner graph registry not found; previous public graph unchanged")
                    if capture.graph_focus_text and capture.graph_inventory_text:
                        # Focused paths have their own explicit owner schema and provenance.
                        compiled_focus = compile_focused_paths(capture.graph_focus_text,
                                                               capture.graph_inventory_text,
                                                               capture.revision)
                    else:
                        capture.notes.append("Owner focused paths not found; previous public paths unchanged")
                current[repo] = {"repo":repo, "status":"captured", "revision":capture.revision,
                                 "wiki_revision":capture.wiki_revision, "captured_at":published_at,
                                 "documents":docs_list, "note":"; ".join(capture.notes)}
                new_successes += 1
            except Exception as exc:
                safe_note = f"Collection failed; prior verified copy retained ({type(exc).__name__})"
                if repo in current:
                    current[repo]["status"] = "fallback"
                    current[repo]["note"] = safe_note
                else:
                    current[repo] = {"repo":repo, "status":"unavailable", "revision":None,
                                     "captured_at":None, "documents":[], "note":safe_note}
        if new_successes == 0:
            raise RuntimeError("No selected repository could be captured: public publication not advanced")
        for repo, record in current.items():
            if repo not in selection and record["status"] != "unavailable":
                record["status"] = "retained"
        # GitBook export is a full coherent snapshot even for selected-only publications.
        gitbook_summary = ["# Summary", "", "* [kOA Graph publication](README.md)", ""]
        for name, record in sorted(current.items()):
            for doc in record.get("documents", []):
                page = PurePosixPath(doc["page"])
                # A prior captured doc lives in the archived release directory.
                if len(page.parts) < 4 or page.parts[0] != "releases" or not RELEASE_RE.fullmatch(page.parts[1]):
                    continue
                relative = Path(*page.parts[2:]).with_suffix(".md")
                dest_md = target / "gitbook" / relative
                if not dest_md.exists():
                    source_md = releases / page.parts[1] / "gitbook" / relative
                    if source_md.is_file() and not source_md.is_symlink():
                        dest_md.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copyfile(source_md, dest_md)
                if dest_md.is_file():
                    gitbook_summary.append(f"* [{name} · {doc['path']}]({relative.as_posix()})")
        (target/"gitbook"/"README.md").write_text(f"# kOA Graph — {publication_id}\n\nPublished snapshot: {published_at} UTC. Documentation only, not audit proof.\n", encoding="utf-8")
        (target/"gitbook"/"SUMMARY.md").write_text("\n".join(gitbook_summary)+"\n", encoding="utf-8")
        manifest = {"schema_version":1, "release_id":publication_id, "published_at":published_at,
                    "mode":mode, "selected":selection, "capture_successes":new_successes,
                    "repos": [current[k] for k in sorted(current, key=str.casefold)]}
        # Never publish a pointer to an archive with missing referenced pages.
        for record in manifest["repos"]:
            for document in record.get("documents", []):
                page = PurePosixPath(document["page"])
                if not page.parts or page.parts[0] != "releases" or ".." in page.parts:
                    raise RuntimeError("Invalid archived page reference")
                if not (docs/"publications"/Path(*page.parts)).is_file():
                    raise RuntimeError(f"Missing frozen document page: {page}")
        if compiled_graph is not None:
            # A dated architecture graph is separate from documentary and test evidence.
            graph_body = json.dumps(compiled_graph, ensure_ascii=False, indent=2) + "\n"
            (target/"graph-public.json").write_text(graph_body, encoding="utf-8")
            graph_path = docs/"data"/"graph-public.json"
            graph_path.parent.mkdir(parents=True, exist_ok=True)
            graph_path.write_text(graph_body, encoding="utf-8")
            manifest["owner_graph_commit"] = compiled_graph["owner_commit"]
            manifest["owner_graph_path"] = f"releases/{publication_id}/graph-public.json"
        else:
            # Selected publication leaves the last approved graph untouched.
            existing_graph = docs/"data"/"graph-public.json"
            if existing_graph.is_file():
                existing = json.loads(existing_graph.read_text(encoding="utf-8"))
                if existing.get("format") == "koa.graph.public.v1":
                    manifest["owner_graph_commit"] = existing["owner_commit"]
                    manifest["owner_graph_path"] = None  # retained, not copied
        # Paths and their evidence are published from the same pinned owner commit.
        # Selected-only releases freeze the previously approved graph unchanged.
        focus_file = docs / "data" / "focus-paths.json"
        if compiled_focus is not None:
            focus_body = json.dumps(compiled_focus, ensure_ascii=False, indent=2) + "\n"
            focus_file.parent.mkdir(parents=True, exist_ok=True)
            focus_file.write_text(focus_body, encoding="utf-8")
        elif focus_file.is_file():
            current_focus = json.loads(focus_file.read_text(encoding="utf-8"))
            if current_focus.get("format") != "koa.graph.focus.public.v1":
                raise ValueError("Existing focused graph has an unexpected format")
            focus_body = focus_file.read_text(encoding="utf-8")
        else:
            focus_body = None
        if focus_body is not None:
            (target / "focus-paths.json").write_text(focus_body, encoding="utf-8")
            resolved_focus = json.loads(focus_body)
            manifest["owner_focus_commit"] = resolved_focus["owner_commit"]
            manifest["owner_focus_path"] = f"releases/{publication_id}/focus-paths.json"
        (target/"manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
        (target/"index.html").write_text(_generate_index(manifest, "../../"), encoding="utf-8")
        index = docs/"publications"/"index.html"
        index.write_text(_generate_index(manifest, ""), encoding="utf-8")
        pointer = docs/"data"/"publication-current.json"
        pointer.parent.mkdir(parents=True, exist_ok=True)
        pointer.write_text(json.dumps({"release_id":publication_id, "published_at":published_at,
                                       "mode":mode, "selected":selection}, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
        return manifest
    except Exception:
        shutil.rmtree(target, ignore_errors=True)
        raise


def republish_current(docs: Path) -> dict:
    """Update the public VIEW without collecting or modifying a dated snapshot."""
    pointer = docs / "data" / "publication-current.json"
    payload = json.loads(pointer.read_text(encoding="utf-8"))
    release_id = payload.get("release_id", "")
    if not RELEASE_RE.fullmatch(release_id):
        raise ValueError("Invalid published release pointer")
    manifest = _load_previous(docs)
    if manifest.get("release_id") != release_id:
        raise ValueError("Manifest release does not match current pointer")
    for record in manifest.get("repos", []):
        for document in record.get("documents", []):
            path = PurePosixPath(document["page"])
            if (not path.parts or path.parts[0] != "releases" or
                    ".." in path.parts or not
                    (docs / "publications" / Path(*path.parts)).is_file()):
                raise RuntimeError("Frozen document missing or invalid")
    (docs / "publications" / "index.html").write_text(
        _generate_index(manifest, ""), encoding="utf-8")
    return manifest


def rollback(docs: Path, publication_id: str, now: str) -> dict:
    if not RELEASE_RE.fullmatch(publication_id):
        raise ValueError("Invalid release ID")
    manifest_file = docs/"publications"/"releases"/publication_id/"manifest.json"
    manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    if manifest.get("release_id") != publication_id:
        raise ValueError("Manifest release mismatch")
    for record in manifest.get("repos", []):
        for document in record.get("documents", []):
            page = PurePosixPath(document["page"])
            if ".." in page.parts or not (docs/"publications"/Path(*page.parts)).is_file():
                raise RuntimeError("Archived release has missing or unsafe document pages")
    # Restore the focused graph associated with this archived release, never
    # silently display a newer graph under an older publication pointer.
    focus_target = docs / "data" / "focus-paths.json"
    focus_rel = manifest.get("owner_focus_path")
    if focus_rel:
        part = PurePosixPath(focus_rel)
        if (".." in part.parts or not part.parts or part.parts[0] != "releases"
                or part.parts[1] != publication_id):
            raise RuntimeError("Invalid archived focus graph reference")
        frozen = docs / "publications" / Path(*part.parts)
        if not frozen.is_file() or frozen.is_symlink():
            raise RuntimeError("Missing frozen focused graph")
        payload = json.loads(frozen.read_text(encoding="utf-8"))
        if payload.get("format") != "koa.graph.focus.public.v1":
            raise RuntimeError("Invalid archived focused graph")
        focus_target.parent.mkdir(parents=True, exist_ok=True)
        focus_target.write_bytes(frozen.read_bytes())
    else:
        focus_target.unlink(missing_ok=True)
    (docs/"publications"/"index.html").write_text(_generate_index(manifest, ""), encoding="utf-8")
    pointer = {"release_id":publication_id, "published_at":now, "snapshot_published_at":manifest["published_at"], "rollback":True}
    (docs/"data"/"publication-current.json").write_text(json.dumps(pointer, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    return manifest


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="kOA Graph: public frozen docs publication (manual)")
    p.add_argument("--docs", type=Path, default=Path("docs"))
    p.add_argument("--inventory", type=Path, default=Path("data/initial_inventory.json"))
    p.add_argument("--additions", type=Path, default=Path("config/publication_repositories.json"))
    p.add_argument("--mode", choices=["all", "selected", "rollback", "republish"], default="selected")
    p.add_argument("--repos", default="")
    p.add_argument("--rollback-release", default="")
    p.add_argument("--publication-id", default="")
    args = p.parse_args(argv)
    now = datetime.now(timezone.utc)
    timestamp = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    release_id = args.publication_id or now.strftime("%Y%m%dT%H%M%SZ") + f"-{os.getenv('GITHUB_RUN_ID','0')}-{os.getenv('GITHUB_RUN_ATTEMPT','1')}"
    if args.mode == "republish":
        result = republish_current(args.docs)
    elif args.mode == "rollback":
        result = rollback(args.docs, args.rollback_release, timestamp)
    else:
        allowed = allowed_repositories(args.inventory, args.additions)
        selected = selected_repositories(allowed, args.mode, args.repos)
        result = _publish_from_captures(args.docs, selected, args.mode, capture_public_repository, release_id, timestamp)
    print(json.dumps({"release":result["release_id"], "repos":len(result["repos"]),
                      "captured":result["capture_successes"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
