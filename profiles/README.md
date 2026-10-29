# kOA repository profiles

This directory is read by the **Profiles & compliance** tab of the desktop application. It does **not** modify any of the audited repositories.

## Layout

- `catalog.json`: 86 practices sourced from the supplied collections (**33 architecture**, **53 security**).
- `library/`: original Markdown files for those practices, displayed in the application.
- `repositories/<repo>/ENGINEERING_PROFILE.md`: standardized engineering profile.
- `repositories/<repo>/SECURITY_PROFILE.md`: standardized security-profile notes and qualification criteria.
- `templates/`: templates for future profiles.

## Snapshot engineering profiles (2026-10-29)

The folder `EP.zip` provided 13 independently captured code snapshots. All 13 have been measured using the RepoSurveyor v1.0 profile/survey engine from the user's supplied tool. A consistent additional scope filter excludes `.koali-update-backups/` and embedded snapshot indexes.

- **12 of 13** mapped to the existing 49-repository governance inventory.
- **1 supplemental project** (`Konnaxion-Universe-Worlds-Manager`) is explicitly selectable in the profile tab without changing the authoritative inventory.
- All 13 profile folders contain `ENGINEERING_PROFILE.md`, `ENGINEERING_METRICS.json` and `PROVENANCE.md`.
- The original Konnaxion profile dated September 16, 2026 is retained as `ENGINEERING_PROFILE_2026-09-16_HISTORICAL.md`; it is not mixed into current metrics.
- Existing security profiles for Konnaxion, Orgo and Koali Linux are unchanged and remain unassessed; their checklist states are never inferred from engineering data.
- `ENGINEERING_PROFILE_INDEX.md` gives the full 13-repository table; `ENGINEERING_PROFILE_INDEX.csv` supports spreadsheets or analysis.

### Interpretation limits

- All measurements reflect **snapshot content**, not live repository state or Git history.
- Fallback line counts are **physical, nonblank source lines** and may include comments. They are not accurate SLOC.
- Lizard, `scc`, and Ctags were unavailable, so precise cyclomatic complexity is **not measured** for these snapshots.
- No tests, CI, CodeQL, CVEs, or deployment checks were executed.
- No automatic quality, maturity, compliance, security or release-readiness grade is produced.

## Manual assessment statuses

Each of the 86 practices can be marked:

| English meaning | UI label | Interpretation |
| --- | --- | --- |
| Not assessed | `Non évalué` | Default; no decision yet |
| Not applicable | `Pas applicable` | Reviewer determined it does not fit the repository |
| Needs improvement | `À améliorer` | Implementation requires further work |
| Applied | `Appliqué` | Implementation is supported by reviewed evidence |

The app saves assessments separately from repository profiles at:

`%LOCALAPPDATA%\kOA-GitHub-Audit\profiles\assessments.json`

This file persists when the app is replaced; back it up separately if needed. Do not put credentials, private keys, or sensitive values in notes. These assessments are **not** exported by GitHub Pages dashboard publication.

To install a new profile: select a repository in **Profiles & compliance**, choose **ENGINEERING_PROFILE.md** or **SECURITY_PROFILE.md**, and click **Importer .md**. The app writes to its own profiles directory, **never to the source repository**. See [the wiki guide](../wiki/Repository-Profiles-and-Checklist.md).
