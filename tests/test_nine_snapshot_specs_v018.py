"""Nine newly supplied ZIPs: bounded traceable observations, not invented certifications."""
import hashlib
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from koa_audit import campaigns, snapshot_runs, specsheets, validation_board

ROOT=Path(__file__).resolve().parents[1]
NEW=('Daat','EncyKlopedia','Interaction-Kernel','kOA-Linux-Koali',
     'Koali-Spaces','Konfid','Konnaxion','Kristal-Framework','Orgo')

class NewSpecsheetTests(unittest.TestCase):
    def test_each_nine_repo_has_source_hashed_specs(self):
        index=specsheets.load(ROOT)
        self.assertEqual(index['state'],'verified_index')
        self.assertEqual(len(index['repositories']),47)
        for slug in NEW:
            with self.subTest(repo=slug):
                row=specsheets.for_repository(ROOT,'Rejean-McCormick/'+slug,index)
                self.assertEqual(row['state'],'snapshot_reviewed')
                self.assertGreaterEqual(len(row['features']),5)
                self.assertGreaterEqual(len(row['technical']),4)
                self.assertIsNone(row['snapshot_commit'])
                self.assertGreaterEqual(len(row['snapshot_sha256']),64)
                for item in row['features']+row['technical']:
                    self.assertFalse(item['execution_verified'])
                    self.assertTrue(item['sources'])
                    for f in item['sources']+item['test_definitions']:
                        self.assertEqual(len(f['sha256']),64)
                        self.assertFalse(f['path'].startswith('/'))

    def test_nine_repos_do_not_award_security_practice_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            board=validation_board.build(ROOT,Path(tmp)/'q.json',Path(tmp)/'p.json')
        self.assertEqual(board['official_repositories'],49)
        self.assertEqual(board['functional_specsheets_reviewed'],47)
        self.assertEqual(board['additional_isolated_test_passes'],127)
        self.assertEqual(board['security_controls_test_verified'],0)
        self.assertEqual(sum(bool(x['isolated_test_run']) for x in board['repositories']),3)
        for rec in board['repositories']:
            if rec['slug'] in NEW:
                self.assertFalse(rec['security_test_passes'])

    def test_no_false_global_feature_pass_when_tests_executed(self):
        for slug in ('Daat','EncyKlopedia','Interaction-Kernel'):
            rec=specsheets.for_repository(ROOT,'Rejean-McCormick/'+slug)
            self.assertTrue(all(not f['execution_verified'] for f in rec['features']))

    def test_archived_junit_matches_manifest_and_fails_closed(self):
        runs=snapshot_runs.load(ROOT)
        self.assertEqual({slug.split('/')[-1]:data['passed'] for slug,data in runs.items()},
                         {'Daat':99,'EncyKlopedia':9,'Interaction-Kernel':19})
        for repo,data in runs.items():
            slug=repo.partition('/')[2]
            content=snapshot_runs.report_for_slug(ROOT,slug)
            self.assertEqual(hashlib.sha256(content).hexdigest(),data['junit_sha256'])
            self.assertFalse(data['git_commit_verified'])
            self.assertTrue(data['test_files'])
        self.assertIsNone(snapshot_runs.report_for_slug(ROOT,'../../tests'))

    def test_campaign_freezes_new_logs_and_index_without_git_conflation(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ,{'LOCALAPPDATA':tmp}):
            store=Path(tmp)/'campaigns'
            created=campaigns.create_campaign(ROOT,'Nouvelle revue des neuf dépôts',store=store,git_probe=False)
            frozen=campaigns.read_campaign(created.stem,store)
            ref=frozen['functional_review']
            self.assertEqual(ref['additional_isolated_tests'],127)
            self.assertEqual(ref['targeted_unit_tests'],45)
            self.assertEqual(len(ref['test_logs']),5)
            self.assertFalse(ref['linked_to_current_commit'])
            self.assertEqual(campaigns.list_campaigns(store)[0]['integrity'],'ok')

if __name__=='__main__':unittest.main()
