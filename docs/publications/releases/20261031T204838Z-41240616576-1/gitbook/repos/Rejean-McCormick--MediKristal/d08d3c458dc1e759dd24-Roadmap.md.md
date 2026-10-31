<!-- Frozen source: https://github.com/Rejean-McCormick/MediKristal/wiki/Roadmap | commit: 93fba2ff54b0d2066bc5f3ba8afecf16ec10590c | SHA-256: 72a3e3d2016a48f92f90974c4f52c5f8939f1919ace9b6f5cd3135c6ee3892e3 -->

# Roadmap

MediKristal should prove **depth of traceability before breadth of coverage**.

## Phase 0 — Documentation and boundaries

- define MediKristal versus Kristal versus kOA-Linux;
- document source authorities;
- define working/promoted states;
- define initial governance roles;
- document UCKK publication boundary;
- define multilingual safety assumptions.

## Phase 1 — Core schema

Formalize schemas for:

```text
source
concept
external mapping
medical assertion
clinical epistemic state
protocol
review event
Smart Vote reading
promotion event
language realization
Runtime Pack manifest
publication representation
```

## Phase 2 — Small Canadian reference domain

Choose one narrow domain and include, where relevant:

```text
SNOMED CT CA concept
ICD-11 condition
LOINC / pCLOCD test
CCDD / DPD medication
source-backed guideline rule
French + English realization
```

Coverage is not the goal. Traceability is.

## Phase 3 — kOA-Linux authoring environment

Demonstrate the local lifecycle:

```text
import source
→ stage
→ modify working Kristal
→ validate
→ review
→ promote
→ compile
→ verify
→ activate
```

## Phase 4 — Smart Vote governance pilot

Implement one competence-aware review class with:

- credentialed eligibility;
- explicit lens definition;
- reproducible aggregation;
- dissent preservation;
- separate promotion authority.

## Phase 5 — Runtime Pack

Build a signed/versioned read-optimized package for local/offline use.

## Phase 6 — Multilingual deterministic realization

Use SemantiK Architect or compatible language artifacts to demonstrate:

```text
same structured medical meaning
→ French realization
→ English realization
```

without requiring generative AI for canonical output.

## Phase 7 — Query surfaces

Provide access for:

- human reference UI;
- API/software consumers;
- AI retrieval.

All three should access the same governed knowledge objects.

## Phase 8 — UCKK publication

Demonstrate:

```text
promoted MediKristal knowledge
→ authorized publication transform
→ UCKK learning/reference object
→ provenance back to source release
```

## Phase 9 — Clinical validation

Before any direct clinical use:

- expert medical review;
- source licensing review;
- terminology validation;
- protocol validation;
- multilingual safety testing;
- privacy/security review;
- regulatory assessment;
- controlled real-world evaluation.

## What not to optimize for yet

Do not treat these as early success metrics:

- number of diseases imported;
- number of database rows;
- number of connected AI models;
- chatbot fluency;
- number of languages claimed without validation.

A stronger early milestone is:

> **One medical result that can be traced, reproduced, reviewed, translated, updated, rolled back, and safely distributed.**
