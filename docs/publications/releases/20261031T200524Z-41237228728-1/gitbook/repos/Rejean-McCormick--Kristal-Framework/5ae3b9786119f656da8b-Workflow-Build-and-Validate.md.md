<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Workflow-Build-and-Validate | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 1360d32d271fd24cfadc296ba0a365276845ac79fc1bb429222b8696f1e096ac -->

# Workflow: Build & Validate

## 1. Identify canonical meaning first

A build may begin from observations, source documents, extracted claims, domain-native models, organizational rules, prior Kristals or machine-generated candidates.

Preserve the domain's true native structure. Do not flatten a DAG/AST/graph merely because a generic assertion representation exists.

## 2. Preserve inherited semantics

For v6, preserve referents, assertions, valuations, applicability, roles, provenance/evidence and actionability.

For v7, preserve KQ/KP/KA/KS identity, Mesh/KOS mappings and unresolved/conflicting states.

For v8, preserve language/query boundaries and completeness semantics.

## 3. Normalize under the Logical Contract

The domain contract determines collection semantics, defaults and logical projection before the v9 Logical Commitment is calculated.

## 4. Validate in layers

```text
schema validation
        ↓
domain semantic validation
        ↓
epistemic/referential validation
        ↓
authority/admission policy where applicable
        ↓
Logical Commitment verification
```

Schema validity alone is not semantic validity or authority.

## 5. Record the Derivation

Declare exact source commitments, transform identity/version, parameters and toolchain/policy inputs that affect the result.

```text
EPISTEMIC PROVENANCE != BUILD PROVENANCE
```

## 6. Build derived capabilities separately

After logical artifacts are valid:

- build v6 portable projections where needed;
- build v8 lexical/query companions;
- build v9 materializations/runtime packs;
- verify every derived output binds to the correct source commitment.

## Checklist

- [ ] Is the native canon explicit?
- [ ] Are semantic IDs stable and not label-derived?
- [ ] Are ordered/set-like collections defined before hashing?
- [ ] Is epistemic provenance separate from build lineage?
- [ ] Are derived indexes rebuildable?
- [ ] Does the declared Logical Commitment recompute exactly?
- [ ] Are external dependencies pinned rather than mutable?
- [ ] Does model output still pass deterministic admission gates?
