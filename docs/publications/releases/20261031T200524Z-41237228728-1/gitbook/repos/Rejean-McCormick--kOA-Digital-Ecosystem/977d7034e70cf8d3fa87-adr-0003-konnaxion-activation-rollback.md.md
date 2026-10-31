<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/4ed4b8928665ebd723b68f8b3f2cb2f196d6374f/docs/2-Technical-Reference/90-reference/adr/adr-0003-konnaxion-activation-rollback.md | commit: 4ed4b8928665ebd723b68f8b3f2cb2f196d6374f | SHA-256: 0a0c0285560650883ed967ef6d755aafe63b8ded82230c182c991444075e7419 -->

# ADR-0003: Konnaxion Activation and Rollback (historical)

**Status:** Superseded by ADR-0009  
**Historical date:** 2026-02-09

This ADR assumed Konnaxion universally owned Runtime Pack verification, activation and rollback.

The current kOA-Linux mapping is more precise:

- `kristal_runtime` owns Runtime Pack verification/compatibility, active-state, activation/rollback receipts and runtime health;
- kOA Node Agent performs narrow privileged node-local transitions when required;
- Konnaxion may own desired/application selection only;
- Koali Space activation is a separate presentation lifecycle.

See `adr-0009-runtime-pack-activation-owner.md`.
