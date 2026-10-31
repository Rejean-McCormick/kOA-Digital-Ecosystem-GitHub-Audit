<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/90865538b0c16be08423843208f4c5e6785a7523/docs/2-Technical-Reference/90-reference/adr/adr-0009-runtime-pack-activation-owner.md | commit: 90865538b0c16be08423843208f4c5e6785a7523 | SHA-256: a8b0faf270e7ce8db04c0fc815ecda721108a3beaab9a6c5f5a1b3b993b5f05a -->

# ADR-0009: Runtime Pack activation ownership

- **Status:** Accepted, amended 2026-09-16 after kOA-Linux contract refresh
- **Supersedes:** ADR-0003 Konnaxion Activation and Rollback

## Context

The earlier Digital Ecosystem revision correctly removed Konnaxion as the universal activation owner, but it still described “kOA-Linux” as one coarse activation owner and introduced a new Digital Ecosystem Runtime Activation State.

The current kOA-Linux contracts are more precise.

## Decision

For a kOA-Linux deployment:

1. `kristal_runtime` owns Runtime Pack verification/compatibility records, active Runtime Pack state, activation/rollback receipts and runtime health.
2. kOA Node Agent performs only the narrow authorized privileged node-local transition when required by profile/contract.
3. kOA-Linux Release Sets coordinate compatible versions across release channels; Release Set state is not Runtime Pack active state.
4. Konnaxion may own desired/application selection but not the local active Runtime Pack record.
5. Koali Space activation is presentation state and is unrelated to Runtime Pack activation.
6. Digital Ecosystem does not create a second authoritative Runtime Activation State.

Standalone deployments may assign a different explicit owner, but still require one authoritative state owner.

## Consequences

`Runtime Activation State` and `Konnaxion State` in Digital Ecosystem are compatibility-only. New documentation references the owner-component records and receipts.
