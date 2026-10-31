"""Offline, private file-tree inventory of dated ZIP snapshots. No certification inference."""
from __future__ import annotations
import hashlib, json, re
from pathlib import Path
BUNDLE = 'KOA-STRUCTURE-SOURCES-2026-10-30.json'
FORMAT = 'koa.private.source_structure.v1'
SHA256 = 'a53858c03d4fb8d1fdfea9d1856e495a80790a7388ef10b9649c4bf2b8689814'

def load(project: Path) -> dict:
    path = Path(project) / 'private_evidence' / BUNDLE
    if not path.is_file() or path.is_symlink() or path.stat().st_size > 7_000_000:
        return {'state':'unavailable','repositories':{}}
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != SHA256:
        return {'state':'unavailable','repositories':{}}
    try:
        data=json.loads(raw)
        if data.get('format') != FORMAT or not isinstance(data.get('repositories'),dict):
            raise ValueError('bad format')
        for key,entry in data['repositories'].items():
            if entry.get('repo') != key or not re.fullmatch(r'[a-f0-9]{64}',entry.get('snapshot_sha256','')):
                raise ValueError('bad repository')
            if len(entry.get('roles',[])) > 15:raise ValueError('too many roles')
            for role in entry['roles']:
                if role['file_count'] != sum(m['file_count'] for m in role['modules']):raise ValueError('bad total')
                for mod in role['modules']:
                    for sample in mod['examples']:
                        p=sample['path']
                        if not re.fullmatch('[a-f0-9]{64}', sample['sha256']) or not p or p.startswith('/') or '..' in p.split('/'):
                            raise ValueError('bad source')
        return {**data,'state':'verified_structure'}
    except (TypeError, ValueError, KeyError, AttributeError):
        return {'state':'unavailable','repositories':{}}

def for_repository(project: Path, repository: str, index: dict | None = None) -> dict:
    index = index if index is not None else load(project)
    return index['repositories'].get(repository,{'state':'not_reviewed','roles':[],'classified_files':0})
