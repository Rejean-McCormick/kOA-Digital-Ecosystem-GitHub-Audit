"""Atlas regressions: source mapping, report navigation and public privacy."""
from __future__ import annotations

import functools
import http.server
import json
import os
import runpy
import tempfile
import threading
import unittest
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import urlopen
from unittest.mock import patch

from koa_audit.ecosystem import atlas, build_public_atlas
from koa_audit import qualification

ROOT=Path(__file__).resolve().parents[1]


class AtlasTest(unittest.TestCase):
    def test_all_inventory_repositories_and_12_reports(self):
        data=atlas(ROOT)
        self.assertEqual(data['format'],'koa_ecosystem.atlas.v1')
        self.assertEqual(data['total'],49)
        self.assertEqual(len(data['repositories']),49)
        self.assertEqual(sum(bool(r['report']) for r in data['repositories']),12)
        self.assertEqual(len(data['systems']),12)
        self.assertTrue(any(l['from']=='skope' and l['status']=='proposed' for l in data['links']))
        self.assertTrue(any(l['from']=='konnaxion' and l['to']=='orgo' for l in data['links']))

    def test_profile_navigation_and_no_raw_leak(self):
        with tempfile.TemporaryDirectory() as temp:
            site=Path(temp)
            result=build_public_atlas(ROOT,site)
            self.assertEqual(result['profiles'],12)
            data=json.loads((site/'data/ecosystem.json').read_text())
            for r in data['repositories']:
                if r['report']:
                    page=site/r['report']
                    self.assertTrue(page.is_file(),r['report'])
                    body=page.read_text()
                    self.assertIn('Engineering Profile',body)
                    self.assertIn(r['name'],body)
                    self.assertIn('snapshot',body.lower())
            combined='\n'.join(p.read_text() for p in site.rglob('*') if p.is_file())
            for disallowed in ('C:\\mycode', 'backend/.env', 'SECRET_987', 'qualification.json', 'assessments.json', 'AGENTS.md'):
                self.assertNotIn(disallowed,combined)

    def test_zero_manual_certification_claims_are_generated(self):
        raw=json.dumps(atlas(ROOT),ensure_ascii=False)
        self.assertNotIn('Étayé par preuve',raw)
        self.assertNotIn('"passed"',raw)

    def test_source_map_group_has_no_invented_edges(self):
        graph=atlas(ROOT)
        self.assertEqual({r['repo'] for r in graph['repositories']},set(qualification.profiles.inventory(ROOT)))
        self.assertEqual(len(graph['links']),7)
        self.assertTrue(all(l['status'] in {'documented','proposed'} for l in graph['links']))

    def test_profile_page_escape_and_counts(self):
        data=atlas(ROOT)
        byname={r['slug']:r for r in data['repositories']}
        self.assertEqual(byname['Konnaxion']['engineering']['counts']['production_nonblank_lines'],109361)
        self.assertEqual(byname['Orgo']['engineering']['counts']['active_files'],363)
        self.assertEqual(byname['kOA-Linux-Koali']['engineering']['counts']['active_files'],1649)


class LocalAtlasServerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        env=runpy.run_path(str(ROOT/'kOA_GitHub_Audit_Launcher.pyw'))
        env['_initialize_project'](ROOT)
        cls.handler=env['_NoConsolePreviewHandler']

    def test_private_qualification_json_and_full_local_profile(self):
        with tempfile.TemporaryDirectory() as temp, patch.dict(os.environ,{'LOCALAPPDATA':temp}):
            handler=functools.partial(self.handler,directory=str(ROOT/'docs'))
            server=http.server.ThreadingHTTPServer(('127.0.0.1',0),handler)
            server.daemon_threads=True
            worker=threading.Thread(target=server.serve_forever,daemon=True)
            worker.start()
            try:
                base=f'http://127.0.0.1:{server.server_port}'
                with urlopen(base+'/data/local-qualification.json',timeout=4) as res:
                    result=json.loads(res.read())
                    self.assertEqual(res.status,200)
                    self.assertEqual(result['format'],'koa_qualification.public_status.v1')
                    self.assertEqual(len(result['repositories']),49)
                    self.assertNotIn('evidence',json.dumps(result))
                    self.assertNotIn('scope',json.dumps(result))
                with urlopen(base+'/local/engineering/Konnaxion',timeout=4) as res:
                    body=res.read().decode('utf8')
                    self.assertIn('109,361',body)
                    self.assertIn('Profil Markdown original',body)
                    self.assertNotIn('<script>',body)
                try:
                    urlopen(base+'/local/engineering/NOT_PRESENT',timeout=4)
                    self.fail('Unknown profile should be 404')
                except HTTPError as e:
                    self.assertEqual(e.code,404)
            finally:
                server.shutdown();server.server_close();worker.join(timeout=3)


if __name__ == '__main__':unittest.main()
