<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/wiki/RuntimeSets | commit: f187a43fc9540ce7d443ff4d2ab26dfdc7a48bfe | SHA-256: d5f80dc3c242bf6d8e42a8485e9d3cb97375a92530c4cd9f0e33bd9b83ed578f -->

# RuntimeSets

A `RuntimeSet` is the immutable artifact composition used for one render request.

It exists to make multilingual generation reproducible, offline-capable and scalable without duplicating shared resources for every language.

## Composition

```text
RuntimeSet
  runtime manifest
  SA compatible version range
  SA↔GF contract version
  GrammarArtifact(s)
  LexicalArtifact(s)
  LocaleDataArtifact(s)
  bridge/profile artifacts
  CapabilityManifest
  ConformanceEvidence
```

Each artifact is content-addressed by SHA-256.

## Runtime manifest

A released manifest pins:

- RuntimeSet ID;
- compatible SA version range;
- SA↔GF contract version;
- grammar artifact hash;
- lexical artifact hashes;
- locale-data hashes;
- bridge/profile artifact hashes;
- capability manifest hash;
- conformance evidence hashes;
- release status.

## Request pinning

A request executes against exactly one RuntimeSet.

If only one released RuntimeSet can serve a language/profile, it can be resolved automatically. If multiple released sets coexist, selection must be explicit through:

- `runtime_selector.runtime_set_id`, or
- `activation.json` mapping `language|profile → runtime_set_id`.

Ambiguity fails closed.

## Readiness

A RuntimeSet is ready only when:

- required files are present;
- every hash matches;
- SA/bridge versions are compatible;
- language/profile is `RELEASED`;
- profile artifacts are present;
- conformance evidence is pinned and passing.

## Immutability

Artifacts are never patched in place. A change creates a new artifact identity and new conformance evidence.

Rollback means activating a previous known-good RuntimeSet.
