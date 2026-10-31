"""The dated publication UI reuses the existing local repository explorer."""
from __future__ import annotations
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from koa_audit.publication_snapshots import _generate_index, Capture, _publish_from_captures, republish_current

class PublicationViewerTests(unittest.TestCase):
    def test_same_local_directory_detail_shell_for_current_and_archive(self):
        m = {'release_id':'20261031T170000Z-1-1','published_at':'2026-10-31T17:00:00Z','repos':[{}], 'selected':['Owner/Kolor']}
        for prefix, styles, uri in [('', '../assets/', '../data/publication-current.json'),
                                    ('../../','../../../assets/','manifest.json')]:
            html = _generate_index(m,prefix)
            for marker in ('class=\'explorer-grid\'',"class='directory'", "class='detail publication-detail'",
                           "class='repo-list'", "id='published-repo-search'", "id='published-detail'",
                           styles+'atlas.css', styles+'i18n.js', styles+'publication-viewer.js', uri):
                self.assertIn(marker, html)
            self.assertNotIn("class='repository'",html)
            self.assertNotIn('https://api.github.com',html)

    def test_republish_changes_only_current_html(self):
        with TemporaryDirectory() as t:
            docs = Path(t) / 'docs'
            capture = lambda name: Capture(name, 'a'*40, {'README.md': '# 1'})
            _publish_from_captures(docs, ['Owner/Kolor'], 'all', capture, '20261031T170000Z-1-1', '2026-10-31T17:00:00Z')
            ptr = (docs/'data/publication-current.json').read_bytes()
            archived = (docs/'publications/releases/20261031T170000Z-1-1/manifest.json').read_bytes()
            (docs/'publications/index.html').write_text('OUTDATED UI')
            republish_current(docs)
            self.assertIn('explorer-grid', (docs/'publications/index.html').read_text())
            self.assertEqual(ptr, (docs/'data/publication-current.json').read_bytes())
            self.assertEqual(archived, (docs/'publications/releases/20261031T170000Z-1-1/manifest.json').read_bytes())

    def test_frozen_manifest_is_only_data_source(self):
        with TemporaryDirectory() as t:
            docs = Path(t)/'docs'
            capture = lambda name: Capture(name,'a'*40,{'README.md':'# Kolor', 'docs/overview.md':'Résumé'},wiki={'Home.md':'Hello'},wiki_revision='b'*40)
            m = _publish_from_captures(docs,['Owner/Kolor'],'selected',capture,'20261031T170000Z-1-1','2026-10-31T17:00:00Z')
            self.assertEqual(len(m['repos']),1)
            current=(docs/'publications/index.html').read_text()
            old=(docs/'publications/releases/20261031T170000Z-1-1/index.html').read_text()
            self.assertIn('data-pointer-url=\'../data/publication-current.json\'',current)
            self.assertIn("data-manifest-url='manifest.json'",old)
            self.assertNotIn('# Kolor',current)
            self.assertEqual(len(m['repos'][0]['documents']),3)

if __name__ == '__main__': unittest.main()
