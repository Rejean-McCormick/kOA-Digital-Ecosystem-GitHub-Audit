<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/wiki/Add-a-Language | commit: f187a43fc9540ce7d443ff4d2ab26dfdc7a48bfe | SHA-256: 7b98afc755cacb8711ef060ad421970f63677d261dfaf5e6ac7078d2a73bc03e -->

# Add a Language

Adding a production language is primarily a **GF/RGL + RuntimeSet release workflow**, not a new SA core implementation.

## Target flow

```text
GF language development
      ↓
build + test
      ↓
PGF grammar artifact
      ↓
SA↔GF bridge artifact
      ↓
lexical/locale artifacts
      ↓
capability profile
      ↓
SA conformance suite
      ↓
immutable evidence
      ↓
RuntimeSet RELEASED
      ↓
activation
```

## 1. Develop the language in GF

Morphology, agreement, syntax and language-specific grammar belong in the GF language repository/RGL work.

GF Wordbench can be used for build, diagnostics and language-development workflows. SA does not patch grammar gaps at runtime. See [[GF Ecosystem|GF-Ecosystem]].

## 2. Build the PGF

Produce an immutable PGF artifact for the concrete language.

## 3. Implement the SA↔GF bridge

Map the SA operations required by the profile to the grammar's admitted GF functions/expressions.

The bridge must consume all semantic slots/features for a unit or fail.

## 4. Build lexical artifacts

Provide exact bindings for semantic concepts required by the profile/workload.

## 5. Define the capability profile

Declare the operation/block/register requirements applications may rely on.

## 6. Run conformance

The exact grammar + bridge + lexicon composition must pass the profile suite completely.

## 7. Release a RuntimeSet

Hash all artifacts, pin conformance evidence and mark the language/profile `RELEASED` only after the gate passes.

## 8. Activate

If more than one released RuntimeSet exists for the same language/profile, explicitly activate one or pin it in the request.

## Scaling rule

The 300th language should require new validated artifacts and conformance evidence, **not a new branch in SA core**.
