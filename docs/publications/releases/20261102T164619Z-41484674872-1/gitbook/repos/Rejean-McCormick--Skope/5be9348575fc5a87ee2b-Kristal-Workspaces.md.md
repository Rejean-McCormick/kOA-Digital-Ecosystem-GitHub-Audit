<!-- Frozen source: https://github.com/Rejean-McCormick/Skope/wiki/Kristal-Workspaces | commit: 3b1bfff4bd6a0f7956f5aacd45ef525bb5f39125 | SHA-256: fc05e5424b40c9e5a48973790da30be2bef227e54f370edc3791841d105f2110 -->

# Kristal workspaces (read-only targets)

A **Kristal** is a separately managed workspace. Skope discovers and selects it as *context*; it does not change the workspace canon or activate downstream publishing.

## Select a workspace

1. Open **00 · Active Kristal**, click **Refresh Kristals**.
2. Choose a discovered workspace and click **Activate selected**.
3. For a workspace outside the discovery root, use **Add folder & activate** with the absolute folder path.
4. For generic Wikidata exploration, you may select **none**.

Detection scans immediate child folders under `C:\mycode\Kristal\locals` (or `KRISTAL_LOCALS_ROOT`), not an arbitrary recursive directory tree. A valid folder contains a non-symlink `kristal.workspace.json` manifest with a recognized `kristal.local-workspace/` format and valid slug.

## What selection changes

- The current research context and proposal target metadata.
- Whether a target-bound scope profile is appropriate for your research.
- Which Catho roster can be consulted when starting the specialized author/works workflow.
- Local selection persistence in the **gitignored** `config/kristals.local.json`.

It does **not** launch a scope pass, an author campaign, a dump scan, a new fast index, or a canonical import. Running author campaigns capture the selected folder **at start**; switching the active UI selection cannot silently retarget an existing worker.

## Portfolio work is different from activating one workspace

Skope 0.15.0-alpha.1 can read **v11 archives or directory portfolios** using `python -m skope portfolio inventory/prepare`. This creates an isolated working SQLite state containing scoped `(namespace_id, KQ/KP)` identities and curated labels. It does not require clicking **Activate selected** 104 times, and it does not change any source Kristal. The portfolio function is **CLI only**. See [Portfolio Enrichment](Portfolio-Enrichment).

## Related API

- `GET /api/kristals` — discovered list and active selection.
- `POST /api/kristals/select` with `{"id":"<discovered-id>"}` — change active target; send `{"id":null}` to clear.
- `POST /api/kristals/add` with `{"path":"<absolute-workspace-folder>"}` — validate and register a manual folder.

Never mistake a scope's `target_slug` for permission to modify its target. See [Safety and Provenance](Safety-and-Provenance) and [Catho Authors Campaign](Catho-Authors-Campaign).
