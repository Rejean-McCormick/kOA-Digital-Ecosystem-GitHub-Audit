"""Readable AI-reviewed validations with no manual confirmation step."""
import tempfile
import unittest
from pathlib import Path
from koa_audit import validation_board

ROOT=Path(__file__).resolve().parents[1]

class AutomaticValidationTests(unittest.TestCase):
    def test_source_verified_stages_are_automatic_without_existing_registry(self):
        with tempfile.TemporaryDirectory() as tmp:
            q=Path(tmp)/'missing-qualification.json'
            board=validation_board.build(ROOT,q,Path(tmp)/'missing-practices.json')
            self.assertFalse(q.exists())
        self.assertEqual(board['source_checked_documentary_jalons'],10)
        self.assertEqual(board['security_controls_test_verified'],0)
        assert all(c['source_sha256'] and c['source_link']
                   for r in board['repositories'] for cat in r['categories']
                   for c in cat['stages'] if c['source_verified'])
        assert all(c['display']=='✓ Validé'
                   for r in board['repositories'] for cat in r['categories']
                   for c in cat['stages'] if c['source_verified'])

    def test_dashboard_does_not_ask_for_manual_approval_or_claim_missing_test_pass(self):
        script=(ROOT/'docs/assets/atlas.js').read_text(encoding='utf-8')
        page=(ROOT/'docs/index.html').read_text(encoding='utf-8')
        self.assertNotIn('exécution non attestée', script)
        self.assertIn("'Tests : à vérifier'",script)
        self.assertIn('✓ Validé',script)
        self.assertIn('sans validation manuelle',page)

if __name__ == '__main__': unittest.main()
