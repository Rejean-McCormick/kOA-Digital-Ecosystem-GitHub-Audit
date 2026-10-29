# Repository Profiles and Checklist

The **Profils & conformité** tab adds human review alongside automated audit findings. It covers each of the **49 reference repositories** and uses **86 source practices**:

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

1. Open **Profils & conformité** and select a repository from the inventory.
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

## Initial repository profiles

- **Konnaxion**: a supplied RepoSurveyor profile dated **September 16, 2026**. Its exact attribution to the repository has not been independently verified; `PROVENANCE.md` records this limitation.
- **Orgo**: preliminary profile from known audit information; full code-line and complexity measurements not yet supplied.
- **kOA-Linux-Koali**: preliminary profile from known audit information; full code-line and complexity measurements not yet supplied.

Missing measurements and nonreviewed security practices remain **unassessed**. The detailed profile collection is expected to grow as repository snapshots are provided.

## Persistence and privacy

Statuses and notes are saved to:

`%LOCALAPPDATA%\kOA-GitHub-Audit\profiles\assessments.json`

This is separate from the extracted app and survives reinstalling the ZIP. Back it up if it is important. Avoid putting secrets in notes. The **Publish to GitHub** dashboard action does **not** upload assessments or full profile Markdown.

## How this connects to the audit

If you select an existing `audit.json` in the dashboard tab, the profiles view can display that repository's last observed status, file counts, and findings. It does **not** rerun the scan or infer pattern compliance. See [Offline Auditing](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit/wiki/Offline-Auditing) for status interpretation.
