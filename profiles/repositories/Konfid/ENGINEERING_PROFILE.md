# Engineering Profile

> **Repository:** `Rejean-McCormick/Konfid`  
> **Snapshot captured:** `2026-10-29T09:19:52.416756` (index-local timestamp; timezone not specified)  
> **Snapshot SHA-256:** `34e129063c065ab9eda3909cd15cc39bdde519ecae411db3ebb975b548088cff`  
> **Source:** `EP.zip` → `konfid_Code_snapshot.zip`  
> **Analysis scope:** RepoSurveyor active-file rules + exclusion of `.koali-update-backups/**` and embedded snapshot indexes.  
> **Limitation:** no project code, CI or tests were executed. `scc`, Lizard and Ctags were unavailable.  

> Generated deterministically using the RepoSurveyor 1.0 survey/profile engine from the supplied code snapshot. This is **not a live checkout**. 
> This is a scale/engineering-surface characterization, not a quality score or release-readiness claim.

## Engineering Footprint

- **99** files in the active engineering surface
- **47** active source files
- **37** production source files
- **10** test source files
- **17** active documentation files
- **5,069** production nonblank physical source lines
- **969** test nonblank physical source lines
- **4** migration-related files
- **2** schema-related files
- **47** probable HTTP route declarations *(medium-confidence framework scan)*
- **52** statically detected test declarations *(not executed-test count)*

## Language Footprint

| Language | Nonblank physical source lines |
|---|---:|
| Python | 6,028 |
| Shell | 10 |

Method: RepoSurveyor extension classification + nonblank physical line count. Comments are included in this fallback measure.

## Structural Surface

| Area | Files | Source files | Docs | Nonblank source lines |
|---|---:|---:|---:|---:|
| `src` | 31 | 31 | 0 | 3,990 |
| `tests` | 9 | 9 | 0 | 904 |
| `migrations` | 4 | 3 | 0 | 580 |
| `tools` | 7 | 3 | 3 | 554 |
| `scripts` | 1 | 1 | 0 | 10 |
| `(root)` | 20 | 0 | 4 | 0 |
| `deploy` | 10 | 0 | 0 | 0 |
| `docs` | 9 | 0 | 9 | 0 |
| `examples` | 4 | 0 | 0 | 0 |
| `.github` | 3 | 0 | 0 | 0 |
| `constraints` | 1 | 0 | 1 | 0 |

## Complexity

Per-function complexity metrics unavailable; no complexity claim is published.

## Verification Surface

- Static test declarations: **52** — static language-aware declaration scan; not collected/executed/passed tests
- No supported existing coverage report detected.

## Detected Engineering Controls

- **Automated tests** — configured/detected via `pyproject.toml`
- **CI configuration** — configured/detected via `.github/workflows/ci.yml`, `.github/workflows/codeql.yml`
- **Containerization** — configured/detected via `Dockerfile`, `docker-compose.yml`

## Analysis Scope

- Active surface: **99** files
- Excluded `archive-copy`: **2** files
- Excluded `diagnostic-evidence`: **1** files
- Excluded `private-local`: **3** files

## Measurement Notes

- Generated: `2026-10-29T13:55:29.896254+00:00`
- RepoSurveyor survey schema: `1.0`
- Source model: extracted snapshot of local files supplied in `EP.zip`; neither live repository state nor Git history was checked.
- Archive copies, diagnostics, dependency caches, generated output, lockfiles and private local configuration are excluded from the active engineering surface.
- Tool/configuration presence is evidence of configured engineering infrastructure, not evidence that its latest run passed.
- Static test declarations are not the same as collected, executed or passing tests.
- Existing coverage reports are not treated as freshly measured coverage.
- RepoSurveyor never converts these measurements into a synthetic quality, maturity or architecture score.
