"""Proof-first rules for 35 more owner-provided source snapshots."""
from pathlib import Path
import hashlib,json,os,tempfile,unittest,zipfile
from unittest.mock import patch
from koa_audit import specsheets, validation_board, campaigns, snapshot_runs
ROOT=Path(__file__).resolve().parents[1]

class SmartDump35Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index=specsheets.load(ROOT)
        cls.provenance=json.loads((ROOT/'private_evidence/SMARTDUMP-35-PROVENANCE-2026-10-30.json').read_text('utf8'))

    def test_coverage_47_of_49_without_inventing_other_two(self):
        self.assertEqual(self.index['state'],'verified_index')
        self.assertEqual(len(self.index['repositories']),47)
        self.assertEqual(len(self.provenance['repos']),35)
        for slug in ('Kompose','Kontexte'):
            self.assertEqual(specsheets.for_repository(ROOT,'Rejean-McCormick/'+slug,self.index)['state'],'not_reviewed')

    def test_every_new_feature_has_explicit_hash_and_no_pass(self):
        for row in self.provenance['repos']:
            repo='Rejean-McCormick/'+row['repository']
            sheet=self.index['repositories'][repo]
            self.assertIsNone(sheet['snapshot_commit'])
            self.assertFalse(sheet['tests_executed'])
            self.assertEqual(len(sheet['snapshot_sha256']),64)
            self.assertGreaterEqual(len(sheet['features']),2)
            for feat in sheet['features']+sheet['technical']:
                self.assertFalse(feat['execution_verified'])
                self.assertIn(feat['status'],('code_observed','specification_only'))
                self.assertTrue(feat['sources'])
                for src in feat['sources']+feat['test_definitions']:
                    self.assertEqual(len(src['sha256']),64)
                    self.assertNotIn('\\',src['path'])
                    self.assertFalse(src['path'].startswith('/'))
                    self.assertNotIn('..',src['path'].split('/'))

    def test_conductor_design_only_and_assets_not_backend(self):
        kon=specsheets.for_repository(ROOT,'Rejean-McCormick/Konductor',self.index)
        self.assertTrue(all(f['status']=='specification_only' for f in kon['features']))
        self.assertIn('conception',kon['overview'].lower())
        asset=specsheets.for_repository(ROOT,'Rejean-McCormick/UCKK-Assets',self.index)
        self.assertIn('pas un dépôt applicatif',asset['overview'])
        publish=specsheets.for_repository(ROOT,'Rejean-McCormick/Konstellation-Publisher',self.index)
        self.assertIn('désactivée',publish['overview'])

    def test_validation_board_does_not_auto_certify(self):
        with tempfile.TemporaryDirectory() as tmp:
            b=validation_board.build(ROOT,Path(tmp)/'claims.json',Path(tmp)/'practices.json')
        self.assertEqual(b['official_repositories'],49)
        self.assertEqual(b['functional_specsheets_reviewed'],47)
        self.assertEqual(b['targeted_unit_tests_passed'],45)
        self.assertEqual(b['additional_isolated_test_passes'],127)
        self.assertEqual(b['security_controls_test_verified'],0)
        self.assertEqual(b['source_checked_documentary_jalons'],0)
        for repo in b['repositories']:
            self.assertFalse(repo['security_test_passes'])

    def test_old_verified_runs_not_cloned_to_new_snapshots(self):
        self.assertEqual(len(snapshot_runs.load(ROOT)),3)
        self.assertTrue(all('Rejean-McCormick/'+r['repository'] not in snapshot_runs.load(ROOT)
                            for r in self.provenance['repos']))

    def test_future_campaign_contains_47_sheets_and_preserves_no_git_alignment(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ,{'LOCALAPPDATA':tmp}):
            store=Path(tmp)/'campaigns'
            path=campaigns.create_campaign(ROOT,'Revues 47',store=store,git_probe=False)
            frozen=campaigns.read_campaign(path.stem,store)
            ref=frozen['functional_review']
            self.assertFalse(ref['linked_to_current_commit'])
            with zipfile.ZipFile(path) as z:
                payload=z.read(ref['member'])
            self.assertEqual(hashlib.sha256(payload).hexdigest(),ref['sha256'])
            self.assertEqual(len(json.loads(payload)['repositories']),47)
            self.assertEqual(campaigns.list_campaigns(store)[0]['integrity'],'ok')

    def test_source_index_stays_private(self):
        path=ROOT/'private_evidence/KOA-SPECSHEETS-2026-10-30.json'
        self.assertLess(path.stat().st_size,1_500_000)
        self.assertNotIn('private_evidence',(ROOT/'docs/data/ecosystem.json').read_text('utf8'))
        self.assertNotIn('Konductor_Initial_Technical_Design',(ROOT/'docs/index.html').read_text('utf8'))

if __name__=='__main__':unittest.main()
