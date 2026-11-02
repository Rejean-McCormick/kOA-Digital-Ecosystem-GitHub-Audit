<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Adapters-v6-v7 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 5d48866ae87b41c30b737d17e4a9650ec0c55152efdfea6d3f9d75f6576f36ee -->

# v6/v7 Adapters

Adapters are anti-corruption boundaries. They let a v8 engine operate over earlier Kristal generations without leaking v8 assumptions into older canonical artifacts.

## v6 adapter

A v6 adapter:

- reads `kristal_state/6.0` unchanged;
- preserves referent namespaces, assertion status, valuation semantics, coordinates, applicability and source/evidence links;
- exposes stable v6 referents through `identity_space: kristal_v6` unless an already-declared v7 mapping exists;
- never invents `KQ` equivalence merely to simplify query.

## v7 adapter

A v7 adapter directly exposes `KQ/KP/KA/KS`, Mesh, KOS, axes, source and projection metadata. Existing labels may be used as display fallback material but do not become v8 lexical authority.

## External KOS adapter

External vocabularies remain external identities/mappings. Adapter code translates transport/schema differences at the edge and must not redefine Kristall identity.

## Determinism

Given the same source snapshot and adapter profile, normalized read output should be reproducible. Adapter version/profile is part of derived lineage.
