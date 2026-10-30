"""Verified, scoped JUnit logs from targeted tests of supplied ZIP snapshots.

A passing test case is not a certification of the whole application. The source
ZIP identity is recorded, but NOT equated with any Git commit.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from xml.etree import ElementTree as ET
from urllib.parse import quote

MANIFEST = 'KOA-TEST-EXECUTIONS-2026-10-30.json'
SHA256 = '2860ef8127a9a391ffd421e3ec3b24faff09d27e9388eccf5b76d68b101c8191'
FORMAT = 'koa.private.snapshot_test_execution.v1'


def load(project: Path) -> dict:
    root = Path(project) / 'private_evidence'
    path = root / MANIFEST
    if not path.is_file() or path.is_symlink() or path.stat().st_size > 200_000:
        return {}
    contents = path.read_bytes()
    if hashlib.sha256(contents).hexdigest() != SHA256:
        return {}
    try:
        data = json.loads(contents)
        if data.get('format') != FORMAT or not isinstance(data.get('runs'), list):
            return {}
        result = {}
        for run in data['runs']:
            repo = run.get('repository')
            if not isinstance(repo, str) or repo in result or not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repo):
                return {}
            name = run.get('junit_member', '')
            if not re.fullmatch(r'[A-Za-z0-9_.-]+\.junit\.xml', name):
                return {}
            report = root / 'test_reports' / name
            if not report.is_file() or report.is_symlink() or report.stat().st_size > 300_000:
                return {}
            content = report.read_bytes()
            if hashlib.sha256(content).hexdigest() != run.get('junit_sha256'):
                return {}
            suite = ET.fromstring(content)
            if suite.tag != 'testsuite' or len(suite.findall('testcase')) != run['passed']:
                return {}
            if not run.get('passed') or any(run.get(k) != 0 for k in ('failed','errors','skipped')):
                return {}
            if not re.fullmatch('[a-f0-9]{64}', run.get('snapshot_sha256','')):
                return {}
            cases = run.get('cases')
            if not isinstance(cases, list) or len(cases) != run['passed']:
                return {}
            if sorted((x.get('name'),x.get('class')) for x in cases) != sorted((x.get('name'),x.get('classname')) for x in suite.findall('testcase')):
                return {}
            result[repo] = {
                'passed': run['passed'], 'failed': 0, 'skipped': 0,
                'framework': 'pytest', 'timestamp_utc': run['timestamp_utc'],
                'scope': run['scope'], 'snapshot_sha256': run['snapshot_sha256'],
                'git_commit_verified': False,
                'test_files': run['test_files'], 'junit_sha256': run['junit_sha256'],
                'junit_link': '/local/spec-tests/' + quote(repo.split('/', 1)[-1]),
            }
        return result
    except (ValueError, TypeError, KeyError, AttributeError, ET.ParseError):
        return {}


def report_for_slug(project: Path, slug: str) -> bytes | None:
    results = load(project)
    matches = [r for r in results if r.split('/')[-1].casefold() == slug.casefold()]
    if len(matches) != 1:
        return None
    index = json.loads((Path(project) / 'private_evidence' / MANIFEST).read_text(encoding='utf-8'))
    for run in index['runs']:
        if run['repository'] == matches[0]:
            return (Path(project) / 'private_evidence' / 'test_reports' / run['junit_member']).read_bytes()
    return None
