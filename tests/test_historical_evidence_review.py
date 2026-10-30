"""Review is searchable private evidence, never an automatic certificate."""
from __future__ import annotations

import hashlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import zipfile

from koa_audit import campaigns, evidence_review, qualification

ROOT=Path(__file__).resolve().parents[1]


class HistoricalReviewTests(unittest.TestCase):
    def test_complete_49_by_5_and_no_certification(self):
        review=evidence_review.load_review(ROOT)
        self.assertEqual(len(review['repositories']),49)
        self.assertEqual(sum(len(r['stages']) for r in review['repositories']),245)
        self.assertEqual(review['certifications_written'],0)
        counts=evidence_review.report_counts(ROOT)
        self.assertEqual((counts['repositories'],counts['cases']),(49,245))
        self.assertIn('aucun jalon qualifié automatiquement',counts['notice'])

    def test_konnaxion_orgo_e2e_report_is_clickable_and_scoped(self):
        for repo in ('Rejean-McCormick/Konnaxion','Rejean-McCormick/Orgo'):
            case=evidence_review.stage_record(ROOT,repo,'integrated')
            self.assertEqual(case['evidence_level'],'Compte rendu E2E local daté')
            ref,content=evidence_review.read_source(ROOT,repo,'integrated',0)
            self.assertTrue(ref['available'])
            self.assertEqual(hashlib.sha256(content).hexdigest(),ref['sha256'])
            self.assertIn(b'2026-09-21',content)
            self.assertIn('local',case['summary'].lower())

    def test_lack_of_prod_proof_is_not_failure(self):
        stage=evidence_review.stage_record(ROOT,'Rejean-McCormick/Konnaxion','production')
        self.assertFalse(stage['sources'])
        suggestion=evidence_review.suggested_qualification(ROOT,'Rejean-McCormick/Konnaxion','production')
        self.assertFalse(suggestion['source_available'])
        self.assertEqual(suggestion['status'],'Non évalué')
        self.assertIn('aucune pièce',suggestion['evidence'])

    def test_report_reference_not_in_bundle_is_plain_text(self):
        repo='Rejean-McCormick/Akor'
        stage=evidence_review.stage_record(ROOT,repo,'implemented')
        self.assertTrue(stage['sources'])
        ref=evidence_review.source_reference(ROOT,repo,'implemented',0)
        self.assertFalse(ref['available'])
        with self.assertRaises(FileNotFoundError):
            evidence_review.read_source(ROOT,repo,'implemented',0)
        content=evidence_review.render_page(ROOT,'/local/review/app/Akor/implemented')
        self.assertIn('Référence externe non incluse',content)

    def test_review_pages_and_source_escape(self):
        page=evidence_review.render_page(ROOT,'/local/review')
        self.assertEqual(page.count('href="/local/review/app/'),49)
        sub=evidence_review.render_page(ROOT,'/local/review/app/Konnaxion/integrated')
        self.assertIn('2026-09-21',sub)
        self.assertIn('source/0',sub)
        src=evidence_review.render_page(ROOT,'/local/review/app/Konnaxion/integrated/source/0')
        self.assertIn('SHA-256',src)
        self.assertIn('<pre>',src)
        self.assertIn('le contenu du document n’est jamais exécuté',src)
        for url in ('/local/review/app/../../file','/local/review/app/Konnaxion/production/source/0',
                    '/local/review/app/Konnaxion/unsafe'):
            with self.subTest(url=url),self.assertRaises((ValueError,FileNotFoundError)):
                evidence_review.render_page(ROOT,url)

    def test_no_claim_written_by_loading_review(self):
        with tempfile.TemporaryDirectory() as temp:
            with patch.object(qualification,'state_path',return_value=Path(temp)/'qualification.json'):
                evidence_review.load_review(ROOT)
                evidence_review.suggested_qualification(ROOT,'Rejean-McCormick/Orgo','qualified')
                self.assertFalse((Path(temp)/'qualification.json').exists())

    def test_bad_sha_detected_even_when_zip_is_parseable(self):
        with tempfile.TemporaryDirectory() as temp:
            folder=Path(temp)/'private_evidence';folder.mkdir()
            original=evidence_review.archive_path(ROOT)
            with zipfile.ZipFile(original) as zin,zipfile.ZipFile(folder/evidence_review.ARCHIVE_NAME,'w') as zout:
                for name in zin.namelist():
                    raw=zin.read(name)
                    if name=='data/review-49.json':raw=raw+b' '
                    zout.writestr(name,raw)
            with self.assertRaises(ValueError):
                evidence_review.load_review(Path(temp))

    def test_campaign_preserves_review_bundle_only_when_manually_referenced(self):
        with tempfile.TemporaryDirectory() as temp:
            temp=Path(temp)
            reg=temp/'qualification.json'
            repo='Rejean-McCormick/Konnaxion'
            candidate=evidence_review.suggested_qualification(ROOT,repo,'integrated')
            qualification.set_claim(ROOT,repo,'integrated','Étayé par preuve',
                                    candidate['evidence'],candidate['scope'],reg)
            claims=qualification.load_state(reg)
            with patch.object(qualification,'load_state',return_value=claims), \
                 patch.object(campaigns.profiles,'load_state',return_value={'assessments':{}}):
                bundle=campaigns.create_campaign(ROOT,'Campagne avec revue historique',store=temp/'campaigns',git_probe=False)
            cid=bundle.stem
            frozen=campaigns.read_campaign(cid,store=temp/'campaigns')
            ref=frozen['historical_review']
            self.assertEqual(ref['kind'],'historical_owner_review_not_certification')
            archived=campaigns.read_archived_review(cid,store=temp/'campaigns')
            self.assertEqual(hashlib.sha256(archived).hexdigest(),ref['sha256'])
            self.assertEqual(archived,evidence_review.archive_path(ROOT).read_bytes())
            self.assertEqual(frozen['repository_profiles_snapshot']['Konnaxion']['qualification']['integrated']['status'],'Étayé par preuve')
            html=campaigns.render_local_page('/local/campaigns/'+cid,store=temp/'campaigns')
            self.assertIn('Télécharger la revue historique figée',html)

    def test_static_site_does_not_include_private_source_bundle(self):
        public=(ROOT/'docs/index.html').read_text(encoding='utf-8')
        self.assertNotIn('private_evidence',public)
        ignore=(ROOT/'.gitignore').read_text(encoding='utf-8')
        self.assertIn('private_evidence/',ignore)
        self.assertTrue(evidence_review.archive_path(ROOT).is_file())

if __name__=='__main__':unittest.main()
