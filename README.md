<div align="center">
  <img src="docs/assets/logo.svg" alt="kOA Digital Ecosystem" width="90" />

  # kOA Digital Ecosystem — GitHub Audit

  **Evidence-based qualification, continuous improvement, engineering profiles, offline auditing, and a public-safe dashboard.**

  **Version 0.9.0 · Interactive ecosystem atlas, clickable Engineering Profiles, evidence qualification**
</div>

## Ecosystem command center — v0.9.0

The main dashboard is now an interactive **application atlas**, inspired by
`kOA-Digital-Ecosystem` authority and contract maps. It supports two
map views: documented system flows and an interactive **49-repository
constellation**. Selecting an application shows its measured Engineering Profile
(if available), public repository, and five independent qualification stages.

**Engineering Profiles are clickable and readable.** On GitHub Pages each of
the 12 measured in-scope repositories has a public-safe engineering report
(`docs/engineering/<repo>.html`), including footprint, languages, configured
controls, provenance, and limitations. In the **local preview** the link
opens the original full Markdown profile, read directly from the application.
A 13th supplemental profile is preserved locally, outside the official 49.

Five progress bars track **manual evidence** for specified, implemented,
qualified, integrated, and production separately. The local preview reads
status-only assessments without exporting proof text or scope. The public
site shows qualification as **unpublished** rather than inventing completion.

In the Windows launcher, start with the **Écosystème** tab and click
**Ouvrir le centre de pilotage (carte + profils)**. No rescan is required.
All original audit and certification functions remain in secondary tabs.
See [`docs/ATLAS_SOURCE_AND_METHOD.md`](docs/ATLAS_SOURCE_AND_METHOD.md).


> **Default operation is local, read-only, and token-free.** The application inspects existing local Git working trees without cloning, fetching, executing project code, changing source repositories, or requiring a GitHub API token.

## What this project does

The audit repository provides a single place to **observe and review** the kOA Digital Ecosystem. It uses a bundled reference inventory of **49 repositories** without claiming that this inventory is live or that every repository has been inspected.

| Capability | What you get | Important boundary |
| --- | --- | --- |
| **Local audit** | Inventory of Git working trees, workflow/configuration indicators, bounded static checks, JSON/CSV/Markdown reports | Does not execute CI, CodeQL, tests, or CVE lookups |
| **Evidence triage** | Targeted rechecks of existing findings and a sanitized evidence ZIP | No raw source or secrets copied into the ZIP |
| **Engineering & security profiles** | Local Markdown profiles by repository, imported through the launcher | Engineering scale is **not** a quality or release-readiness score |
| **Manual practice checklist** | 33 architecture + 53 security practices with four explicit review states | Similar names, counts, missing controls, duplicates never score projects negatively |
| **Qualification milestones** | Specified, implemented, qualified, integrated and production-proven — each with declared scope and evidence | No automatic grade or production claim; assessments stay on this PC |
| **Ecosystem atlas** | Interactive 12-owner conceptual contract map, 49-repository constellation, per-application detail and clickable Engineering Profiles | Public-safe reports; manual qualification is local only |
| **Historical diagnostics** | Metadata imports from existing kOA diagnostic tool families | Historical outcomes remain separate from current observations |

The application uses the kOA brand color **`#1e6864`** and the supplied logo in the dashboard.

## Quick start — Windows

**Requirements:** Windows and Python **3.11+** with Tkinter. Git for Windows is only required for optional GitHub publication or certain Git metadata operations.

1. Download and **extract the complete ZIP** into a normal folder. Do not run the launcher inside the ZIP.
2. Double-click **`kOA_GitHub_Audit_Launcher.pyw`**.
3. The initial **Écosystème** tab contains the main action **Ouvrir le centre de pilotage (carte + profils)**.
4. Switch between the **documented conceptual contract map (12 owners)** and **the full 49-repository constellation**. Select an application to see its detail.
5. Click **Voir l’Engineering Profile** to read the original local Markdown report (if available). The public Pages version offers a safer, condensed report.
6. Review evidence-based stages and patterns in **Certification & profils**, or browse the private **Registre des 49**. The dashboard refresh button reflects these local status changes.
7. Use **Audit local**, **Vérification + ZIP**, and **Rapports** only when you need a new inspection or targeted analysis. No rescan is necessary to open existing profiles.

If the launcher does not open, run **`DIAGNOSTIC_LAUNCHER.cmd`** for troubleshooting. Since v0.6.1, the local preview server handles Windows `pythonw.exe` without console output.

## Engineering and security profiles

The **Certification & profils** tab covers the 49 repositories in the bundled inventory, plus one explicitly registered supplemental profile, and reads:

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

**New in v0.8.0:** `EP.zip` provided **13 repository code snapshots** (captured 2026-10-29). Every snapshot now has an engineering profile derived from the RepoSurveyor 1.0 survey engine, an `ENGINEERING_METRICS.json`, and a `PROVENANCE.md`. **12** repositories belong to the 49-repository inventory. The additional `Konnaxion-Universe-Worlds-Manager` is selectable but explicitly **supplemental**; this does not enlarge the governed inventory. Start with [the index of measured profiles](profiles/ENGINEERING_PROFILE_INDEX.md).

The profiles measure the extracted snapshot content, **not live Git state**. Optional `scc`, Lizard and Ctags metrics were unavailable here, so cyclomatic complexity is marked unknown. Static test declarations are not executed tests and configured controls are not proven successful. The pre-existing September 2026 Konnaxion profile remains archived as historical evidence; it must not be compared as though it measured the same snapshot.

The bundled catalog includes **33 architecture patterns** and **53 security patterns**. Each entry can be marked:

- **Not assessed** (`Non évalué`) — default; no conclusion has been made.
- **Not applicable** (`Pas applicable`) — the reviewer considers it outside the repository's scope.
- **Needs improvement** (`À améliorer`) — improvement is warranted.
- **Applied** (`Appliqué`) — the reviewer has evidence supporting implementation.

Add an explanatory note or evidence reference where useful, without including passwords, tokens, or private material. Three explicit practice decisions (`Pas applicable`, `À améliorer`, `Appliqué`) require a short rationale or evidence reference; the default is never counted against a project. Manual assessments are stored **outside the extracted application** at `%LOCALAPPDATA%\kOA-GitHub-Audit\profiles\assessments.json` so replacing the app ZIP does not overwrite them. They are **not published by the dashboard button**.

There are **13 measured Engineering Profiles** (12 in the official inventory, plus one supplemental project) from the user-supplied October 29 snapshots, including Konnaxion, Orgo and kOA-Linux-Koali. See [the measured profile index](profiles/ENGINEERING_PROFILE_INDEX.md); the September 2026 Konnaxion profile is preserved separately as historical material.

No missing profile or unreviewed practice is silently classified as compliant. An `ENGINEERING_PROFILE.md` describes **engineering size/surface**; it does not establish feature completion, code quality, security certification, or release readiness.

For adding profiles, select the repository and profile type, then **Importer .md** in the tab. A profile is installed under **this audit application only**; audited source repositories stay unchanged.

## Certification and continuous improvement

The application's **Certification & profils** tab is governed by the user-provided ecosystem maturity map, which keeps five stages separate: **specified / architected**, **implemented**, **tested / qualified**, **integrated**, and **production-proven**. No engineering metric or static finding automatically marks a stage achieved or failed. Each claim requires explicit human review, a scope and evidence; a qualified local test never turns into a production certification.

The private **Registre des 49** tab summarizes all 49 inventory repositories without calculating a global score: five independently attested stages, engineering-profile availability, reviewed practice count and manually identified improvement areas. Double-click a row to open its detailed record. **Not assessed** and **Not applicable** never become failures.

Local qualification records are stored separately at `%LOCALAPPDATA%\kOA-GitHub-Audit\profiles\qualification.json`. They remain on the user's PC, are not included in the public dashboard, and do not modify source repositories. Read [Certification and Continuous Improvement](docs/CERTIFICATION_AND_IMPROVEMENT.md) for the source-derived model and treatment of false positives.

## Interactive dashboard and GitHub Pages

The primary `docs/index.html` is an **interactive application directory and atlas**, not a grade or vulnerability scoreboard. It provides the source-grounded system map and 49-repository constellation, allows applications to be selected, and opens directly readable Engineering Profiles.

- **Local preview:** in **Écosystème**, click **Ouvrir le centre de pilotage (carte + profils)**. A loopback-only server provides the full local profile Markdown and current **status-only** qualification registry. The free-form evidence references, notes and scope are **never** exposed through its JSON endpoint.
- **Public GitHub Pages:** `docs/engineering/<repo>.html` contains only allowlisted summary measurements, without private file paths or original Markdown. The site now includes **the names of the 49 public repositories** and documented conceptual roles, because the requested map must identify the applications. Users should review this explicit new public scope before publishing.
- **Completion graphics:** five bars show separately specified, implemented, qualified, integrated and production-proven statuses. Each state requires user review. On public Pages qualification is displayed as **not published**, never as zero-quality or failed completion.
- **Coverage:** the current bundled data shows **12/49 measured engineering profiles** and the last supplied local audit covered **47/49 repositories**. These count different kinds of evidence. Neither indicator is a test pass rate or product completion percentage.
- **Archived diagnostics:** the previous scan summary is retained as `docs/observations.html`, secondary to the application journey. Legacy false positives, filename matches, similar repositories and unknown API states are not automatic failures.
- **Publish:** **Publier sur GitHub** asks for approval and uses the configured Git credentials. It pushes an allowlist of generated atlas files and profile pages plus aggregate audit JSON to the dedicated **audit repository only** (never source checkouts, never force-push, no raw reports). GitHub permissions may block publishing. If needed enable GitHub Pages under **Settings → Pages → Source: GitHub Actions**.

The browser reloads the publication data when requested; no remote page can inspect your `C:\mycode` folder. The GitHub Wiki is a separate service. See [atlas sources and public/private boundaries](docs/ATLAS_SOURCE_AND_METHOD.md) and [dashboard instructions](docs/DASHBOARD_FR.md).

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
- **`REVIEW`** means a heuristic finding should be checked in context; not a negative certification status.
- **`OBSERVED_INFORMATIONAL`** means informational observations only (for example, an `.env`-style filename or a workflow action referenced by a tag). This is **not an incident**.
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
- **[Certification framework](wiki/Certification-and-Continuous-Improvement.md)** — evidence-scoped milestones and conservative scan interpretation.
- **[Profiles and checklist](wiki/Repository-Profiles-and-Checklist.md)** — importing reports and recording assessments.
- **[Dashboard and publishing](wiki/Dashboard-and-Publishing.md)** — preview, publication, and privacy.
- **[Troubleshooting](wiki/Troubleshooting.md)** — Windows launcher, preview and Git publishing problems.
- [Existing technical documentation](docs/ARCHITECTURE.md) and [French UI guide](docs/LAUNCHER_FR.md).

**GitHub Wiki publication:** `wiki/` is a set of ready-to-use Wiki Markdown pages, not an automatically published GitHub Wiki. GitHub Wikis are separate repositories. See [Wiki-Publishing](wiki/Wiki-Publishing.md) for the one-time setup and safe publishing steps.

## Security, governance, and license

This audit repository has **no authority to change source projects, approve releases, or certify security**. The `kOA-Digital-Ecosystem` repository retains inventory/governance authority; specialized diagnostics retain their own qualification meaning. The application does not replace CodeQL, advisory-database analysis, secret scanning, or production tests. See [SECURITY.md](SECURITY.md).

**No open-source license has been selected.**


## Local Kristal kOA Ecosystem source (v0.9.1)

The Windows dashboard now reads the **canonical Kristal catalogs directly** from your
local repository, without copying them into the public GitHub Pages site.

Default directory (editable in the **Écosystème** tab):

```text
C:\mycode\Kristal\locals\Kristal-kOA-Ecosystem
```

Use **Vérifier Kristal** to check the source, then click **Ouvrir le centre de
pilotage**. In the browser, choose **Kristal canonique · 49 dépôts** and select
an application. The **Kristal (local)** detail tab shows the repository's
canonical description, explicitly linked components, and their sourced/claimed
relations. **Actualiser** reloads these catalogs; no repository-wide audit is run.

The local reader uses only:

- `knowledge-base/sources/repositories.json`
- `knowledge-base/sources/components.json`
- `knowledge-base/sources/relations.json`

These are editorial canonical inputs in Kristal; generated `views/`, the portable
state, `.kristal/v8`, `.kristal/v9` and local paths are **not** used as new evidence.
Repository matching is exact by GitHub `owner/repo`, so 49 official repositories
can be reconciled while component links remain explicitly limited to the ones
actually present in the graph. A semantic relation is **not** a proven runtime
integration, passed test, or certification.

`KOA_KRISTAL_SOURCE` may override the default for a session. A selected source
folder is remembered outside the application under your local application-data
directory. The HTTP preview binds exclusively to `127.0.0.1`; its `/api/kristal/atlas`
endpoint returns an allowlisted local projection. Neither that endpoint nor the
Kristal catalogs are part of the published GitHub Pages artifact. If the folder
is missing, the bundled kOA map and Engineering Profiles still work.
