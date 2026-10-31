"""Private, evidence-first application validation matrix.

The 86 bundled patterns are an evaluation catalogue, not 86 automated checks.
Only an independently checked, source-hashed documentary adjudication receives a
verified documentary tick. Neither historical CI metadata nor code/profile
presence confers a pass, a security certification or production readiness.
"""
from __future__ import annotations

import json
import re
import hashlib
from pathlib import Path
from urllib.parse import quote

from . import evidence_adjudication, profiles, qualification, specsheets, spec_tests, snapshot_runs, source_structure

FORMAT = 'koa.validation_board.private.v1'
CI_SNAPSHOT_SHA256 = '8913d64a8e389ac4dc86810cbe3cd4ca2e248933cb499fbb4cc2b1f1683fed45'
STAGE_CATEGORY = {
    'specified': 'Architecture',
    'implemented': 'Implémentation',
    'qualified': 'Tests',
    'integrated': 'Intégration',
    'production': 'Production',
}


def _load_historical_ci(project: Path) -> dict[str, dict]:
    """Read ONLY a dated, bundled, sanitized CI observation snapshot."""
    path = project / 'private_evidence' / 'KOA-CI-OBSERVATIONS-2026-10-28.json'
    if not path.is_file() or path.is_symlink() or path.stat().st_size > 100_000:
        return {}
    rawbytes = path.read_bytes()
    if hashlib.sha256(rawbytes).hexdigest() != CI_SNAPSHOT_SHA256:
        return {}  # the bundled historical observation was changed
    raw = json.loads(rawbytes)
    if raw.get('format') != 'koa.ci_observations.snapshot.v1' or not isinstance(raw.get('repositories'), list):
        return {}
    allowed = set(profiles.inventory(project))
    result = {}
    for entry in raw['repositories']:
        repo = entry.get('repository')
        if repo not in allowed or repo in result:
            continue
        sha = entry.get('run_head_sha', '')
        meta_sha = entry.get('metadata_head_sha', '')
        match = bool(re.fullmatch(r'[0-9a-f]{40}', sha) and sha == meta_sha and entry.get('same_observed_head') is True)
        ci_pass = bool(match and entry.get('run_status') == 'completed' and entry.get('run_conclusion') == 'success')
        result[repo] = {
            'observed_at': str(entry.get('observed_at', ''))[:40],
            'run_at': str(entry.get('run_created_at', ''))[:40],
            'run_head_sha': sha if re.fullmatch(r'[0-9a-f]{40}', sha) else None,
            'same_observed_head': match,
            'success_observed': ci_pass,
            'conclusion': entry.get('run_conclusion') if entry.get('run_conclusion') in ('success','failure','cancelled','skipped','timed_out','unknown') else 'unknown',
            'source_snapshot_sha256': CI_SNAPSHOT_SHA256,
        }
    return result


def build(project: Path, qualification_path: Path | None = None,
          practice_path: Path | None = None) -> dict:
    """No network, scans, external executables, or source repo writes."""
    project = Path(project)
    patterns = profiles.catalog(project)
    historic_ci = _load_historical_ci(project)
    verified_run_snapshots = spec_tests.load(project)
    extra_runs = snapshot_runs.load(project)
    spec_index = specsheets.load(project)
    structure_index = source_structure.load(project)
    assessment_state = profiles.load_state(practice_path)['assessments']
    claim_state = qualification.load_state(qualification_path)['claims']
    # Evidence source is verified against archive and every referenced file hash.
    # Never fall back to blessing statuses when the archive has been tampered with.
    adjudicated = {
        (x['repository'], x['stage']): x
        for x in evidence_adjudication.load(project)['cases']
        if x['status'] == 'Étayé par preuve'
    }
    repositories = []
    total_verified = 0
    for repo in profiles.inventory(project):
        slug = repo.partition('/')[2]
        claims = claim_state.get(repo, {})
        stage_list = []
        for stage_id, stage_label in qualification.STAGES:
            raw = claims.get(stage_id, {})
            record = raw if isinstance(raw, dict) else {}
            state = record.get('status', 'Non évalué')
            if state not in qualification.STATES:
                state = 'Non évalué'
            documentary = adjudicated.get((repo, stage_id))
            source = documentary.get('source') if documentary else None
            # Proof-backed documentary judgement only when the same reviewed
            # source and explicitly scoped claim were recorded in local state.
            verified = bool(state == 'Étayé par preuve' and documentary and source and
                record.get('scope') == documentary['scope'] and
                source['sha256'] in record.get('evidence', '') and
                source['member'] in record.get('evidence', ''))
            if verified:
                label = '✓ Pièce documentaire vérifiée · portée limitée'
            elif state == 'Étayé par preuve':
                label = 'Décision locale · pièce non recoupée dans cette revue'
            elif state == 'À documenter':
                label = 'À documenter'
            elif state == 'Non applicable':
                label = 'Non applicable (décision locale)'
            else:
                label = 'Non évalué'
            stage_list.append({
                'id': stage_id, 'category': STAGE_CATEGORY[stage_id],
                'label': stage_label, 'status': state, 'display': label,
                'source_verified': verified,
                'scope': documentary['scope'] if verified else (record.get('scope', '')[:300] if state == 'Étayé par preuve' else ''),
                'source_sha256': source['sha256'] if verified else None,
                'source_link': ('/local/review/app/' + quote(slug) + '/' + stage_id + '/expert') if verified else None,
                'version_alignment': 'non attestée' if verified else 'inconnue',
            })
            total_verified += bool(verified)
        per_repo = assessment_state.get(repo, {})
        practice_rows = []
        for pat in patterns:
            raw = per_repo.get(pat['id'], {})
            rec = raw if isinstance(raw, dict) else {}
            status = rec.get('status', 'Non évalué')
            if status not in profiles.STATUSES:
                status = 'Non évalué'
            # "Appliqué" here is an owner assessment, not a verified test pass.
            practice_rows.append({
                'id': pat['id'], 'family': pat['family'],
                'section': pat['category'], 'title': pat['title'],
                'status': status, 'source_verified': False,
                'display': ('Évaluation locale : appliqué (à recouper)' if status == 'Appliqué'
                     else 'Évaluation locale : à améliorer' if status == 'À améliorer'
                     else 'Pas applicable (évaluation locale)' if status == 'Pas applicable'
                     else 'Non évalué'),
                'reviewed_at': str(rec.get('reviewed_at', ''))[:45],
            })
        categories = []
        for title, stage_ids, family in [
            ('Tests', ['qualified'], None),
            ('Sécurité', [], 'security'),
            ('Architecture', ['specified'], 'architecture'),
            ('Implémentation', ['implemented'], None),
            ('Intégration', ['integrated'], None),
            ('Production', ['production'], None),
        ]:
            stages = [s for s in stage_list if s['id'] in stage_ids]
            practices = [p for p in practice_rows if p['family'] == family] if family else []
            categories.append({'id': title.lower(), 'label': title,
                'stages': stages, 'practices': practices,
                'verified_count': sum(s['source_verified'] for s in stages),
                'evaluated_practices': sum(p['status'] != 'Non évalué' for p in practices),
                'practice_count': len(practices)})
        repositories.append({
            'repo': repo, 'slug': slug, 'categories': categories,
            'specsheet': specsheets.for_repository(project, repo, spec_index),
            'structure': source_structure.for_repository(project, repo, structure_index),
            'targeted_test_run': verified_run_snapshots.get(repo),
            'isolated_test_run': extra_runs.get(repo),
            'verified_stages': sum(s['source_verified'] for s in stage_list),
            'assessed_practices': sum(p['status'] != 'Non évalué' for p in practice_rows),
            'source_verified_test': any(s['id'] == 'qualified' and s['source_verified'] for s in stage_list),
            'historical_ci': historic_ci.get(repo),
            'security_test_passes': 0,  # No per-control execution logs in the provided archive.
        })
    return {
        'format': FORMAT, 'local_only': True, 'official_repositories': len(repositories),
        'criteria': {'security_per_repo': 53, 'architecture_per_repo': 33, 'qualification_per_repo': 5},
        'functional_specsheets_reviewed': sum(r['specsheet']['state'] == 'snapshot_reviewed' for r in repositories),
        'source_structure_repositories': sum(bool(r['structure'].get('roles')) for r in repositories),
        'source_structure_files_classified': sum(r['structure'].get('classified_files',0) for r in repositories),
        'targeted_unit_tests_passed': sum(r['passed'] for r in verified_run_snapshots.values()),
        'additional_isolated_test_passes': sum(r['passed'] for r in extra_runs.values()),
        'isolated_test_runs': len(extra_runs),
        'source_checked_documentary_jalons': total_verified,
        'security_controls_test_verified': 0,
        'historical_ci_success_on_observed_head': sum(v['success_observed'] for v in historic_ci.values()),
        'notice': ('Les coches désignent des pièces documentaires relues et hachées, dans leur portée. '
          'Elles ne signifient ni certificat global, ni test de sécurité réussi, ni version Git liée.'),
        'repositories': repositories,
    }
