<!-- Frozen source: https://github.com/Rejean-McCormick/Skope/wiki/Testing-and-Validation | commit: 3b1bfff4bd6a0f7956f5aacd45ef525bb5f39125 | SHA-256: cb455ce281545017950e61d42eae1532c0e4697a5238dcef049004cfdf866aa5 -->

# Testing and validation

## Reproducing the Python suite

```bash
python -m pip install -e '.[test]'
python -m pytest tests -q
```

For the source archive of **Skope 0.15.0-alpha.1**, the release validation reports **129 passed** in the analysis environment. This covers fixture-based index querying, scope/campaign validation, server behavior, author workflows, reconciliation transactions and extraction simulation. This includes **11 native portfolio tests**, plus the 118 inherited tests. The test result must **not** be misrepresented as exercising the real data volume or a complete long-running production extraction.

## JavaScript validation

```bash
node --check skope/static/app.js
# Repeat node --check for each skope/static/*.js
node tests/test_workspace_ui_0142.cjs
```

All **11** `skope/static/*.js` files passed `node --check` in the analysis environment; `tests/test_workspace_ui_0142.cjs` also passed.

**Separate graph simulation:** `tests/test_density_dom.cjs` requires `jsdom` and `@napi-rs/canvas`. In the analysis environment this test **could not start because `jsdom` was not installed**. Do not count it as passed. It is a DOM/Canvas simulation, not a complete Windows GUI validation.

## New portfolio validation (0.15.0-alpha.1)

The release notes document a **read-only inventory** of the supplied 104-Kristal batch: 104 projects, 6,945 curated French terms (6,566 KQ; 379 KP) from 23 projects. Tests simulate indexed search and Skope fast-locator acquisition; they check resuming from intact SHA-256 chunks, rejection of corruption, scoped mapping decisions and preservation of full Wikidata statements. They **do not** constitute a completed real-world acquisition from the operator's `D:` dump.

The existing `tests/test_workspace_ui_0142.cjs` is reported passing. `tests/test_density_dom.cjs` was **not successfully executed**, due to optional dependencies. See [Portfolio Enrichment](Portfolio-Enrichment).

## What is still unverified

- Access to the original multi-gigabyte index and dump on `D:`.
- Real locator/sidecar compatibility, backend throughput and free-space behavior.
- Full end-to-end Windows browser UX for large campaigns and data extraction.
- Live source-specific results for the Catho unresolved roster or Botany selection.
- Any online documentary source verification (not implemented by Skope).

## Release-specific notes

The archive's `VALIDATION_0_15_0_ALPHA1.md` documents 129 Python tests, the first-pass read-only inventory, and mock-based acquisition. Historical `VALIDATION_0_14_4.md` remains as a historical report. Neither constitutes an actual source retrieval from the operator's production Wikidata dump.

## Useful checks before release

1. `python -m pytest tests -q` and JavaScript syntax checks.
2. `GET /api/config` should report `server_release: "0.15.0-alpha.1"`.
3. `GET /api/scope-profiles/catalog` should show five bundled valid profiles without errors.
4. `GET /api/meta` should confirm a finalized, compatible index.
5. `GET /api/diagnostics/reader` should show the actual server interpreter and source/locator situation.
6. On a **copy/test environment**, exercise controlled pause/resume and reviewed-CSV refusal paths before a production run.

See [Troubleshooting](Troubleshooting) and [Versioning and Migration](Versioning-and-Migration).
