<!-- Frozen source: https://github.com/Rejean-McCormick/Skope/wiki/Getting-Started | commit: 3b1bfff4bd6a0f7956f5aacd45ef525bb5f39125 | SHA-256: a1d25c70e3682cff5349127b568e4f86a5ac44c453d8880219a1e03cc4e27bcf -->

# Getting started: first safe research session

This sequence uses the local browser and an **existing** read-only compact index.

1. **Start the server:** run `Start_Skope.cmd` or `python -m skope serve --db ...`; open `http://127.0.0.1:8767`.
2. **Inspect the source:** use `/api/meta` to confirm a finalized compatible SQLite index; `/api/diagnostics/reader` reports the running interpreter and reader (for later extraction).
3. **Optional target selection:** in **Active Kristal**, click **Refresh Kristals**, select one, then **Activate selected**. A generic scope does not require a Kristal.
4. **Choose a scope:** in **Scope catalog**, select an existing profile and, for multi-pass campaigns, the desired pass. Built-in examples cover Botany, Catho and Economics.
5. **Apply and inspect:** click **Apply scope settings**, review root, incoming/outgoing direction, allowed PIDs, depth, entity budget and geography; click **Calculate scope**.
6. **Read the preview:** open **Scope Explorer**. Graph, Entities, Convergence and Manifest show an index-derived working selection; the graph layout is not a geographic map.
7. **Stop here by default.** If the preview is appropriate and the operator deliberately wants a persistent inventory, use **Start batch QID collection**. That is a separate action with separate constraints and disk use.
8. **Optional verified extraction:** after the QID job completes, use **Check sources**/**preflight**, inspect every blocker, and explicitly start **Full Wikidata Records** only if the verified source and random-access prerequisites pass.

## Optional: bulk enrichment of v11 Kristals (CLI)

For an entire portfolio, use the *separate* native `skope portfolio` CLI rather than activating 104 Kristal workspaces one by one in the browser. `Run_Portfolio_Prepare.cmd` accepts a v11 ZIP by drag and drop and prepares a review CSV using the already-finalized index. Full-source `acquire` is a separate step requiring a verified dump and fast locator. No canon publication is performed. See [Portfolio Enrichment](Portfolio-Enrichment) and [Portfolio CLI Reference](Portfolio-CLI-Reference).

## Safe demonstration without a production volume

`fixtures/demo.recipe.json` and `fixtures/demo.wikidata.jsonl` describe a small example, while Python tests construct fixture indexes. The ZIP **does not** provide a ready-to-run production-compatible SQLite database for the UI. Running tests is a safe way to inspect behavior when `D:` is unavailable.

```bash
python -m pytest tests -q
```

## Five things to remember

- **Selecting** a Kristal or importing a JSON profile never starts a campaign.
- **Calculating** a preview does not collect every matching entity.
- **Completed QID collection** is not equivalent to completed full-source extraction.
- **Reviewing** a candidate is distinct from **confirming** a documented identity.
- A source JSON snapshot is **source material**, not automatically verified scientific or historical truth.

See [Workflows](Workflows), [User Interface](User-Interface), [Scope Catalog](Scope-Catalog).
