"""Guardrails: implementation and test definitions never become certification."""
import hashlib
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from koa_audit import specsheets, spec_tests, validation_board

ROOT = Path(__file__).resolve().parents[1]


class FunctionalSpecificationTests(unittest.TestCase):
    def test_three_exact_snapshot_specs_and_all_49_repositories(self):
        with tempfile.TemporaryDirectory() as tmp:
            board = validation_board.build(ROOT,Path(tmp)/'q.json',Path(tmp)/'p.json')
        self.assertEqual(board['official_repositories'],49)
        self.assertEqual(board['functional_specsheets_reviewed'],47)
        self.assertEqual(board['additional_isolated_test_passes'],127)
        self.assertEqual(board['targeted_unit_tests_passed'],45)
        by_slug={x['slug']:x for x in board['repositories']}
        self.assertEqual(len(by_slug['KonnaxionDiag']['specsheet']['features']),4)
        self.assertEqual(len(by_slug['Konnaxion-Capsule-Manager']['specsheet']['features']),6)
        self.assertEqual(len(by_slug['Konnaxion-Worlds']['specsheet']['features']),6)
        self.assertEqual(by_slug['Orgo']['specsheet']['state'],'snapshot_reviewed')
        self.assertEqual(len(by_slug['Orgo']['specsheet']['features']),7)
        self.assertEqual(board['security_controls_test_verified'],0)

    def test_present_feature_is_never_marked_passed(self):
        data=specsheets.load(ROOT)
        self.assertEqual(data['state'],'verified_index')
        for repo,item in data['repositories'].items():
            self.assertIsNone(item['snapshot_commit'])
            self.assertFalse(item['tests_executed'])
            for f in item['features']:
                self.assertFalse(f['execution_verified'])
                self.assertIn(f['status'],{'code_observed','specification_only'})
                self.assertTrue(f['sources'])
                for source in f['sources']+f['test_definitions']:
                    self.assertEqual(len(source['sha256']),64)
                    self.assertFalse(source['path'].startswith('/'))

    def test_vote_is_only_a_manifest_in_snapshot(self):
        spec=specsheets.for_repository(ROOT,'Rejean-McCormick/Konnaxion-Worlds')
        vote=next(x for x in spec['features'] if 'vote' in x['title'].lower())
        self.assertEqual(vote['status'],'specification_only')
        self.assertFalse(vote['test_definitions'])
        self.assertFalse(vote['execution_verified'])

    def test_45_targeted_checks_are_source_and_junit_bound(self):
        runs=spec_tests.load(ROOT)
        self.assertEqual(runs['Rejean-McCormick/KonnaxionDiag']['passed'],3)
        self.assertEqual(runs['Rejean-McCormick/Konnaxion-Capsule-Manager']['passed'],42)
        self.assertTrue(all(r['git_commit_verified'] is False for r in runs.values()))
        for r in runs.values():
            self.assertTrue(r['test_files'])
            self.assertEqual(len(r['junit_sha256']),64)

    def test_junit_link_is_only_a_local_endpoint(self):
        r=spec_tests.load(ROOT)['Rejean-McCormick/KonnaxionDiag']
        self.assertEqual(r['junit_link'],'/local/spec-tests/KonnaxionDiag')
        data=spec_tests.report_for_slug(ROOT,'KonnaxionDiag')
        self.assertIn(b'tests="3"',data)
        self.assertNotIn(b'hostname',data)
        self.assertIsNone(spec_tests.report_for_slug(ROOT,'../../private_evidence'))

    def test_snapshot_index_tamper_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest=Path(tmp)/'private_evidence';dest.mkdir()
            raw=(ROOT/'private_evidence'/specsheets.BUNDLE).read_bytes()
            (dest/specsheets.BUNDLE).write_bytes(raw+b' ')
            self.assertEqual(specsheets.load(Path(tmp))['repositories'],{})

    def test_junit_tamper_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest=Path(tmp)/'private_evidence';(dest/'test_reports').mkdir(parents=True)
            shutil.copy(ROOT/'private_evidence'/spec_tests.MANIFEST,dest/spec_tests.MANIFEST)
            for p in (ROOT/'private_evidence/test_reports').iterdir():
                shutil.copy(p,dest/'test_reports'/p.name)
            self.assertEqual(len(spec_tests.load(Path(tmp))),2)
            with (dest/'test_reports/Capsule-Manager.junit.xml').open('ab') as out:
                out.write(b'corrupted')
            self.assertEqual(spec_tests.load(Path(tmp)),{})

    def test_only_loopback_can_open_raw_junit(self):
        launcher=(ROOT/'kOA_GitHub_Audit_Launcher.pyw').read_text(encoding='utf-8')
        self.assertIn('"/local/spec-tests/"',launcher)
        self.assertIn('spec_tests.report_for_slug(ROOT, slug)',launcher)
        self.assertIn('self.client_address[0] not in ("127.0.0.1", "::1")',launcher)
        assert 'private_evidence' not in (ROOT/'docs/data/ecosystem.json').read_text(encoding='utf-8')


if __name__=='__main__': unittest.main()

class FrozenFunctionalEvidenceTest(unittest.TestCase):
    def test_new_campaign_contains_frozen_specs_and_junit_proofs(self):
        import os
        import zipfile
        from unittest.mock import patch
        from koa_audit import campaigns
        with tempfile.TemporaryDirectory() as tmp:
            folder=Path(tmp)
            with patch.dict(os.environ, {'LOCALAPPDATA':str(folder/'state')}):
                made=campaigns.create_campaign(ROOT,'Fiche fonctionnelle contrôlée',store=folder/'campaigns',git_probe=False)
            snapshot=campaigns.read_campaign(made.stem,folder/'campaigns')
            ref=snapshot['functional_review']
            self.assertEqual(ref['targeted_unit_tests'],45)
            self.assertIs(ref['linked_to_current_commit'],False)
            with zipfile.ZipFile(made) as z:
                self.assertIn(ref['member'],z.namelist())
                self.assertEqual(hashlib.sha256(z.read(ref['member'])).hexdigest(),ref['sha256'])
                self.assertEqual(len(ref['test_logs']),5)
                self.assertEqual(ref['additional_isolated_tests'],127)
                for log in ref['test_logs']:
                    self.assertEqual(hashlib.sha256(z.read(log['member'])).hexdigest(),log['sha256'])
            self.assertEqual(campaigns.list_campaigns(folder/'campaigns')[0]['integrity'],'ok')
