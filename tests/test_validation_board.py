"""Prevent 'successful tests' and 'green certification' from being inferred."""
import json
import tempfile
import unittest
from pathlib import Path

from koa_audit import evidence_adjudication, profiles, qualification, validation_board

ROOT=Path(__file__).resolve().parents[1]


class ValidationBoardTests(unittest.TestCase):
    def test_unreviewed_has_all_categories_without_false_passes(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            board=validation_board.build(ROOT, root/'q.json', root/'p.json')
        self.assertEqual(board['official_repositories'],49)
        self.assertEqual(board['source_checked_documentary_jalons'],0)
        self.assertEqual(board['security_controls_test_verified'],0)
        self.assertEqual(len(board['repositories']),49)
        for item in board['repositories']:
            self.assertEqual([c['label'] for c in item['categories']],
                ['Tests','Sécurité','Architecture','Implémentation','Intégration','Production'])
            self.assertEqual(next(c for c in item['categories'] if c['label']=='Sécurité')['practice_count'],53)
            self.assertEqual(next(c for c in item['categories'] if c['label']=='Architecture')['practice_count'],33)
            self.assertEqual(item['verified_stages'],0)

    def test_reviewed_sources_only_return_ten_bounded_documentary_checks(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            q=root/'q.json';p=root/'p.json'
            merge=evidence_adjudication.import_documentary_review(ROOT,q)
            self.assertEqual(merge['totals']['evidenced'],10)
            board=validation_board.build(ROOT,q,p)
        self.assertEqual(board['source_checked_documentary_jalons'],10)
        self.assertEqual(sum(x['verified_stages'] for x in board['repositories']),10)
        self.assertEqual(sum(x['source_verified_test'] for x in board['repositories']),2)
        expected={'Daat':1,'EncyKlopedia':1,'Konnaxion':4,'Orgo':4}
        for item in board['repositories']:
            self.assertEqual(item['verified_stages'],expected.get(item['slug'],0))
            for category in item['categories']:
                for s in category['stages']:
                    if s['source_verified']:
                        self.assertTrue(s['source_link'].startswith('/local/review/app/'))
                        self.assertRegex(s['source_sha256'],r'^[a-f0-9]{64}$')
                        self.assertEqual(s['version_alignment'],'non attestée')
                        self.assertTrue(s['scope'])
                    if s['id']=='production':self.assertFalse(s['source_verified'])

    def test_applied_security_practice_is_not_pass(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);q=root/'q.json';p=root/'p.json'
            profiles.set_assessment(ROOT,'Rejean-McCormick/Orgo','SEC-01','Appliqué',
                'Évaluation déclarée : référence historique insuffisante pour un PASS', p)
            board=validation_board.build(ROOT,q,p)
        orgo=next(x for x in board['repositories'] if x['slug']=='Orgo')
        security=next(c for c in orgo['categories'] if c['label']=='Sécurité')
        self.assertEqual(security['evaluated_practices'],1)
        item=next(x for x in security['practices'] if x['id']=='SEC-01')
        self.assertEqual(item['status'],'Appliqué')
        self.assertFalse(item['source_verified'])
        self.assertEqual(board['security_controls_test_verified'],0)

    def test_forged_source_in_user_state_does_not_turn_green(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);q=root/'q.json';p=root/'p.json'
            qualification.set_claim(ROOT,'Rejean-McCormick/Konnaxion','qualified',
                'Étayé par preuve','Essai local déclaré sans source originale hashée','Périmètre fictif',q)
            board=validation_board.build(ROOT,q,p)
        k=next(x for x in board['repositories'] if x['slug']=='Konnaxion')
        self.assertFalse(k['source_verified_test'])
        self.assertEqual(k['verified_stages'],0)
        self.assertEqual(board['source_checked_documentary_jalons'],0)

    def test_historical_ci_success_only_at_same_observed_sha(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            board=validation_board.build(ROOT,root/'q.json',root/'p.json')
        self.assertEqual(board['historical_ci_success_on_observed_head'],3)
        matched=[x['slug'] for x in board['repositories']
                 if x['historical_ci'] and x['historical_ci']['success_observed']]
        self.assertEqual(sorted(matched),['EncyKlopedia','Koali-Control-Panel','Koali-Scenario-Mosaic'])
        docs=next(x for x in board['repositories'] if x['slug']=='initkoa-docs')['historical_ci']
        self.assertEqual(docs['conclusion'],'success')
        self.assertFalse(docs['success_observed']) # old CI SHA != observed repo head
        self.assertFalse(docs['same_observed_head'])

    def test_no_inference_from_github_ci_to_qualification(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            board=validation_board.build(ROOT,root/'q.json',root/'p.json')
        enc=next(x for x in board['repositories'] if x['slug']=='EncyKlopedia')
        self.assertTrue(enc['historical_ci']['success_observed'])
        self.assertEqual(enc['verified_stages'],0)
        self.assertFalse(enc['source_verified_test'])

    def test_local_only_api_and_layout(self):
        launcher=(ROOT/'kOA_GitHub_Audit_Launcher.pyw').read_text(encoding='utf-8')
        html=(ROOT/'docs/index.html').read_text(encoding='utf-8')
        js=(ROOT/'docs/assets/atlas.js').read_text(encoding='utf-8')
        self.assertIn('route == "/api/validation/board"',launcher)
        self.assertIn('validation_board.build(ROOT)',launcher)
        self.assertIn('id="validations"',html)
        self.assertIn('id="validation-detail"',html)
        self.assertIn("getJSON('/api/validation/board?at='",js)
        self.assertNotIn('validation_board.private.v1', (ROOT/'docs/data/ecosystem.json').read_text(encoding='utf-8'))

if __name__=='__main__':unittest.main()
