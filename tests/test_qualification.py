"""Certification assertions require explicit scoped evidence; patterns are never auto-rated."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from koa_audit import qualification, profiles
from koa_audit.dashboard import publish_reports

ROOT = Path(__file__).resolve().parents[1]


class QualificationTests(unittest.TestCase):
    def test_unreviewed_never_promoted(self):
        with tempfile.TemporaryDirectory() as temp:
            registry = Path(temp) / "qualifications.json"
            p = qualification.progress(ROOT, "Rejean-McCormick/Orgo", registry)
            self.assertEqual(p["assessed"], 0)
            self.assertEqual(p["evidenced"], 0)
            self.assertEqual(len(p["stages"]), 5)
            self.assertTrue(all(v["status"] == "Non évalué" for v in p["stages"].values()))

    def test_scoped_support_requires_reference(self):
        with tempfile.TemporaryDirectory() as temp:
            registry = Path(temp) / "qualifications.json"
            repo = "Rejean-McCormick/Konnaxion"
            for evidence, scope in (("", "local"), ("docs/status", ""), ("a", "local")):
                with self.assertRaises(ValueError):
                    qualification.set_claim(ROOT, repo, "qualified", "Étayé par preuve", evidence, scope, registry)
            qualification.set_claim(ROOT, repo, "qualified", "Étayé par preuve",
                                    "Owner E2E report 2026-09-21", "Konnaxion / Orgo IK local", registry)
            claims = qualification.progress(ROOT, repo, registry)
            self.assertEqual(claims["evidenced"], 1)
            self.assertEqual(claims["stages"]["production"]["status"], "Non évalué")
            self.assertEqual(claims["stages"]["qualified"]["scope"], "Konnaxion / Orgo IK local")
            # Distinct owner, no promotion.
            self.assertEqual(qualification.progress(ROOT, "Rejean-McCormick/Orgo", registry)["assessed"], 0)

    def test_reviewed_non_applicable_is_not_negative(self):
        with tempfile.TemporaryDirectory() as temp:
            registry = Path(temp) / "qualifications.json"
            repo = "Rejean-McCormick/Koali-Spaces"
            qualification.set_claim(ROOT, repo, "production", "Non applicable",
                                    "Scope is presentation only", "Presentation", registry)
            p = qualification.progress(ROOT, repo, registry)
            self.assertEqual(p["assessed"], 1)
            self.assertEqual(p["evidenced"], 0)
            self.assertEqual(p["stages"]["production"]["status"], "Non applicable")

    def test_pattern_status_needs_review_note(self):
        with tempfile.TemporaryDirectory() as temp:
            registry = Path(temp) / "assessments.json"
            with self.assertRaises(ValueError):
                profiles.set_assessment(ROOT, "Rejean-McCormick/Akor", "SEC-01", "À améliorer", "", registry)
            with self.assertRaises(ValueError):
                profiles.set_assessment(ROOT, "Rejean-McCormick/Akor", "SEC-01", "Appliqué", "", registry)
            with self.assertRaises(ValueError):
                profiles.set_assessment(ROOT, "Rejean-McCormick/Akor", "SEC-01", "Pas applicable", "", registry)
            self.assertEqual(profiles.progress(ROOT, "Rejean-McCormick/Akor", registry)["reviewed"], 0)

    def test_public_data_aggregates_no_secret_or_claims(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp)/"audit.json"
            source.write_text(json.dumps({
                "format": "koa_audit.local_observation.v1",
                "generated_at": "2026-10-29T17:10:00Z", "declared_repositories": 49,
                "repositories_scanned": 1, "findings_by_type": {"SENSITIVE_FILENAME": 1},
                "repositories": [{"repository": "Rejean-McCormick/Akor", "status": "REVIEW",
                                  "location": "C:\\PRIVATE\\SECRET_KEY", "findings": [{"path": ".env"}]}],
            }))
            result = publish_reports([source], Path(temp)/"docs")
            self.assertEqual(result["local_snapshots"], 1)
            payload = (Path(temp)/"docs/data/dashboard.json").read_text()
            for private in ("PRIVATE", "SECRET_KEY", ".env", "Akor", "claims", "certification", "C:\\"):
                self.assertNotIn(private, payload)
            data = json.loads(payload)
            self.assertEqual(data["snapshots"][0]["engineering_profiles"], 12)

if __name__ == "__main__":
    unittest.main()

class ConservativeScanClassificationTests(unittest.TestCase):
    def test_filenames_and_unpinned_actions_are_informational(self):
        from koa_audit.local_scan import scan_repository
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp) / "sample"
            (repo / '.github' / 'workflows').mkdir(parents=True)
            (repo / '.env.local').write_text('DO_NOT_PUBLISH=value\n')
            (repo / '.github' / 'workflows' / 'ci.yml').write_text(
                'on: push\njobs:\n  a:\n    steps:\n      - uses: actions/checkout@v4\n'
            )
            result = scan_repository(repo)
            self.assertEqual(result['status'], 'OBSERVED_INFORMATIONAL')
            self.assertEqual(result['finding_counts']['SENSITIVE_FILENAME'], 1)
            self.assertEqual(result['finding_counts']['WORKFLOW_UNPINNED_ACTION'], 1)
            self.assertTrue(all(item['severity']=='info' for item in result['findings']))
            self.assertNotIn('DO_NOT_PUBLISH',json.dumps(result))

class EcosystemBoardTests(unittest.TestCase):
    def test_49_repos_with_neutral_independent_stages(self):
        with tempfile.TemporaryDirectory() as temp:
            board = qualification.ecosystem_board(ROOT,
                Path(temp)/'qualification.json', Path(temp)/'assessments.json')
            self.assertEqual(len(board), 49)
            self.assertEqual(sum(1 for r in board if r['engineering_profile']), 12)
            self.assertTrue(all(all(v=='Non évalué' for v in r['stages'].values()) for r in board))
            self.assertTrue(all(r['practice_counts']['Non évalué']==86 for r in board))
            self.assertNotIn('Rejean-McCormick/Konnaxion-Universe-Worlds-Manager',
                             {r['repository'] for r in board})
