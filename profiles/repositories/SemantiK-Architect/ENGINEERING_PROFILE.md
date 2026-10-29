# Engineering Profile

> **Repository:** `Rejean-McCormick/SemantiK-Architect`  
> **Snapshot captured:** `2026-10-29T09:20:10.590570` (index-local timestamp; timezone not specified)  
> **Snapshot SHA-256:** `b785d96bdab921534bf4875209aed5380e03602cf6eefaba58a284fbe66d9961`  
> **Source:** `EP.zip` → `SemantiK_Architect_Code_snapshot.zip`  
> **Analysis scope:** RepoSurveyor active-file rules + exclusion of `.koali-update-backups/**` and embedded snapshot indexes.  
> **Limitation:** no project code, CI or tests were executed. `scc`, Lizard and Ctags were unavailable.  

> Generated deterministically using the RepoSurveyor 1.0 survey/profile engine from the supplied code snapshot. This is **not a live checkout**. 
> This is a scale/engineering-surface characterization, not a quality score or release-readiness claim.

## Engineering Footprint

- **280** files in the active engineering surface
- **121** active source files
- **95** production source files
- **26** test source files
- **68** active documentation files
- **5,065** production nonblank physical source lines
- **1,099** test nonblank physical source lines
- **19** schema-related files
- **68** statically detected test declarations *(not executed-test count)*

## Language Footprint

| Language | Nonblank physical source lines |
|---|---:|
| Python | 6,164 |

Method: RepoSurveyor extension classification + nonblank physical line count. Comments are included in this fallback measure.

## Structural Surface

| Area | Files | Source files | Docs | Nonblank source lines |
|---|---:|---:|---:|---:|
| `src` | 91 | 91 | 0 | 4,681 |
| `tests` | 26 | 26 | 0 | 1,099 |
| `tools` | 4 | 4 | 0 | 384 |
| `docs` | 57 | 0 | 57 | 0 |
| `profiles` | 38 | 0 | 5 | 0 |
| `runtime` | 30 | 0 | 2 | 0 |
| `schemas` | 16 | 0 | 0 | 0 |
| `(root)` | 8 | 0 | 2 | 0 |
| `examples` | 8 | 0 | 2 | 0 |
| `.github` | 2 | 0 | 0 | 0 |

## Complexity

Per-function complexity metrics unavailable; no complexity claim is published.

## Verification Surface

- Static test declarations: **68** — static language-aware declaration scan; not collected/executed/passed tests
- No supported existing coverage report detected.

## Detected Engineering Controls

- **Architecture decisions** — configured/detected via `docs/adr/ADR-0001-single-canonical-architecture.md`, `docs/adr/ADR-0002-articulation-not-content-selection.md`, `docs/adr/ADR-0003-typed-semantic-graph-and-obligations.md` (+13 more)
- **CI configuration** — configured/detected via `.github/workflows/ci.yml`
- **Machine-readable schemas** — configured/detected via `schemas/capability_manifest.schema.json`, `schemas/capability_profile.schema.json`, `schemas/communication_request.schema.json` (+13 more)

## Analysis Scope

- Active surface: **280** files
- Excluded `diagnostic-evidence`: **2** files
- Excluded `local-ignore`: **1** files

## Measurement Notes

- Generated: `2026-10-29T13:55:27.259742+00:00`
- RepoSurveyor survey schema: `1.0`
- Source model: extracted snapshot of local files supplied in `EP.zip`; neither live repository state nor Git history was checked.
- Archive copies, diagnostics, dependency caches, generated output, lockfiles and private local configuration are excluded from the active engineering surface.
- Tool/configuration presence is evidence of configured engineering infrastructure, not evidence that its latest run passed.
- Static test declarations are not the same as collected, executed or passing tests.
- Existing coverage reports are not treated as freshly measured coverage.
- RepoSurveyor never converts these measurements into a synthetic quality, maturity or architecture score.
