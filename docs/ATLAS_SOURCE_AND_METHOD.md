# kOA ecosystem atlas — sources and method

**Release:** 0.9.0

## Source-grounded map

The conceptual map follows the user-supplied `znapshot_kOA_Digital_Ecosystem_10291320.zip`:

- `docs/1-Overview/index.md` — owner map and direction of selected handoffs;
- `docs/1-Overview/Components.md` — ownership and non-ownership boundaries;
- `docs/1-Overview/Integration.md` — contract/lifecycle integration cautions;
- `docs/2-Technical-Reference/10-system/authority-map.md` — authoritative owner boundaries;
- `docs/2-Technical-Reference/10-system/components.md` — subsystem roles.

**No inferred application dependencies.** Only seven source-documented
conceptual relationships are displayed in the contract map. The Skope to
EncyKlopedia route is explicitly **proposed/not qualified**. The 49-repository
constellation is a navigational index, not an inferred dependency graph.

## UX structure

Guidance drawn from the supplied `senior-interface-ux-patterns-v2`:

- UX-01, UX-05: Navigate by the business object (application/repository).
- UX-06, UX-07: Keep report-opening actions next to the selected repository.
- UX-08: Present actionable, interpretable overview metrics.
- UX-11: Preserve repository selection with a URL `?app=...` when navigating reports.
- UX-15–UX-18: Keep the principal task first; leave technical diagnostics as a secondary option without losing audit functions.

## Evidence levels

1. Inventory: 49 repositories in the audited authoritative inventory.
2. Measured Engineering Profiles: 12 inventory repositories with snapshots
   measured on October 29, 2026; one additional profile outside the scope.
3. Audit coverage: last published local audit (47/49, October 28, 2026).
4. Qualification: five **independent manual** decisions. They may be marked
   evidenced only with proof and scope. No score is invented from tests,
   file names, file sizes, duplicates, or the existence of automation.

## Public vs. local privacy

The public atlas publishes repository names **from the public 49-repo
inventory**, conceptual roles, and allowlisted technical counts. It publishes
neither Markdown profile originals nor file-path lists. The loopback preview
serves local original profiles and *status-only* qualification JSON, never
free-form evidence or scope descriptions. The private endpoints do not exist
on GitHub Pages. Local state survives application upgrades under
`%LOCALAPPDATA%\\kOA-GitHub-Audit\\profiles`.
