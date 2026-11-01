<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/wiki/Testing-and-Qualification | commit: 01bfc9126e06db9560d1c84e4b315026a28690af | SHA-256: 8a58f4abf2903af598f3be80b0a758e745f75e5c2cf0ea339a50524731047502 -->

# Testing, Validation, and Qualification

## Available repository checks

With a compatible Node.js installation and installed dependencies:

```powershell
npm test
npm run test:ui
npm run build
npm run test:e2e:smoke
npm run test:e2e
npm run check:svelte-structure
npm run check:frontend-security
npm run release:preflight
npm run release:check
```

E2E commands require the appropriate Playwright browser installations and dependencies. The full pipeline is a **qualification condition**; the existence of scripts in `package.json` does not prove they passed on a user's computer.

## Essential neutral-selector regressions

- Starting without an active Kristal does not automatically open Théophile or Catho.
- The catalog lists only authorized immediate subdirectories.
- An incompatible entry appears unavailable and cannot be opened.
- Malicious names, symbolic links, and paths outside the root are rejected.
- Switching Kristals resets queries and rebuilds an authorized context.
- A Manager export never expands read permissions.
- `stale` Discovery is not presented as canon validation.
- Relationships remain schema-compliant with more than 10 source types.
- The interface remains usable on the supported Node/Windows version.

## Validation inherited from previous patches

Targeted unit tests were run while preparing earlier archives, including the local selector, Catho reader, and relationship partitioning. Snapshot documentation records these results, **but no complete Windows/Playwright build was reproduced for this documentation edition**. The wiki therefore makes no claim of release 1.0 certification or cross-repository conformance.

## October 17 semantic-display patch: documented evidence

The accompanying local change report (`RAPPORT_Konstellation_presentation_semantique_FR_2026-10-17.md`) records:

| Check | Reported outcome |
| --- | --- |
| Targeted reader and display tests | **15/15 passed** |
| Svelte structural check | 19 files, no findings |
| Frontend security check | 24 files, no findings |
| Documentation links | 75 documents / 81 links, no findings |
| Catho derived graph | 4,527 entities, 13,217 assertions, 50 relation definitions |
| Catho `P138` presentation | 2 edges labelled **« Nommé d’après »** |

These results are **recorded test evidence from that patch**, not new executions performed by this wiki update. **A full Astro/Svelte build and Windows-browser E2E test were not executed in that report.** Regression tests should include `aquin` versus `Joaquín`, duplicate-title diversity without identity merging, raw-code fallback, facet visibility, and preservation of original predicates and provenance.

## Releasing 1.0

Do not tag `1.0.0` until the reproducible lockfile, contracts, tests, build evidence, E2E, benchmarks, security checks, and release manifest satisfy the documented gates. See `docs/25-release-1.0.md`, `docs/VALIDATION-v1.0-RC.md`, and `docs/IMPLEMENTATION.md`.
