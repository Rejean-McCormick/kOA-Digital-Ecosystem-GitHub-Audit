"""Regression tests: immutable evidence, bounded capture, provenance and local collection."""
import json
import os
import shutil
import subprocess
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

from koa_audit import campaigns, evidence_collector

PROJECT=Path(__file__).resolve().parent.parent
REPO='Rejean-McCormick/Orgo'


class ImprovedCampaignTests(unittest.TestCase):
    def test_preflight_rejects_unreadable_campaign_size_no_partial_writes(self):
        with tempfile.TemporaryDirectory() as td:
            store=Path(td)/'campaigns'
            with patch.object(campaigns, 'MAX_CAMPAIGN', 300), patch.dict(os.environ, {'LOCALAPPDATA':str(Path(td)/'state')}):
                with self.assertRaisesRegex(ValueError,'trop volumineuse'):
                    campaigns.create_campaign(PROJECT,'Campagne trop grande',store=store,git_probe=False)
            self.assertFalse(list(store.glob('*.zip')) if store.exists() else [])
            self.assertFalse(list(store.glob('*.tmp')) if store.exists() else [])

    def test_attached_proof_is_cliquable_escaped_and_downloadable(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            proof=root/'test.xml'
            proof.write_text('<testsuite tests="3" failures="0"/>',encoding='utf-8')
            with patch.dict(os.environ,{'LOCALAPPDATA':str(root/'state')}):
                target=campaigns.create_campaign(PROJECT,'Evidence clickable',store=root/'store',git_probe=False,
                    extra_proofs={REPO:[proof]})
            record=campaigns.read_campaign(target.stem,root/'store')['repository_profiles_snapshot']['Orgo']
            self.assertEqual(record['attached_proofs'][0]['summary']['recognition'],'junit_xml_summary')
            info,raw=campaigns.read_proof(target.stem,'Orgo',0,root/'store')
            self.assertEqual(info['sha256'],campaigns._hash(raw))
            self.assertIn(b'tests="3"',raw)
            page=campaigns.render_local_page('/local/campaigns/'+target.stem+'/app/Orgo',root/'store')
            self.assertIn('/proof/Orgo/0',page)
            viewer=campaigns.render_local_page('/local/campaigns/'+target.stem+'/proof/Orgo/0',root/'store')
            self.assertIn('&lt;testsuite',viewer)
            self.assertIn('/download/Orgo/0',viewer)
            self.assertNotIn('<testsuite',viewer)
            with self.assertRaises(ValueError):
                campaigns.read_proof(target.stem,'../Orgo',0,root/'store')
            with self.assertRaises(ValueError):
                campaigns.read_proof(target.stem,'Orgo',1,root/'store')

    def test_version_provenance_same_different_unknown(self):
        previous={'historical_audit':{'recorded_git':{'head':'a'*40}},
                  'observed_git':{'status':'verified_git_origin','head':'a'*40,
                                  'worktree':'tracked_files_clean_untracked_not_checked'}}
        result=campaigns.version_alignment(previous)
        self.assertEqual(result['git_comparison'],'git_commit_same')
        self.assertEqual(result['profile_to_git'],'unknown_independent_snapshot')
        previous['observed_git']['head']='b'*40
        self.assertEqual(campaigns.version_alignment(previous)['git_comparison'],'git_commit_different')
        previous['observed_git']['status']='origin_not_verified'
        self.assertEqual(campaigns.version_alignment(previous)['git_comparison'],'single_git_reference')
        self.assertEqual(campaigns.version_alignment({})['git_comparison'],'unknown')

    def test_comparison_link_and_manual_evidence_changes(self):
        with tempfile.TemporaryDirectory() as td:
            base=Path(td)
            store=base/'store'; state=base/'state'
            qual_file=state/'kOA-GitHub-Audit'/'profiles'/'qualification.json'
            qual_file.parent.mkdir(parents=True)
            with patch.dict(os.environ,{'LOCALAPPDATA':str(state)}):
                old=campaigns.create_campaign(PROJECT,'Ancien état local',store=store,git_probe=False)
                qual_file.write_text(json.dumps({'format':'koa_qualification.evidence.v1','claims':{
                    REPO:{'specified':{'status':'Étayé par preuve','scope':'Définition locale',
                                        'evidence':'CONTRACTS evidence 123', 'reviewed_at':'2026-10-30T00:00:00Z'}}
                }},ensure_ascii=False),encoding='utf-8')
                new=campaigns.create_campaign(PROJECT,'Nouvel état local',store=store,git_probe=False)
            diff=campaigns.compare_campaigns(old.stem,new.stem,store)
            self.assertEqual(diff['totals']['stage_new_evidence'],1)
            self.assertEqual(diff['newer']['coverage']['stages']['specified']['counts']['Étayé par preuve'],1)
            webpage=campaigns.render_local_page(f'/local/campaigns/compare/{old.stem}--{new.stem}',store)
            self.assertIn('Évolution des cinq jalons',webpage)
            self.assertIn('gris',webpage.casefold())
            overview=campaigns.render_local_page('/local/campaigns/'+new.stem,store)
            self.assertIn('qualification',overview.casefold())
            self.assertIn('/local/campaigns/compare/',overview)
            self.assertEqual(campaigns.read_campaign(old.stem,store)['repository_profiles_snapshot']['Orgo']['qualification']['specified']['status'],'Non évalué')

    def test_list_cache_invalidated_and_open_full_verification(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            with patch.dict(os.environ,{'LOCALAPPDATA':str(root/'state')}):
                saved=campaigns.create_campaign(PROJECT,'Campagne stable',store=root/'store',git_probe=False)
            campaigns._LIST_VERIFIED.clear()
            with patch.object(campaigns,'_stream_sha256',wraps=campaigns._stream_sha256) as spy:
                campaigns.list_campaigns(root/'store')
                hashes=spy.call_count
                campaigns.list_campaigns(root/'store')
                self.assertEqual(spy.call_count,hashes)
                campaigns.read_campaign(saved.stem,root/'store')
                self.assertGreater(spy.call_count,hashes)
            with saved.open('ab') as f: f.write(b'alteration')
            self.assertEqual(campaigns.list_campaigns(root/'store')[0]['integrity'],'failed')

    def test_static_collector_uses_verified_git_and_exposes_no_paths(self):
        if not shutil.which('git'): self.skipTest('git unavailable')
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            def git(*args):
                return subprocess.run(['git',*args],cwd=root,capture_output=True,check=True,text=True).stdout.strip()
            git('init','-q');git('config','user.email','test@example.invalid');git('config','user.name','test')
            (root/'README.md').write_text('Hello')
            (root/'app.py').write_text('print(1)')
            (root/'.secret').write_text('TOKEN_PRIVATE_SENTINEL') # intentionally untracked
            git('add','README.md','app.py');git('commit','-qm','initial')
            git('remote','add','origin','https://github.com/Rejean-McCormick/Orgo.git')
            output=evidence_collector.collect(root,REPO)
            self.assertEqual(output['tracked_files'],2)
            self.assertEqual(output['git']['head'],git('rev-parse','HEAD'))
            self.assertEqual(output['optional_tools']['status'],'not_requested')
            text=json.dumps(output)
            self.assertNotIn(str(root),text)
            self.assertNotIn('TOKEN_PRIVATE_SENTINEL',text)
            self.assertNotIn('app.py',text)
            with self.assertRaisesRegex(ValueError,'Origine GitHub'):
                evidence_collector.collect(root,'Rejean-McCormick/Konnaxion')
            true_run=evidence_collector._run
            with patch('koa_audit.evidence_collector.shutil.which',side_effect=lambda item: '/usr/bin/'+item if item in ('scc','lizard') else None),\
                 patch('koa_audit.evidence_collector._run') as run:
                def fake(command,timeout):
                    if command[0].endswith('scc'):
                        return {'status':'ok','data':json.dumps([{'Name':'Python','Count':1,'Code':2,'Comment':0}]).encode()}
                    if command[0].endswith('lizard'):
                        return {'status':'ok','data':b'NLOC,CCN,token,PARAM,length,location,file,function,long_name,start,end\n3,2,14,1,4,loc,file,name,long,1,3\n'}
                    return true_run(command,timeout)
                run.side_effect=fake
                measured=evidence_collector.collect(root,REPO,static_tools=True)
            self.assertEqual(measured['optional_tools']['scc']['status'],'measured')
            self.assertEqual(measured['optional_tools']['lizard']['functions'],1)
            self.assertEqual(measured['optional_tools']['lizard']['max_ccn'],2)
            self.assertEqual(measured['optional_tools']['ctags']['status'],'not_installed')

    def test_static_collector_report_is_source_labeled_not_certified(self):
        source={'format':'koa_evidence.static_metadata.v1','repository':REPO,
                'tracked_files':5,'github_workflow_files':2,
                'git':{'status':'verified_git_origin','head':'a'*40,'worktree':'tracked_changes_present'}}
        details=campaigns.describe_proof(Path('static.json'),json.dumps(source).encode())
        self.assertEqual(details['source_commit_reported'],'a'*40)
        self.assertEqual(details['recognition'],'koa_static_metadata_summary')
        self.assertNotIn('certified',str(details))
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); report=root/'static.json'
            report.write_text(json.dumps(source))
            with patch.dict(os.environ,{'LOCALAPPDATA':str(root/'state')}):
                made=campaigns.create_campaign(PROJECT,'Mesure importée',store=root/'store',git_probe=False,
                      extra_proofs={REPO:[report]})
            record=campaigns.read_campaign(made.stem,root/'store')['repository_profiles_snapshot']['Orgo']
            self.assertEqual(record['attached_proofs'][0]['source_commit'],'a'*40)
            self.assertEqual(record['version_alignment']['profile_to_git'],'unknown_independent_snapshot')


if __name__=='__main__': unittest.main()
