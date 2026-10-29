"""Generate a navigable, source-grounded ecosystem atlas and safe public engineering reports.

The system relationships are curated from the user-provided kOA Digital Ecosystem
owner/contract map (2026-10-29 snapshot). Not inferred from repository names.
Only public repository names and allowlisted engineering measurements are exported.
No local path, raw source, secret, assessment note, or unreviewed qualification
claim is included. The 5 qualification axes are strictly manual.
"""
from __future__ import annotations

import html
import json
import re
from pathlib import Path
from typing import Any
from urllib.parse import quote

from . import profiles

FORMAT = 'koa_ecosystem.atlas.v1'
# A curated conceptual map, NOT a dependency graph or automatically proven integration.
# labels are documented authority boundaries in the official ecosystem overview.
OWNERS = [
    ('Konnaxion', 'Konnaxion', 'Civic decisions', 'civic', 'konnaxion'),
    ('Orgo', 'Orgo', 'Governed work', 'civic', 'orgo'),
    ('EncyKlopedia', 'EncyKlopedia', 'Source acquisition', 'knowledge', 'encyklopedia'),
    ('Da’at', 'Daat', 'Mapping / ACL', 'knowledge', 'daat'),
    ('Kristal', 'Kristal-Framework', 'Epistemic authority', 'knowledge', 'kristal'),
    ('kOA-Linux', 'kOA-Linux-Koali', 'Platform admission', 'platform', 'linux'),
    ('Koali Spaces', 'Koali-Spaces', 'Presentation / shell', 'platform', 'spaces'),
    ('Interaction Kernel', 'Interaction-Kernel', 'Versioned envelopes', 'protocol', 'ik'),
    ('SemantiK Architect', 'SemantiK-Architect', 'Language realization', 'language', 'architect'),
    ('Runtime Orchestrator', 'SemantiK_Runtime_Orchestrator', 'RuntimeSet sequencing', 'language', 'orchestrator'),
    ('SenTient', 'SenTient', 'Candidate resolution', 'knowledge', 'sentient'),
    ('Skope', 'Skope', 'Local scope / recipe', 'knowledge', 'skope'),
]
# Only source-documented flows; proposed != qualified.  Endpoints are model owners
# (not an assertion that their current GitHub repos are already integrated).
CONNECTIONS = [
    {'from':'konnaxion','to':'orgo','label':'Decision profile / governed handoff','status':'documented'},
    {'from':'orgo','to':'daat','label':'Immutable exports, as needed','status':'documented'},
    {'from':'encyklopedia','to':'daat','label':'Evidence / candidate handoff','status':'documented'},
    {'from':'daat','to':'kristal','label':'Kristal-native contract','status':'documented'},
    {'from':'kristal','to':'linux','label':'Runtime Pack / platform admission','status':'documented'},
    {'from':'architect','to':'orchestrator','label':'Owner-preserving release sequencing','status':'documented'},
    {'from':'skope','to':'encyklopedia','label':'Candidate handoff; not qualified','status':'proposed'},
]
SOURCE = 'kOA Digital Ecosystem — docs/1-Overview/index.md, Components.md, Integration.md; snapshot 2026-10-29'
STAGE_IDS = ('specified','implemented','qualified','integrated','production')
STAGE_LABELS = ('Spécifié','Implémenté','Qualifié','Intégré','Production')


def _bounded_nonnegative(v: Any) -> int:
    return min(max(v, 0), 10_000_000_000) if isinstance(v, int) and not isinstance(v, bool) else 0


def _slug(repo: str) -> str:
    name=repo.split('/',1)[-1]
    if not re.fullmatch(r'[A-Za-z0-9_.-]+',name):
        raise ValueError('Nom de dépôt non autorisé')
    return name


def _metrics(project: Path, repo: str) -> dict | None:
    path=profiles.profile_directory(project,repo)/'ENGINEERING_METRICS.json'
    if not path.is_file() or path.is_symlink() or path.stat().st_size > 1_000_000:
        return None
    raw=json.loads(path.read_text(encoding='utf-8-sig'))
    if not isinstance(raw,dict) or raw.get('format') != 'koa_profiles.engineering_metrics.v1' or raw.get('repository') != repo:
        raise ValueError('Profil de mesures incohérent : '+repo)
    counts=raw.get('counts') or {}
    if not isinstance(counts,dict): raise ValueError('Mesures invalides')
    measure={k:_bounded_nonnegative(counts.get(k)) for k in (
        'active_files','source_files','production_source_files','test_source_files','active_docs',
        'production_nonblank_lines','test_nonblank_lines','migration_files','schema_files')}
    langs=raw.get('language_nonblank_lines') or {}
    if not isinstance(langs,dict): raise ValueError('Langages invalides')
    lang_data=[{'language':name,'lines':_bounded_nonnegative(lines)}
               for name,lines in langs.items()
               if isinstance(name,str) and re.fullmatch(r'[A-Za-z0-9 +#./-]{1,38}',name)]
    lang_data=sorted(lang_data,key=lambda x:-x['lines'])[:15]
    allowed_controls={
        'Automated tests','CI configuration','Browser/E2E testing','Linting',
        'Pre-commit hooks','Static typing','Containerization','Architecture decisions',
    }
    controls=[s for s in raw.get('controls_configured',[]) if isinstance(s,str) and s in allowed_controls]
    snap=raw.get('snapshot') or {}
    method=raw.get('method') or {}
    return {'counts':measure,'languages':lang_data,'controls':controls,
            'static_test_declarations':_bounded_nonnegative(raw.get('static_test_declarations')),
            'routes_probable':_bounded_nonnegative(raw.get('routes_probable')),
            'snapshot_index_date':str(snap.get('index_generated_at_local',''))[:32],
            'snapshot_sha256':str(snap.get('sha256','')) if re.fullmatch(r'[0-9a-f]{64}',str(snap.get('sha256',''))) else '',
            'complexity_measured':bool(method.get('complexity_measured',False)),
            'tests_executed':bool(method.get('tests_executed',False)),
            'source_model':'snapshot de code fourni',
            'method':'RepoSurveyor 1.0 — fichiers actifs, hors caches et copies exclues'}


def atlas(project: Path) -> dict:
    inventory=profiles.inventory(project)
    by_short={_slug(r).casefold():r for r in inventory}
    mapped={slug.casefold():(label,role,group,nodeid) for label,slug,role,group,nodeid in OWNERS}
    rows=[]
    for repo in inventory:
        slug=_slug(repo)
        info=mapped.get(slug.casefold())
        metrics=_metrics(project,repo)
        document=profiles.profile_directory(project,repo)/'ENGINEERING_PROFILE.md'
        has_local_profile=document.is_file() and not document.is_symlink() and document.stat().st_size < 2_000_000
        rows.append({'repo':repo,'slug':slug,'name':slug,'has_local_profile':bool(has_local_profile),
            'group':info[2] if info else 'other',
            'role':info[1] if info else 'Dépôt de l’inventaire · responsabilité non cartographiée ici',
            'node_id':info[3] if info else None,
            'engineering':metrics,
            'report':f'engineering/{quote(slug,safe="")}.html' if metrics else None})
    nodes=[]
    for label,short,role,group,nodeid in OWNERS:
        repo=by_short.get(short.casefold())
        if repo:
            nodes.append({'id':nodeid,'label':label,'repo':repo,'group':group,'role':role})
    return {'format':FORMAT,'source':SOURCE,'total':len(inventory),
            'qualifications':'Manual only; local claims not included in this public file',
            'systems':nodes,'links':[v for v in CONNECTIONS
                 if v['from'] in {n['id'] for n in nodes} and v['to'] in {n['id'] for n in nodes}],
            'repositories':rows,
            'groups':[
                {'id':'civic','label':'Civic & workflows'},
                {'id':'knowledge','label':'Knowledge & referents'},
                {'id':'platform','label':'Platform & presentation'},
                {'id':'protocol','label':'Cross-system protocols'},
                {'id':'language','label':'Language & release'},
                {'id':'other','label':'Other repositories (unmapped here)'},
            ]}


def _e(value: Any) -> str:
    return html.escape(str(value),quote=True)


def _f(value: int) -> str:
    return f'{value:,}'.replace(',',' ')


def _profile_html(repo: dict) -> str:
    data=repo['engineering']
    counts=data['counts']
    metrics=[('Fichiers actifs','active_files'),('Fichiers source','source_files'),
             ('Sources de production','production_source_files'),('Sources de tests','test_source_files'),
             ('Documentation active','active_docs'),('Lignes non vides en production','production_nonblank_lines'),
             ('Lignes non vides en tests','test_nonblank_lines'),('Fichiers de migration','migration_files'),
             ('Fichiers de schéma','schema_files')]
    rows=''.join(f'<tr><th>{_e(label)}</th><td>{_f(counts[key])}</td></tr>' for label,key in metrics)
    languages=''.join(f'<tr><th>{_e(row["language"])}</th><td>{_f(row["lines"])}</td></tr>' for row in data['languages'])
    controls=''.join(f'<li>{_e(control)}</li>' for control in data['controls']) or '<li>Non identifié dans les fichiers actifs</li>'
    title=_e(repo['name'])
    back=f"../index.html?app={quote(repo['slug'],safe='')}#apps"
    return f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Engineering Profile — {title}</title>
<link rel="stylesheet" href="../assets/profile-report.css"></head><body><header><a href="{back}">← Retour à la carte kOA</a><span>kOA · ENGINEERING PROFILE</span></header>
<main><div class="eyebrow">RAPPORT D'INGÉNIERIE · SNAPSHOT</div><h1>{title}</h1><p class="lead">Mesures déterministes issues d'un instantané fourni. Ce rapport public reprend les données autorisées du profil complet, sans chemins de fichiers ni contenu source.</p>
<div class="info"><span>Source : {_e(data['source_model'])}</span><span>Capture (heure locale de l’index, fuseau non indiqué) : {_e(data['snapshot_index_date'] or 'Non précisée')}</span><span>Tests exécutés : non</span><span>Complexité cyclomatique : non mesurée</span></div>
<section><h2>Surface d’ingénierie</h2><table>{rows}</table></section><section><h2>Langages</h2><table>{languages}</table><p>« Lignes non vides » n’est pas une mesure de code pur et peut inclure des commentaires.</p></section>
<section><h2>Surface de vérification</h2><div class="large">{_f(data['static_test_declarations'])}</div><p>Déclarations de tests détectées statiquement; ni exécutées ni attestées réussies.</p><div class="large">{_f(data['routes_probable'])}</div><p>Routes HTTP probables; détection heuristique.</p></section>
<section><h2>Outillage configuré / détecté</h2><ul>{controls}</ul><p>La présence d’un outil ne prouve pas une exécution réussie.</p></section>
<section><h2>Provenance & limites</h2><p>{_e(data['method'])}</p><p>Empreinte du snapshot (SHA-256) : <code>{_e(data['snapshot_sha256'])}</code></p><p>Les fichiers privés, caches, sauvegardes et copies hors périmètre ont été exclus. Ni le projet ni ses CI n'ont été exécutés. Ceci n'est ni une certification, ni une appréciation de la qualité ou de la complétion.</p></section>
<a class="back" href="{back}">← Revenir aux applications</a></main></body></html>'''


def build_public_atlas(project: Path, docs: Path | None = None) -> dict:
    """Rebuild only our own public-safe generated atlas and report pages."""
    project=Path(project)
    docs=Path(docs) if docs is not None else project/'docs'
    payload=atlas(project)
    target=docs/'data'/'ecosystem.json'
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(payload,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    report_dir=docs/'engineering';report_dir.mkdir(exist_ok=True)
    count=0
    for repo in payload['repositories']:
        if repo['engineering']:
            (report_dir/f"{repo['slug']}.html").write_text(_profile_html(repo),encoding='utf-8')
            count+=1
    return {'repos':payload['total'],'profiles':count,'location':str(target)}
