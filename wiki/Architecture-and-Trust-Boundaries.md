# Architecture and Trust Boundaries

## Layers

```text
Explicit local roots (read-only)
        |
        v
Discovery & inventory binding (local Git metadata)
        |
        v
Bounded static inspection (LOCAL_OBSERVE)
        |
        +--> audit.json / audit.csv / SUMMARY.md   [local]
        |
        +--> targeted triage ZIP                    [local, confidential]
        |
        +--> allowlisted aggregate dashboard.json  [optional publication]

Provided pattern libraries --> Manual profiles & checklist [local]
Previous diagnostic summaries --> Historical metadata imports [local]
```

## Ownership

- **`kOA-Digital-Ecosystem`** remains the governance/reference inventory authority.
- **Source repositories** own their code, workflows and release decisions.
- **Specialist diagnostic tools** own their own historical qualification semantics.
- **This audit repository** observes, summarizes and supports manual review. It never authorizes a release or production deployment.

## Trust rules

- Default local audit: no token, no network, no target project execution and no source-repository modification.
- Optional remote `OBSERVE`: a distinct GitHub API observation with incomplete access possible.
- Optional GitHub Pages publishing: explicit write **only to the audit repository**, not to target projects.
- Manual checklist: never inferred to be Applied from a config or a heuristic alert count.
- Historical imports: provenance preserved and never automatically promoted to current verdicts.

## Files and formats

| File | Role | Public by default? |
| --- | --- | --- |
| `data/initial_inventory.json` | Bundled inventory snapshot | In the audit repository |
| `reports/audit.json` | Detailed local paths, statuses, findings | **No** |
| `reports/triage.zip` | Confidential sanitized evidence metadata | **No** |
| `profiles/repositories/*/*.md` | Reviewed engineering/security profiles | **Not automatically published to Pages** |
| `%LOCALAPPDATA%/.../assessments.json` | Manual review notes and statuses | **No** |
| `docs/data/dashboard.json` | Public-safe numerical aggregate | Designed for Pages publication |
| `wiki/*.md` | Human-written documentation | Public if the GitHub Wiki is published in a public repo |

The public-safe aggregate is deliberately narrow. It omits raw reports, repository identities, Windows paths, source code, and credentials.
