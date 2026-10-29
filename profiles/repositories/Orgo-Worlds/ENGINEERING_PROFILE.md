# Engineering Profile

> **Repository:** `Rejean-McCormick/Orgo-Worlds`  
> **Snapshot captured:** `2026-10-29T09:19:42.146911` (index-local timestamp; timezone not specified)  
> **Snapshot SHA-256:** `14e463c9761535656e131fd8c8c4b4e17b90ab5a976e17161080f1c9e0a79b10`  
> **Source:** `EP.zip` → `Orgo_Worlds_Code_snapshot.zip`  
> **Analysis scope:** RepoSurveyor active-file rules + exclusion of `.koali-update-backups/**` and embedded snapshot indexes.  
> **Limitation:** no project code, CI or tests were executed. `scc`, Lizard and Ctags were unavailable.  

> Generated deterministically using the RepoSurveyor 1.0 survey/profile engine from the supplied code snapshot. This is **not a live checkout**. 
> This is a scale/engineering-surface characterization, not a quality score or release-readiness claim.

## Engineering Footprint

- **195** files in the active engineering surface
- **48** active source files
- **36** production source files
- **12** test source files
- **54** active documentation files
- **2,934** production nonblank physical source lines
- **393** test nonblank physical source lines
- **10** probable HTTP route declarations *(medium-confidence framework scan)*
- **4** statically detected test declarations *(not executed-test count)*

## Language Footprint

| Language | Nonblank physical source lines |
|---|---:|
| TypeScript | 1,537 |
| JavaScript | 1,043 |
| Python | 693 |
| PowerShell | 54 |

Method: RepoSurveyor extension classification + nonblank physical line count. Comments are included in this fallback measure.

## Structural Surface

| Area | Files | Source files | Docs | Nonblank source lines |
|---|---:|---:|---:|---:|
| `tools` | 31 | 19 | 5 | 1,604 |
| `apps` | 12 | 10 | 0 | 1,118 |
| `scripts` | 14 | 12 | 0 | 530 |
| `(root)` | 39 | 2 | 6 | 42 |
| `packages` | 16 | 5 | 2 | 33 |
| `world-packs` | 44 | 0 | 13 | 0 |
| `docs` | 27 | 0 | 27 | 0 |
| `fakeplant` | 9 | 0 | 1 | 0 |
| `runtime` | 2 | 0 | 0 | 0 |
| `.github` | 1 | 0 | 0 | 0 |

## Complexity

Per-function complexity metrics unavailable; no complexity claim is published.

## Verification Surface

- Static test declarations: **4** — static language-aware declaration scan; not collected/executed/passed tests
- No supported existing coverage report detected.

## Detected Engineering Controls

- **CI configuration** — configured/detected via `.github/workflows/ci.yml`
- **Static typing** — configured/detected via `apps/api/tsconfig.json`, `apps/web/tsconfig.json`, `packages/ui/tsconfig.json`

## Analysis Scope

- Active surface: **195** files
- Excluded `archive-copy`: **3** files
- Excluded `diagnostic-evidence`: **2** files

## Measurement Notes

- Generated: `2026-10-29T13:55:27.065271+00:00`
- RepoSurveyor survey schema: `1.0`
- Source model: extracted snapshot of local files supplied in `EP.zip`; neither live repository state nor Git history was checked.
- Archive copies, diagnostics, dependency caches, generated output, lockfiles and private local configuration are excluded from the active engineering surface.
- Tool/configuration presence is evidence of configured engineering infrastructure, not evidence that its latest run passed.
- Static test declarations are not the same as collected, executed or passing tests.
- Existing coverage reports are not treated as freshly measured coverage.
- RepoSurveyor never converts these measurements into a synthetic quality, maturity or architecture score.
