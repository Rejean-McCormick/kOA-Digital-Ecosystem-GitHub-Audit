<!-- Frozen source: https://github.com/Rejean-McCormick/Skope/wiki/Development-and-Contributing | commit: 3b1bfff4bd6a0f7956f5aacd45ef525bb5f39125 | SHA-256: 57807ab41abdd1b97bcce97262ca0c82b385a6b610f975635d8213f1e8999a1c -->

# Development and contributing

Skope is an MIT-licensed standalone Python package that serves a small client-side HTML/JS/CSS UI. Treat data integrity and explicit human approvals as part of the public interface contract.

## Repository map

```text
skope/
  api.py              HTTP routes, local-only server, static UI
  cli.py              serve / meta / preview / export
  db.py               compact SQLite read-only adapter
  scope.py            recipe validation and preview traversal
  scope_profiles.py   JSON library parsing/catalog
  massive.py          persistent QID collection
  extraction.py       verified random-access source extraction
  fastio.py           dump reader and locator adapter
  scope_common.py     sidecar compatibility
  geography.py        optional geography annotations
  author_campaign.py  Catho roster, person and P50 work orchestration
  reconciliation.py   single identity review and audit
  reconciliation_batch.py batch triage/staging/CSV transaction
  kristal_registry.py local workspace discovery/selection
  project.py          target and default paths
  export.py           proposal/plan ZIPs
  static/             vanilla browser UI
scopes/               drop-in JSON profiles
config/               extraction profiles and guidance
tests/                fixture-based Python + JS tests
contracts/            draft recipe schema
```

## Developer workflow

```bash
python -m pip install -e '.[test]'
python -m pytest tests -q
for file in skope/static/*.js; do node --check "$file"; done
node tests/test_workspace_ui_0142.cjs
```

The optional `test_density_dom.cjs` requires `jsdom` and `@napi-rs/canvas`, which are not pinned by an included Node manifest; explicitly install compatible development dependencies in an isolated environment if you intend to execute it.

## Contribution guidelines

- Add tests for new routes, profile validation, stale-review rejection, name collisions and resumable jobs.
- Never make catalog refresh, page load, or workspace selection implicitly execute acquisition.
- Keep source index, dump, existing locator and Kristal canon read-only; new output must stay in explicitly approved working/evidence roots.
- Prefer bounded index queries and avoid index-wide sort/join scans for name search.
- Treat a verified-dump manifest as *prior provenance*, not a fresh source checksum.
- Do not transform ranked identity scores into probabilities or auto-confirmations.
- Do not add source/web access inside batch identity confirmation without reviewing the human attestation and trust model.
- Keep `VERSION`, packaging metadata, server release and README headings aligned for new versions.

## Licensing and deployment

The project snapshot contains an **MIT License**. The Wikidata dump, Kristal workspaces, historical inventories and external documentary sources can have independent rights and privacy requirements; none of those datasets is bundled by the code's MIT grant.


## Native portfolio development (0.15.0-alpha.1)

Modify `skope/portfolio.py` and its dispatch in `skope/cli.py` for v11 portfolio enrichment; do **not** resurrect an independent bridge product. Preserve `(namespace_id, KQ/KP)` identity scope, SHA-256/input/index pins, resumable SQLite state, distinction between `lexical_only_unverified` and reviewer-attested seeds, and exact original Wikidata statement contents. Only `diK` and the Authoring Kit may qualify canonical crosswalk/publication in their respective contracts. The new tests are in `tests/test_portfolio_015.py`; run the full historical Python suite as well. See [Portfolio Enrichment](Portfolio-Enrichment).
