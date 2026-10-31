"""Read three native test run reports from user-supplied, isolated ZIP snapshots.

Test execution proves only the named cases on the exact ZIP bytes. A separate
SHA-256 check is required for each report; no git commit is inferred.
"""
from __future__ import annotations
import hashlib
import json
import re
from pathlib import Path
from xml.etree import ElementTree as ET
from urllib.parse import quote

MANIFEST = 'KOA-ISOLATED-TEST-RUNS-2026-10-30.json'
SHA256 = '11aa86a63fc146c9da1790cc8ffdb506485da654c57acda49ade6a5cbdd9dd76'
FORMAT = 'koa.private.isolated_snapshot_test_runs.v1'


def load(project: Path) -> dict:
    directory = Path(project) / 'private_evidence'
    source = directory / MANIFEST
    if not source.is_file() or source.is_symlink() or source.stat().st_size > 100_000:
        return {}
    original = source.read_bytes()
    if hashlib.sha256(original).hexdigest() != SHA256:
        return {}
    try:
        data = json.loads(original)
        if data.get('format') != FORMAT or not isinstance(data.get('runs'), list) or len(data['runs']) != 3:
            return {}
        out = {}
        for raw in data['runs']:
            repo = raw.get('repository', '')
            if not re.fullmatch(r'Rejean-McCormick/[A-Za-z0-9_.-]{1,90}', repo) or repo in out:
                return {}
            filename = raw.get('junit_member', '')
            if not re.fullmatch(r'[A-Za-z0-9_.-]{1,90}\.junit\.xml', filename):
                return {}
            file = directory / 'snapshot_test_reports' / filename
            if not file.is_file() or file.is_symlink() or file.stat().st_size > 200_000:
                return {}
            xml = file.read_bytes()
            if hashlib.sha256(xml).hexdigest() != raw.get('junit_sha256'):
                return {}
            suite = ET.fromstring(xml)
            if suite.tag != 'testsuite' or any(suite.iter('failure')) or any(suite.iter('error')) or any(suite.iter('skipped')):
                return {}
            if int(suite.get('tests', '0')) != len(suite.findall('testcase')) or int(suite.get('tests','0')) != raw['passed'] or raw['passed'] < 1:
                return {}
            if any(raw.get(k) != 0 for k in ('failed', 'errors', 'skipped')) or raw.get('snapshot_commit') is not None:
                return {}
            if not re.fullmatch(r'[0-9a-f]{64}', raw.get('snapshot_sha256', '')):
                return {}
            if not isinstance(raw.get('test_files'), list) or not raw['test_files']:
                return {}
            for f in raw['test_files']:
                if not re.fullmatch(r'[0-9a-f]{64}', f.get('sha256', '')) or not f.get('path') or f['path'].startswith('/') or '..' in f['path'].split('/'):
                    return {}
            out[repo] = {'passed':raw['passed'],'failed':0,'skipped':0,'framework':raw['framework'],
                         'timestamp_utc':raw['timestamp_utc'],'scope':raw['scope'],'snapshot_sha256':raw['snapshot_sha256'],
                         'git_commit_verified':False,'test_files':raw['test_files'],'junit_sha256':raw['junit_sha256'],
                         'junit_link':'/local/snapshot-tests/'+quote(repo.partition('/')[2])}
        return out
    except (OSError,ValueError,TypeError,KeyError,AttributeError,ET.ParseError):
        return {}


def report_for_slug(project: Path, slug: str) -> bytes | None:
    if not re.fullmatch(r'[A-Za-z0-9_.-]{1,90}',slug):
        return None
    runs=load(project)
    repo='Rejean-McCormick/'+slug
    if repo not in runs:
        return None
    index=json.loads((Path(project)/'private_evidence'/MANIFEST).read_text('utf-8'))
    run=next((r for r in index['runs'] if r['repository']==repo),None)
    if run is None:
        return None
    return (Path(project)/'private_evidence'/'snapshot_test_reports'/run['junit_member']).read_bytes()
