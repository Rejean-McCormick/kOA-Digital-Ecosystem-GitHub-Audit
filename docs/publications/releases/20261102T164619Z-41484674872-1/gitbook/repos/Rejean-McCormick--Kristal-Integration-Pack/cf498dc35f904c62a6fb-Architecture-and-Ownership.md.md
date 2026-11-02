<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Integration-Pack/wiki/Architecture-and-Ownership | commit: 949de422daed28c0b84684b509e675807ac9c48b | SHA-256: 547b24571064e343eb30ee50ca6bd4395da94658e6484433162eea1b9dc25229 -->

# Architecture and Ownership

The Integration Pack is a narrow interoperability layer, **not a new Kristal implementation**.

## Responsibility boundaries

| System | Owns or supplies | What the Integration Pack may do |
| --- | --- | --- |
| Kristal Framework v11 | Schemas, semantic identity rules, dictionary audit, coverage and preflight checks | Execute exact SHA-256-pinned readers and validators |
| Kristal Authoring Kit | Authoring workflow, artifact registration, explicit dictionary selection, migration recovery | Produce a non-mutating preflight report; **never select a catalog** |
| diK | Dictionary imports and review proposals, including alpha.7 source receipts | Inspect incoming catalog, provenance and receipt without adopting it |
| Arketype | Template/workspace generation | Document integration baseline; no Arketype installation performed here |
| Kompiler | Query execution, Context Packs and optional derived projection | Invoke allowlisted local API methods |
| Konstellation | Navigation and application reader surfaces | Supply a guarded *legacy* overlay candidate; never override owner integration |
| Manager / collection owner / C3 | Fleet/collection metadata and structural checks | Delegate a local C3 preflight, not recreate the checker |

## Two distinct paths

### Framework v11 path (read-only)

```text
Registry + Semantic Graph + Crosswalk + Dictionary Catalog
                          |
            Pinned Framework draft.4
                          |
             check / coverage / view
                          |
            Validation or derived output
```

An additional `v11-handoff` operation checks the dictionary-side interface before a **separate** Kit import. There is no implicit write or activation edge between the Pack and the Kit.

### Historical Kompiler path

```text
Authorized local Kompiler API -> Context Pack (derived)
                                  |
                       optional compatible v7 Surface
                                  |
                         v6 projection (derived)
                                  |
                     Konstellation reader configuration
```

The historical bridge is **not** a v9/v10/v11-to-v6 semantic converter. No source commitments or canonical state are published by the Pack.

## Semantic invariant

KQ/KP/KA/KS are canonical identifiers in the Framework v11 semantic graph. Wikidata Q/P identifiers live only in external references governed by approved mappings. Display labels, aliases and translations may *describe* an identity but cannot create or replace one.

See [[Dictionary-and-Wikidata-Rules]], [[Derived-Views-and-Coverage]], and [[Security-and-Trust-Boundaries]].
