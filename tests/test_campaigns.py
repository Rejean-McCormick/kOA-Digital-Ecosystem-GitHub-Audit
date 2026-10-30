"""Campaigns are local snapshots; never run source tests or write GitHub."""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

from koa_audit import campaigns

PROJECT = Path(__file__).resolve().parent.parent


class CampaignsTest(unittest.TestCase):
    def test_snapshot_49_profiles_versions_manual_assessments(self):
        with tempfile.TemporaryDirectory() as td:
            folder = Path(td)
            store = folder / 'campagnes'
            audit = folder / 'audit.json'
            audit.write_text(json.dumps({
                'format': 'koa_audit.local_observation.v1',
                'generated_at': '2026-10-28T20:42:13Z',
                'repositories': [
                    {'repository': 'Rejean-McCormick/Konnaxion',
                     'location': str(folder / 'not-existing'),
                     'status': 'REVIEW', 'files_enumerated': 123,
                     'files_inspected': 110, 'finding_counts': {'PYTHON_SHELL_TRUE': 2},
                     'git': {'head': 'c'*40, 'remote_repository': 'Rejean-McCormick/Konnaxion'}}
                ],
            }), encoding='utf-8')
            with patch.dict(os.environ, {'LOCALAPPDATA': str(folder / 'state')}):
                created = campaigns.create_campaign(PROJECT, 'Bilan octobre 2026', audit, store=store, git_probe=False)
            self.assertEqual(created.suffix, '.zip')
            snap = campaigns.read_campaign(created.stem, store)
            self.assertEqual(len(snap['repository_profiles_snapshot']), 49)
            k = snap['repository_profiles_snapshot']['Konnaxion']
            self.assertEqual(k['historical_audit']['recorded_git']['head'], 'c'*40)
            self.assertEqual(k['historical_audit']['recorded_git']['links']['download_zip'],
                             'https://github.com/Rejean-McCormick/Konnaxion/archive/' + 'c'*40 + '.zip')
            self.assertFalse(k['qualification']['production']['status'] == 'Étayé par preuve')
            self.assertTrue(k['profiles']['engineering'])
            self.assertTrue(k['profiles']['metrics'])
            self.assertEqual(campaigns.list_campaigns(store)[0]['integrity'], 'ok')
            self.assertIn('Konnaxion', campaigns.render_local_page('/local/campaigns/'+created.stem, store))
            self.assertIn('Engineering Profile', campaigns.render_local_page('/local/campaigns/'+created.stem+'/engineering/Konnaxion',store))
            with zipfile.ZipFile(created) as archive:
                names = archive.namelist()
                self.assertNotIn('audit.json', names)
                self.assertNotIn('backend/.env', names)
                self.assertIn('campaign.json', names)
                self.assertIn('profiles/Konnaxion/ENGINEERING_PROFILE.md', names)
                self.assertNotIn(str(folder / 'not-existing'), archive.read('campaign.json').decode())

    def test_tampering_detected_and_does_not_replace_campaign(self):
        with tempfile.TemporaryDirectory() as td:
            store=Path(td)/'store'
            with patch.dict(os.environ, {'LOCALAPPDATA':str(Path(td)/'state')}):
                made=campaigns.create_campaign(PROJECT,'Campagne sans audit',store=store,git_probe=False)
            with made.open('ab') as stream:
                stream.write(b'tampered')
            with self.assertRaisesRegex(ValueError, 'SHA-256'):
                campaigns.read_campaign(made.stem,store)
            self.assertEqual(campaigns.list_campaigns(store)[0]['integrity'],'failed')

    def test_manual_evidence_is_frozen_not_live(self):
        with tempfile.TemporaryDirectory() as td:
            folder=Path(td)
            state=folder/'state'
            with patch.dict(os.environ,{'LOCALAPPDATA':str(state)}):
                qualification_state=state/'kOA-GitHub-Audit/profiles/qualification.json'
                qualification_state.parent.mkdir(parents=True)
                qualification_state.write_text(json.dumps({'format':'koa_qualification.evidence.v1',
                    'claims':{'Rejean-McCormick/Orgo':{'specified':{
                        'status':'Étayé par preuve','scope':'Architecture documentée',
                        'evidence':'CONTRACTS.md version 1', 'reviewed_at':'2026-10-10T00:00:00Z'}}}}),encoding='utf-8')
                proof=folder/'junit.xml'
                proof.write_text('<testsuite tests="3" failures="0"/>',encoding='utf-8')
                old=campaigns.create_campaign(PROJECT,'Qualification Orgo ancienne',store=folder/'store',
                    extra_proofs={'Rejean-McCormick/Orgo':[proof]},git_probe=False)
                qualification_state.write_text(json.dumps({'format':'koa_qualification.evidence.v1','claims':{}}))
                frozen=campaigns.read_campaign(old.stem,folder/'store')
                record=frozen['repository_profiles_snapshot']['Orgo']
                self.assertEqual(record['qualification']['specified']['status'],'Étayé par preuve')
                self.assertEqual(len(record['attached_proofs']),1)
                with zipfile.ZipFile(old) as z:
                    self.assertIn(b'<testsuite',z.read('proofs/Orgo/00.xml'))
                newer=campaigns.create_campaign(PROJECT,'Qualification Orgo nouvelle',store=folder/'store',git_probe=False)
                now=campaigns.read_campaign(newer.stem,folder/'store')
                self.assertEqual(now['repository_profiles_snapshot']['Orgo']['qualification']['specified']['status'],'Non évalué')

    def test_kristal_projection_is_frozen_not_live(self):
        from tests.test_kristal_source import fixture
        with tempfile.TemporaryDirectory() as td:
            folder=Path(td)
            source=folder/'kristal';fixture(source)
            with patch.dict(os.environ,{'LOCALAPPDATA':str(folder/'state')}):
                saved=campaigns.create_campaign(PROJECT,'Kristal October snapshot',store=folder/'campaigns',
                                                 kristal_folder=source,git_probe=False)
                old=campaigns.read_campaign(saved.stem,folder/'campaigns')
                self.assertEqual(old['kristal']['status'],'frozen_local_projection')
                row=old['repository_profiles_snapshot']['Akor']['kristal']
                self.assertEqual(row['association'],'explicit')
                self.assertEqual(len(row['components']),1)
                # After creating the snapshot, the source can change freely.
                (source/'knowledge-base/sources/components.json').write_text('{"components":[]}')
                still=campaigns.read_campaign(saved.stem,folder/'campaigns')
                self.assertEqual(still['repository_profiles_snapshot']['Akor']['kristal'],row)
                text=campaigns.render_local_page('/local/campaigns/'+saved.stem+'/app/Akor',folder/'campaigns')
                self.assertIn('Kristal à la date',text)
                self.assertIn('composant(s) explicite(s)',text)

    def test_git_origin_guard_and_sha_validation(self):
        sha='a'*40
        self.assertTrue(campaigns._origin_matches('git@github.com:Rejean-McCormick/Orgo.git','Rejean-McCormick/Orgo'))
        self.assertFalse(campaigns._origin_matches('https://token@github.com/Rejean-McCormick/Orgo','Rejean-McCormick/Orgo'))
        self.assertFalse(campaigns._origin_matches('https://github.com/attacker/Orgo','Rejean-McCormick/Orgo'))
        self.assertFalse(campaigns._github_link('owner/Orgo','main'))
        self.assertTrue(campaigns._github_link('owner/Orgo',sha))
        with tempfile.TemporaryDirectory() as td:
            git=shutil.which('git')
            if not git:
                self.skipTest('git not installed')
            root=Path(td)/'repo';root.mkdir()
            def run(*args):
                return subprocess.run([git,*args],cwd=root,check=True,capture_output=True,text=True).stdout.strip()
            run('init','-q')
            run('config','user.email','local@example.com')
            run('config','user.name','test')
            (root/'README.md').write_text('hello')
            run('add','README.md')
            run('commit','-qm','initial')
            run('remote','add','origin','https://github.com/Rejean-McCormick/Orgo.git')
            git_obs=campaigns._git_observation(root,'Rejean-McCormick/Orgo')
            self.assertEqual(git_obs['status'],'verified_git_origin')
            self.assertEqual(git_obs['worktree'],'tracked_files_clean_untracked_not_checked')
            self.assertEqual(git_obs['head'],run('rev-parse','HEAD'))
            (root/'README.md').write_text('dirty')
            self.assertEqual(campaigns._git_observation(root,'Rejean-McCormick/Orgo')['worktree'],'tracked_changes_present')
            self.assertEqual(campaigns._git_observation(root,'Rejean-McCormick/Konnaxion')['status'],'origin_not_verified')

    def test_existing_junit_coverage_sarif_are_labeled_import_only(self):
        xml=campaigns.describe_proof(Path('junit.xml'),b'<testsuites><testsuite tests="7" failures="1" errors="0" skipped="2"/></testsuites>')
        self.assertEqual(xml['recognition'],'junit_xml_summary')
        self.assertEqual(xml['totals']['tests'],7)
        self.assertEqual(xml['totals']['failures'],1)
        self.assertEqual(xml['execution'],'report_imported_not_rerun')
        self.assertEqual(campaigns.describe_proof(Path('coverage.xml'),b'<coverage line-rate="0.74"/>')['line_coverage_pct'],74)
        sarif=campaigns.describe_proof(Path('results.sarif'),json.dumps({'version':'2.1.0','runs':[{'results':[{},{}]}]}).encode())
        self.assertEqual(sarif['results_observed'],2)
        self.assertEqual(campaigns.describe_proof(Path('note.md'),b'ok')['recognition'],'document_only')

    def test_bad_evidence_does_not_write_archive(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            with patch.dict(os.environ,{'LOCALAPPDATA':str(root/'state')}):
                with self.assertRaises(ValueError):
                    campaigns.create_campaign(PROJECT,'Campagne impossible',store=root/'store',
                        extra_proofs={'Rejean-McCormick/Konnaxion':[root/'bad.env']},git_probe=False)
            self.assertEqual(list((root/'store').glob('*.zip')) if (root/'store').exists() else [],[])


if __name__=='__main__': unittest.main()
