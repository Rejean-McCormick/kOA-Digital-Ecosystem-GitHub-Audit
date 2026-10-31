<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/wiki/Troubleshooting | commit: 01bfc9126e06db9560d1c84e4b315026a28690af | SHA-256: 8faa6a157d8a2b0140caf86c310aa9296ef38c53ab9fa073aed12168afa3ab6a -->

# Troubleshooting

## The server still displays Théophile

Make sure you launched **`Konstellation.cmd`** from the **neutral-selector** version, and that the console shows `config/local-catalog.json`, not `theophile-biblical.enriched.pack.json` or `config/active-reader.json`. Close older sessions and restart. An older launcher can retain the demo profile.

## My Kristals is empty or Catho is missing

1. Check `directory` in `config/local-catalog.json`.
2. Confirm that this parent folder exists and contains **immediate subdirectories**.
3. Check for `A-Kristal-Catho/kristal.workspace.json`.
4. Check for symbolic links or names outside the supported syntax.
5. Inspect reader errors; a Kristal can be listed but unavailable.

## “V9 state” shows a single row

That is the state's **technical topology**, not the domain corpus. For Catho, use the `node-edge-json/1` recipe and a reader version that exposes graph `kind` values as perspectives. Without this recipe, an arbitrary Kristal might not have a specialized semantic view.

## `relation-registry: /relations/1/domain must NOT have more than 10 items`

An older implementation of `v9:node_kind` exposed **13 types** where the schema allowed only 10. Install the relation-partitioning fix supplied in later archives. **Do not silently increase the schema limit or delete assertions.**

## `skippedOversize is not defined`

This was a bug in an older local reader with fresh Discovery. Confirm that the updated reader is installed; the fix was included in the October 16 patches. Do not “repair” the canon to work around a reader-side JavaScript exception.

## `stale` / `integrity: mismatch`

Derived Discovery may contain old file sizes or fingerprints. Regenerate **derived metadata** with the Authoring Kit, then verify again with Manager. A Discovery mismatch **does not by itself prove** canonical content has changed.

## `/brand-logo.svg` returns 404

A missing visual asset, unrelated to Kristal reading. Check `public/` asset paths and UI references; do not attribute this 404 to the Framework.

## `/api/fleet` returns 404

The Manager preview is optional and may be disabled. The **neutral selector works without `/api/fleet`**, using `/api/kristals`.

## `/api/kompiler/capabilities` returns 503

Kompiler is unconfigured or unreachable. This service is optional for basic local navigation.

## The console exits / port 4321 is busy

Read the first error after `Starting Konstellation`. Check the Node version (minimum 24.15), `package.json`, backend configuration, `npm run build`, and whether another instance is using port 4321. The launcher attempts to stop a prior process **identified as Konstellation**, without indiscriminately terminating other applications.

## How to provide a useful bug report

Include the **launcher name**, **patch version**, **first error lines**, and the result of `GET /api/health` if the server starts. **Redact** sensitive private paths, tokens, and confidential data before sharing.

## Raw codes, English statuses, or cryptic facets remain visible

Confirm that the **October 17 semantic-display patch** has been applied to the active Konstellation installation, then stop and restart `Konstellation.cmd` so its Astro assets are rebuilt. Check the actual files `src/lib/semantic-display.mjs`, `src/components/Astrolabe.svelte`, and `server/integrations/kristal-local-v10.mjs`.

- **`P138`** should appear as **« Nommé d’après »** in supported relation views.
- **`not_evaluated`** and **`unspecified`** should display **« Non évalué »** and **« Non précisé »** in the updated inspector.
- An **unknown `P…` or `Q…` code** should receive an unresolved label, not an invented meaning.
- Some technical details remain intentionally inspectable in provenance panels.
- Facets without values and routine `v9:node_kind` filters should be hidden unless already applied.

These checks apply to the specified **French semantic-display patch**; older snapshots and other reader surfaces may not show the same presentation.

## Astrolabe returns unrelated word fragments

Test `aquin` against names including **Thomas d’Aquin** and **Joaquín**. If Joaquín still matches by suffix alone, an old frontend or old reader build is probably active. Clear stale browser content and restart before investigating new data issues. This patch does not promise full fuzzy matching, translation of all titles, or universal identity deduplication.

See [[Semantic Labels and Localization|Semantic-Labels-and-Localization]] and [[Astrolabe and Search|Astrolabe-and-Search]].
