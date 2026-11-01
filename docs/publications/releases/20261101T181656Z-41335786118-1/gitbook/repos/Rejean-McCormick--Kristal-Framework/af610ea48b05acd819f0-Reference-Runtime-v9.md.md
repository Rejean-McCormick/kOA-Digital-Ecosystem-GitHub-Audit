<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Reference-Runtime-v9 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 7194e7ca05aac0300c76340a34555080f2fecc96f2cb26c9681a1769d63eefe4 -->

# Reference Runtime — v9

The Framework includes a **non-normative JavaScript reference implementation** for the v9 architecture while preserving inherited v6/v8 behavior.

The specification, schemas and TCK remain authoritative.

## Reference v9 behavior

The runtime demonstrates:

- Logical Artifact commitment calculation;
- State Snapshot commitment calculation;
- materialization-manifest verification;
- Derivation, Exchange and Activation validation;
- local immutable state publication;
- atomic local activation pointer update;
- inherited v6/v7/v8 reading/query tooling.

## Baseline profiles

```text
kristal.logical/jcs-sha256-v1
kristal.state-commitment/jcs-sha256-v1
```

## Intentionally not claimed as core

The reference runtime does not make these mandatory:

- distributed consensus;
- remote CAS/network protocol;
- Parquet/Arrow materialization;
- private commitment cryptography;
- automatic materialization planner;
- Merkle membership proofs.

Those remain future/optional profiles and implementation concerns.

## Independent qualification

Use [[KristalDiag-v9]] to verify v9 commitments and lifecycle behavior independently from the JavaScript reference code.
