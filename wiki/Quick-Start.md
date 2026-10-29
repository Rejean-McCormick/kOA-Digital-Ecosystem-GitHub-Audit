# Quick Start — Windows

## Requirements

- Windows with **Python 3.11 or later**, with Tkinter enabled.
- A local directory containing Git working trees, for example `C:\mycode`.
- Git for Windows for local Git metadata and optional GitHub dashboard/wiki publishing. No GitHub API token is required for an offline audit.

## Launch the application

1. Download the full release ZIP and extract **all files** to a normal folder.
2. Double-click `kOA_GitHub_Audit_Launcher.pyw` inside the extracted folder.
3. Select the **Audit local** tab; choose the directory containing your projects.
4. Use **Découvrir les dépôts locaux** to discover them, then **Scanner localement** to create an audit.
5. Use **Rapports** to review `audit.json`, `audit.csv`, and `SUMMARY.md`.

The interface currently uses French labels. See the French documentation inside `docs/` if needed.

## Other tabs

- **Vérification + ZIP**: recheck selected findings from an existing `audit.json` without rescanning everything; create a confidential, sanitized evidence ZIP.
- **Profils & conformité**: select any of the 49 inventory repositories, read profile Markdown, review 86 catalog practices, and save manual statuses.
- **Tableau de bord**: preview the dashboard locally, refresh it using existing audit reports, and optionally publish **aggregate-only** information to GitHub Pages.
- **Import historique**: attach past diagnostic summary metadata to an explicit repository.

## Where data is stored

| Item | Where |
| --- | --- |
| Local audit reports | The output directory selected for the run, typically `reports/` (Git ignored) |
| Sanitized evidence ZIP | The path you select for triage output |
| Engineering/security profile Markdown | `profiles/repositories/<repository>/` in the audit application |
| Manual checklist assessments | `%LOCALAPPDATA%\kOA-GitHub-Audit\profiles\assessments.json` |
| Public-safe dashboard aggregates | `docs/data/dashboard.json` |

**Do not put credentials in free-form notes or share raw audit reports publicly.**

## No need to scan again for a known issue

Use the **Verification + ZIP** tab if you already have a report and need to validate a specific finding. A previous problem marked resolved does not need a full audit solely for documentation.

## If the launcher stays invisible

Run `DIAGNOSTIC_LAUNCHER.cmd` in the extracted folder. See [Troubleshooting](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit/wiki/Troubleshooting).
