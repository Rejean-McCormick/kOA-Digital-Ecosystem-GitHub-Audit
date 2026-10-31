<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Ecosystem-Integration | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: aca161f8d35a82c89dd1a82b202b1bb931182690354b145f79ded9a479f3263a -->

# Ecosystem Integration

> **v9 note:** V9 preserves ecosystem authority boundaries while adding pinned state/artifact composition. See [[Federation-and-Coverage-v9]].


Kristal v8 participates in larger systems without absorbing their authority.

## General pattern

```text
source system / acquisition
        ↓
canonical evidence / state
        ↓
Kristal v6 / Kristall v7
        ↓
optional v8 Language + Query layers
        ↓
consumer / AI / interaction layer
        ↓
owner admission / execution contract
```

## AI integration

AI clients should preferably use:

```text
approximate discovery
   ↓
semantic identity resolution
   ↓
exact KQP query
   ↓
AI Context Compiler
```

rather than treating rendered prose or vector similarity as semantic authority.

## Operational owners

Interaction kernels, workflow systems, Orgo/Konnaxion-like services or other owners remain responsible for admission and execution. Kristal can describe actionability and supply context; it does not acquire execution permission.

## External KOS

Wikidata, UNESCO, MeSH, GBIF, GeoNames and similar systems can be mapped through anti-corruption/KOS adapters. Their identifiers do not replace Kristall semantic identity merely because a mapping exists.

## Projection is not canon

Consumer indexes, UI summaries, query caches, lexicalized views and AI context bundles are rebuildable projections.
