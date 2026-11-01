<!-- Frozen source: https://github.com/Rejean-McCormick/Skope/wiki/Portfolio-CLI-Reference | commit: 3b1bfff4bd6a0f7956f5aacd45ef525bb5f39125 | SHA-256: a139286a20767847394b67822028da40803448f4ef3714ef7e37dd76cc8e7e0c -->

# Portfolio CLI reference (0.15.0-alpha.1)

This is the **native Skope** workflow, invoked as `python -m skope portfolio …` or `skope portfolio …`. It is **not** a separate bridge executable and has no browser routes in this release.

## Commands

| Subcommand | Required arguments | Useful flags | Purpose |
| --- | --- | --- | --- |
| `inventory` | `--input`, `--work` | `--include-metadata` | Extract v11 project/curated term inventory into `portfolio.sqlite` |
| `prepare` | `--input`, `--work`, `--db`, `--review-out` | `--max-queries` (default 25,000), `--limit` (8), `--suggest-draft` | Inventory + bounded discovery + candidate review CSV |
| `status` | `--work` | — | Print counts, source hash, index identity and mappings status |
| `discover` | `--work`, `--db` | `--max-queries` (1,000), `--limit` (8) | Resume cached searches in existing read-only index |
| `suggest-draft` | `--work` | — | Tentative exact-label **unverified** matches, excluding `A-Kristal` |
| `review-csv` | `--work`, `--out` | — | Export candidate list for independent review |
| `approve-review` | `--work`, `--csv` | — | Record reviewer-attested choices among listed candidates only |
| `export-seeds` | `--work`, `--out` | `--include-draft` | Write selected QID inventory and extraction intent |
| `acquire` | `--work`, `--db`, `--profile`, `--out` | `--batch-size` (200), `--max-batches`, `--include-draft` | Resume verified local full-record retrieval by fast locator |
| `propose` | `--work`, `--evidence`, `--out` | `--max-claims` (1,000,000), `--include-draft` | Write noncanonical full-claim proposals and linked QID queue |

`--max-queries` must be 1–500,000. Discovery `--limit` must be 1–30. Acquisition batch size is 1–2,000. `--max-batches` lets you stop acquisition cleanly between chunks and resume in a later run; the evidence directory must refer to the same QIDs, source profile and parameters. `--max-claims` is an output budget, not a relevance filter.

### Windows examples

```powershell
$py = "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe"
$zip = "C:\Kristals\Kristals-v11-normalized-batch104-candidate.2.zip"
$db = "D:\EncyKlopedia\30_working\wikidata\wikidata.compact.sqlite"
$work = "D:\EncyKlopedia\30_working\skope-portfolios\batch104"

& $py -m skope portfolio inventory --input $zip --work $work
& $py -m skope portfolio discover --work $work --db $db --max-queries 1000
& $py -m skope portfolio review-csv --work $work --out "$work\review.csv"
& $py -m skope portfolio suggest-draft --work $work
& $py -m skope portfolio status --work $work
& $py -m skope portfolio export-seeds --work $work --out "$work\seeds" --include-draft
```

For the combined one-step first pass use `prepare` instead of `inventory` + `discover` + `review-csv`. Avoid running `inventory --include-metadata` in the same work directory as a previous default `inventory`; source and inventory options are pinned.

### Reviewing a CSV

The candidate CSV contains `namespace`, `semantic_id`, candidate external ID/label/description, `review_decision`, `reviewer`, `documentary_evidence` and `reason` among other fields. To record a reviewed **working** decision, set `review_decision` to `confirm` **only** on the correct listed candidate and supply all three review fields; otherwise leave it `unverified`.

```powershell
& $py -m skope portfolio approve-review --work $work --csv "$work\review.csv"
```

This does **not** edit a diK crosswalk and does not reassign any KQ/KP. To include only reviewer-attested identities in acquisition, **omit `--include-draft`** on `export-seeds`, `acquire` and `propose`.

### Full-source extraction and proposals

```powershell
& $py -m skope portfolio acquire --work $work --db $db `
  --profile botany-canada-full-wikidata --out "$work\evidence" --batch-size 200

& $py -m skope portfolio propose --work $work `
  --evidence "$work\evidence" --out "$work\claims.jsonl"
```

The above requires approved-*working* QID selections and an installed verified dump source profile. The example extraction profile is about **source access**, not a Botany scope restriction. For draft acquisition, append `--include-draft` **to both steps**; doing so marks associated proposal `identity_status` as `lexical_only_unverified`.

If the local dump/locator is missing, `acquire` **fails**; Skope does not fetch the huge dump or build a locator. The standalone development `propose --evidence fixture.jsonl` mode is **unverified**, even though it may contain valid Wikidata-shaped JSON.

See [Portfolio Enrichment](Portfolio-Enrichment), [Configuration and Paths](Configuration-and-Paths), [Data Formats](Data-Formats) and [Known Limitations](Known-Limitations).
