"""Kristal source adapter tests never modify the source repository."""
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
from unittest.mock import patch
from urllib.request import urlopen

from koa_audit import kristal_source

ROOT=Path(__file__).resolve().parents[1]
INVENTORY=["Rejean-McCormick/Akor", "Rejean-McCormick/Orgo", "Rejean-McCormick/Ekole"]


def fixture(folder: Path):
    source=folder/'knowledge-base'/'sources'
    source.mkdir(parents=True)
    (source/'repositories.json').write_text(json.dumps({"format":"x","repositories":[
        {"id":"koa:repo:akor","full_name":INVENTORY[0],"name":"Akor", "repository_role":"member", "architectural_membership":"mapped","description":"An observatory"},
        {"id":"koa:repo:orgo","full_name":INVENTORY[1],"name":"Orgo","repository_role":"member","architectural_membership":"mapped"}]}))
    (source/'components.json').write_text(json.dumps({"format":"x","components":[
        {"id":"koa:akor","label":"Akor","description":"Akor component","repository_ref":"koa:repo:akor","assertion_status":"sourced"},
        {"id":"koa:ekole","label":"Ekole","description":"Ekole component","assertion_status":"sourced"},
    ]}))
    (source/'relations.json').write_text(json.dumps({"format":"x","relations":[
        {"subject":"koa:akor","predicate":"koa:connects_to","object":"koa:ekole","assertion_status":"claimed","source_refs":["foo"]},
        {"subject":"koa:akor","predicate":"koa:contributes_to","object":"koa:ekole","assertion_status":"sourced"}
    ]}))


class KristalAdapterTest(unittest.TestCase):
    def test_explicit_identity_mapping_and_statuses(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp);fixture(p)
            before={f:f.read_bytes() for f in (p/'knowledge-base/sources').glob('*.json')}
            result=kristal_source.build_local_kristal_view(p,INVENTORY)
            self.assertEqual(result['matched'],2)
            self.assertEqual(result['mapped_components'],1)
            self.assertEqual(result['catalog_relations'],2)
            self.assertEqual(len(result['repositories']),3)
            self.assertEqual(result['repositories'][0]['relations'][0]['evidence'],'claimed')
            self.assertEqual(result['repositories'][0]['relations'][0]['predicate'],'connects_to')
            self.assertFalse(result['repositories'][2]['found'])
            raw=json.dumps(result)
            for x in ('local_path','C:\\mycode','evidence_value','api_key','source_refs'):
                self.assertNotIn(x,raw)
            self.assertEqual(before,{f:f.read_bytes() for f in (p/'knowledge-base/sources').glob('*.json')})

    def test_diagnostic_candidates_are_not_promoted_to_explicit_links(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp);fixture(p)
            src=p/'knowledge-base/sources'
            repos=json.loads((src/'repositories.json').read_text())
            repos['repositories'][1]['source_refs']=['src:github-orgo']
            (src/'repositories.json').write_text(json.dumps(repos))
            comps=json.loads((src/'components.json').read_text())
            comps['components'].extend([
                {'id':'koa:orgo','label':'Orgo','kind':'workflow_system',
                 'source_refs':['src:github-orgo'],'assertion_status':'sourced'},
                {'id':'koa:orgo-helper','label':'Internal helper','source_refs':['src:github-orgo'],
                 'assertion_status':'claimed'}])
            (src/'components.json').write_text(json.dumps(comps))
            relations=json.loads((src/'relations.json').read_text())
            relations['relations'].append({'subject':'koa:orgo','predicate':'koa:connects_to',
                                          'object':'koa:akor','assertion_status':'sourced'})
            (src/'relations.json').write_text(json.dumps(relations))
            before={f.name:f.read_bytes() for f in src.glob('*.json')}
            result=kristal_source.build_local_kristal_view(p,INVENTORY)
            self.assertEqual(result['explicit_repositories'],1)
            self.assertEqual(result['candidate_repositories'],1)
            self.assertEqual(result['unlinked_repositories'],0)  # Ekole isn't in catalog
            orgo=result['repositories'][1]
            self.assertEqual(orgo['association'],'candidate')
            self.assertEqual(orgo['components'],[])
            self.assertEqual({c['id'] for c in orgo['candidates']},{'koa:orgo','koa:orgo-helper'})
            self.assertTrue(all(c['status']=='CANDIDATE_NOT_VALIDATED' for c in orgo['candidates']))
            self.assertTrue(orgo['candidate_relations'])
            self.assertFalse(orgo['relations'])
            self.assertNotIn('src:github-orgo',json.dumps(result))
            self.assertNotIn('source_refs',json.dumps(result))
            self.assertEqual(before,{f.name:f.read_bytes() for f in src.glob('*.json')})

    def test_missing_catalog_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(FileNotFoundError):
                kristal_source.build_local_kristal_view(Path(tmp),INVENTORY)

    def test_remembers_root_outside_repository(self):
        with tempfile.TemporaryDirectory() as tmp,patch.dict(os.environ, {'LOCALAPPDATA':tmp, 'KOA_KRISTAL_SOURCE':''}):
            expected=Path(tmp)/'Kristal'
            kristal_source.save_source_root(expected)
            self.assertEqual(kristal_source.get_source_root(),expected)
            self.assertFalse((ROOT/'kristal-source.json').exists())

    def test_json_endpoint_is_live_and_responds_when_folder_missing(self):
        env=runpy.run_path(str(ROOT/'kOA_GitHub_Audit_Launcher.pyw'))
        env['_initialize_project'](ROOT)
        handler=env['_NoConsolePreviewHandler']
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ,{'LOCALAPPDATA':tmp}):
            source=Path(tmp)/'Kristal';fixture(source)
            server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(handler,directory=str(ROOT/'docs')))
            server.daemon_threads=True
            server.kristal_source=source
            t=threading.Thread(target=server.serve_forever,daemon=True);t.start()
            try:
                base=f'http://127.0.0.1:{server.server_port}'
                with urlopen(base+'/api/kristal/atlas',timeout=5) as r:
                    result=json.loads(r.read())
                self.assertEqual(result['format'],kristal_source.FORMAT)
                self.assertEqual(result['state'],'ready')
                self.assertEqual(result['matched'],2)
                # No pre-generated JSON is needed; refresh reads source again.
                source.rename(Path(tmp)/'moved')
                with urlopen(base+'/api/kristal/atlas',timeout=5) as r:
                    failed=json.loads(r.read())
                self.assertEqual(failed['state'],'missing')
            finally:
                server.shutdown();server.server_close();t.join(timeout=5)


if __name__=='__main__':unittest.main()
