"""Static regression checks for the public FR/EN GitHub Pages interface."""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


class BilingualPublicationTests(unittest.TestCase):
    def test_both_published_views_have_switch(self):
        for page in ("index.html", "observations.html"):
            html = (DOCS / page).read_text(encoding="utf-8")
            with self.subTest(page=page):
                self.assertEqual(html.count('data-lang="fr"'), 1)
                self.assertEqual(html.count('data-lang="en"'), 1)
                self.assertIn('aria-pressed="false"', html)
                self.assertIn('assets/i18n.js', html)
                self.assertLess(html.index('assets/i18n.js'), html.index('assets/atlas.js' if page == 'index.html' else 'assets/observations.js'))

    def test_translation_table_covers_both_views(self):
        src = (DOCS / "assets/i18n.js").read_text(encoding="utf-8")
        table = re.search(r"const en = (\{.*?\});\s*en\[", src, flags=re.DOTALL)
        self.assertIsNotNone(table)
        entries = json.loads(table.group(1))
        self.assertGreaterEqual(len(entries), 300)
        self.assertEqual(entries['Campagnes'], 'Campaigns')
        self.assertEqual(entries['Wiki GitHub (si disponible)'], 'GitHub Wiki (if available)')
        self.assertEqual(entries['Étayé par preuve'], 'Supported by evidence')
        self.assertNotIn('GitBook', src)
        self.assertIn("localStorage.getItem(storageKey)", src)

    def test_static_publication_boundary(self):
        workflow = (ROOT / '.github/workflows/dashboard-pages.yml').read_text(encoding='utf-8')
        self.assertIn('path: docs', workflow)
        self.assertIn('actions/deploy-pages@', workflow)
        self.assertTrue((DOCS / '.nojekyll').exists())
        self.assertTrue((DOCS / 'PUBLISH_FR_EN.md').exists())


if __name__ == '__main__':
    unittest.main()
