"""Locally bundled, source-attributed functional specifications.

The bundle is a static review of user-provided ZIP snapshots. Presence of source
or a test *definition* is never treated as a successful test execution. No
network, Git operation, code execution, or mutation of repositories.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

FORMAT = 'koa.private.specsheets.snapshot.v1'
BUNDLE = 'KOA-SPECSHEETS-2026-10-30.json'
SHA256 = '7870986ddebebef693cb0abc3d50f6bc99e254ff090a2ad473d4de906e14d4c0'
ALLOWED_STATUSES = {'code_observed', 'specification_only'}


def load(project: Path) -> dict:
    """Fail closed if the reviewed source index is missing or altered."""
    path = Path(project) / 'private_evidence' / BUNDLE
    empty = {'format': FORMAT, 'repositories': {}, 'state': 'unavailable'}
    if not path.is_file() or path.is_symlink() or path.stat().st_size > 500_000:
        return empty
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != SHA256:
        return empty
    try:
        data = json.loads(raw)
        if data.get('format') != FORMAT or not isinstance(data.get('repositories'), dict):
            return empty
        for key, item in data['repositories'].items():
            if not isinstance(key, str) or not isinstance(item, dict) or item.get('repo') != key:
                return empty
            if not re.fullmatch('[a-f0-9]{64}', item.get('snapshot_sha256', '')):
                return empty
            if item.get('snapshot_commit') is not None or item.get('tests_executed') is not False:
                return empty
            for name in ('features', 'technical'):
                if not isinstance(item.get(name), list) or len(item[name]) > 75:
                    return empty
                for row in item[name]:
                    if row.get('status') not in ALLOWED_STATUSES or row.get('execution_verified') is not False:
                        return empty
                    for group in ('sources', 'test_definitions'):
                        for source in row.get(group, []):
                            if not re.fullmatch('[a-f0-9]{64}', source.get('sha256', '')):
                                return empty
                            path_text = source.get('path', '')
                            if not path_text or path_text.startswith('/') or '..' in path_text.split('/'):
                                return empty
        return {**data, 'state': 'verified_index'}
    except (ValueError, KeyError, TypeError, AttributeError):
        return empty


def for_repository(project: Path, repo: str, index: dict | None = None) -> dict:
    index = index if index is not None else load(project)
    row = index['repositories'].get(repo)
    if not row:
        return {
            'state': 'not_reviewed', 'overview': '', 'features': [], 'technical': [],
            'notice': 'Pas de snapshot fonctionnel examiné pour ce dépôt. Ce n’est ni une absence de fonctionnalités ni un échec.'
        }
    return {
        'state': 'snapshot_reviewed', 'overview': row['overview'],
        'snapshot': row['snapshot'], 'snapshot_sha256': row['snapshot_sha256'],
        'snapshot_commit': None, 'features': row['features'], 'technical': row['technical'],
        'notice': 'Code et tests présents dans le snapshot; aucun résultat d’exécution ni SHA Git du snapshot attesté.',
        'verified_execution_count': 0,
    }
