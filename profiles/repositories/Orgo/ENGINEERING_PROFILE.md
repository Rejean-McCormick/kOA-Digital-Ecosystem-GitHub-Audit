# Engineering Profile

> **Repository:** `Rejean-McCormick/Orgo`  
> **Snapshot captured:** `2026-10-29T09:19:41.417697` (index-local timestamp; timezone not specified)  
> **Snapshot SHA-256:** `e48be0980da709a7a04e196d8a49e3e9202a2b3836f2406b8bb078c7fe572ca2`  
> **Source:** `EP.zip` → `Orgo_Code_snapshot.zip`  
> **Analysis scope:** RepoSurveyor active-file rules + exclusion of `.koali-update-backups/**` and embedded snapshot indexes.  
> **Limitation:** no project code, CI or tests were executed. `scc`, Lizard and Ctags were unavailable.  

> Generated deterministically using the RepoSurveyor 1.0 survey/profile engine from the supplied code snapshot. This is **not a live checkout**. 
> This is a scale/engineering-surface characterization, not a quality score or release-readiness claim.

## Engineering Footprint

- **363** files in the active engineering surface
- **162** active source files
- **138** production source files
- **24** test source files
- **92** active documentation files
- **21,233** production nonblank physical source lines
- **2,623** test nonblank physical source lines
- **2** migration-related files
- **3** schema-related files
- **120** probable HTTP route declarations *(medium-confidence framework scan)*
- **69** statically detected test declarations *(not executed-test count)*

## Language Footprint

| Language | Nonblank physical source lines |
|---|---:|
| TypeScript | 15,418 |
| JavaScript | 3,056 |
| SQL | 1,741 |
| Python | 1,424 |
| CSS | 1,217 |
| PowerShell | 981 |
| Shell | 19 |

Method: RepoSurveyor extension classification + nonblank physical line count. Comments are included in this fallback measure.

## Structural Surface

| Area | Files | Source files | Docs | Nonblank source lines |
|---|---:|---:|---:|---:|
| `apps` | 107 | 93 | 2 | 18,133 |
| `tools` | 79 | 51 | 11 | 3,945 |
| `(root)` | 77 | 6 | 18 | 820 |
| `validation` | 11 | 4 | 5 | 555 |
| `scripts` | 8 | 8 | 0 | 403 |
| `docs` | 55 | 0 | 55 | 0 |
| `charters` | 19 | 0 | 0 | 0 |
| `.github` | 4 | 0 | 1 | 0 |
| `examples` | 3 | 0 | 0 | 0 |

## Complexity

Per-function complexity metrics unavailable; no complexity claim is published.

## Verification Surface

- Static test declarations: **69** — static language-aware declaration scan; not collected/executed/passed tests
- No supported existing coverage report detected.

## Detected Engineering Controls

- **CI configuration** — configured/detected via `.github/workflows/ci.yml`, `.github/workflows/deep-qualification.yml`, `.github/workflows/levelupdiag.yml`
- **Containerization** — configured/detected via `apps/api/Dockerfile`, `apps/web/Dockerfile`, `docker-compose.yml`
- **Static typing** — configured/detected via `apps/api/tsconfig.json`, `apps/web/tsconfig.json`

## Analysis Scope

- Active surface: **363** files
- Excluded `diagnostic-evidence`: **1** files
- Excluded `private-local`: **3** files

## Measurement Notes

- Generated: `2026-10-29T13:55:33.399949+00:00`
- RepoSurveyor survey schema: `1.0`
- Source model: extracted snapshot of local files supplied in `EP.zip`; neither live repository state nor Git history was checked.
- Archive copies, diagnostics, dependency caches, generated output, lockfiles and private local configuration are excluded from the active engineering surface.
- Tool/configuration presence is evidence of configured engineering infrastructure, not evidence that its latest run passed.
- Static test declarations are not the same as collected, executed or passing tests.
- Existing coverage reports are not treated as freshly measured coverage.
- RepoSurveyor never converts these measurements into a synthetic quality, maturity or architecture score.
