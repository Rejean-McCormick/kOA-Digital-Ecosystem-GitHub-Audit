# Engineering Profile

> **Repository:** `Rejean-McCormick/kOA-Linux-Koali`  
> **Snapshot captured:** `2026-10-29T09:19:49.178190` (index-local timestamp; timezone not specified)  
> **Snapshot SHA-256:** `2bc4ea44e9d2a0313b4d5abe999e9c2bf7650fa177f2001ba3d3699be99b737a`  
> **Source:** `EP.zip` → `koa-linux_Code_snapshot.zip`  
> **Analysis scope:** RepoSurveyor active-file rules + exclusion of `.koali-update-backups/**` and embedded snapshot indexes.  
> **Limitation:** no project code, CI or tests were executed. `scc`, Lizard and Ctags were unavailable.  

> Generated deterministically using the RepoSurveyor 1.0 survey/profile engine from the supplied code snapshot. This is **not a live checkout**. 
> This is a scale/engineering-surface characterization, not a quality score or release-readiness claim.

## Engineering Footprint

- **1,649** files in the active engineering surface
- **743** active source files
- **524** production source files
- **219** test source files
- **573** active documentation files
- **111,068** production nonblank physical source lines
- **33,147** test nonblank physical source lines
- **17** migration-related files
- **86** schema-related files
- **1,299** statically detected test declarations *(not executed-test count)*

## Language Footprint

| Language | Nonblank physical source lines |
|---|---:|
| Python | 131,295 |
| Rust | 12,165 |
| SQL | 547 |
| PowerShell | 130 |
| Shell | 78 |

Method: RepoSurveyor extension classification + nonblank physical line count. Comments are included in this fallback measure.

## Structural Surface

| Area | Files | Source files | Docs | Nonblank source lines |
|---|---:|---:|---:|---:|
| `components` | 365 | 326 | 15 | 59,361 |
| `integrations` | 248 | 127 | 11 | 20,145 |
| `host` | 105 | 36 | 3 | 10,188 |
| `operations` | 41 | 39 | 1 | 9,981 |
| `assembly` | 40 | 38 | 1 | 8,836 |
| `interfaces` | 28 | 12 | 1 | 8,583 |
| `tests` | 89 | 83 | 1 | 8,112 |
| `docs` | 520 | 28 | 520 | 7,717 |
| `tools` | 34 | 33 | 1 | 6,215 |
| `ci` | 20 | 12 | 2 | 2,445 |
| `release` | 21 | 5 | 2 | 2,200 |
| `dev` | 17 | 3 | 1 | 273 |
| `.tandem_tour8` | 3 | 1 | 1 | 159 |
| `packaging` | 38 | 0 | 1 | 0 |
| `profiles` | 32 | 0 | 2 | 0 |

## Complexity

Per-function complexity metrics unavailable; no complexity claim is published.

## Verification Surface

- Static test declarations: **1,299** — static language-aware declaration scan; not collected/executed/passed tests
- No supported existing coverage report detected.

## Detected Engineering Controls

- **Automated tests** — configured/detected via `assembly/pyproject.toml`, `components/audit-broker/pyproject.toml`, `components/governance-policy-runtime/pyproject.toml` (+11 more)
- **CI configuration** — configured/detected via `.github/workflows/components.yml`, `.github/workflows/contracts.yml`, `.github/workflows/documentation.yml` (+5 more)
- **Containerization** — configured/detected via `dev/containers/compose.yaml`, `dev/local-services/compose.yaml`
- **Linting** — configured/detected via `assembly/pyproject.toml`, `components/audit-broker/pyproject.toml`, `components/governance-policy-runtime/pyproject.toml` (+8 more)
- **Machine-readable schemas** — configured/detected via `docs/schemas/ai-context-package.schema.json`, `docs/schemas/ai-navigation.contract.schema.json`, `docs/schemas/architecture-patterns.contract.schema.json` (+17 more)
- **Pre-commit hooks** — configured/detected via `.pre-commit-config.yaml`
- **Static typing** — configured/detected via `components/audit-broker/pyproject.toml`, `components/publication-gateway/pyproject.toml`, `integrations/semantik-architect/adapter/pyproject.toml` (+2 more)

## Analysis Scope

- Active surface: **1,649** files
- Excluded `diagnostic-evidence`: **1** files

## Measurement Notes

- Generated: `2026-10-29T13:55:29.534421+00:00`
- RepoSurveyor survey schema: `1.0`
- Source model: extracted snapshot of local files supplied in `EP.zip`; neither live repository state nor Git history was checked.
- Archive copies, diagnostics, dependency caches, generated output, lockfiles and private local configuration are excluded from the active engineering surface.
- Tool/configuration presence is evidence of configured engineering infrastructure, not evidence that its latest run passed.
- Static test declarations are not the same as collected, executed or passing tests.
- Existing coverage reports are not treated as freshly measured coverage.
- RepoSurveyor never converts these measurements into a synthetic quality, maturity or architecture score.
