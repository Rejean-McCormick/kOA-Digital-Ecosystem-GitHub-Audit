# Engineering Profile

> **Repository:** `Rejean-McCormick/Koali-Spaces`  
> **Snapshot captured:** `2026-10-29T09:19:51.967421` (index-local timestamp; timezone not specified)  
> **Snapshot SHA-256:** `b710f090f320c70f4b0aa7df6c41ce253af4e2d6c7313f5be763fa83ecda76ef`  
> **Source:** `EP.zip` → `koali-spaces_Code_snapshot.zip`  
> **Analysis scope:** RepoSurveyor active-file rules + exclusion of `.koali-update-backups/**` and embedded snapshot indexes.  
> **Limitation:** no project code, CI or tests were executed. `scc`, Lizard and Ctags were unavailable.  

> Generated deterministically using the RepoSurveyor 1.0 survey/profile engine from the supplied code snapshot. This is **not a live checkout**. 
> This is a scale/engineering-surface characterization, not a quality score or release-readiness claim.

## Engineering Footprint

- **363** files in the active engineering surface
- **134** active source files
- **112** production source files
- **22** test source files
- **189** active documentation files
- **7,980** production nonblank physical source lines
- **1,478** test nonblank physical source lines
- **16** schema-related files
- **42** statically detected test declarations *(not executed-test count)*

## Language Footprint

| Language | Nonblank physical source lines |
|---|---:|
| TypeScript | 4,495 |
| JavaScript | 3,508 |
| Python | 609 |
| CSS | 510 |
| PowerShell | 336 |

Method: RepoSurveyor extension classification + nonblank physical line count. Comments are included in this fallback measure.

## Structural Surface

| Area | Files | Source files | Docs | Nonblank source lines |
|---|---:|---:|---:|---:|
| `src` | 71 | 71 | 0 | 4,408 |
| `server` | 17 | 17 | 0 | 1,683 |
| `tests-runtime` | 10 | 10 | 0 | 835 |
| `scripts` | 13 | 13 | 0 | 767 |
| `tests` | 11 | 11 | 0 | 574 |
| `launcher` | 3 | 2 | 0 | 450 |
| `.tandem_tour8` | 4 | 3 | 0 | 330 |
| `docs` | 184 | 2 | 184 | 186 |
| `tools` | 1 | 1 | 0 | 134 |
| `(root)` | 26 | 4 | 5 | 91 |
| `contracts` | 13 | 0 | 0 | 0 |
| `interface` | 4 | 0 | 0 | 0 |
| `public` | 3 | 0 | 0 | 0 |
| `config` | 2 | 0 | 0 | 0 |
| `.github` | 1 | 0 | 0 | 0 |

## Complexity

Per-function complexity metrics unavailable; no complexity claim is published.

## Verification Surface

- Static test declarations: **42** — static language-aware declaration scan; not collected/executed/passed tests
- No supported existing coverage report detected.

## Detected Engineering Controls

- **Architecture decisions** — configured/detected via `docs/06-surface-layer/adr/0000-template.md`, `docs/06-surface-layer/adr/0001-common-oidc-sso-profile.md`, `docs/06-surface-layer/adr/README.md` (+4 more)
- **CI configuration** — configured/detected via `.github/workflows/ci.yml`
- **Linting** — configured/detected via `eslint.config.mjs`
- **Machine-readable schemas** — configured/detected via `docs/06-surface-layer/schemas/application-conformance-profile.schema.json`, `docs/06-surface-layer/schemas/runtime-registration.schema.json`, `docs/06-surface-layer/schemas/surface-descriptor-public.schema.json` (+1 more)
- **Static typing** — configured/detected via `tsconfig.json`

## Analysis Scope

- Active surface: **363** files
- Excluded `archive-copy`: **68** files
- Excluded `diagnostic-evidence`: **1** files

## Measurement Notes

- Generated: `2026-10-29T13:55:29.838858+00:00`
- RepoSurveyor survey schema: `1.0`
- Source model: extracted snapshot of local files supplied in `EP.zip`; neither live repository state nor Git history was checked.
- Archive copies, diagnostics, dependency caches, generated output, lockfiles and private local configuration are excluded from the active engineering surface.
- Tool/configuration presence is evidence of configured engineering infrastructure, not evidence that its latest run passed.
- Static test declarations are not the same as collected, executed or passing tests.
- Existing coverage reports are not treated as freshly measured coverage.
- RepoSurveyor never converts these measurements into a synthetic quality, maturity or architecture score.
