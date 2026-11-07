"""Public, read-only GitHub documentation destinations."""
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class GithubDocumentationLinksTests(unittest.TestCase):
    def test_public_urls_and_visibility(self):
        js=(ROOT/'docs/assets/atlas.js').read_text(encoding='utf-8')
        page=(ROOT/'docs/index.html').read_text(encoding='utf-8')
        self.assertIn("root+'#readme'",js)
        self.assertIn("root+'/wiki'",js)
        self.assertIn('githubDocumentationLinks(r.repo)',js)
        self.assertIn('githubDocumentationLinks(current.repo)',js)
        self.assertIn('data-workspace="applications" id="apps"', page)
        self.assertIn('id="repo-list"', page)
        self.assertIn("getJSON('data/documentation-candidates.json?", js)
        self.assertIn('Array.isArray(candidates?.repositories)?candidates.repositories:[]', js)
        self.assertIn('additional_documented:true', js)

    def test_new_candidates_do_not_mutate_official_inventory(self):
        official=json.loads((ROOT/'data/initial_inventory.json').read_text(encoding='utf-8'))
        candidates=json.loads((ROOT/'docs/data/documentation-candidates.json').read_text(encoding='utf-8'))
        self.assertEqual(len(official),49)
        self.assertEqual({x['repo'] for x in candidates['repositories']},{'Rejean-McCormick/Kolor','Rejean-McCormick/Karacter'})
        self.assertFalse({x['repo'] for x in candidates['repositories']}.intersection({x['github_repo'] for x in official}))

if __name__=='__main__':
    unittest.main()
