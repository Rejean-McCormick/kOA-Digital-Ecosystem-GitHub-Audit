<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Referents-and-Domain-Neutral-Model | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 444273a7b8a29d9e6b62f5e49871765fb34b8b78a049f52fba0e97e8ec8c9760 -->

# Referents & Domain-Neutral Model

> **v9 compatibility note:** This page documents the retained v6 portable-state semantics. V9 preserves the contract as a frozen substrate and may wrap/project it through Logical Artifacts without redefining it. See [[Version-Stack-v6-v7-v8-v9]].

Kristal keeps **identity of what an assertion is about** separate from the assertion itself.

A referent may represent a person, collective, place, work, document, concept, process, object, system or another stable domain entity.

## Domain neutrality

The core should remain shallow enough that consumers can build different navigation lenses without redefining referent identity.

A botanical reader might navigate family → genus → species. An automotive reader might navigate manufacturer → platform → model → year. A historical reader might organize by technology → manifestation → occurrence.

These are domain projections over stable identities.

## External identifiers

Wikidata, VIAF, provider IDs and similar identifiers are external anchors. They can aid matching and provenance; they do not replace the internal referent identity or establish the truth of assertions about it.

## Taxon concept vs taxon name

The same principle becomes especially important in domains with changing classification: the referent concept should not be confused with one current label or external identifier.
