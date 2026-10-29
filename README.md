<div align="center">
  <img src="docs/assets/logo.svg" alt="kOA Digital Ecosystem" width="90" />

  # kOA Digital Ecosystem — GitHub Audit

  **Offline repository auditing, engineering profiles, manual compliance tracking, and a public-safe dashboard.**

  **Version 0.7.1 · Documentation release**
</div>

> **Default operation is local, read-only, and token-free.** The application inspects existing local Git working trees without cloning, fetching, executing project code, changing source repositories, or requiring a GitHub API token.

## What this project does

The audit repository provides a single place to **observe and review** the kOA Digital Ecosystem. It uses a bundled reference inventory of **49 repositories** without claiming that this inventory is live or that every repository has been inspected.

| Capability | What you get | Important boundary |
| --- | --- | --- |
| **Local audit** | Inventory of Git working trees, workflow/configuration indicators, bounded static checks, JSON/CSV/Markdown reports | Does not execute CI, CodeQL, tests, or CVE lookups |
| **Evidence triage** | Targeted rechecks of existing findings and a sanitized evidence ZIP | No raw source or secrets copied into the ZIP |
| **Engineering & security profiles** | Local Markdown profiles by repository, imported through the launcher | Engineering scale is **not** a quality or release-readiness score |
| **Manual compliance checklist** | 33 architecture practices + 53 security practices with four review states | States are user assessments, not automatic certifications |
| **Dashboard** | Visual aggregate metrics, campaign history, inspection/CI visibility, engineering indicators | Public dashboard uses approved aggregate counts only |
| **Historical diagnostics** | Metadata imports from existing kOA diagnostic tool families | Historical outcomes remain separate from current observations |

The application uses the kOA brand color **`#1e6864`** and the supplied logo in the dashboard.

## Quick start — Windows

**Requirements:** Windows, Python **3.11+** with Tkinter, and locally available Git repositories. Git for Windows is useful for local Git metadata and is required when using the optional GitHub publication feature.

1. Download and **extract the complete ZIP** into a normal folder. Do not run the launcher from inside the archive.
2. Double-click **`kOA_GitHub_Audit_Launcher.pyw`**.
3. Open **Audit local**, select a root folder such as `C:\mycode`, and choose **Discover local repositories**, then **Scan locally** (the interface buttons are currently labeled in French).
4. Use **Reports** to view `SUMMARY.md`, `audit.csv`, and `audit.json`.
5. Use **Verification + ZIP** if a finding needs targeted confirmation. You do **not** need to repeat a full audit for a known finding.
6. Open **Profiles & compliance** to view or import engineering/security profiles and review each repository's checklist.
7. Open **Dashboard** to preview aggregated data. Publishing to GitHub is an **explicit, separate** action.

If the launcher does not open, run **`DIAGNOSTIC_LAUNCHER.cmd`** for visible troubleshooting output. Since v0.6.1, the local preview server handles `pythonw.exe` without a console.

## Engineering and security profiles

The **Profiles & compliance** tab covers the 49 repositories and reads:

```text
profiles/
├── catalog.json                         # 86 catalog entries
├── library/                             # Source pattern Markdown
├── repositories/
│   └── <repository-name>/
│       ├── ENGINEERING_PROFILE.md
│       └── SECURITY_PROFILE.md
└── templates/                            # Templates for future profiles
```

The bundled catalog includes **33 architecture patterns** and **53 security patterns**. Each entry can be marked:

- **Not assessed** (`Non évalué`) — default; no conclusion has been made.
- **Not applicable** (`Pas applicable`) — the reviewer considers it outside the repository's scope.
- **Needs improvement** (`À améliorer`) — improvement is warranted.
- **Applied** (`Appliqué`) — the reviewer has evidence supporting implementation.

Add an explanatory note or evidence reference where useful, without including passwords, tokens, or private material. Manual assessments are stored **outside the extracted application** at `%LOCALAPPDATA%\kOA-GitHub-Audit\profiles\assessments.json` so replacing the app ZIP does not overwrite them. They are **not published by the dashboard button**.

Three initial profile folders are included:

| Repository | Status of engineering profile |
| --- | --- |
| **Konnaxion** | Supplied RepoSurveyor profile (September 16, 2026); repository attribution is **provisional** and explicitly noted in `PROVENANCE.md` |
| **Orgo** | Preliminary profile using available local-audit observations; RepoSurveyor code/complexity measures not yet provided |
| **kOA-Linux-Koali** | Preliminary profile using available local-audit observations; RepoSurveyor code/complexity measures not yet provided |

No missing profile or unreviewed practice is silently classified as compliant. An `ENGINEERING_PROFILE.md` describes **engineering size/surface**; it does not establish feature completion, code quality, security certification, or release readiness.

For adding profiles, select the repository and profile type, then **Importer .md** in the tab. A profile is installed under **this audit application only**; audited source repositories stay unchanged.

## Dashboard and GitHub Pages

`docs/index.html` is a static dashboard with local-audit and GitHub/CI views kept separate. It displays **aggregate** metrics such as inventory coverage, inspection findings, files inspected, engineering-control indicators, and campaign trends. The displayed figures describe **published snapshots**, not a live filesystem feed.

- **Preview locally:** Dashboard → **Aperçu dans le navigateur**.
- **Build aggregated data without rerunning an audit:** Dashboard → **Mettre à jour le tableau de bord**, or use the `dashboard-publish` CLI command.
- **Publish (optional):** Dashboard → **Publier sur GitHub (1 clic)**. It uses the PC's existing Git credentials and normally pushes only the allowlisted aggregate dashboard data and Pages deployment workflow to the **audit repository**, never to the 49 source repositories. GitHub permissions may prevent the push.
- **First-time Pages configuration:** In the audit repository, choose **Settings → Pages → Source: GitHub Actions** if required. `.github/workflows/dashboard-pages.yml` deploys `docs/` after the relevant push.

The browser checks for updated published data approximately every **three minutes**; it cannot access `C:\mycode` remotely. **GitHub Pages and GitHub Wiki are different services.** The wiki source pages live in the `wiki/` folder and need their own optional publishing step.

**Privacy:** the dashboard does not publish raw `audit.json`/CSV, repository names, Windows paths, source code, secrets, or per-repository findings. Inspect `docs/data/dashboard.json` before making it public. Detailed Markdown profiles and checklist assessments are **not** automatically published to Pages.

## Command line

Run these commands from the extracted project root:

```powershell
# Inventory without a scan (offline)
python -m koa_audit local-plan --root "C:\mycode" --max-depth 4

# Full local audit: reports are written on your PC only
python -m koa_audit local-audit --root "C:\mycode" --max-depth 4 --out reports

# Targeted recheck of existing results (offline)
python -m koa_audit local-triage --root "C:\mycode" --audit-json reports/audit.json --out reports/triage.zip

# Regenerate public-safe data from an existing report (no scan, no push)
python -m koa_audit dashboard-publish --audit-json reports/audit.json --out docs

# Optional publication via existing Git credentials
python -m koa_audit dashboard-sync

# Run the repository's test suite
python -m unittest discover -s tests -v
```

Selected options: repeat `--root` for multiple folders; use `--limit` for a pilot; use `--max-files` to adjust the per-repository inspection budget; use `--only-inventory` to skip locally discovered repositories outside the bundled 49-repository inventory. The older `audit` and `plan` subcommands access the **remote GitHub API** and are optional; they are **not** required for local auditing.

## Understanding results

- **`INSPECTED_NO_PATTERN_MATCH`** means no configured static pattern matched the inspected content — **not** that a repository is secure.
- **`REVIEW`** means a heuristic finding should be checked in context.
- **`PARTIAL`** means the inspection had limitations, such as files above its scanning budget.
- Missing CodeQL/CI/security-alert data is **unknown**, not zero and not passed.
- The **manual compliance checklist** is independent of these automated observation statuses.
- Historical diagnostics retain their provenance and never replace new audit findings.

> A known false positive should be resolved by **targeted triage**, not by rerunning the complete 49-repository audit. In the October 2026 `Konnaxion-Capsule-Manager` investigation, the older generic `verify=False` rule produced six false TLS alerts. The improved v0.4.1 rule identifies HTTP/TLS contexts more precisely; separate HTTPS health-check behavior still requires its own review.

## Project structure

```text
koa_audit/            # Local scanner, triage, reporting, profiles, dashboard
profiles/             # Pattern catalog, original pattern library, repository profiles
wiki/                 # English GitHub Wiki page sources (publish separately)
docs/                 # GitHub Pages site and reference documentation
config/               # Historical diagnostic catalog
data/                 # Reference inventory snapshot and provenance
tests/                # Automated tests
reports/              # Local generated reports (ignored by Git)
```

## Documentation

- **[Wiki home](wiki/Home.md)** — English user and maintainer guides (source files, usable without publishing).
- **[Wiki quick start](wiki/Quick-Start.md)** — Windows setup and main workflows.
- **[Profiles and checklist](wiki/Repository-Profiles-and-Checklist.md)** — importing reports and recording assessments.
- **[Dashboard and publishing](wiki/Dashboard-and-Publishing.md)** — preview, publication, and privacy.
- **[Troubleshooting](wiki/Troubleshooting.md)** — Windows launcher, preview and Git publishing problems.
- [Existing technical documentation](docs/ARCHITECTURE.md) and [French UI guide](docs/LAUNCHER_FR.md).

**GitHub Wiki publication:** `wiki/` is a set of ready-to-use Wiki Markdown pages, not an automatically published GitHub Wiki. GitHub Wikis are separate repositories. See [Wiki-Publishing](wiki/Wiki-Publishing.md) for the one-time setup and safe publishing steps.

## Security, governance, and license

This audit repository has **no authority to change source projects, approve releases, or certify security**. The `kOA-Digital-Ecosystem` repository retains inventory/governance authority; specialized diagnostics retain their own qualification meaning. The application does not replace CodeQL, advisory-database analysis, secret scanning, or production tests. See [SECURITY.md](SECURITY.md).

**No open-source license has been selected.**
