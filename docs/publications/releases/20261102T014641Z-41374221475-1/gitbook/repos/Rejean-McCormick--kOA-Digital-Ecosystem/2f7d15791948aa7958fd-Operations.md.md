<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/wiki/Operations | commit: dd52671208ae86295bfcc5f896d236a20182faba | SHA-256: ce4fcf16f9f647469fb65ac6789bed996bf8eec96b27823a5897f4d4cd2c7e66 -->

# Operations

Operations follow system ownership and explicit integration contracts rather than a single global pipeline.

## Cross-system flow

```text
Konnaxion <---- Interaction Kernel ----> Orgo
     \                                  /
      \------ IK Profiles to Da'at ----/
                         |
                      Kristal v5
                         |
                  Runtime Pack / refs
                         |
           deployment activation owner
              (kOA-Linux when present)
```

## Operational rules

- no cross-system database writes;
- at-least-once delivery with idempotent processing and reconciliation;
- source-system domain state remains authoritative at its owner;
- Kristal compilation, validation, recognition, publication and activation are tracked separately;
- exactly one authoritative physical Runtime Pack activation owner exists per deployment;
- production/reference gates are Profile/policy decisions, not universal compile semantics.

Current product snapshots do not yet prove full IK adapter/conformance coverage. Runbooks must identify whether they describe implemented behavior or target migration behavior.
