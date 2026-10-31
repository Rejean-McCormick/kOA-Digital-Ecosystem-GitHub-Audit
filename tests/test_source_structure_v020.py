"""Regression controls for the corrected, conservative source-structure view."""
import hashlib
import os
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch
from koa_audit import source_structure, specsheets, validation_board, campaigns

ROOT = Path(__file__).resolve().parents[1]

class SourceStructureReviewTests(unittest.TestCase):
    def test_47_zip_identity_bound_structures_and_unknown_repos(self):
        index=source_structure.load(ROOT)
        self.assertEqual(index['state'],'verified_structure')
        self.assertEqual(len(index['repositories']),47)
        sheets=specsheets.load(ROOT)['repositories']
        self.assertEqual(set(index['repositories']),set(sheets))
        for key,entry in index['repositories'].items():
            self.assertEqual(entry['snapshot_sha256'],sheets[key]['snapshot_sha256'])
            self.assertGreaterEqual(entry['classified_files'],0)
            self.assertEqual(entry['classified_files'],sum(x['file_count'] for x in entry['roles']))
            for role in entry['roles']:
                self.assertEqual(role['module_count'],len(role['modules']))
                self.assertTrue(all('execution_verified' not in mod for mod in role['modules']))
        self.assertEqual(source_structure.for_repository(ROOT,'Rejean-McCormick/Kompose')['state'],'not_reviewed')
        self.assertEqual(source_structure.for_repository(ROOT,'Rejean-McCormick/Kontexte')['state'],'not_reviewed')

    def test_review_corrections_are_source_limited(self):
        data=specsheets.load(ROOT)
        self.assertEqual(data['state'],'verified_index')
        skope=data['repositories']['Rejean-McCormick/Skope']
        self.assertFalse(any('Prévisualiser un graphe' in x['title'] for x in skope['features']))
        geo=next(x for x in skope['features'] if 'portée géographique' in x['title'])
        self.assertEqual(geo['status'],'specification_only')
        sentient=data['repositories']['Rejean-McCormick/SenTient']
        self.assertFalse(any('Rechercher des entités Wikidata' in x['title'] for x in sentient['features']))
        self.assertTrue(any('dumps Wikidata' in x['title'] for x in sentient['features']))
        for repo,row in data['repositories'].items():
            for f in row['features']+row['technical']:
                if f['status']=='code_observed':
                    self.assertTrue(any(not s['path'].startswith(('tests/','test/','docs/','wiki/','examples/'))
                        and '/tests/' not in s['path'] for s in f['sources']))
                self.assertFalse(f['execution_verified'])

    def test_reference_counts_do_not_become_qualification(self):
        with tempfile.TemporaryDirectory() as t:
            board=validation_board.build(ROOT,Path(t)/'q.json',Path(t)/'p.json')
        self.assertEqual(board['functional_specsheets_reviewed'],47)
        self.assertEqual(board['security_controls_test_verified'],0)
        self.assertEqual(board['targeted_unit_tests_passed']+board['additional_isolated_test_passes'],172)
        self.assertEqual(board['source_structure_repositories'],47)
        self.assertGreater(board['source_structure_files_classified'],4000)
        self.assertEqual(board['source_checked_documentary_jalons'],0)

    def test_modified_structure_file_fails_closed(self):
        with tempfile.TemporaryDirectory() as t:
            dest=Path(t)/'private_evidence';dest.mkdir()
            original=(ROOT/'private_evidence'/source_structure.BUNDLE).read_bytes()
            (dest/source_structure.BUNDLE).write_bytes(original+b'\n')
            self.assertEqual(source_structure.load(Path(t))['state'],'unavailable')

    def test_new_campaign_freezes_exact_source_map_with_hash(self):
        with tempfile.TemporaryDirectory() as t, patch.dict(os.environ,{'LOCALAPPDATA':t}):
            campaign=campaigns.create_campaign(ROOT,'Revue systématique',store=Path(t)/'campaigns',git_probe=False)
            details=campaigns.read_campaign(campaign.stem,Path(t)/'campaigns')
            ref=details['functional_review']['source_structure']
            self.assertFalse(ref['linked_to_current_commit'])
            with zipfile.ZipFile(campaign) as z:
                source=z.read(ref['member'])
                self.assertEqual(hashlib.sha256(source).hexdigest(),ref['sha256'])
            self.assertEqual(source,(ROOT/'private_evidence'/source_structure.BUNDLE).read_bytes())

if __name__=='__main__':unittest.main()
