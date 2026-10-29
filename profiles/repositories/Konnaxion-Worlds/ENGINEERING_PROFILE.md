# Engineering Profile

> **Repository:** `Rejean-McCormick/Konnaxion-Worlds`  
> **Snapshot captured:** `2026-10-29T09:20:06.767048` (index-local timestamp; timezone not specified)  
> **Snapshot SHA-256:** `b9c26095cd514823ca852690a6ca8b63c666eabe868b6e3430d798b503329b6f`  
> **Source:** `EP.zip` → `Konnaxion_Worlds_Code_snapshot.zip`  
> **Analysis scope:** RepoSurveyor active-file rules + exclusion of `.koali-update-backups/**` and embedded snapshot indexes.  
> **Limitation:** no project code, CI or tests were executed. `scc`, Lizard and Ctags were unavailable.  

> Generated deterministically using the RepoSurveyor 1.0 survey/profile engine from the supplied code snapshot. This is **not a live checkout**. 
> This is a scale/engineering-surface characterization, not a quality score or release-readiness claim.

## Engineering Footprint

- **507** files in the active engineering surface
- **82** active source files
- **67** production source files
- **15** test source files
- **155** active documentation files
- **8,582** production nonblank physical source lines
- **1,150** test nonblank physical source lines
- **5** migration-related files
- **1** schema-related files
- **38** probable HTTP route declarations *(medium-confidence framework scan)*
- **69** statically detected test declarations *(not executed-test count)*

## Language Footprint

| Language | Nonblank physical source lines |
|---|---:|
| Python | 9,569 |
| PowerShell | 163 |

Method: RepoSurveyor extension classification + nonblank physical line count. Comments are included in this fallback measure.

## Structural Surface

| Area | Files | Source files | Docs | Nonblank source lines |
|---|---:|---:|---:|---:|
| `backend` | 80 | 70 | 3 | 8,789 |
| `tools` | 8 | 6 | 1 | 579 |
| `scripts` | 3 | 3 | 0 | 201 |
| `(root)` | 19 | 3 | 4 | 163 |
| `legacy-world-packs` | 218 | 0 | 99 | 0 |
| `universes` | 137 | 0 | 12 | 0 |
| `docs` | 36 | 0 | 36 | 0 |
| `.github` | 3 | 0 | 0 | 0 |
| `examples` | 3 | 0 | 0 | 0 |

## Complexity

Per-function complexity metrics unavailable; no complexity claim is published.

## Verification Surface

- Static test declarations: **69** — static language-aware declaration scan; not collected/executed/passed tests
- No supported existing coverage report detected.

## Detected Engineering Controls

- **CI configuration** — configured/detected via `.github/workflows/ci.yml`, `.github/workflows/postgres-integration.yml`

## Analysis Scope

- Active surface: **507** files
- Excluded `archive-copy`: **2** files
- Excluded `diagnostic-evidence`: **2** files
- Excluded `private-local`: **1** files

## Measurement Notes

- Generated: `2026-10-29T13:55:32.629971+00:00`
- RepoSurveyor survey schema: `1.0`
- Source model: extracted snapshot of local files supplied in `EP.zip`; neither live repository state nor Git history was checked.
- Archive copies, diagnostics, dependency caches, generated output, lockfiles and private local configuration are excluded from the active engineering surface.
- Tool/configuration presence is evidence of configured engineering infrastructure, not evidence that its latest run passed.
- Static test declarations are not the same as collected, executed or passing tests.
- Existing coverage reports are not treated as freshly measured coverage.
- RepoSurveyor never converts these measurements into a synthetic quality, maturity or architecture score.
