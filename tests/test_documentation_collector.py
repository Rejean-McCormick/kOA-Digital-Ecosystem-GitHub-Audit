"""Documentation graph collector: classification, provenance and safety."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile, ZipInfo
from koa_audit.documentation_collector import collect_zip, write_private_index


class DocumentationCollectorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.dir = Path(self.tmp.name)
        self.inventory = self.dir / 'inventory.json'
        self.inventory.write_text(json.dumps([{'github_repo':'owner/Orgo'}]),encoding='utf-8')

    def archive(self, entries):
        p = self.dir / 'input.zip'
        with ZipFile(p, 'w') as z:
            for k,v in entries.items():
                z.writestr(k,v)
        return p

    def test_candidates_and_duplicate_snapshots(self):
        z=self.archive({'repos/Orgo/README.md':'# Orgo',
                        'repos/Kolor/README.md':'# Kolor',
                        'repos/Kolor/wiki/interne-wiki/Home.md':'# Wiki',
                        'repos/Karacter/docs/00_VISION.md':'# Vision',
                        'repos/Orgo-a6379623/README.md':'# old clone',
                        'repos/Kolor/src/secret.py':'PRIVATE',
                        'repos/Karacter/.env':'SECRET'})
        r=collect_zip(z,self.inventory)
        names={e['snapshot_folder']:e for e in r['repositories']}
        self.assertEqual(r['inventory_baseline_count'],1)
        self.assertEqual(names['Orgo']['discovery_status'],'inventory_match')
        self.assertEqual(names['Orgo-a6379623']['discovery_status'],'snapshot_copy_candidate')
        self.assertEqual(names['Kolor']['discovery_status'],'unregistered_candidate')
        self.assertEqual(names['Karacter']['documentation_count'],1)
        self.assertEqual(names['Kolor']['documentation_count'],2)
        self.assertEqual(names['Orgo']['github_links']['documentation'], 'https://github.com/owner/Orgo#readme')
        self.assertEqual(names['Orgo']['github_links']['wiki'], 'https://github.com/owner/Orgo/wiki')
        self.assertFalse(names['Orgo']['github_links']['availability_verified'])
        self.assertIsNone(names['Kolor']['github_links'])  # not yet admitted to inventory
        self.assertIsNone(names['Orgo-a6379623']['github_links'])
        s=json.dumps(r)
        self.assertNotIn('PRIVATE',s)
        self.assertNotIn('SECRET',s)
        self.assertEqual(r['source']['git_revision_verified'],False)
        self.assertEqual(r['repositories'],collect_zip(z,self.inventory)['repositories'])

    def test_unsafe_and_collision(self):
        z=self.archive({'repos/Orgo/../README.md':'unsafe',
                        'repo/fake/README.md':'other',
                        'repos/Orgo/README.md':'good'})
        r=collect_zip(z,self.inventory)
        self.assertEqual(r['repositories'][0]['documentation_count'],1)
        self.assertGreaterEqual(r['discarded']['invalid_or_outside_repo'],1)
        p=self.dir/'collision.zip'
        with ZipFile(p,'w') as f:
            f.writestr('repos/Kolor/README.md','a')
            f.writestr('repos/Kolor/readme.md','b')
        with self.assertRaises(ValueError): collect_zip(p,self.inventory)

    def test_write_only_private_new_file(self):
        r={'format':'test'}
        out=self.dir/'private'/'document-index.json'
        write_private_index(r,out)
        self.assertTrue(out.exists())
        with self.assertRaises(FileExistsError): write_private_index(r,out)
        with self.assertRaises(ValueError): write_private_index(r,self.dir/'docs'/'index.json')

if __name__ == '__main__':
    unittest.main()
