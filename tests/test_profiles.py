from __future__ import annotations
import json
import tempfile
import unittest
from pathlib import Path

from koa_audit import profiles

ROOT=Path(__file__).resolve().parents[1]

class ProfilesTest(unittest.TestCase):
    def test_all_49_repos_and_86_user_pattern_sources(self):
        repos=profiles.inventory(ROOT)
        self.assertEqual(len(repos),49)
        pts=profiles.catalog(ROOT)
        self.assertEqual(len(pts),86)
        self.assertEqual(len(set(x['id'] for x in pts)),86)
        self.assertEqual(sum(x['family']=='architecture' for x in pts),33)
        self.assertEqual(sum(x['family']=='security' for x in pts),53)
        self.assertIn('Circuit Breaker',profiles.get_pattern_text(ROOT,'ARCH-01'))
        self.assertIn('Separate Identity Planes',profiles.get_pattern_text(ROOT,'SEC-01'))

    def test_assessments_untested_by_default_and_saved_locally(self):
        with tempfile.TemporaryDirectory() as tmp:
            state=Path(tmp)/'assessments.json'
            repo='Rejean-McCormick/Konnaxion'
            p=profiles.progress(ROOT,repo,state)
            self.assertEqual(p['total'],86)
            self.assertEqual(p['reviewed'],0)
            self.assertEqual(p['Non évalué'],86)
            profiles.set_assessment(ROOT,repo,'SEC-01','À améliorer','Preuve à demander',state)
            profiles.set_assessment(ROOT,repo,'ARCH-01','Pas applicable','Aucun appel réseau',state)
            p=profiles.progress(ROOT,repo,state)
            self.assertEqual(p['reviewed'],2)
            self.assertEqual(p['À améliorer'],1)
            self.assertEqual(p['Pas applicable'],1)
            self.assertEqual(profiles.get_assessment(ROOT,repo,'SEC-01',state)['note'],'Preuve à demander')
            raw=json.loads(state.read_text())
            self.assertNotIn('secrets',raw)
            self.assertEqual(raw['format'],profiles.STATE_FORMAT)

    def test_profiles_and_provenance(self):
        konnaxion=profiles.get_profile(ROOT,'Rejean-McCormick/Konnaxion','ENGINEERING_PROFILE.md')
        self.assertIn('109,361',konnaxion)
        self.assertIn('Lizard',konnaxion)
        for repo in ('Orgo','kOA-Linux-Koali'):
            s=profiles.get_profile(ROOT,'Rejean-McCormick/'+repo,'ENGINEERING_PROFILE.md')
            self.assertIn('active engineering surface',s)
            self.assertIn('snapshot',s.lower())
        self.assertIsNone(profiles.get_profile(ROOT,'Rejean-McCormick/Akor','ENGINEERING_PROFILE.md'))

    def test_engineering_profiles_for_all_13_ep_snapshots(self):
        from pathlib import Path
        canonical=profiles.inventory(ROOT)
        self.assertEqual(len(canonical),49)
        selectable=profiles.profile_repositories(ROOT)
        self.assertEqual(len(selectable),50)
        extra='Rejean-McCormick/Konnaxion-Universe-Worlds-Manager'
        self.assertIn(extra,selectable)
        self.assertNotIn(extra,canonical)
        self.assertEqual(len(list((ROOT/'profiles/repositories').glob('*/ENGINEERING_METRICS.json'))),13)
        for metric_path in (ROOT/'profiles/repositories').glob('*/ENGINEERING_METRICS.json'):
            raw=json.loads(metric_path.read_text(encoding='utf-8'))
            self.assertEqual(raw['format'],'koa_profiles.engineering_metrics.v1')
            self.assertGreater(raw['counts']['active_files'],0)
            self.assertFalse(raw['method']['code_executed'])
            self.assertFalse(raw['method']['tests_executed'])
            self.assertTrue(profiles.get_profile(ROOT,raw['repository'],'ENGINEERING_PROFILE.md'))
        self.assertEqual(profiles.progress(ROOT,extra)['total'],86)

    def test_import_profile_and_reject_invalid_repo(self):
        with tempfile.TemporaryDirectory() as tmp:
            temp_root=Path(tmp)
            (temp_root/'data').mkdir()
            (temp_root/'data/initial_inventory.json').write_text((ROOT/'data/initial_inventory.json').read_text())
            src=temp_root/'report.md'
            src.write_text('# Profile\nNo secret\n')
            dest=profiles.install_profile(temp_root,'Rejean-McCormick/Orgo','ENGINEERING_PROFILE.md',src)
            self.assertIn('No secret',dest.read_text())
            with self.assertRaises(ValueError):
                profiles.install_profile(temp_root,'../../etc','SECURITY_PROFILE.md',src)
            with self.assertRaises(ValueError):
                profiles.set_assessment(ROOT,'Rejean-McCormick/Orgo','SEC-999','Appliqué','',temp_root/'out.json')
            with self.assertRaises(ValueError):
                profiles.set_assessment(ROOT,'Rejean-McCormick/Orgo','SEC-01','Verdict confirmé','',temp_root/'out.json')

    def test_existing_audit_linkage_without_scan(self):
        report=ROOT/'reports/local/audit.json'
        if not report.is_file():
            with tempfile.TemporaryDirectory() as tmp:
                source=Path(tmp)/'audit.json'
                source.write_text(json.dumps({'format':'koa_audit.local_observation.v1','repositories':[{'repository':'Rejean-McCormick/Orgo','status':'REVIEW','files_enumerated':102,'files_inspected':90,'finding_counts':{'X':3},'git':{'head':'abc123'}}]}))
                result=profiles.audit_context(ROOT,'Rejean-McCormick/Orgo',source)
                self.assertEqual(result['findings'],3)
                self.assertEqual(result['files_enumerated'],102)
                self.assertIsNone(profiles.audit_context(ROOT,'Rejean-McCormick/Akor',source))

if __name__=='__main__': unittest.main()
