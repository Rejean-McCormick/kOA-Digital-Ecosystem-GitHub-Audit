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
    rows = []
    for r in manifest["repos"]:
        links = []
        for d in r.get("documents", []):
            links.append(f"<li><a href='{_e(prefix + d['page'])}'>{_e(d['path'])}</a> <small>({_e(d['kind'])})</small></li>")
        if not links:
            links = [f"<li><small>{_l('Aucune copie disponible', 'No captured copy')}</small></li>"]
        repo_link = f"https://github.com/{r['repo']}"
        flag = (f"<strong>{_l('↻ Conservé', '↻ Retained')}</strong>" if r["status"] in {"retained", "fallback"} else
                f"<strong>{_l('✓ Capturé', '✓ Captured')}</strong>" if r["status"] == "captured" else
                f"<strong>{_l('— Indisponible', '— Unavailable')}</strong>")
        rows.append("<section class='repository'>"+f"<h2>{_e(r['repo'])}</h2><p>{flag} · <small>{_e(r.get('captured_at') or '—')}</small></p>"
                    + f"<p><a href='{_e(repo_link)}'>{_l('Dépôt source', 'Source repository')}</a> · <code>{_e((r.get('revision') or '—')[:12])}</code></p>"
                    + (f"<p><small>{_e(r['note'])}</small></p>" if r.get('note') else "")
                    + "<ul>"+"".join(links)+"</ul></section>")
    release = manifest["release_id"]
    stats = f"{len(manifest['repos'])} · {len(manifest.get('selected', []))}"
    body = ("<header><p><a href='"+_e(prefix+"../index.html")+"'>kOA Digital Ecosystem</a></p>"
            "<div class='head'><nav><button type='button' id='fr' aria-label='Français'>FR</button> <button type='button' id='en' aria-label='English'>EN</button></nav><h1>kOA Graph — " + _l('Publications datées', 'Published snapshots') + "</h1><p>"
            + _e(manifest['published_at']) + " UTC · <code>"+_e(release)+"</code></p></div>"
            "<p>" + _l('Contenu figé à la publication. Les sources GitHub peuvent évoluer sans changer cette copie.',
                        'Frozen publication. Live GitHub repositories may change without modifying this copy.') + "</p>"
            f"<p><strong>{_e(stats)}</strong> " + _l('dépôts · sélection actualisée', 'repositories · selected refreshed') + "</p></header><main>"+"".join(rows)+"</main>"
            "<footer>" + _l('Copie documentaire, pas une preuve de certification.', 'Documentation copy only, not certification evidence.') + "</footer>")
    style = ("<style>body{background:#f2f7f4;color:#173733;font:15px system-ui;margin:auto;padding:20px;max-width:1250px}"
             "a{color:#166860}header{background:white;border-radius:16px;padding:18px 25px;margin-bottom:16px}"
             "main{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:12px}"
             ".repository{background:white;border:1px solid #d9e6df;border-radius:14px;padding:18px;overflow-wrap:anywhere}"
             ".repository h2{font-size:18px;margin-top:0}.repository ul{padding-left:19px;line-height:1.7}"
             "small,footer{color:#60726b}code{font-size:12px}footer{margin-top:23px}"
             "html[lang=fr] .en,html[lang=en] .fr{display:none}button{padding:7px 12px;background:#e6f3ed;border:1px solid #bfd9cd;border-radius:8px;cursor:pointer}</style>")
    return ("<!doctype html><html lang='fr'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
            "<title>kOA Graph — Published snapshots</title>"+style+"</head><body>"+body+"<script>"
            "const key='koa-graph-ui-language-v1';const q=new URLSearchParams(location.search).get('lang');"
            "function setLanguage(l){if(!['fr','en'].includes(l))return;document.documentElement.lang=l;try{localStorage.setItem(key,l)}catch(e){}}"
            "let initial=q;try{initial=initial||localStorage.getItem(key)}catch(e){}setLanguage(initial||'fr');"
            "document.getElementById('fr').onclick=()=>setLanguage('fr');document.getElementById('en').onclick=()=>setLanguage('en');"
            "</script></body></html>")


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
    (docs/"publications"/"index.html").write_text(_generate_index(manifest, ""), encoding="utf-8")
    pointer = {"release_id":publication_id, "published_at":now, "snapshot_published_at":manifest["published_at"], "rollback":True}
    (docs/"data"/"publication-current.json").write_text(json.dumps(pointer, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    return manifest


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="kOA Graph: public frozen docs publication (manual)")
    p.add_argument("--docs", type=Path, default=Path("docs"))
    p.add_argument("--inventory", type=Path, default=Path("data/initial_inventory.json"))
    p.add_argument("--additions", type=Path, default=Path("config/publication_repositories.json"))
    p.add_argument("--mode", choices=["all", "selected", "rollback"], default="selected")
    p.add_argument("--repos", default="")
    p.add_argument("--rollback-release", default="")
    p.add_argument("--publication-id", default="")
    args = p.parse_args(argv)
    now = datetime.now(timezone.utc)
    timestamp = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    release_id = args.publication_id or now.strftime("%Y%m%dT%H%M%SZ") + f"-{os.getenv('GITHUB_RUN_ID','0')}-{os.getenv('GITHUB_RUN_ATTEMPT','1')}"
    if args.mode == "rollback":
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
