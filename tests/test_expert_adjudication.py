"""Evidence-bound review; respect existing user decisions, no Git or source execution."""
from __future__ import annotations
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from koa_audit import evidence_adjudication as expert, evidence_review, qualification, campaigns

ROOT=Path(__file__).resolve().parents[1]


class ExpertReviewTests(unittest.TestCase):
    def test_245_complete_with_ten_documentary_support_and_no_prod(self):
        d=expert.load(ROOT)
        self.assertEqual((len(d['cases']),d['summary']['evidenced_scoped'],d['summary']['to_document']),(245,10,235))
        self.assertEqual(sum(c['status']=='Étayé par preuve' and c['stage']=='production' for c in d['cases']),0)
        self.assertTrue(all(c['version_alignment']=='not_attested' for c in d['cases']))

    def test_primary_sources_are_really_read_sha_verified(self):
        d=expert.load(ROOT)
        originals={c['source']['sha256'] for c in d['cases'] if c['source']}
        self.assertGreaterEqual(len(originals),3)
        for c in d['cases']:
            if c['status']=='Étayé par preuve':
                self.assertEqual(c['review_coverage'],'original_primary_document_read_and_sha_verified')
                self.assertTrue(len(c['source']['sha256'])==64)

    def test_atomic_import_and_idempotency(self):
        with tempfile.TemporaryDirectory() as temp:
            target=Path(temp)/'profiles/qualification.json'
            first=expert.import_documentary_review(ROOT,target)
            self.assertEqual((first['added'],first['preserved']), (245,0))
            self.assertEqual(first['totals']['evidenced'],10)
            stable=target.read_bytes()
            second=expert.import_documentary_review(ROOT,target)
            self.assertEqual((second['added'],second['preserved']), (0,245))
            self.assertEqual(target.read_bytes(),stable)
            r=qualification.get_claim(ROOT,'Rejean-McCormick/Konnaxion','qualified',target)
            self.assertEqual(r['status'],'Étayé par preuve')
            self.assertIn('NON établi',r['evidence'])
            self.assertIn('2026-09-21',r['scope'])

    def test_preserve_preexisting_manual_decisions_and_backup(self):
        with tempfile.TemporaryDirectory() as temp:
            path=Path(temp)/'qualification.json'
            qualification.set_claim(ROOT,'Rejean-McCormick/Konnaxion','integrated','À documenter',
                                    'Ma revue personnelle', 'Mon périmètre',path)
            original=path.read_bytes()
            result=expert.import_documentary_review(ROOT,path)
            self.assertEqual((result['added'],result['preserved']), (244,1))
            rec=qualification.get_claim(ROOT,'Rejean-McCormick/Konnaxion','integrated',path)
            self.assertEqual(rec['evidence'],'Ma revue personnelle')
            self.assertEqual(rec['status'],'À documenter')
            self.assertEqual(path.with_name(path.name+'.before-documentary-review-20261030.bak').read_bytes(),original)
            self.assertEqual(result['totals']['evidenced'],9)

    def test_report_pages_link_to_primary_document_even_if_prior_review_omitted_it(self):
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as tmp:
            target=Path(tmp)/'qualification.json'
            expert.import_documentary_review(ROOT,target)
            with patch.object(qualification,'state_path',return_value=target):
                page=evidence_review.render_page(ROOT,'/local/review/app/Konnaxion/implemented')
        self.assertIn('source historique, commit des clones NON établi',page)
        self.assertIn('/local/review/app/Konnaxion/implemented/expert',page)
        original=evidence_review.render_page(ROOT,'/local/review/app/Konnaxion/implemented/expert')
        self.assertIn('KONNAXION &lt;-&gt; ORGO IK E2E PASS',original)
        self.assertIn('SHA-256',original)
        with self.assertRaises(FileNotFoundError):
            evidence_review.render_page(ROOT,'/local/review/app/Konnaxion/production/expert')

    def test_campaign_can_freeze_ten_scoped_decisions_without_rewriting_old(self):
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as temp:
            store=Path(temp)/'campaigns'
            state_path=Path(temp)/'qualification.json'
            expert.import_documentary_review(ROOT,state_path)
            known=qualification.load_state(state_path)
            with patch.object(campaigns.qualification,'load_state',return_value=known), \
                 patch.object(campaigns.profiles,'load_state',return_value={'assessments':{}}):
                zip_path=campaigns.create_campaign(ROOT,'Revue documentaire 2026-10-30',store=store,git_probe=False)
            snap=campaigns.read_campaign(zip_path.stem,store=store)
            self.assertEqual(snap['repository_profiles_snapshot']['Konnaxion']['qualification']['qualified']['status'],'Étayé par preuve')
            self.assertIn('historical_review',snap)
            self.assertEqual(snap['repository_profiles_snapshot']['Konnaxion']['qualification']['production']['status'],'À documenter')

if __name__=='__main__':unittest.main()
