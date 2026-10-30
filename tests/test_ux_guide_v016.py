"""Guide v2 UX-01/05/15-18: keep one dominant journey and preserve safeguards."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class UXGuideTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (ROOT/'docs/index.html').read_text(encoding='utf-8')
        cls.js = (ROOT/'docs/assets/atlas.js').read_text(encoding='utf-8')
        cls.launcher = (ROOT/'kOA_GitHub_Audit_Launcher.pyw').read_text(encoding='utf-8')

    def test_three_primary_intentions_not_ten_competing_tabs(self):
        self.assertEqual(self.html.count('class="workspace-nav'), 3)
        for name in ('validations','applications','campagnes'):
            self.assertIn(f'data-nav="{name}"',self.html)
        self.assertEqual(self.launcher.count('self.tabs.add('),4)
        self.assertIn('self.dossier_tabs.add(',self.launcher)
        self.assertIn('self.advanced_tabs.add(',self.launcher)

    def test_context_navigation_keeps_old_deep_links(self):
        for anchor in ('#validations','#apps','#cartographie','#qualification','#historique-campagnes'):
            self.assertIn(anchor,self.js)
        self.assertIn("window.addEventListener('hashchange'",self.js)
        self.assertIn("setWorkspace('applications','#apps')",self.js)
        self.assertIn('self._open_profiles_page()',self.launcher)

    def test_reviewed_practices_are_progressively_disclosed(self):
        self.assertIn("el('details','validation-practices')",self.js)
        self.assertIn('source_verified',self.js)
        self.assertIn('source_sha256',self.js)
        self.assertIn('Les pièces historiques vérifiées ne sont pas automatiquement liées au commit actuel',self.html)

    def test_expert_tools_and_publication_preserved_but_secondary(self):
        self.assertIn('self._build_dashboard_settings(settings_tab)',self.launcher)
        self.assertIn('self._sync_dashboard',self.launcher)
        self.assertIn('self._run_dashboard',self.launcher)
        self.assertIn('self._run_triage',self.launcher)
        self.assertIn('self._build_campaigns(campaigns_tab)',self.launcher)
        self.assertIn("historyLink.hidden=!qualification",self.js)

if __name__ == '__main__':unittest.main()
