<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Derivations-and-Reproducibility-v9 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 5a03b5a4ffabb03262de6b6bd49d8f38ecc5f51c984f2c475768993cb2983b92 -->

# Derivations and Reproducibility

A v9 **Derivation** records how an artifact was computationally produced.

```text
inputs
+ transform
+ parameters
+ toolchain/policies
→ outputs
```

This is build lineage, not epistemic authority.

```text
EPISTEMIC PROVENANCE != BUILD PROVENANCE
```

## Exact-input rule

A deterministic derivation must declare every input that can affect output, or eliminate that variability.

Typical inputs include:

- source snapshot/commitment;
- schemas;
- transform version;
- configuration;
- policy;
- random seed;
- locale when relevant;
- external datasets.

A strong deterministic build must not read unpinned mutable network state.

## Change pruning

An implementation may rebuild an artifact after source bytes change and discover that the resulting logical commitment is unchanged.

```text
source bytes changed
      ↓
recompute
      ↓
same logical commitment
      ↓
no logical downstream invalidation required
```

This is an optimization; the normative requirement is that declared commitments remain correct.
