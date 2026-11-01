<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/90865538b0c16be08423843208f4c5e6785a7523/docs/2-Technical-Reference/30-artifacts/kristal-runtime-state.md | commit: 90865538b0c16be08423843208f4c5e6785a7523 | SHA-256: d6714c3bb2927a2dbbbc0b3c56b992d1d179fc8576dd1816eacb8c1439336ae2 -->

# Kristal Runtime local state on kOA-Linux

This page references the current kOA-Linux `kristal_runtime` component contract.

## Authoritative local records

`kristal_runtime` owns local Runtime Pack state including:

- verification/compatibility record;
- active Runtime Pack record;
- activation receipt;
- rollback receipt;
- runtime health state.

## Boundary

`kristal_runtime` does not own:

- Kristal's global epistemic semantics;
- Orgo/Konnaxion domain state;
- governance policy;
- resource scheduling;
- host privilege;
- release-channel identity.

## Privileged transition

When activation requires node-local privileged mutation, kOA Node Agent executes the narrow authorized transition. The owner of active Runtime Pack state remains `kristal_runtime`.
