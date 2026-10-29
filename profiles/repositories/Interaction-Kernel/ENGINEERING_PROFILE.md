# Engineering Profile

> **Repository:** `Rejean-McCormick/Interaction-Kernel`  
> **Snapshot captured:** `2026-10-29T09:19:43.041256` (index-local timestamp; timezone not specified)  
> **Snapshot SHA-256:** `807afae17c440b16961f3bbdb8266f8b32050528df784b73f731154864eea7da`  
> **Source:** `EP.zip` → `interaction_kernel_Code_snapshot.zip`  
> **Analysis scope:** RepoSurveyor active-file rules + exclusion of `.koali-update-backups/**` and embedded snapshot indexes.  
> **Limitation:** no project code, CI or tests were executed. `scc`, Lizard and Ctags were unavailable.  

> Generated deterministically using the RepoSurveyor 1.0 survey/profile engine from the supplied code snapshot. This is **not a live checkout**. 
> This is a scale/engineering-surface characterization, not a quality score or release-readiness claim.

## Engineering Footprint

- **165** files in the active engineering surface
- **47** active source files
- **30** production source files
- **17** test source files
- **43** active documentation files
- **1,206** production nonblank physical source lines
- **550** test nonblank physical source lines
- **25** schema-related files
- **25** statically detected test declarations *(not executed-test count)*

## Language Footprint

| Language | Nonblank physical source lines |
|---|---:|
| Python | 1,432 |
| TypeScript | 140 |
| JavaScript | 108 |
| PowerShell | 42 |
| Shell | 34 |

Method: RepoSurveyor extension classification + nonblank physical line count. Comments are included in this fallback measure.

## Structural Surface

| Area | Files | Source files | Docs | Nonblank source lines |
|---|---:|---:|---:|---:|
| `runtime` | 27 | 23 | 0 | 750 |
| `tools` | 15 | 9 | 4 | 470 |
| `adapters` | 11 | 6 | 4 | 309 |
| `scripts` | 9 | 9 | 0 | 227 |
| `contracts` | 38 | 0 | 0 | 0 |
| `docs` | 25 | 0 | 25 | 0 |
| `locks` | 18 | 0 | 2 | 0 |
| `(root)` | 14 | 0 | 5 | 0 |
| `tck` | 6 | 0 | 3 | 0 |
| `.github` | 2 | 0 | 0 | 0 |

## Complexity

Per-function complexity metrics unavailable; no complexity claim is published.

## Verification Surface

- Static test declarations: **25** — static language-aware declaration scan; not collected/executed/passed tests
- No supported existing coverage report detected.

## Detected Engineering Controls

- **Architecture decisions** — configured/detected via `docs/adrs/ADR-IK-01-runtime-pack-activation-owner.md`, `docs/adrs/ADR-IK-02-kristal-pin.md`, `docs/adrs/ADR-IK-03-decision-record.md` (+5 more)
- **CI configuration** — configured/detected via `.github/workflows/ci.yml`
- **Machine-readable schemas** — configured/detected via `contracts/schemas/artifact-ref.schema.json`, `contracts/schemas/envelope.schema.json`, `contracts/schemas/export-manifest.schema.json` (+7 more)
- **Static typing** — configured/detected via `runtime/typescript/tsconfig.json`

## Analysis Scope

- Active surface: **165** files
- Excluded `diagnostic-evidence`: **2** files

## Measurement Notes

- Generated: `2026-10-29T13:55:27.464648+00:00`
- RepoSurveyor survey schema: `1.0`
- Source model: extracted snapshot of local files supplied in `EP.zip`; neither live repository state nor Git history was checked.
- Archive copies, diagnostics, dependency caches, generated output, lockfiles and private local configuration are excluded from the active engineering surface.
- Tool/configuration presence is evidence of configured engineering infrastructure, not evidence that its latest run passed.
- Static test declarations are not the same as collected, executed or passing tests.
- Existing coverage reports are not treated as freshly measured coverage.
- RepoSurveyor never converts these measurements into a synthetic quality, maturity or architecture score.
