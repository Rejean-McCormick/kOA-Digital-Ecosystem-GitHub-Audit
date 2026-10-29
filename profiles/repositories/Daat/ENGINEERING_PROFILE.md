# Engineering Profile

> **Repository:** `Rejean-McCormick/Daat`  
> **Snapshot captured:** `2026-10-29T09:19:42.522007` (index-local timestamp; timezone not specified)  
> **Snapshot SHA-256:** `cf066769f22d478a59da3e1c16ccf90d1179a74afff5476fbc1fe3044648693d`  
> **Source:** `EP.zip` → `Daat_Code_snapshot.zip`  
> **Analysis scope:** RepoSurveyor active-file rules + exclusion of `.koali-update-backups/**` and embedded snapshot indexes.  
> **Limitation:** no project code, CI or tests were executed. `scc`, Lizard and Ctags were unavailable.  

> Generated deterministically using the RepoSurveyor 1.0 survey/profile engine from the supplied code snapshot. This is **not a live checkout**. 
> This is a scale/engineering-surface characterization, not a quality score or release-readiness claim.

## Engineering Footprint

- **134** files in the active engineering surface
- **25** active source files
- **18** production source files
- **7** test source files
- **72** active documentation files
- **885** production nonblank physical source lines
- **539** test nonblank physical source lines
- **16** schema-related files
- **82** statically detected test declarations *(not executed-test count)*

## Language Footprint

| Language | Nonblank physical source lines |
|---|---:|
| Python | 1,415 |
| Shell | 9 |

Method: RepoSurveyor extension classification + nonblank physical line count. Comments are included in this fallback measure.

## Structural Surface

| Area | Files | Source files | Docs | Nonblank source lines |
|---|---:|---:|---:|---:|
| `src` | 24 | 14 | 0 | 777 |
| `tests` | 7 | 7 | 0 | 539 |
| `tools` | 2 | 2 | 0 | 50 |
| `examples` | 3 | 1 | 0 | 49 |
| `(root)` | 13 | 1 | 8 | 9 |
| `wiki` | 34 | 0 | 34 | 0 |
| `docs` | 30 | 0 | 30 | 0 |
| `contracts` | 10 | 0 | 0 | 0 |
| `mappings` | 10 | 0 | 0 | 0 |
| `.github` | 1 | 0 | 0 | 0 |

## Complexity

Per-function complexity metrics unavailable; no complexity claim is published.

## Verification Surface

- Static test declarations: **82** — static language-aware declaration scan; not collected/executed/passed tests
- No supported existing coverage report detected.

## Detected Engineering Controls

- **Architecture decisions** — configured/detected via `docs/decisions/ADR-0001-DAAT-PURPOSE.md`, `docs/decisions/ADR-0002-ALIGNMENT-MEASUREMENT.md`, `docs/decisions/ADR-0003-IK-PROFILE-GOVERNANCE.md`
- **Automated tests** — configured/detected via `pyproject.toml`
- **CI configuration** — configured/detected via `.github/workflows/test.yml`

## Analysis Scope

- Active surface: **134** files
- Excluded `diagnostic-evidence`: **1** files
- Excluded `local-ignore`: **2** files

## Measurement Notes

- Generated: `2026-10-29T13:55:27.345403+00:00`
- RepoSurveyor survey schema: `1.0`
- Source model: extracted snapshot of local files supplied in `EP.zip`; neither live repository state nor Git history was checked.
- Archive copies, diagnostics, dependency caches, generated output, lockfiles and private local configuration are excluded from the active engineering surface.
- Tool/configuration presence is evidence of configured engineering infrastructure, not evidence that its latest run passed.
- Static test declarations are not the same as collected, executed or passing tests.
- Existing coverage reports are not treated as freshly measured coverage.
- RepoSurveyor never converts these measurements into a synthetic quality, maturity or architecture score.
