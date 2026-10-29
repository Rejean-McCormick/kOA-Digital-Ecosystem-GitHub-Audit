# Engineering Profile

> **Repository:** `Rejean-McCormick/Kristal-Framework`  
> **Snapshot captured:** `2026-10-29T09:20:09.355540` (index-local timestamp; timezone not specified)  
> **Snapshot SHA-256:** `33ab2e2f39dd933bc179c643ac7579c3be703ddca108a76a20e0119b13cd0ec5`  
> **Source:** `EP.zip` → `Kristal-Framework_Code_snapshot.zip`  
> **Analysis scope:** RepoSurveyor active-file rules + exclusion of `.koali-update-backups/**` and embedded snapshot indexes.  
> **Limitation:** no project code, CI or tests were executed. `scc`, Lizard and Ctags were unavailable.  

> Generated deterministically using the RepoSurveyor 1.0 survey/profile engine from the supplied code snapshot. This is **not a live checkout**. 
> This is a scale/engineering-surface characterization, not a quality score or release-readiness claim.

## Engineering Footprint

- **619** files in the active engineering surface
- **72** active source files
- **58** production source files
- **14** test source files
- **293** active documentation files
- **8,288** production nonblank physical source lines
- **1,415** test nonblank physical source lines
- **3** migration-related files
- **73** schema-related files
- **93** statically detected test declarations *(not executed-test count)*

## Language Footprint

| Language | Nonblank physical source lines |
|---|---:|
| Python | 6,217 |
| JavaScript | 3,099 |
| HTML | 387 |

Method: RepoSurveyor extension classification + nonblank physical line count. Comments are included in this fallback measure.

## Structural Surface

| Area | Files | Source files | Docs | Nonblank source lines |
|---|---:|---:|---:|---:|
| `tools` | 48 | 35 | 6 | 6,651 |
| `reference` | 44 | 36 | 4 | 3,038 |
| `tests` | 1 | 1 | 0 | 14 |
| `spec` | 241 | 0 | 201 | 0 |
| `examples` | 64 | 0 | 1 | 0 |
| `tck` | 62 | 0 | 9 | 0 |
| `schemas` | 50 | 0 | 4 | 0 |
| `docs` | 32 | 0 | 32 | 0 |
| `history` | 23 | 0 | 23 | 0 |
| `profiles` | 23 | 0 | 3 | 0 |
| `(root)` | 12 | 0 | 5 | 0 |
| `contracts` | 12 | 0 | 0 | 0 |
| `.github` | 3 | 0 | 1 | 0 |
| `migration` | 3 | 0 | 3 | 0 |
| `compat` | 1 | 0 | 1 | 0 |

## Complexity

Per-function complexity metrics unavailable; no complexity claim is published.

## Verification Surface

- Static test declarations: **93** — static language-aware declaration scan; not collected/executed/passed tests
- No supported existing coverage report detected.

## Detected Engineering Controls

- **CI configuration** — configured/detected via `.github/workflows/ci.yml`, `.github/workflows/release-qualification.yml`
- **Machine-readable schemas** — configured/detected via `profiles/github/schemas/kristal-github-binding.schema.json`, `profiles/github/schemas/kristal-github-collection-index.schema.json`, `profiles/github/schemas/kristal-github-read-surface.schema.json` (+27 more)

## Analysis Scope

- Active surface: **619** files
- Excluded `diagnostic-evidence`: **2** files

## Measurement Notes

- Generated: `2026-10-29T13:55:33.076321+00:00`
- RepoSurveyor survey schema: `1.0`
- Source model: extracted snapshot of local files supplied in `EP.zip`; neither live repository state nor Git history was checked.
- Archive copies, diagnostics, dependency caches, generated output, lockfiles and private local configuration are excluded from the active engineering surface.
- Tool/configuration presence is evidence of configured engineering infrastructure, not evidence that its latest run passed.
- Static test declarations are not the same as collected, executed or passing tests.
- Existing coverage reports are not treated as freshly measured coverage.
- RepoSurveyor never converts these measurements into a synthetic quality, maturity or architecture score.
