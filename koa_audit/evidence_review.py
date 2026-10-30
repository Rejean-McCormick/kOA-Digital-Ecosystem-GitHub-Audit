"""Offline historical evidence review (49 repositories x 5 stages).

The review is PRIVATE input supplied by the owner, not an authority for
automatic certification. No source repository, public docs or Git is written.
"""
from __future__ import annotations

import hashlib
import html
import json
import os
import tempfile
import re
import zipfile
from pathlib import Path
from urllib.parse import quote

from . import qualification, profiles

FORMAT = 'koa.evidence_review.v1'
ARCHIVE_NAME = 'KOA-REVUE-2026-10-30.zip'
SOURCE_MARKER = 'KOA-REVUE-2026-10-30'
MAX_ARCHIVE_BYTES = 8 * 1024 * 1024
MAX_MEMBER_BYTES = 3 * 1024 * 1024
SLUG = re.compile(r'[A-Za-z0-9_.-]{1,120}\Z')


def persistent_archive_path() -> Path:
    base = Path(os.environ.get('LOCALAPPDATA') or (Path.home() / '.local' / 'share'))
    return base / 'kOA-GitHub-Audit' / 'evidence_reviews' / ARCHIVE_NAME


def archive_path(project: Path) -> Path:
    bundled = Path(project) / 'private_evidence' / ARCHIVE_NAME
    return bundled if bundled.is_file() else persistent_archive_path()


def preserve_review_locally(project: Path) -> Path:
    """Persist an immutable private copy outside the upgraded application directory."""
    source = archive_path(project)
    if not source.is_file():
        raise FileNotFoundError('Bibliothèque historique introuvable')
    load_review(project)  # Check schema, index, SHA of the inventory.
    target = persistent_archive_path()
    if source.resolve() == target.resolve():
        return target
    target.parent.mkdir(parents=True, exist_ok=True)
    with source.open('rb') as f:
        raw = f.read(MAX_ARCHIVE_BYTES + 1)
    if len(raw) > MAX_ARCHIVE_BYTES:
        raise ValueError('Bibliothèque privée trop volumineuse')
    if target.exists():
        if hashlib.sha256(target.read_bytes()).digest() != hashlib.sha256(raw).digest():
            raise ValueError('Une autre bibliothèque est déjà préservée; aucune ancienne version écrasée')
        return target
    fd, temporary = tempfile.mkstemp(prefix='koa-review-', suffix='.tmp', dir=target.parent)
    try:
        with os.fdopen(fd, 'wb') as out:
            out.write(raw)
            out.flush(); os.fsync(out.fileno())
        # Publish without ever replacing a pre-existing immutable review.
        try:
            os.link(temporary, target)
        except FileExistsError:
            if hashlib.sha256(target.read_bytes()).digest() != hashlib.sha256(raw).digest():
                raise ValueError('Revue privée concurrente différente, aucune version écrasée')
        except OSError:
            if os.name == 'nt' and not target.exists():
                os.rename(temporary, target)  # Windows rename fails if target exists.
            else:
                raise
    finally:
        Path(temporary).unlink(missing_ok=True)
    return target


def _read_member(z: zipfile.ZipFile, member: str, manifest: dict) -> bytes:
    if member not in manifest:
        raise ValueError('Source sans empreinte de provenance')
    item = z.getinfo(member)
    if item.file_size > MAX_MEMBER_BYTES or item.file_size < 0:
        raise ValueError('Source trop volumineuse')
    raw = z.read(member)
    if hashlib.sha256(raw).hexdigest() != manifest[member]:
        raise ValueError('Empreinte de source différente du manifeste')
    return raw


def _open(project: Path):
    path = archive_path(project)
    if not path.is_file() or path.is_symlink() or path.stat().st_size > MAX_ARCHIVE_BYTES:
        raise FileNotFoundError('Revue historique privée absente du dossier private_evidence')
    return zipfile.ZipFile(path)


def load_review(project: Path) -> dict:
    """Check the indexed review and the SHA of the whole source set on demand."""
    with _open(project) as z:
        manifest = json.loads(z.read('MANIFEST_SHA256.json'))
        if manifest.get('format') != 'koa.evidence_review.manifest.v1':
            raise ValueError('Manifeste de preuves inattendu')
        sha = manifest['sha256']
        raw = _read_member(z, 'data/review-49.json', sha)
        review = json.loads(raw)
        entries = review.get('repositories')
        if review.get('format') != FORMAT or not isinstance(entries, list) or len(entries) != 49:
            raise ValueError('La revue doit contenir les 49 dossiers officiels')
        known = set(profiles.inventory(project))
        if {r.get('repository') for r in entries} != known:
            raise ValueError('La revue ne correspond pas au registre officiel des 49')
        for r in entries:
            stages = r.get('stages')
            if not isinstance(stages, list) or len(stages) != len(qualification.STAGES) or {s.get('stage') for s in stages} != set(qualification.STAGE_IDS):
                raise ValueError('Cinq jalons attendus pour chaque dépôt')
        return review


def repo_record(project: Path, repo: str) -> dict:
    canonical = profiles.repo_key(repo, project)
    return next(r for r in load_review(project)['repositories'] if r['repository'] == canonical)


def stage_record(project: Path, repo: str, stage: str) -> dict:
    if stage not in qualification.STAGE_IDS:
        raise ValueError('Jalon inconnu')
    return next(s for s in repo_record(project, repo)['stages'] if s['stage'] == stage)


def source_reference(project: Path, repo: str, stage: str, index: int) -> dict:
    st = stage_record(project, repo, stage)
    sources = st.get('sources') or []
    if not 0 <= index < len(sources):
        raise ValueError('Référence de source absente')
    name = sources[index]
    if not isinstance(name, str) or len(name) > 260 or '\\' in name or name.startswith('/') or '..' in Path(name).parts:
        raise ValueError('Référence de source non reconnue')
    with _open(project) as z:
        manifest = json.loads(z.read('MANIFEST_SHA256.json'))['sha256']
        if name not in manifest:
            # Some historical external audit references deliberately have no archived copy.
            return {'source': name, 'available': False, 'sha256': None}
        return {'source': name, 'available': True, 'sha256': manifest[name]}


def read_source(project: Path, repo: str, stage: str, index: int) -> tuple[dict, bytes]:
    ref = source_reference(project, repo, stage, index)
    if not ref['available']:
        raise FileNotFoundError('Document source non fourni dans cette revue historique')
    with _open(project) as z:
        manifest = json.loads(z.read('MANIFEST_SHA256.json'))['sha256']
        return ref, _read_member(z, ref['source'], manifest)


def suggested_qualification(project: Path, repo: str, stage: str) -> dict:
    """Form prefill only; leaves state Non évalué until explicit human action."""
    record = stage_record(project, repo, stage)
    candidates = [source_reference(project, repo, stage, i)
                  for i in range(len(record.get('sources') or []))]
    present = [ref for ref in candidates if ref['available']]
    if present:
        primary = present[0]
        evidence = f"{SOURCE_MARKER} :: {primary['source']} :: SHA-256 {primary['sha256']}"
    else:
        evidence = f"{SOURCE_MARKER} :: source à compléter ; aucune pièce directement consultable pour ce jalon"
    return {'repository': profiles.repo_key(repo, project), 'stage': stage,
            'status': 'Non évalué', 'scope': str(record.get('scope', ''))[:300],
            'evidence': evidence[:1500], 'source_available': bool(present)}


def report_counts(project: Path) -> dict:
    entries = load_review(project)['repositories']
    counts = {}
    for _, title in qualification.STAGES:
        counts[title] = 0
    for repo in entries:
        for stage in repo['stages']:
            if stage.get('sources'):
                title = next(t for k, t in qualification.STAGES if k == stage['stage'])
                counts[title] += 1
    return {'repositories': len(entries), 'cases': len(entries)*5,
            'source_references_by_stage': counts,
            'notice': 'Sources historiques à examiner ; aucun jalon qualifié automatiquement.'}


def _page(title: str, content: str) -> str:
    return ("<!doctype html><html lang='fr'><head><meta charset='utf-8'>"
            "<meta name='viewport' content='width=device-width,initial-scale=1'>"
            '<title>'+html.escape(title)+'</title><style>'
            ':root{font-family:Segoe UI,Arial,sans-serif;color:#183b39;background:#f4f7f7}'
            'body{max-width:1100px;margin:auto;padding:28px}a{color:#1e6864}'
            'header{display:flex;justify-content:space-between;align-items:center;gap:12px}'
            'nav a{margin-right:12px}h1{font-size:30px}h2{font-size:20px}'
            '.panel{background:white;border:1px solid #dae6e4;border-radius:12px;padding:20px;margin:14px 0}'
            '.muted{color:#566d69}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px}'
            '.tag{font-size:12px;padding:5px 9px;background:#edf4f2;border-radius:20px;display:inline-block}'
            'li{margin:7px 0}pre{white-space:pre-wrap;overflow-wrap:anywhere;max-height:65vh;overflow:auto}'
            '.actions a{display:inline-block;margin:5px 9px 5px 0}.track{height:9px;background:#e0ebe8;border-radius:8px;overflow:hidden}'
            '.fill{height:100%;background:#1e6864}table{border-collapse:collapse;width:100%;background:white}'
            'th,td{padding:11px;border-bottom:1px solid #e1eae8;text-align:left}'
            '</style></head><body><header><strong>kOA · REVUE HISTORIQUE PRIVÉE</strong>'
            '<nav><a href="/index.html">Centre de pilotage</a><a href="/local/review">49 applications</a>'
            '<a href="/local/campaigns">Campagnes</a></nav></header>'+content+'</body></html>')


def render_page(project: Path, route: str) -> str:
    parts = route.strip('/').split('/')
    if parts[:2] != ['local', 'review']:
        raise ValueError('Route de revue invalide')
    data = load_review(project)
    if len(parts) == 2:
        from . import evidence_adjudication
        totals = evidence_adjudication.current_summary(project)
        rows = []
        for r in data['repositories']:
            slug = r['repository'].split('/', 1)[-1]
            source_stages = sum(bool(s.get('sources')) for s in r['stages'])
            rows.append('<tr><td><a href="/local/review/app/'+quote(slug)+'">'+html.escape(slug)+'</a></td>'
                        '<td>'+str(source_stages)+'/5 jalons avec références documentaires</td>'
                        '<td>'+('Profil mesuré' if r.get('engineering_profile') else 'Profil non fourni')+'</td></tr>')
        return _page('Revue des 245 dossiers',
                     '<h1>Les 245 dossiers de preuve historique</h1>'
                     '<p class="muted">Sources datées 2026-09-21 à 2026-10-30. Les références documentaires seules ne prouvent pas une qualification globale. '
                     f"{totals['evidenced']} jalons sont étayés à portée LIMITÉE dans le registre local, "
                     f"{totals['to_document']} sont à documenter, {totals['unreviewed']} non évalués. "
                     "Aucune preuve de production dans ce lot.</p>"
                     '<div class="panel"><strong>49 applications · 5 jalons chacune</strong> · '
                     "Conclusions documentaires inscrites sans écraser les décisions existantes. "
                     "Pour conserver ces conclusions dans l'historique, créer une NOUVELLE campagne datée.</div>"
                     '<table><tr><th>Application</th><th>Références par jalon</th><th>Ingénierie</th></tr>'+
                     ''.join(rows)+'</table>')
    if len(parts) >= 4 and parts[2] == 'app' and SLUG.fullmatch(parts[3]):
        slug = parts[3]
        repo = next((r for r in data['repositories'] if r['repository'].split('/')[-1] == slug), None)
        if repo is None:
            raise ValueError('Dépôt non documenté')
        if len(parts) == 4:
            blocks = []
            for s in repo['stages']:
                target = '/local/review/app/'+quote(slug)+'/'+s['stage']
                blocks.append('<div class="panel"><h2><a href="'+target+'">'+html.escape(s['title'])+'</a></h2>'
                              '<span class="tag">'+html.escape(s['evidence_level'])+'</span><p>'+
                              html.escape(s['summary'])+'</p><p class="muted">'+
                              str(len(s.get('sources', [])))+' références · Conclusion documentaire : '+
                              html.escape(qualification.get_claim(project,repo['repository'],s['stage'])['status'])+
                              '</p></div>')
            sha = repo.get('local_audit_commit') or ''
            link = ('<a href="https://github.com/'+html.escape(repo['repository'])+'/archive/'+sha+'.zip" '
                    'target="_blank" rel="noopener noreferrer">Télécharger le ZIP GitHub du commit observé</a>'
                    if re.fullmatch(r'[0-9a-fA-F]{40}', sha) else '')
            return _page('Revue · '+slug, '<h1>'+html.escape(slug)+'</h1>'
                         '<p class="muted">Commit observé lors de l’audit : <code>'+html.escape(sha or 'inconnu')+
                         '</code> · Ne prouve pas que tous les documents portent sur ce commit. '+link+'</p>'
                         '<div class="grid">'+''.join(blocks)+'</div>')
        if len(parts) == 5 and parts[4] in qualification.STAGE_IDS:
            stage_id = parts[4]
            s = next(x for x in repo['stages'] if x['stage'] == stage_id)
            from . import evidence_adjudication
            resolution = evidence_adjudication.decision(project,repo['repository'],stage_id)
            state = qualification.get_claim(project,repo['repository'],stage_id)
            expert_link = ('<a href="/local/review/app/'+quote(slug)+'/'+stage_id+'/expert">'+
                'Ouvrir le document primaire relu avec SHA-256</a>' if resolution.get('source') else '')
            sources = []
            for i, path in enumerate(s['sources']):
                ref = source_reference(project, repo['repository'], stage_id, i)
                if ref['available']:
                    sources.append('<li><a href="/local/review/app/'+quote(slug)+'/'+stage_id+'/source/'+str(i)+'">'+
                                   html.escape(path)+'</a> <small>SHA-256 '+html.escape(ref['sha256'][:16])+'…</small></li>')
                else:
                    sources.append('<li>'+html.escape(path)+' <span class="tag">Référence externe non incluse</span></li>')
            return _page('Preuve · '+slug+' · '+stage_id,
                         '<p><a href="/local/review/app/'+quote(slug)+'">← Fiche '+html.escape(slug)+'</a></p>'
                         '<h1>'+html.escape(slug)+' · '+html.escape(s['title'])+'</h1>'
                         '<div class="panel"><h2>Conclusion documentaire du 30 octobre 2026</h2>'
                         '<span class="tag">'+html.escape(state['status'])+'</span>'
                         '<p><strong>Portée retenue :</strong> '+html.escape(state['scope'])+'</p>'
                         '<p><strong>Référence :</strong> '+html.escape(state['evidence'])+'</p>'
                         '<p>'+html.escape(resolution['explanation'])+'</p>'+expert_link+'</div>'
                         '<div class="panel"><span class="tag">'+html.escape(s['evidence_level'])+'</span>'
                         '<h2>Ce que la source indique</h2><p>'+html.escape(s['summary'])+'</p>'
                         '<h2>Portée</h2><p>'+html.escape(s['scope'])+'</p>'
                         '<h2>Limites</h2><p>'+html.escape(s['limitations'])+'</p>'
                         '<h2>Prochaine action</h2><p>'+html.escape(s['next_action'])+'</p>'
                         '</div><div class="panel"><h2>Pièces et références</h2><ul>'+(''.join(sources) or '<li>Aucune pièce de cette portée fournie.</li>')+
                         '</ul><p class="muted">Les sources sont consultables ici. Les décisions documentaires sont inscrites dans le registre local et restent limitées à la portée décrite.</p></div>')
        if (len(parts) == 6 and parts[4] in qualification.STAGE_IDS and parts[5] == 'expert'):
            from . import evidence_adjudication
            adjudication = evidence_adjudication.decision(project,repo['repository'],parts[4])
            source = adjudication.get('source')
            if not source:
                raise FileNotFoundError('Aucune pièce primaire probante dans la revue datée pour ce jalon')
            with _open(project) as bundle:
                manifest = json.loads(bundle.read('MANIFEST_SHA256.json'))['sha256']
                raw = _read_member(bundle,source['member'],manifest)
            if hashlib.sha256(raw).hexdigest() != source['sha256']:
                raise ValueError('Empreinte documentaire divergente')
            try:
                body=raw.decode('utf-8-sig')
            except UnicodeDecodeError:
                raise ValueError('Pièce non textuelle')
            return _page('Preuve étudiée · '+slug,
                '<p><a href="/local/review/app/'+quote(slug)+'/'+parts[4]+'">← Revenir au jalon</a></p>'
                '<h1>Source primaire lue et vérifiée</h1><p>'+html.escape(source['member'])+'</p>'
                '<p class="muted">SHA-256 : '+html.escape(source['sha256'])+
                '. Source historique, pas de correspondance avec le commit actuel attestée.</p>'
                '<div class="panel"><pre>'+html.escape(body)+'</pre></div>')
        if (len(parts) == 7 and parts[4] in qualification.STAGE_IDS and parts[5] == 'source'
                and parts[6].isdigit()):
            ref, raw = read_source(project, repo['repository'], parts[4], int(parts[6]))
            try:
                body = raw.decode('utf-8-sig')
            except UnicodeDecodeError:
                raise ValueError('Document non textuel non prévisualisable')
            return _page('Source originale · '+slug, '<p><a href="/local/review/app/'+quote(slug)+'/'+parts[4]+'">← Revenir au jalon</a></p>'
                         '<h1>Document source archivé</h1><p>'+html.escape(ref['source'])+'</p>'
                         '<p class="muted">SHA-256 : <code>'+html.escape(ref['sha256'])+'</code>. '
                         'Affichage texte : le contenu du document n’est jamais exécuté.</p>'
                         '<div class="panel"><pre>'+html.escape(body)+'</pre></div>')
    raise ValueError('Document ou jalon de revue introuvable')
