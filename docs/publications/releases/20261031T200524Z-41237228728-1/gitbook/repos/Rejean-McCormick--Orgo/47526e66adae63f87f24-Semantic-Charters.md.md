<!-- Frozen source: https://github.com/Rejean-McCormick/Orgo/wiki/Semantic-Charters | commit: b89ca31f268c521cbd70ab1c736338a8c5039df7 | SHA-256: 6f0cafe14b8e2210388e9263ed20c36b6d5ee66a356ac9f8c18e487bc76e8189 -->

# Semantic Charters

Orgo's **Semantic Charters** provide a reusable vocabulary layer for describing organizational concepts across different domains.

They are not another workflow engine and they do not replace Cases, Tasks or labels.

## Why Charters exist

Different organizations often use different words for similar concepts. Orgo's charter model helps keep domain vocabulary interoperable without forcing every organization into exactly the same terminology.

The charter system can align selected concepts with **Wikidata-compatible identifiers** while keeping Orgo's own organizational relationships focused on workflow needs.

## Three levels

The current charter model is layered:

```text
General
   ↓
Family
   ↓
Domain specialization
```

Examples of families include:

- care;
- programs;
- operations;
- groups;
- incidents.

Domain specializations can refine these families for contexts such as hospitals, schools, social services, manufacturing, transport/logistics, facilities, sports groups, associations or IT help desks.

## What gets reused

Orgo can reuse selected public identifiers for concepts and properties where they already fit.

It can also define its own refinements when organizational workflow needs a more precise relation.

The public principle is:

> **Reuse shared meaning where it fits; specialize only where Orgo needs a clearer operational relation.**

## Offline-friendly by design

The charter concept is compatible with a filtered local subset of public semantic data. Orgo does not need to import the entire Wikidata graph just to use common identifiers.

This keeps semantic assistance useful in local/offline environments while preserving Orgo's own workflow model.
