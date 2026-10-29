# Engineering Profile

> **Repository:** `Rejean-McCormick/Konnaxion-Capsule-Manager`  
> **Snapshot captured:** `2026-10-29T09:20:07.844345` (index-local timestamp; timezone not specified)  
> **Snapshot SHA-256:** `b8b5d705c81f672bc8754a46ae14cc99fb79469ad037484c8e8bb0b13057bc24`  
> **Source:** `EP.zip` → `Konnaxion_Capsule_Manager_Code_snapshot.zip`  
> **Analysis scope:** RepoSurveyor active-file rules + exclusion of `.koali-update-backups/**` and embedded snapshot indexes.  
> **Limitation:** no project code, CI or tests were executed. `scc`, Lizard and Ctags were unavailable.  

> Generated deterministically using the RepoSurveyor 1.0 survey/profile engine from the supplied code snapshot. This is **not a live checkout**. 
> This is a scale/engineering-surface characterization, not a quality score or release-readiness claim.

## Engineering Footprint

- **366** files in the active engineering surface
- **270** active source files
- **192** production source files
- **78** test source files
- **45** active documentation files
- **83,736** production nonblank physical source lines
- **15,642** test nonblank physical source lines
- **2** schema-related files
- **127** probable HTTP route declarations *(medium-confidence framework scan)*
- **801** statically detected test declarations *(not executed-test count)*

## Language Footprint

| Language | Nonblank physical source lines |
|---|---:|
| Python | 97,342 |
| PowerShell | 1,500 |
| JavaScript | 536 |

Method: RepoSurveyor extension classification + nonblank physical line count. Comments are included in this fallback measure.

## Structural Surface

| Area | Files | Source files | Docs | Nonblank source lines |
|---|---:|---:|---:|---:|
| `kx_manager` | 80 | 80 | 0 | 31,909 |
| `kx_agent` | 46 | 46 | 0 | 26,359 |
| `tests` | 73 | 73 | 0 | 15,277 |
| `tools` | 50 | 46 | 1 | 11,182 |
| `kx_builder` | 10 | 10 | 0 | 8,403 |
| `kx_shared` | 7 | 7 | 0 | 2,928 |
| `kx_cli` | 7 | 7 | 0 | 2,700 |
| `(root)` | 52 | 1 | 18 | 620 |
| `docs` | 26 | 0 | 26 | 0 |
| `profiles` | 6 | 0 | 0 | 0 |
| `.github` | 3 | 0 | 0 | 0 |
| `policies` | 3 | 0 | 0 | 0 |
| `templates` | 3 | 0 | 0 | 0 |

## Complexity

Per-function complexity metrics unavailable; no complexity claim is published.

## Verification Surface

- Static test declarations: **801** — static language-aware declaration scan; not collected/executed/passed tests
- No supported existing coverage report detected.

## Detected Engineering Controls

- **Automated tests** — configured/detected via `pyproject.toml`
- **CI configuration** — configured/detected via `.github/workflows/ci.yml`, `.github/workflows/full-tests.yml`
- **Linting** — configured/detected via `pyproject.toml`
- **Static typing** — configured/detected via `pyproject.toml`

## Analysis Scope

- Active surface: **366** files
- Excluded `diagnostic-evidence`: **1** files
- Excluded `private-local`: **1** files

## Measurement Notes

- Generated: `2026-10-29T13:55:30.262925+00:00`
- RepoSurveyor survey schema: `1.0`
- Source model: extracted snapshot of local files supplied in `EP.zip`; neither live repository state nor Git history was checked.
- Archive copies, diagnostics, dependency caches, generated output, lockfiles and private local configuration are excluded from the active engineering surface.
- Tool/configuration presence is evidence of configured engineering infrastructure, not evidence that its latest run passed.
- Static test declarations are not the same as collected, executed or passing tests.
- Existing coverage reports are not treated as freshly measured coverage.
- RepoSurveyor never converts these measurements into a synthetic quality, maturity or architecture score.
