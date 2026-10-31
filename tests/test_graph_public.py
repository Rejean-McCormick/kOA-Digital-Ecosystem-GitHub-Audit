"""Source-owned graph stays distinct from audit findings and frozen documents."""
from __future__ import annotations

import json
from pathlib import Path
import unittest
from tempfile import TemporaryDirectory

from koa_audit.graph_public import compile_public_graph
from koa_audit.publication_snapshots import Capture, _publish_from_captures

class GraphPublicTests(unittest.TestCase):
    def setUp(self):
        # Self-contained fixture; GitHub Actions does not checkout the source owner repo.
        root=Path(__file__).resolve().parents[1]
        self.inventory=(root/'data/initial_inventory.json').read_text(encoding='utf-8')
        registry={
          'format':'koa.graph.registry.v1','owner_repository':'Rejean-McCormick/kOA-Digital-Ecosystem',
          'reference_inventory':'docs/inventory/repositories.json','reference_count':49,
          'additional_repositories':[{'github_repo': 'Rejean-McCormick/Kolor', 'admission':'discovered_not_admitted'},
                                     {'github_repo': 'Rejean-McCormick/Karacter', 'admission':'discovered_not_admitted'}],
          'systems':[{'id':'konnaxion','github_repo':'Rejean-McCormick/Konnaxion','label':'Konnaxion',
                      'responsibility':'Civic state','group':'civic', 'evidence_state':'documented_responsibility',
                      'source':'docs/1-Overview/Components.md'},
                     {'id':'orgo','github_repo':'Rejean-McCormick/Orgo','label':'Orgo',
                      'responsibility':'Workflow state','group':'civic', 'evidence_state':'documented_responsibility',
                      'source':'docs/1-Overview/Components.md'}],
          'relations':[{'from':'konnaxion','to':'orgo','label':'Governed handoff',
                         'evidence_state':'documented_passage','verification':'not_certified',
                         'source':'docs/1-Overview/Integration.md'}]
        }
        self.registry=json.dumps(registry,ensure_ascii=False)

    def test_compilation_keeps_reference_and_candidates_distinct(self):
        g = compile_public_graph(self.registry,self.inventory,'a'*40)
        self.assertEqual(g['reference_count'],49)
        self.assertEqual(g['candidate_count'],2)
        self.assertEqual(len(g['repositories']),51)
        self.assertEqual(len(g['systems']),2)
        self.assertEqual(len(g['links']),1)
        self.assertTrue(all(c['verification']=='not_certified' for c in g['links']))
        self.assertEqual({r['name'] for r in g['repositories'] if r['admission']=='discovered_not_admitted'}, {'Kolor','Karacter'})
        self.assertFalse('local_root' in json.dumps(g))

    def test_bad_source_revision_and_unsupported_evidence_refused(self):
        with self.assertRaises(ValueError):
            compile_public_graph(self.registry,self.inventory,'main')
        data=json.loads(self.registry)
        data['relations'][0]['verification']='certified'
        with self.assertRaises(ValueError):
            compile_public_graph(json.dumps(data),self.inventory,'a'*40)

    def test_publication_pins_source_and_retains_graph_on_selected_update(self):
        with TemporaryDirectory() as t:
            root=Path(t)/'docs'
            def collector(repo):
                if repo.endswith('kOA-Digital-Ecosystem'):
                    return Capture(repo,'a'*40,{'README.md':'Hello'},
                        graph_registry_text=self.registry, graph_inventory_text=self.inventory)
                return Capture(repo,'b'*40,{'README.md':'Other'})
            owner='Rejean-McCormick/kOA-Digital-Ecosystem'
            other='Rejean-McCormick/Kolor'
            _publish_from_captures(root,[owner,other],'all',collector,'20261031T170000Z-1-1','2026-10-31T17:00:00Z')
            path=root/'data'/'graph-public.json'
            before=path.read_bytes()
            self.assertEqual(json.loads(before)['owner_commit'],'a'*40)
            _publish_from_captures(root,[other],'selected',collector,'20261031T180000Z-1-1','2026-10-31T18:00:00Z')
            self.assertEqual(before,path.read_bytes())

if __name__ == '__main__':
    unittest.main()
