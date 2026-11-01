<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/wiki/Selecting-a-Kristal | commit: 01bfc9126e06db9560d1c84e4b315026a28690af | SHA-256: 1442e0d7ee43d0d5cab16907a94bef98cb34483222d81c03dc20c7d83362ea15 -->

# My Kristals — Choose What to Open

## Neutral landing page

Konstellation starts with no active Kristal. **My Kristals** is the entry point. The client requests `GET /api/kristals`, explicitly selects an available reader, and requests a new `bootstrap` for the chosen Kristal.

### What the catalog recognizes

- The **parent directory** configured by the operator (`directory`).
- **Immediate subdirectories** containing `kristal.workspace.json`; no recursive search and no unrestricted access to a path entered in the browser.
- Whether the local reader can inspect the state; an entry that fails inspection can remain listed but **unavailable**.
- For certain Kristals, an optional `readModels` recipe for reading a **derived projection**; Catho is the first configured example.

An entry marked “available” means **readable by the configured adapter**, not “C1-qualified,” “published,” or “approved by Manager.”

## Select and switch

1. In **My Kristals**, select a card.
2. Review its source, availability, and displayed read status.
3. Click **Open in Explorer** if a reader is available.
4. Use perspectives, queries, and Explorer views.
5. Return to **My Kristals** to choose another corpus.

An entry originating **only from a Manager inventory** is not automatically openable without a matching authorized reader. The hosted v10 view may display technical topology without decoding domain knowledge.

## Data modes that must not be confused

| Source | Interpretation |
| --- | --- |
| Local v10 reader | Inspects a selected workspace and reads the bytes needed to open it |
| Manager inventory | Operational observations, potentially enriched with diagnostics; not permission to read |
| Authoring Kit Discovery | Noncanonical reader guidance and metadata freshness |
| Hosted v10 collection | GitHub manifests and structure; specialized semantic reading not guaranteed |
| Théophile corpus | Historical/demo data, not a mandatory corpus |

## Handling local references

The browser cannot choose an arbitrary Windows path. The server determines the root through `config/local-catalog.json`. Operators should edit this file under their own control, then **restart** Konstellation.

See [[Configuration|Configuration]], [[Manager and Discovery|Manager-and-Discovery]], and [[Kristal Readers|Kristal-Readers]].
