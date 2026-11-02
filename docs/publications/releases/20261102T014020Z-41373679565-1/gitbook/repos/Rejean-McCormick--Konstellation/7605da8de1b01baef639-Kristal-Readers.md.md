<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/wiki/Kristal-Readers | commit: 01bfc9126e06db9560d1c84e4b315026a28690af | SHA-256: 6490f45b8e41291dd0cc9bebd42d622c330fa9a3a8b86bafd2e26bc22879bd18 -->

# Kristal Readers and Adapter Selection

## Local v10 reader

The **`kristal-local-catalog-v10`** adapter discovers immediate subdirectories under the authorized root and calls `kristal-local-v10` for the chosen Kristal. The reader checks the presence and structure of local state; it can work **without a domain projection** by showing the topology of declared members.

For explicitly declared derived models, `node-edge-json/1` uses a manifest plus JSON nodes and edges. The manifest must identify its derived status and include the required fingerprint declarations. The reader must validate the files it consumes **at read time**, even if Manager already ran its checks.

## v9 compatibility within Framework v10

- **v9:** semantic states, logical artifacts, identities, and commitments.
- **v10 draft.3.2:** hosted-network architecture, publication, directories, read surfaces, and complementary Discovery profiles.
- **Konstellation RC2:** adapts certain surfaces for navigation but does not universally decode every logical artifact family.

“V9 state” is a legitimate technical view, but it is not an ergonomic landing page for a Catho graph with domain kinds.

## Noncanonical display normalization

The local reader uses `src/lib/semantic-display.mjs` to generate human-facing French labels for known predicates and selected unverified-research titles. It preserves original identifiers in relation/assertion metadata (`originalPredicate`, `upstreamRef`, and related fields) and leaves the canonical Kristal untouched. Presentation preferences may override generic labels when explicitly configured, but they do not redefine relations.

Unknown Wikidata property or item codes receive an explanatory **unresolved** display string rather than an invented translation. Display normalization is **not** identity resolution, epistemic validation, or full internationalization. See [[Semantic Labels and Localization|Semantic-Labels-and-Localization]].

## Hosted v10 reader

The `kristal-v10` / GitHub reader primarily targets **hosting structure**—indexes, manifests, and links—without presuming native domain concepts are available. A hosted entry does not imply activation or full semantic reading.

## v6 reader and normalized packs

The repository retains a v6 compatibility reader and contracts for existing integrations. This does not freeze the development of v10 reading. Local Théophile packs are **demonstration corpora**, not the required model for every Kristal.

## Reference files / modules

- `server/integrations/local-catalog.mjs`
- `server/integrations/kristal-local-v10.mjs`
- `server/integrations/kristal.mjs`
- `server/integrations/kristal-v10.mjs`
- `server/integrations/kristal-v6.mjs`
- `server/integrations/reader-policy.mjs`
- `contracts/upstream/`

See [[Developing a Reader|Developing-a-Reader]] and [[Contracts and Versions|Contracts-and-Versions]].
