"""Dated, source-checked *documentary* assessment explicitly requested by the owner.

No tests run, no cross-commit attribution, no security grade. The 245 rows
record the scope of the supplied evidence, not the health of the 49 products.
Unreviewed/user-edited registry entries are never replaced without consent.
"""
from __future__ import annotations

import hashlib
import json
import os
import tempfile
import zipfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from . import evidence_review, profiles, qualification

NAME = "KOA-ADJUDICATION-2026-10-30.json"
FORMAT = "koa.expert_adjudication.v1"
SOURCE_MARKER = "KOA-REVUE-2026-10-30"
MAX_SIZE = 700_000


def _source(project: Path) -> Path:
    return Path(project) / "private_evidence" / NAME


def load(project: Path) -> dict:
    path = _source(project)
    if path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_SIZE:
        raise ValueError("Décisions documentaires privées absentes ou trop volumineuses")
    data = json.loads(path.read_text(encoding="utf-8"))
    entries = data.get("cases")
    if data.get("format") != FORMAT or not isinstance(entries, list) or len(entries) != 245:
        raise ValueError("Le registre documentaire doit contenir 245 dossiers")
    review = evidence_review.load_review(project)
    known = {(r['repository'], s['stage']) for r in review['repositories'] for s in r['stages']}
    if len(known) != 245 or {(v['repository'], v['stage']) for v in entries} != known:
        raise ValueError("Les dossiers ne correspondent pas à la revue source")
    source_zip = evidence_review.archive_path(project)
    if hashlib.sha256(source_zip.read_bytes()).hexdigest() != data.get("source_review_archive_sha256"):
        raise ValueError("La revue utilisée pour qualifier a changé : import refusé")
    with zipfile.ZipFile(source_zip) as archive:
        sha = json.loads(archive.read('MANIFEST_SHA256.json'))['sha256']
        for entry in entries:
            if entry.get('status') not in ('Étayé par preuve', 'À documenter'):
                raise ValueError('Statut documentaire invalide')
            if not isinstance(entry.get('scope'), str) or not entry['scope'] or len(entry['scope']) > 300:
                raise ValueError('Portée documentaire invalide')
            src = entry.get('source')
            if entry['status'] == 'Étayé par preuve':
                if not isinstance(src,dict) or src.get('member') not in sha:
                    raise ValueError('Conclusion étayée sans source originale')
                member = src['member']
                if sha[member] != src.get('sha256'):
                    raise ValueError('Empreinte du document de qualification divergente')
                original = archive.read(member)
                if hashlib.sha256(original).hexdigest() != sha[member]:
                    raise ValueError('Document probant altéré')
                if entry.get('version_alignment') != 'not_attested':
                    raise ValueError('Aucun SHA Git exact ne peut être imputé à ce document')
            elif src is not None:
                raise ValueError('Source probante attachée à un statut insuffisant')
    counts = Counter(x['status'] for x in entries)
    if counts != {'Étayé par preuve':10, 'À documenter':235}:
        raise ValueError('Le bilan documentaire daté ne correspond pas aux 245 conclusions')
    return data


def current_summary(project: Path, path: Path | None = None) -> dict:
    claims = qualification.load_state(path)['claims']
    inventory = profiles.inventory(project)
    counts = Counter((claims.get(repo,{}).get(stage,{}) or {}).get('status','Non évalué')
                     for repo in inventory for stage in qualification.STAGE_IDS)
    return {'total':245, 'evidenced':counts['Étayé par preuve'],
            'to_document':counts['À documenter'], 'unreviewed':counts['Non évalué'],
            'not_applicable':counts['Non applicable']}


def import_documentary_review(project: Path, path: Path | None = None) -> dict:
    """One-time merge of owner-requested assessment; never overwrite ANY existing stage.

    A real file, once present, gets a separate backup before it is changed.
    All primary evidence is validated before any write. Atomic write on same disk.
    """
    data = load(project)
    path = Path(path) if path else qualification.state_path()
    state = qualification.load_state(path)
    original = path.read_bytes() if path.is_file() else None
    fresh = 0
    preserved = 0
    stamp = datetime.now(timezone.utc).isoformat(timespec='seconds')
    for entry in data['cases']:
        repo, stage = entry['repository'], entry['stage']
        per_repo = state['claims'].setdefault(repo, {})
        if stage in per_repo:  # Even a previously saved 'Non évalué' may be intentional.
            preserved += 1
            continue
        src = entry.get('source')
        if src:
            evidence = (SOURCE_MARKER + ' :: REVUE DOCUMENTAIRE DU 2026-10-30 :: '
                + src['member'] + ' :: SHA-256 ' + src['sha256']
                + ' :: source historique, commit des clones NON établi. '
                + entry['explanation'])
        else:
            evidence = (SOURCE_MARKER + ' :: REVUE DOCUMENTAIRE DU 2026-10-30 :: '
                + entry['observed_documentary_level'] + ' :: ' + entry['original_summary']
                + ' :: ' + entry['explanation'])
        per_repo[stage] = {
            'status':entry['status'], 'scope':entry['scope'][:300],
            'evidence':evidence[:1500], 'reviewed_at':stamp,
            'adjudication_origin':'source-bounded-documentary-review-2026-10-30',
            'source_revision':'2026-10-30',
        }
        fresh += 1
    if fresh:
        path.parent.mkdir(parents=True,exist_ok=True)
        if original is not None:
            backup = path.with_name(path.name+'.before-documentary-review-20261030.bak')
            if not backup.exists():
                # Create-only; no prior backup is replaced.
                with backup.open('xb') as stream:
                    stream.write(original)
                    stream.flush(); os.fsync(stream.fileno())
        fd,tmp=tempfile.mkstemp(prefix='koa-review-merge-',suffix='.tmp',dir=path.parent)
        try:
            with os.fdopen(fd,'w',encoding='utf-8') as stream:
                json.dump(state,stream,ensure_ascii=False,sort_keys=True,indent=2)
                stream.write('\n');stream.flush();os.fsync(stream.fileno())
            Path(tmp).replace(path)
        finally:
            Path(tmp).unlink(missing_ok=True)
    return {'added':fresh, 'preserved':preserved, 'totals':current_summary(project,path),
            'source_review':'2026-10-30', 'new_campaign_required':bool(fresh)}


def decision(project:Path, repo:str, stage:str)->dict:
    qualification._validate_repo(project,repo)
    if stage not in qualification.STAGE_IDS:
        raise ValueError('Jalon inconnu')
    return next(x for x in load(project)['cases'] if x['repository']==repo and x['stage']==stage)
