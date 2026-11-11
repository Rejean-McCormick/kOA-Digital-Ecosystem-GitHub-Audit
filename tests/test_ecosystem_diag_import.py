"""Read-only, private adapter regression tests for kOA ecosystem diagnostic."""
import json
import os
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

from koa_audit import ecosystem_diag as module


def campaign(level=True):
    summary = {
        'schema': module.SOURCE_SCHEMA, 'suite': module.SUITE, 'suite_version': '5.0.0',
        'run_id': '20261110T192300Z-83d16444', 'selection': 'complet', 'verdict': 'PARTIAL',
        'target_repo_root': r'C:\mycode', 'started_at': '2026-11-10T19:23:00+00:00',
        'ended_at': '2026-11-10T19:24:18+00:00', 'coverage': {
            'inventory': {'present': 53, 'declared': 53, 'truncated': 2, 'complete': False},
            'relations': 58, 'api': {'static_calls': 5, 'routes_matched': 0},
            'traces': {'correlated_pairs': 0, 'ik_receipts': 0},
            'journeys': {'declared': 0, 'evidence_complete': 0},
            'global_end_to_end': {'status': 'NON_CERTIFIE', 'explanation': 'private detail'},
        }, 'levels': [{'id': 'N00', 'verdict': 'PARTIAL'}], 'counts': {'PARTIAL': 1}
    }
    result = {'schema': module.LEVEL_SCHEMA, 'suite': module.SUITE, 'run_id': summary['run_id'],
              'level_id': 'N00', 'verdict': 'PARTIAL', 'findings': [{'message': 'SECRET-PRIVATE-MESSAGE'}],
              'target_repo_root': r'C:\mycode\private'}
    return summary, result


class EcosystemDiagImportTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)

    def make_zip(self, bad_level=False):
        summary, detail = campaign()
        if bad_level:
            detail['run_id'] = 'different'
        target = self.base / 'latest.zip'
        with zipfile.ZipFile(target, 'w') as archive:
            archive.writestr('latest/summary.json', json.dumps(summary))
            archive.writestr('latest/levels/N00/result.json', json.dumps(detail))
        return target

    def test_import_zip_sanitized(self):
        record = module.normalize(self.make_zip())
        self.assertEqual(record['coverage']['inventory']['present'], 53)
        self.assertEqual(record['coverage']['relations'], 58)
        self.assertEqual(record['integrity']['consistent_level_results'], 1)
        self.assertEqual(record['qualification']['ecosystem_e2e_certification'], 'NOT_ESTABLISHED')
        dumped = json.dumps(record)
        for prohibited in ('C:\\mycode', 'SECRET-PRIVATE-MESSAGE', 'private detail'):
            self.assertNotIn(prohibited, dumped)

    def test_refuse_mismatched_level(self):
        with self.assertRaisesRegex(ValueError, 'niveaux'):
            module.normalize(self.make_zip(bad_level=True))

    def test_reject_wrong_suite(self):
        summary, _ = campaign()
        summary['suite'] = 'LevelUpDiag-Orgo'
        f = self.base / 'summary.json'
        f.write_text(json.dumps(summary))
        with self.assertRaisesRegex(ValueError, 'ne provient pas'):
            module.normalize(f)

    def test_refuse_ambiguous_zip(self):
        z = self.base / 'twos.zip'
        with zipfile.ZipFile(z, 'w') as archive:
            archive.writestr('a/summary.json', '{}')
            archive.writestr('b/summary.json', '{}')
        with self.assertRaisesRegex(ValueError, 'exactement un'):
            module.normalize(z)

    def test_keep_existing_and_private(self):
        with patch.dict(os.environ, {'LOCALAPPDATA': str(self.base)}):
            record, output = module.import_campaign(self.make_zip())
            self.assertTrue(output.exists())
            self.assertIn('kOA-GitHub-Audit', str(output))
            self.assertEqual(module.local_summary()['latest']['run_id'], record['run_id'])
            again, second = module.import_campaign(self.make_zip())
            self.assertEqual(output, second)
            with self.assertRaisesRegex(ValueError, 'docs'):
                module.save(record, self.base / 'docs' / 'private.json')

    def test_refuse_conflicting_sha(self):
        record, out = module.import_campaign(self.make_zip(), self.base / 'reports' / 'one.json')
        other = dict(record)
        other['integrity'] = dict(record['integrity'], summary_sha256='0'*64)
        with self.assertRaisesRegex(ValueError, 'empreinte'):
            module.save(other, out)

    def test_does_not_certify_even_if_source_passes(self):
        summary, detail = campaign()
        summary['verdict'] = 'PASS'
        summary['counts'] = {'PASS': 1}
        summary['levels'][0]['verdict'] = 'PASS'
        summary['coverage']['global_end_to_end']['status'] = 'CERTIFIE_DECLARED'
        detail['verdict'] = 'PASS'
        z = self.base / 'pass.zip'
        with zipfile.ZipFile(z, 'w') as archive:
            archive.writestr('latest/summary.json', json.dumps(summary))
            archive.writestr('latest/levels/N00/result.json', json.dumps(detail))
        record = module.normalize(z)
        self.assertEqual(record['qualification']['ecosystem_e2e_certification'], 'NOT_ESTABLISHED')


if __name__ == '__main__':
    unittest.main()
