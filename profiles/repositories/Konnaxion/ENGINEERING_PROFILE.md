# Engineering Profile

> **Repository:** `Rejean-McCormick/Konnaxion`  
> **Snapshot captured:** `2026-10-29T09:20:04.489512` (index-local timestamp; timezone not specified)  
> **Snapshot SHA-256:** `0e016950aa7e468d5e6c88a02518cc5c9e0c99c9f5fe75391dd9cd45b3707319`  
> **Source:** `EP.zip` → `Konnaxion_Code_snapshot.zip`  
> **Analysis scope:** RepoSurveyor active-file rules + exclusion of `.koali-update-backups/**` and embedded snapshot indexes.  
> **Limitation:** no project code, CI or tests were executed. `scc`, Lizard and Ctags were unavailable.  

> Generated deterministically using the RepoSurveyor 1.0 survey/profile engine from the supplied code snapshot. This is **not a live checkout**. 
> This is a scale/engineering-surface characterization, not a quality score or release-readiness claim.

## Engineering Footprint

- **1,166** files in the active engineering surface
- **859** active source files
- **796** production source files
- **63** test source files
- **196** active documentation files
- **109,361** production nonblank physical source lines
- **7,886** test nonblank physical source lines
- **57** migration-related files
- **7** schema-related files
- **55** probable HTTP route declarations *(medium-confidence framework scan)*
- **276** statically detected test declarations *(not executed-test count)*

## Language Footprint

| Language | Nonblank physical source lines |
|---|---:|
| TypeScript | 82,660 |
| Python | 30,107 |
| JavaScript | 1,971 |
| PowerShell | 1,172 |
| CSS | 657 |
| HTML | 544 |
| Shell | 73 |
| SQL | 63 |

Method: RepoSurveyor extension classification + nonblank physical line count. Comments are included in this fallback measure.

## Structural Surface

| Area | Files | Source files | Docs | Nonblank source lines |
|---|---:|---:|---:|---:|
| `frontend` | 540 | 521 | 5 | 85,824 |
| `backend` | 375 | 319 | 17 | 29,272 |
| `scripts` | 5 | 5 | 0 | 752 |
| `(root)` | 50 | 6 | 15 | 464 |
| `tools` | 5 | 4 | 0 | 380 |
| `cinematic` | 8 | 2 | 0 | 346 |
| `koali` | 2 | 2 | 0 | 209 |
| `docs` | 158 | 0 | 158 | 0 |
| `PlantUML` | 18 | 0 | 0 | 0 |
| `.github` | 4 | 0 | 1 | 0 |
| `Structurizr` | 1 | 0 | 0 | 0 |

## Complexity

Per-function complexity metrics unavailable; no complexity claim is published.

## Verification Surface

- Static test declarations: **276** — static language-aware declaration scan; not collected/executed/passed tests
- No supported existing coverage report detected.

## Detected Engineering Controls

- **Automated tests** — configured/detected via `backend/pyproject.toml`
- **Browser/E2E testing** — configured/detected via `frontend/playwright-smokeREADME.txt`, `frontend/playwright.config.ts`, `frontend/playwright.ct.config.ts` (+3 more)
- **CI configuration** — configured/detected via `.github/workflows/ci.yml`, `.github/workflows/full-qualification.yml`
- **Containerization** — configured/detected via `backend/compose/local/django/Dockerfile`, `backend/compose/local/docs/Dockerfile`, `backend/compose/production/django/Dockerfile` (+4 more)
- **Linting** — configured/detected via `backend/pyproject.toml`, `frontend/eslint.config.mjs`
- **Pre-commit hooks** — configured/detected via `backend/.pre-commit-config.yaml`
- **Static typing** — configured/detected via `backend/pyproject.toml`, `frontend/tsconfig.json`

## Analysis Scope

- Active surface: **1,166** files
- Excluded `archive-copy`: **5** files
- Excluded `diagnostic-evidence`: **1** files
- Excluded `private-local`: **4** files

## Measurement Notes

- Generated: `2026-10-29T13:55:32.224365+00:00`
- RepoSurveyor survey schema: `1.0`
- Source model: extracted snapshot of local files supplied in `EP.zip`; neither live repository state nor Git history was checked.
- Archive copies, diagnostics, dependency caches, generated output, lockfiles and private local configuration are excluded from the active engineering surface.
- Tool/configuration presence is evidence of configured engineering infrastructure, not evidence that its latest run passed.
- Static test declarations are not the same as collected, executed or passing tests.
- Existing coverage reports are not treated as freshly measured coverage.
- RepoSurveyor never converts these measurements into a synthetic quality, maturity or architecture score.

## Historical Profile Reference (Not Current)

- A user-supplied RepoSurveyor profile was captured on **2026-09-16** and is preserved as `ENGINEERING_PROFILE_2026-09-16_HISTORICAL.md`.
- That previous run reported Lizard complexity metrics. They are **not reproduced or projected forward** to this 2026-10-29 snapshot.
- Differences in file scope, snapshot content and tool availability mean the two totals are not a controlled trend.
