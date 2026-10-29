# Repository Profiles and Checklist

The **Certification & profils** tab adds human review alongside automated audit findings. It covers each of the **49 reference repositories**, plus one explicitly registered supplemental profile, and uses **86 source practices**:

- **33 architecture patterns** from the supplied senior architecture collection.
- **53 security patterns** from the supplied senior security collection.

These source documents are bundled under `profiles/library/`; the catalog is `profiles/catalog.json`.

## Profile types

| File | Purpose | What it cannot establish alone |
| --- | --- | --- |
| `ENGINEERING_PROFILE.md` | Reproducible engineering surface: active files, source/test/doc footprint, source languages, probable routes/tests, optionally complexity | Feature completeness, code quality, security, production readiness |
| `SECURITY_PROFILE.md` | Scope, evidence, open questions, and security-review decisions | A penetration test, vulnerability absence, compliance certification |

Standard templates are included in `profiles/templates/`.

## Working with a repository

1. Open **Certification & profils** and select a repository from the inventory.
2. Choose **Architecture** or **Sécurité** as the practice family.
3. Click a practice to read its original description in the detail pane.
4. Assign a status and, when available, an evidence reference or short justification.
5. Click **Enregistrer**. Each repository's assessments remain independent.
6. Read `ENGINEERING_PROFILE.md` or `SECURITY_PROFILE.md` from the same tab.
7. Use **Importer .md** to install a prepared profile after selecting its type and target repository.

## Status vocabulary

| UI state | English | When to choose it |
| --- | --- | --- |
| `Non évalué` | Not assessed | Default; no review has established a decision |
| `Pas applicable` | Not applicable | The practice is out of scope, with a reason |
| `À améliorer` | Needs improvement | Relevant practice is incomplete or needs stronger evidence |
| `Appliqué` | Applied | Implementation was reviewed and supported by evidence |

**Never auto-promote a practice to Applied based on a scan, a config file, or the mere presence of a profile.** The checklist is an explicit, manual assessment.

## Engineering snapshot profiles (October 29, 2026)

The user supplied 13 full code snapshots inside `EP.zip`. Using RepoSurveyor v1.0 consistently on each extracted snapshot, the application now includes **13 measured `ENGINEERING_PROFILE.md` reports**. Each also has an `ENGINEERING_METRICS.json` file and `PROVENANCE.md` with archive SHA-256 and capture time.

- **12** reports belong to the official inventory of 49 projects.
- `Konnaxion-Universe-Worlds-Manager` is a **supplemental** selectable profile, *not* a newly governed repository. This is intentionally separate from the inventory.
- Konnaxion's earlier September 2026 profile is kept as a clearly labeled historical artifact. It must not be mixed with the October snapshot's measurements.
- Security practice assessments remain **Not assessed** until explicitly reviewed.

See the repository's profile directory and the main project's `profiles/ENGINEERING_PROFILE_INDEX.md` for the full measurement table.

The snapshot survey did not run project tests, CI, CodeQL or a security evaluation. Lizard, Ctags and `scc` were not available; thus precise complexity metrics for these snapshots are unavailable.

## Persistence and privacy

Statuses and notes are saved to:

`%LOCALAPPDATA%\kOA-GitHub-Audit\profiles\assessments.json`

This is separate from the extracted app and survives reinstalling the ZIP. Back it up if it is important. Avoid putting secrets in notes. The **Publish to GitHub** dashboard action does **not** upload assessments or full profile Markdown.

## How this connects to the audit

If you select an existing `audit.json` in the dashboard tab, the profiles view can display that repository's last observed status, file counts, and findings. It does **not** rerun the scan or infer pattern compliance. See [Offline Auditing](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit/wiki/Offline-Auditing) for status interpretation.

## Qualification stages are independent of the 86 practices

The five maturity stages (specified, implemented, qualified, integrated, production-proven) are not inferred from the practice checklist or diagnostic observations. Use the upper **Qualification by evidence** panel to record an explicit scope and a provenance reference. See [Certification & Continuous Improvement](Certification-and-Continuous-Improvement.md).
