<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Migration-v7-to-v8 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 7a29ea00ddb078bb757ee2e217559cac2656ce85185751e864f0462004f6fabb -->

# Migration from v7 to v8

Migration is optional because v8 is additive. A valid v7 Kristall can be used unchanged by a v8 processor.

## Recommended adoption

1. keep v7 registries and Mesh unchanged;
2. declare v8 capability metadata;
3. create external lexical Kristals for desired languages/domains;
4. define deterministic lexical stack policy;
5. build rebuildable query indexes from canonical artifacts;
6. expose typed KQP query with pagination/completeness;
7. add AI context compilation and optional compact encoding;
8. add semantic fingerprint profiles only where they provide value.

Existing v7 labels may seed a lexical worklist or fallback lexicon. Extracting them is a convenience operation, not a semantic migration.

## No forced rewrite

Do not:

- convert every v7 label before using v8;
- mint new semantic IDs for existing v7 identities;
- replace inherited hashes with semantic fingerprints;
- make query indexes or AI bundles canonical.

## Production adoption

Introduce derived indexes and AI query paths as read-side capabilities first. Canonical mutation/admission remains governed by existing source contracts until explicitly upgraded under a separate write protocol.
