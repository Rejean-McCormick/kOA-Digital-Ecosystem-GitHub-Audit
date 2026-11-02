<!-- Frozen source: https://github.com/Rejean-McCormick/Skope/wiki/User-Interface | commit: 3b1bfff4bd6a0f7956f5aacd45ef525bb5f39125 | SHA-256: f93e68372813655a35d8ba7e325dbb67ba22d2bd21db8d29b8ddb014a6381d71 -->

# User interface guide (0.15.0-alpha.1)

**Portfolio note:** The new bulk v11 Kristal enrichment flow has **no dedicated browser dashboard** in this alpha. Use [Portfolio Enrichment](Portfolio-Enrichment) via `python -m skope portfolio` or `Run_Portfolio_Prepare.cmd`. All controls below describe the existing browser UI.

The local browser app organizes day-to-day research under **Scopes**, **Identity batches**, and **Graph explorer**, while the sidebar retains explicit configuration and data-acquisition tools.

## Scopes / left sidebar

**Active Kristal:** refresh, select and activate workspaces. **Scope catalog:** refresh valid JSON profiles, choose a pass and apply its settings. **Scope configuration:** inspect root QID, relation PIDs, direction, depth, budget, convergence and geography; collapsed by default in the compact dashboard. **Data acquisition:** explicit QID collection and full JSON extraction controls; also collapsed by default.

## Scope Explorer

**Open Scope Explorer** opens a large overlay. The primary tabs are:

| Tab | Intended use |
| --- | --- |
| Graph | Visualize aggregated connectivity, density layers and an inspectable neighborhood |
| Entities | Inspect included QIDs and the reasons they entered the preview |
| Convergence | Review supported external candidates; explicit acceptance may change a **new preview** |
| Manifest | Inspect/copy the validated working recipe |

The graph is a schematic relationship layout, **not a spatial/geographic map**. Clicking **Calculate scope** recomputes the preview; it is not a mass job.

## Identity batches

Open the dedicated identity workspace for existing Catho campaign unresolved persons. **Batch analysis** is the default view. It provides a progress state, category filters (`Ranked suggestions`, `Needs review`, `No viable candidate`), pagination, staging of **unverified** proposals and an evidence ZIP including the human-review CSV. The separate per-person review remains available.

**Validate CSV — dry run** checks input before the guarded **Confirm documented identities in batch** action. Neither action visits linked documentary websites.

## Accessibility and state

Overlays provide close controls and escape behavior. UI actions invoke the same server routes documented in [API Reference](API-Reference). API/backend status is authoritative: a browser notification alone does not establish successful extraction or confirmation. Refreshing the browser does not create a job.

See [Workflows](Workflows), [Identity Reconciliation](Identity-Reconciliation) and [Batch Identity Review](Batch-Identity-Review).
