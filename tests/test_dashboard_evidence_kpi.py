"""The atlas must not count a reviewed-but-undocumented case as proven."""
from __future__ import annotations
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class EvidenceCounterTests(unittest.TestCase):
    def test_true_evidence_count_is_primary_kpi(self):
        js = (ROOT/'docs/assets/atlas.js').read_text(encoding='utf8')
        html = (ROOT/'docs/index.html').read_text(encoding='utf8')
        self.assertIn('Jalons étayés par preuve',html)
        self.assertIn('textContent=`${count(evidenced)} / ${count(total*5)}`',js)
        self.assertNotIn('textContent=`${count(assessed)} / ${count(total*5)}`',js)
        self.assertIn('dossiers examinés',js)
        self.assertIn('à documenter',js)
        self.assertIn('Campagne figée du',js)
        self.assertIn('registre actuel :',js)

    def test_245_review_cases_not_245_evidenced_claims(self):
        d = json.loads((ROOT/'private_evidence/KOA-ADJUDICATION-2026-10-30.json').read_text(encoding='utf8'))
        self.assertEqual(len(d['cases']),245)
        self.assertEqual(sum(c['status']=='Étayé par preuve' for c in d['cases']),10)
        self.assertEqual(sum(c['status']=='À documenter' for c in d['cases']),235)
        self.assertEqual(sum(c['status']=='Étayé par preuve' and c['stage']=='production' for c in d['cases']),0)

if __name__=='__main__':unittest.main()
