<!-- Frozen source: https://github.com/Rejean-McCormick/MediKristal/wiki/Protocols-and-Clinical-Logic | commit: 93fba2ff54b0d2066bc5f3ba8afecf16ec10590c | SHA-256: 35de56aa14d47ca8fe2e9cb99c66c4affabd2fbfbd79c74e541a0291aa02407d -->

# Protocols and Clinical Logic

MediKristal separates **medical knowledge** from **rules that act on patient context**.

## Why protocols are separate

A medical source may establish that a condition is associated with a symptom. A protocol establishes what should happen under defined conditions.

```text
knowledge assertion
≠ protocol rule
```

## Conceptual rule

```json
{
  "protocol_id": "protocol:adult_pneumonia_initial_assessment",
  "version": "1.0",
  "applies_to": {
    "age_min": 18,
    "jurisdiction": "CA-QC"
  },
  "trigger": {
    "all": [
      {"symptom": "symptom:fever"},
      {"symptom": "symptom:cough"}
    ]
  },
  "then": [
    {"consider_test": "test:oxygen_saturation"},
    {"consider_test": "test:chest_xray"}
  ],
  "provenance_refs": ["source:guideline-example"],
  "status": "under_review"
}
```

## Deterministic does not mean simplistic

MediKristal favors explicit and auditable execution. That can include deterministic rules, thresholds, decision trees, contraindication checks, and validated scoring systems.

Probabilistic medical information can still be represented, but it should remain explicit:

```text
model identity
version
inputs
calibration / evidence
output meaning
applicability
policy governing use
```

The goal is not to ban probability. It is to prevent hidden authority.

## Future standards

MediKristal can begin with simple JSON rules, then move toward standard computable representations:

- [Clinical Quality Language (CQL)](https://cql.hl7.org/)
- [FHIR Clinical Reasoning](https://hl7.org/fhir/clinicalreasoning-module.html)
- `PlanDefinition`
- `ActivityDefinition`
- `Library`
- `ValueSet`

## Required explanation

A protocol output should expose:

```text
which rule fired
which patient facts matched
which assertions were used
which source versions supported them
which warnings or exclusions applied
which Runtime Pack produced the result
```

## Safety boundary

MediKristal can support clinical reasoning without collapsing the distinction between information and professional decision.

```text
validated information / protocol output
≠ automated final clinical decision
```
