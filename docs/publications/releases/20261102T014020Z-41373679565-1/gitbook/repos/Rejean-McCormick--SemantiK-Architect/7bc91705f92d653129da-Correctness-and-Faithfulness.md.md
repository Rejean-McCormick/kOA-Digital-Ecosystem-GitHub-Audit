<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/wiki/Correctness-and-Faithfulness | commit: f187a43fc9540ce7d443ff4d2ab26dfdc7a48bfe | SHA-256: 16e028d162ad8218a0fb1be098da443eb4e718b4abec5e8861a0c5d9e0a8391e -->

# Correctness & Faithfulness

Faithfulness is a hard correctness property in SemantiK Architect.

## Core invariants

### No invention

Every output domain claim must come from submitted semantics or an explicitly declared deterministic derivation.

### No silent omission

Every communication obligation must be discharged or the request fails.

### Role preservation

Agent, patient, recipient, location, time, quantity and other roles must not be swapped.

### Polarity and modality preservation

Negation, uncertainty, obligation, permission, hypotheticality and other relevant modalities must remain intact.

### Identity preservation

Entities, identifiers, names, numbers and references must not be silently substituted.

### No status elevation

Uncertain or hypothetical meaning must not be rendered as unqualified fact.

## Coverage

A successful result records coverage at least as:

```text
obligation_id
  → block_id
  → realization_unit_id(s)
```

The planner also preserves the semantic references associated with each unit so that an obligation cannot be declared covered while one of its required semantic statements vanished during planning.

## Determinism

For identical:

- canonical semantic request;
- presentation/profile versions;
- SA version;
- RuntimeSet identity;
- SA↔GF contract version;

SA produces the same deterministic structured result.

Operational values such as latency or trace IDs are excluded from deterministic result identity.

## Runtime AI policy

Probabilistic models are not required by the canonical production path. AI may assist development of grammars, lexicons, mappings, tests and documentation, but release authority comes from conformance evidence against immutable artifacts.
