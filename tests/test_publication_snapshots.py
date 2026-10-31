"""Offline tests: all build, selected build, cached failures, rollback and safety."""
from __future__ import annotations

import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from koa_audit.publication_snapshots import (
    Capture, _publish_from_captures, allowed_repositories, rollback,
    selected_repositories,
)


class PublicationTests(unittest.TestCase):
    def test_known_only_public(self):
        with TemporaryDirectory() as t:
            t = Path(t)
            (t/'in.json').write_text(json.dumps([
                {'github_repo':'Owner/Alpha','scope':'PUBLIC'},
                {'github_repo':'Owner/Private','scope':'PRIVATE'},
            ]))
            (t/'extras.json').write_text(json.dumps([{'github_repo':'Owner/Kolor','scope':'PUBLIC'}]))
            allowed = allowed_repositories(t/'in.json', t/'extras.json')
            self.assertEqual(allowed, ['Owner/Alpha','Owner/Kolor'])
            self.assertEqual(selected_repositories(allowed,'selected','Kolor,Alpha'), ['Owner/Kolor','Owner/Alpha'])
            with self.assertRaises(ValueError):
                selected_repositories(allowed,'selected','../../escape')

    def capture(self, name: str):
        return Capture(name, 'a'*40, {'README.md': f'# {name}\n<iframe src="https://evil.com"></iframe>'},
                       wiki_revision='b'*40, wiki={'Home.md': 'Hello wiki'})

    def build(self, docs: Path, repos: list[str], id: str, fetch=None):
        return _publish_from_captures(docs, repos, 'selected', fetch or self.capture,
                                      id, '2026-10-31T17:00:00Z')

    def test_snapshot_html_escapes_source_and_is_dated(self):
        with TemporaryDirectory() as tmp:
            docs = Path(tmp)/'docs'
            result = self.build(docs, ['Owner/Kolor'], '20261031T170000Z-1-1')
            self.assertEqual(result['capture_successes'],1)
            pages = result['repos'][0]['documents']
            self.assertEqual(len(pages),2)
            self.assertEqual(result['repos'][0]['wiki_revision'],'b'*40)
            html = (docs/'publications'/pages[0]['page']).read_text()
            self.assertNotIn('<iframe',html)
            self.assertIn('&lt;iframe',html)
            self.assertIn('2026-10-31T17:00:00Z', (docs/'publications'/'index.html').read_text())
            self.assertIn('gitbook',str(list((docs/'publications'/'releases').rglob('SUMMARY.md'))))
            self.assertTrue((docs/'data'/'publication-current.json').exists())

    def test_selected_retains_previous_source_without_copy_or_live_reload(self):
        with TemporaryDirectory() as tmp:
            docs = Path(tmp)/'docs'
            self.build(docs,['Owner/Kolor'],'20261031T170000Z-1-1')
            old = json.loads((docs/'publications'/'releases'/'20261031T170000Z-1-1'/'manifest.json').read_text())
            self.build(docs,['Owner/Karacter'],'20261031T170200Z-2-1')
            updated = json.loads((docs/'publications'/'releases'/'20261031T170200Z-2-1'/'manifest.json').read_text())
            by_repo = {r['repo']:r for r in updated['repos']}
            self.assertEqual(by_repo['Owner/Kolor']['status'],'retained')
            self.assertEqual(by_repo['Owner/Kolor']['documents'],old['repos'][0]['documents'])
            self.assertTrue((docs/'publications'/old['repos'][0]['documents'][0]['page']).exists())
            self.assertEqual(len(updated['repos']),2)
            summary = (docs/'publications'/'releases'/'20261031T170200Z-2-1'/'gitbook'/'SUMMARY.md').read_text()
            self.assertIn('Owner/Kolor', summary)
            self.assertIn('Owner/Karacter', summary)

    def test_failed_selected_repo_keeps_old_dated_copy(self):
        with TemporaryDirectory() as tmp:
            docs = Path(tmp)/'docs'
            self.build(docs,['Owner/Kolor'],'20261031T170000Z-1-1')
            def broken(name):
                if name == 'Owner/Kolor':
                    raise RuntimeError('live repo broken')
                return self.capture(name)
            result = self.build(docs,['Owner/Kolor','Owner/Karacter'],'20261031T170200Z-2-1',broken)
            by_repo = {r['repo']:r for r in result['repos']}
            self.assertEqual(by_repo['Owner/Kolor']['status'],'fallback')
            self.assertEqual(by_repo['Owner/Kolor']['revision'],'a'*40)
            self.assertTrue(by_repo['Owner/Kolor']['documents'])

    def test_total_failure_never_advances_public_pointer(self):
        with TemporaryDirectory() as tmp:
            docs = Path(tmp)/'docs'
            self.build(docs,['Owner/Kolor'],'20261031T170000Z-1-1')
            before = (docs/'data'/'publication-current.json').read_text()
            def fail(name): raise RuntimeError('broken')
            with self.assertRaisesRegex(RuntimeError,'No selected'):
                self.build(docs,['Owner/Kolor'],'20261031T170200Z-2-1',fail)
            self.assertEqual(before, (docs/'data'/'publication-current.json').read_text())
            self.assertFalse((docs/'publications'/'releases'/'20261031T170200Z-2-1').exists())

    def test_rollback_restores_published_pointer_without_rewriting_archive(self):
        with TemporaryDirectory() as tmp:
            docs = Path(tmp)/'docs'
            self.build(docs,['Owner/Kolor'],'20261031T170000Z-1-1')
            self.build(docs,['Owner/Karacter'],'20261031T170200Z-2-1')
            original = (docs/'publications'/'releases'/'20261031T170000Z-1-1'/'manifest.json').read_bytes()
            rollback(docs,'20261031T170000Z-1-1','2026-10-31T20:00:00Z')
            p=json.loads((docs/'data'/'publication-current.json').read_text())
            self.assertEqual(p['release_id'],'20261031T170000Z-1-1')
            self.assertTrue(p['rollback'])
            self.assertEqual(original,(docs/'publications'/'releases'/'20261031T170000Z-1-1'/'manifest.json').read_bytes())

    def test_invalid_release_rejected(self):
        with TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                self.build(Path(tmp),['Owner/Kolor'],'../../escape')


if __name__ == '__main__':
    unittest.main()
