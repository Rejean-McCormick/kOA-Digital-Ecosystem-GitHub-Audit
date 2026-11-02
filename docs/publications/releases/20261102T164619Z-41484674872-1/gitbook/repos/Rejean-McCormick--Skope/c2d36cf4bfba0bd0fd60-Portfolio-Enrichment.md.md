<!-- Frozen source: https://github.com/Rejean-McCormick/Skope/wiki/Portfolio-Enrichment | commit: 3b1bfff4bd6a0f7956f5aacd45ef525bb5f39125 | SHA-256: 77c0111480e0a9cf4b016cba033ab18990d5741315a44a190173b7a097f43ca5 -->

# Native portfolio enrichment — Skope 0.15.0-alpha.1

Skope can prepare research enrichment across a **portfolio of Kristal Framework v11 projects**, using the same local Wikidata index and existing verified full-source reader as other Skope workflows. The feature is **built into Skope**, not a separately installed Skope–diK bridge.

> **Current delivery: native CLI, not a browser dashboard.** This pipeline produces candidates, full-source evidence and *proposals*. It does not alter a Kristal canon, issue approved diK `exactMatch` records or publish an Authoring Kit release.

## Boundaries and ownership

```text
v11 Kristal ZIP or project folders  (read-only)
   → inventory of scoped KQ/KP + curated labels
   → bounded/resumable lookup in existing compact Wikidata index
   → optional unverified draft seeds OR separately documented reviewer decisions
   → QID inventory and verified full Wikidata entity acquisition
   → full-claim proposals + separate related-QID discovery queue
   → diK crosswalk and lexicon qualification   [NOT IMPLEMENTED IN SKOPE]
   → Authoring Kit v11 candidate publication    [NOT IMPLEMENTED IN SKOPE]
```

Skope owns *research* and *source acquisition*; diK owns semantic identities and approved dictionaries/crosswalks; the Authoring Kit owns canonical publication. A semantic key is **`(namespace_id, KQ/KP)`**, never KQ or KP alone across different projects. Wikidata Q/P values remain external identifiers.

## Prerequisites

- Skope **0.15.0-alpha.1**, Python **3.11+** (bundled Windows `.cmd` expects Python **3.12** at its configured path).
- A ZIP or folder of v11 Kristal projects, with `.kristal/v11/dik.project.json` and curated dictionary JSON under `.kristal/v11/dictionaries/`.
- An already-finalized EncyK `wikidata.compact.sqlite` index for *discovery*. Skope does **not** create or modify it.
- For raw acquisition, a configured Skope extraction profile pointing to the **already verified original Wikidata dump** and functioning random-access locator/reader. The compact index alone is **not sufficient** for claim-level evidence.
- A dedicated writable **portfolio work directory**. `portfolio.sqlite`, reports and downloaded evidence are working files; original Kristal archives/dumps remain untouched.

The portfolio importer currently takes curated `fr`/`en` preferred terms; it skips metadata-prefixed dictionaries unless `--include-metadata` is supplied to the `inventory` subcommand. It cannot infer a semantic identity from an unlabeled KQ/KP. A scoped inventory may have **many projects but few queryable concepts**.

## Recommended Windows run (PowerShell)

From `C:\mycode\Skope`, using the installed Python 3.12 interpreter:

```powershell
$py = "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe"
$batch = "C:\Kristals\Kristals-v11-normalized-batch104-candidate.2.zip"
$index = "D:\EncyKlopedia\30_working\wikidata\wikidata.compact.sqlite"
$work = "D:\EncyKlopedia\30_working\skope-portfolios\batch104"

# Research preparation; can continue interrupted indexed searches.
& $py -m skope portfolio prepare --input $batch --work $work --db $index `
  --review-out "$work\review-candidates.csv" --max-queries 10000 --suggest-draft

& $py -m skope portfolio status --work $work

# Unverified draft QIDs must be included explicitly, not treated as approved mappings.
& $py -m skope portfolio export-seeds --work $work --out "$work\seeds" --include-draft

# Optional: edit CSV and set review_decision=confirm ONLY with independent evidence,
# reviewer, documentary_evidence and reason for a listed Q/P candidate.
& $py -m skope portfolio approve-review --work $work --csv "$work\review-candidates.csv"

# Acquire original full Wikidata entities via installed verified-source profile.
& $py -m skope portfolio acquire --work $work --db $index `
  --profile botany-canada-full-wikidata --include-draft `
  --out "$work\full-evidence" --batch-size 200

# Generate complete statement proposals; no KA or canonical Kristal writes.
& $py -m skope portfolio propose --work $work --include-draft `
  --evidence "$work\full-evidence" --out "$work\enrichment-proposals.jsonl"
```

**Important:** `botany-canada-full-wikidata` is used here as a *source-access profile*; this command does not impose the Botany domain. Check its actual dump path, verified manifest, locator and settings on the target computer first. No original full dump has been downloaded or scanned automatically. A `--include-draft` proposal is **still unverified**, even when its raw Wikidata statements were faithfully extracted.

For the first preparation only, you can also drag the v11 ZIP onto **`Run_Portfolio_Prepare.cmd`**. Its default output is `portfolio-work/` inside Skope. Change the script's embedded index path for other installations. The drag-and-drop launcher does **not** acquire source records or publish anything.

## Stage semantics and resume behavior

| Stage | Main command | Output | What it does **not** establish |
| --- | --- | --- | --- |
| Inventory | `inventory` or `prepare` | `portfolio.sqlite`, `inventory.json` | Neither candidate Q/P identities nor facts |
| Discovery | `discover` / `prepare` | Cached bounded name-search results | Equivalence, certainty or comprehensive search |
| Tentative selection | `suggest-draft` / `prepare --suggest-draft` | Unverified mapping seeds | `exactMatch`; no `A-Kristal` automatic matching |
| Review | `review-csv`, `approve-review` | Reviewed working decisions in SQLite | diK approval or canonical write |
| Seed export | `export-seeds` | QID JSONL, mappings JSONL, extraction-intent manifest | A completed full-source acquisition |
| Acquisition | `acquire` | SHA-256-checked `.jsonl.gz` chunks + source manifest | Independent truth of Wikidata statements |
| Proposal | `propose` | Full statement proposals, related QID queue, report | A KP, KA or new Kristal release |

`discover` uses query caching in `portfolio.sqlite`. An inventory can be re-run against the **same** source/options in its existing work folder. If the source ZIP, inventory mode or index identity changes, **start a new work directory** rather than silently reusing old results. `acquire` resumes only verified, complete chunks with unchanged source/selection/profile parameters. A partial or mismatching chunk causes a refusal, not silent acceptance.

## Mapping and claim safeguards

- `suggest-draft` considers a **single exact normalized preferred-label candidate among the bounded search hits**. That is weaker than a unique Wikidata identity. Ambiguous hits and collisions within one namespace are skipped. No `A-Kristal` is auto-selected.
- `approve-review` needs an **already listed** Q/P candidate, a reviewer, documentary evidence and a reason. These are *working review attestations*, not a diK crosswalk transaction. A URL is not automatically fetched for factual verification.
- `acquire` retrieves **full raw source entities** only from a preverified dump with a ready fast locator. It does not turn indexed edges into statements or scan the whole dump when the locator is missing.
- `propose` carries full original `mainsnak`, claim `id`, `rank`, `qualifiers` and `references`, and source provenance. Without a reviewed Wikidata P ↔ Kristal KP decision, `semantic_property` stays **null**. Linked QIDs go to a **separate discovery queue**; they are not silently imported as concepts.
- Standalone `.jsonl` / `.jsonl.gz` files are accepted for **development fixtures**, and are labeled unverified. Production evidence directories must supply a checked `snapshot-manifest.json` and chunks.

## In the submitted 104-Kristal batch

The 0.15.0-alpha.1 release notes report a read-only inventory of **104 projects** and **6,945 curated French business terms** (6,566 KQ, 379 KP), located in **23 projects**. Another **81 projects** have no suitable curated domain labels for direct name-based matching and need alternative roots/scopes/seeds. These counts are input-specific, not promises for other backups.

## What is still missing

1. Actual production run against your Windows `D:` index and verified full dump, with time/resource benchmarks.
2. Alternative scope/seed generation for sparsely labeled Kristals.
3. Transactional handoff of reviewed mappings to diK and validated canonical publication by the Authoring Kit.
4. A native browser dashboard for portfolio jobs (the browser's existing individual scope workflows remain separate).

Continue with [Portfolio CLI Reference](Portfolio-CLI-Reference), [Full-Record Extraction](Full-Record-Extraction), [Data Formats](Data-Formats), [Safety and Provenance](Safety-and-Provenance), and [Known Limitations](Known-Limitations).
