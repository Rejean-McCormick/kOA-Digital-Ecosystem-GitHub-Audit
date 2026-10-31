"""Typed focused-path graph: evidence boundaries, publication, rollback, no network."""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from koa_audit.focus_graph import compile_focused_paths
from koa_audit.publication_snapshots import Capture, _publish_from_captures, rollback, republish_current

OWNER = 'Rejean-McCormick/kOA-Digital-Ecosystem'


def label(value):
    return {'fr':value, 'en':value}


class FocusGraphTests(unittest.TestCase):
    def setUp(self):
        self.inventory = (Path(__file__).resolve().parents[1] / 'data' / 'initial_inventory.json').read_text(encoding='utf-8')
        self.graph = {
            'format': 'koa.graph.focus.v1',
            'owner_repository': OWNER,
            'reference_inventory': 'docs/inventory/repositories.json',
            'notice': label('Pas une preuve globale'),
            'paths': [{
                'id':'decision','title':label('Décision'), 'summary':label('Un parcours'),
                'spine': [
                    {'id':id,'label':label(id),'description':label(id), 'repo':repo,'kind':kind}
                    for id,repo,kind in [
                        ('kn','Rejean-McCormick/Konnaxion','application'),
                        ('ik','Rejean-McCormick/Interaction-Kernel','protocol'),
                        ('or','Rejean-McCormick/Orgo','application')]
                ],
                'spine_links': [
                    {'from':a,'to':b,'label':label(a+' to '+b),'status':'qualified_local',
                     'contract':'governance.decision.execute/1.0.0',
                     'evidence':{'repo':OWNER,'path':'docs/2-Technical-Reference/40-integration/contract-map.md'}}
                    for a,b in [('kn','ik'),('ik','or')]
                ],
                'branches': [
                    {'id':'orgo-diagnostic','anchor':2,'side':'below','label':label('Diagnostic'),
                     'description':label('Owner scope'), 'status':'documented', 'contract':'',
                     'steps':[{'id':'diag','label':label('LevelUpDiag-Orgo'),
                               'description':label('Independent tests'), 'kind':'application',
                               'repo':'Rejean-McCormick/LevelUpDiag-Orgo'}],
                     'evidence':{'repo':'Rejean-McCormick/Orgo','path':'README.md'}}
                ]
            }]
        }

    def compile(self, graph=None, sha='a'*40):
        return compile_focused_paths(json.dumps(graph if graph is not None else self.graph,ensure_ascii=False),self.inventory,sha)

    def test_compiles_pinned_paths_without_certification_claim(self):
        got=self.compile()
        self.assertEqual(got['format'],'koa.graph.focus.public.v1')
        self.assertEqual(got['owner_commit'],'a'*40)
        self.assertEqual(got['paths'][0]['spine_links'][0]['status'],'qualified_local')
        self.assertEqual(len(got['paths'][0]['branches']),1)
        self.assertNotIn('local_root',json.dumps(got))

    def test_refuses_unpinned_commit_and_forged_public_path(self):
        with self.assertRaises(ValueError):self.compile(sha='main')
        for field,value in [('repo','Outside/Invented'),('path','../../secrets.md')]:
            bad=deepcopy(self.graph)
            bad['paths'][0]['spine_links'][0]['evidence'][field]=value
            with self.assertRaises(ValueError):self.compile(bad)

    def test_refuses_dangling_edge_and_invalid_anchor(self):
        bad=deepcopy(self.graph)
        bad['paths'][0]['spine_links'][0]['to']='nonexistent'
        with self.assertRaises(ValueError):self.compile(bad)
        bad=deepcopy(self.graph)
        bad['paths'][0]['branches'][0]['anchor']=99
        with self.assertRaises(ValueError):self.compile(bad)

    def test_full_then_selected_then_rollback_reuses_exact_pinned_path(self):
        with TemporaryDirectory() as t:
            docs=Path(t)/'docs'
            def collector(repo):
                if repo==OWNER:
                    return Capture(repo,'a'*40,{'README.md':'Documentation'},
                                   graph_focus_text=json.dumps(self.graph,ensure_ascii=False),
                                   graph_inventory_text=self.inventory)
                return Capture(repo,'b'*40,{'README.md':'Another repo'})
            rid1='20261031T210000Z-1-1'
            rid2='20261031T210200Z-1-1'
            _publish_from_captures(docs,[OWNER],'all',collector,rid1,'2026-10-31T21:00:00Z')
            ref=docs/'data'/'focus-paths.json'
            frozen=ref.read_bytes()
            self.assertTrue((docs/'publications'/'releases'/rid1/'focus-paths.json').exists())
            _publish_from_captures(docs,['Rejean-McCormick/Kolor'],'selected',collector,rid2,'2026-10-31T21:02:00Z')
            self.assertEqual(ref.read_bytes(),frozen)
            self.assertEqual((docs/'publications'/'releases'/rid2/'focus-paths.json').read_bytes(),frozen)
            republish_current(docs)
            self.assertEqual(ref.read_bytes(),frozen)
            ref.write_text('{}')
            rollback(docs,rid1,'2026-10-31T22:00:00Z')
            self.assertEqual(ref.read_bytes(),frozen)

    def test_rollback_to_pre_focus_release_drops_stale_focus(self):
        with TemporaryDirectory() as t:
            docs=Path(t)/'docs';rid='20261031T210000Z-1-1'
            def plain(repo):return Capture(repo,'b'*40,{'README.md':'Hi'})
            _publish_from_captures(docs,['Rejean-McCormick/Kolor'],'all',plain,rid,'2026-10-31T21:00:00Z')
            target=docs/'data'/'focus-paths.json';target.parent.mkdir(parents=True,exist_ok=True)
            target.write_text('{"format":"koa.graph.focus.public.v1"}')
            rollback(docs,rid,'2026-10-31T23:00:00Z')
            self.assertFalse(target.exists())

if __name__=='__main__': unittest.main()
