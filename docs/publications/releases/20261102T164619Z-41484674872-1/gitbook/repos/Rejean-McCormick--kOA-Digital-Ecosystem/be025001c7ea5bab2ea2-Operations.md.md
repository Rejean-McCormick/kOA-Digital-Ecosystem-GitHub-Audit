<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/1-Overview/Operations.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: 731bb996d028433c9135df00800087b5ca01febfc2ec9880f280624591018a7a -->

# Operations

Operations follow system ownership and explicit integration contracts rather than a single global pipeline.

## Cross-system flow

```text
Konnaxion <---- Interaction Kernel ----> Orgo
     \                                  /
      \------ IK Profiles to Da'at ----/
                         |
                      Kristal v6
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
