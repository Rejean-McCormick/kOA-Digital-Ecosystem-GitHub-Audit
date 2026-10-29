# kOA repository profiles

This directory is read by the **Profiles & compliance** tab of the desktop application. It does **not** modify any of the audited repositories.

## Layout

- `catalog.json`: 86 practices sourced from the supplied collections (**33 architecture**, **53 security**).
- `library/`: original Markdown files for those practices, displayed in the application.
- `repositories/<repo>/ENGINEERING_PROFILE.md`: standardized engineering profile.
- `repositories/<repo>/SECURITY_PROFILE.md`: standardized security-profile notes and qualification criteria.
- `templates/`: templates for future profiles.

## Initial profiles

- **Konnaxion:** provided RepoSurveyor engineering profile dated September 16, 2026. Its attribution to this specific repository is **provisional**; consult `PROVENANCE.md`.
- **Orgo** and **kOA-Linux-Koali:** preliminary profiles based on existing local-audit observations. Precise engineering size, code-line and complexity measurements were **not** supplied for these two projects and are not fabricated.
- The initial security profiles are **unassessed templates**, not security certifications.

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
