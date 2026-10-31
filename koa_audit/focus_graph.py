"""Compile the owner-maintained kOA Graph focused paths from one pinned Git revision.

Architecture paths are descriptive and scope-limited. Never infer deployment,
validation or execution permissions from a diagram edge.
"""
from __future__ import annotations

import hashlib
import json
import re

OWNER = 'Rejean-McCormick/kOA-Digital-Ecosystem'
REPO_RE = re.compile(r'^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$')
ID_RE = re.compile(r'^[a-z][a-z0-9_-]{1,63}$')
SHA_RE = re.compile(r'^[a-f0-9]{40}$')
PATH_RE = re.compile(r'^(?:docs/|doc/|documentation/)[A-Za-z0-9_. /-]+\.(?:md|mdx|txt|rst|adoc)$|^README\.md$')
STATES = frozenset({'qualified_local', 'implemented_owner', 'documented', 'candidate', 'optional'})
KINDS = frozenset({'application', 'protocol', 'artifact', 'interface'})


def _languages(value, where: str):
    if not isinstance(value, dict) or set(value) != {'fr', 'en'}:
        raise ValueError(f'{where}: expected exact fr/en labels')
    for lang, label in value.items():
        if not isinstance(label, str) or not 0 < len(label.strip()) <= 320:
            raise ValueError(f'{where}: missing/oversized {lang} label')


def _source(src, valid_repos, where):
    if not isinstance(src, dict) or set(src) != {'repo', 'path'}:
        raise ValueError(f'{where}: evidence source missing')
    repo, path = src['repo'], src['path']
    if repo not in valid_repos or not isinstance(path, str):
        raise ValueError(f'{where}: source outside official public inventory')
    if ('..' in path.split('/') or '\\' in path or not PATH_RE.fullmatch(path)
            or '//' in path or path.startswith('/')):
        raise ValueError(f'{where}: unsafe evidence path')


def compile_focused_paths(source_text: str, inventory_text: str, source_commit: str) -> dict:
    """Fail closed for malformed IDs, dangling links and untrusted source references."""
    if not SHA_RE.fullmatch(source_commit):
        raise ValueError('Must pin source to the actual immutable Git commit')
    source = json.loads(source_text)
    inventory = json.loads(inventory_text)
    if (not isinstance(source, dict) or source.get('format') != 'koa.graph.focus.v1'
            or source.get('owner_repository') != OWNER
            or source.get('reference_inventory') != 'docs/inventory/repositories.json'):
        raise ValueError('Unexpected owner focused-path schema')
    if not isinstance(inventory, list) or len(inventory) != 49:
        raise ValueError('Unexpected reference inventory size')
    repos = set()
    for item in inventory:
        if not isinstance(item, dict) or item.get('scope') != 'PUBLIC':
            raise ValueError('Only explicitly public inventory entries are admissible')
        repo = item.get('github_repo')
        if not isinstance(repo, str) or not REPO_RE.fullmatch(repo) or repo in repos:
            raise ValueError('Invalid or duplicate reference repository')
        repos.add(repo)
    _languages(source.get('notice'), 'notice')
    paths = source.get('paths')
    if not isinstance(paths, list) or not (1 <= len(paths) <= 12):
        raise ValueError('Expected a bounded set of paths')
    seen_paths = set()
    for path in paths:
        if not isinstance(path, dict) or not isinstance(path.get('id'), str) or not ID_RE.fullmatch(path['id']) or path['id'] in seen_paths:
            raise ValueError('Invalid or duplicate path')
        seen_paths.add(path['id'])
        for key in ('title', 'summary'):
            _languages(path.get(key), f'{path["id"]}/{key}')
        spine = path.get('spine')
        links = path.get('spine_links')
        branches = path.get('branches')
        if (not isinstance(spine, list) or not 3 <= len(spine) <= 7
                or not isinstance(links, list) or len(links) != len(spine)-1
                or not isinstance(branches, list) or len(branches) > 12):
            raise ValueError(f'{path["id"]}: invalid path geometry')
        used_ids = set()
        def check_node(node):
            if not isinstance(node, dict) or not isinstance(node.get('id'), str) or not ID_RE.fullmatch(node['id']):
                raise ValueError('Invalid node ID')
            if node['id'] in used_ids:
                raise ValueError('Node ID duplicated within path')
            used_ids.add(node['id'])
            _languages(node.get('label'), 'node label')
            _languages(node.get('description'), 'node description')
            if node.get('kind') not in KINDS:
                raise ValueError('Unknown node kind')
            repo = node.get('repo')
            if repo is not None and repo not in repos:
                raise ValueError('Node references a repository outside the explicit inventory')
            if node['kind'] in ('application', 'protocol') and repo is None:
                raise ValueError('Application/protocol node must identify its owner repository')
        for node in spine:
            check_node(node)
        for i, link in enumerate(links):
            if link.get('from') != spine[i]['id'] or link.get('to') != spine[i+1]['id']:
                raise ValueError('Spine links must follow the declared main path, without shortcuts')
            _languages(link.get('label'), 'spine edge label')
            _source(link.get('evidence'), repos, 'spine link')
            if link.get('status') not in STATES:
                raise ValueError('Unknown edge status')
            if not isinstance(link.get('contract'), str) or len(link['contract']) > 180:
                raise ValueError('Invalid contract label')
        used_branches = set()
        for branch in branches:
            if not isinstance(branch, dict) or not isinstance(branch.get('id'), str) or not ID_RE.fullmatch(branch['id']) or branch['id'] in used_branches:
                raise ValueError('Invalid or duplicate branch')
            used_branches.add(branch['id'])
            if not isinstance(branch.get('anchor'), int) or isinstance(branch.get('anchor'),bool) or not 0 <= branch['anchor'] < len(spine):
                raise ValueError('Invalid branch anchor')
            if branch.get('side') not in ('above', 'below') or branch.get('status') not in STATES:
                raise ValueError('Invalid branch type/status')
            for key in ('label','description'):
                _languages(branch.get(key), 'branch/'+key)
            _source(branch.get('evidence'), repos, 'branch')
            if not isinstance(branch.get('contract'), str) or len(branch['contract']) > 180:
                raise ValueError('Invalid branch contract')
            steps=branch.get('steps')
            if not isinstance(steps,list) or not 1 <= len(steps) <= 5:
                raise ValueError('Invalid branch length')
            for step in steps:
                check_node(step)
    return {
        'format':'koa.graph.focus.public.v1',
        'owner_repository':OWNER,
        'owner_commit':source_commit,
        'source_sha256':hashlib.sha256(source_text.encode('utf-8')).hexdigest(),
        'inventory_sha256':hashlib.sha256(inventory_text.encode('utf-8')).hexdigest(),
        'source_date':source.get('source_date'),
        'notice':source['notice'],
        'paths':paths,
    }
