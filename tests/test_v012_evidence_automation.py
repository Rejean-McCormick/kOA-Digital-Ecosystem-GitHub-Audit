"""v0.12: bounded opt-in report discovery, frozen evidence & private atlas view."""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from koa_audit import campaigns, evidence_discovery

PROJECT = Path(__file__).resolve().parents[1]
REPO = "Rejean-McCormick/Orgo"


class V012EvidenceTests(unittest.TestCase):
    def _clone(self, base: Path) -> Path:
        clone=base/'clone';clone.mkdir()
        def git(*args):
            return subprocess.run(['git', *args], cwd=clone, text=True,
                                  stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True).stdout.strip()
        git('init', '-q');git('config', 'user.email', 'tester@example.invalid')
        git('config','user.name','tester')
        (clone/'README.md').write_text('Synthetic local evidence only',encoding='utf-8')
        git('add','README.md');git('commit','-qm','test')
        git('remote','add','origin','https://github.com/'+REPO+'.git')
        return clone

    @unittest.skipUnless(shutil.which('git'), 'Git local required')
    def test_discovery_only_curated_filenames_and_no_copy(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); clone=self._clone(root)
            (clone/'reports').mkdir();(clone/'other').mkdir()
            wanted=clone/'reports'/'junit.xml'
            wanted.write_text('<testsuite tests="7" errors="1" failures="0"/>',encoding='utf-8')
            (clone/'other'/'junit.xml').write_text('<testsuite tests="500"/>')
            (clone/'coverage.xml').write_text('<coverage line-rate="0.63"/>')
            (clone/'security.sarif').write_text(json.dumps({'version':'2.1.0','runs':[{'results':[{}]}]}))
            (clone/'reports'/'coverage.json').write_text('{"private-key":"placeholder"}')
            (clone/'.env').write_text('SECRET=private_hidden')
            records=evidence_discovery.discover(clone,REPO)
            self.assertEqual({row['name'] for row in records},
                             {'reports/junit.xml','coverage.xml','security.sarif'})
            text=json.dumps([{k:v for k,v in row.items() if k!='path'} for row in records])
            self.assertNotIn('private_hidden',text)
            self.assertNotIn(str(clone),text)
            self.assertTrue(all(len(item['sha256']) == 64 for item in records))
            self.assertTrue(wanted.exists())
            self.assertTrue(all(x['version_relation']=='unverified_preexisting_report' for x in records))

    @unittest.skipUnless(shutil.which('git'), 'Git local required')
    def test_wrong_git_identity_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            clone=self._clone(Path(td))
            with self.assertRaisesRegex(ValueError,'Origine GitHub'):
                evidence_discovery.discover(clone,'Rejean-McCormick/Konnaxion')

    @unittest.skipUnless(shutil.which('git'), 'Git local required')
    def test_symlink_and_size_not_imported(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); clone=self._clone(root)
            outside=root/'outside';outside.mkdir()
            (outside/'junit.xml').write_text('<testsuite tests="2"/>')
            try:
                (clone/'reports').symlink_to(outside,target_is_directory=True)
            except (OSError, NotImplementedError):
                self.skipTest('Symlinks not permitted on this machine')
            (clone/'coverage.xml').write_bytes(b'x'*300)
            with patch.object(evidence_discovery,'MAX_REPORT_READ',100):
                self.assertEqual(evidence_discovery.discover(clone,REPO),[])

    def test_version_reference_relation_is_not_artifact_certification(self):
        a,b='a'*40,'b'*40
        rec={'observed_git':{'status':'verified_git_origin','head':a},'historical_audit':None}
        self.assertEqual(campaigns.proof_version_relation({'source_commit':a},rec),
            'collector_git_head_matches_reference_not_artifact_attestation')
        self.assertEqual(campaigns.proof_version_relation({'source_commit':b},rec),
            'collector_git_head_differs_from_reference')
        self.assertEqual(campaigns.proof_version_relation({},rec),
            'unverified_report_not_bound_to_commit')

    def test_campaign_artifact_comparison_and_immutable_snapshots(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);state=root/'state';store=root/'store'
            junit=root/'junit.xml';junit.write_text('<testsuite tests="5"/>')
            with patch.dict(os.environ,{'LOCALAPPDATA':str(state)}):
                old=campaigns.create_campaign(PROJECT,'Before attached results',store=store,
                                              git_probe=False,extra_proofs={REPO:[junit]})
                junit.write_text('<testsuite tests="9"/>')
                new=campaigns.create_campaign(PROJECT,'After attached results',store=store,
                                              git_probe=False,extra_proofs={REPO:[junit]})
            comp=campaigns.compare_campaigns(old.stem,new.stem,store)
            self.assertEqual(comp['totals']['proof_files_added'],1)
            self.assertEqual(comp['totals']['proof_files_removed'],1)
            self.assertEqual(comp['totals']['stage_new_evidence'],0)
            first=campaigns.read_campaign(old.stem,store)
            self.assertEqual(first['repository_profiles_snapshot']['Orgo']['attached_proofs'][0]['summary']['totals']['tests'],5)
            page=campaigns.render_local_page('/local/campaigns/compare/'+old.stem+'--'+new.stem,store)
            self.assertIn('Rapports ajoutés / retirés',page)
            self.assertIn('/app/Orgo',page)
            self.assertEqual('junit.xml',campaigns.read_proof(old.stem,'Orgo',0,store)[0]['name'])

    def test_discovered_report_changed_before_capture_must_be_reapproved(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);state=root/'state';store=root/'store'
            proof=root/'coverage.xml'
            proof.write_text('<coverage line-rate="0.75"/>')
            original=campaigns._hash(proof.read_bytes())
            proof.write_text('<coverage line-rate="0.50"/>')
            with patch.dict(os.environ,{'LOCALAPPDATA':str(state)}):
                with self.assertRaisesRegex(ValueError,'modifié depuis la découverte'):
                    campaigns.create_campaign(PROJECT,'Unapproved changed file',store=store,git_probe=False,
                        extra_proofs={REPO:[proof]},expected_proof_sha256={proof:original})
            self.assertFalse(list(store.glob('*.zip')) if store.exists() else [])

    def test_private_latest_summary_does_not_include_notes_or_local_paths(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);store=root/'store'
            self.assertFalse(campaigns.latest_summary(store)['available'])
            with patch.dict(os.environ,{'LOCALAPPDATA':str(root/'private')}):
                first=campaigns.create_campaign(PROJECT,'First local capture',store=store,git_probe=False)
                second=campaigns.create_campaign(PROJECT,'Second local capture',store=store,git_probe=False)
            info=campaigns.latest_summary(store)
            self.assertTrue(info['available'])
            self.assertEqual(info['latest']['id'],second.stem)
            self.assertEqual(info['previous_id'],first.stem)
            self.assertEqual(info['latest']['repository_count'],49)
            self.assertIn(REPO,info['latest']['repositories'])
            payload=json.dumps(info)
            self.assertNotIn(str(root),payload)
            self.assertNotIn('source_model',payload)
            timeline=campaigns.render_local_page('/local/campaigns',store)
            self.assertIn('Évolution de la couverture documentaire',timeline)
            self.assertIn('First local capture',timeline)
            self.assertIn('Second local capture',timeline)

    def test_html_js_uses_private_endpoint_but_static_dashboard_safely_falls_back(self):
        html=(PROJECT/'docs'/'index.html').read_text(encoding='utf-8')
        js=(PROJECT/'docs'/'assets'/'atlas.js').read_text(encoding='utf-8')
        launcher=(PROJECT/'kOA_GitHub_Audit_Launcher.pyw').read_text(encoding='utf-8')
        self.assertIn('id="latest-campaign"',html)
        self.assertIn('/api/campaigns/summary',js)
        self.assertIn('campaignSummary?.format',js)
        self.assertIn('route == "/api/campaigns/summary"',launcher)
        self.assertIn('privateCampaigns?.available',js)


if __name__ == '__main__':
    unittest.main()
