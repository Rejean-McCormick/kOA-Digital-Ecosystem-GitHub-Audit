<!-- Frozen source: https://github.com/Rejean-McCormick/MediKristal/wiki/What-MediKristal-Is | commit: 93fba2ff54b0d2066bc5f3ba8afecf16ec10590c | SHA-256: 463f9d9f7e6dfbeadfe09db46b1958b16976e31f5c00803102680e821cf2a569 -->

# What MediKristal Is

## Short definition

**MediKristal is a medical knowledge compilation and orchestration system that transforms validated medical sources into semantic, versioned, multilingual, queryable, governable Kristal artifacts.**

A useful mental model is a **living, machine-readable reference work of medicine**.

It is intended to make medical knowledge easier to:

- connect across terminology systems;
- inspect and cite;
- update without erasing history;
- review by qualified professionals;
- represent in multiple languages;
- compile into local Runtime Packs;
- query through human interfaces, APIs, or AI systems;
- distribute in authorized forms without losing provenance.

## What problem it addresses

Medicine already has large, authoritative knowledge systems. The problem is that they were built for different purposes.

```text
SNOMED CT       → clinical concepts
ICD-11          → classification
LOINC / pCLOCD  → tests and observations
CCDD / DPD      → Canadian drugs and products
RxNorm          → normalized drug interoperability
guidelines      → recommendations
local protocols → jurisdiction-specific action
```

The hard part is the **relationship between these layers**.

MediKristal therefore focuses on orchestration rather than replacement.

## What MediKristal is not

MediKristal is not:

- a chatbot;
- a large language model;
- an autonomous diagnostic engine;
- a replacement for SNOMED CT, ICD-11, LOINC, CCDD, DPD, or RxNorm;
- a single universal medical database that erases source identity;
- an automatic authority over physicians;
- a substitute for professional clinical judgment;
- a claim that uncertainty can be removed from medicine.

## Formalized knowledge, not generated knowledge

The core distinction is:

```text
AI-generated wording ≠ medical knowledge authority
```

MediKristal aims to make the medical knowledge itself explicit:

```text
Concept
Relationship
Source
Version
Jurisdiction
Applicability
Uncertainty
Review
Promotion status
Language realization
```

An AI can then consult this structure instead of reconstructing medical knowledge from unstructured prose or relying only on model memory.

## Reference work and protocol system

MediKristal has two related but distinct functions:

### 1. Medical reference

Represent what is known, by whom, under which source/version, and how concepts relate.

### 2. Clinical protocol representation

Represent explicit rules that apply medical knowledge to a defined context.

These must not be collapsed:

```text
Medical knowledge
≠ Clinical guideline
≠ Local protocol
≠ Patient data
≠ Recommendation
≠ Final clinical decision
```

## Questions MediKristal should answer

For any significant result, a mature MediKristal system should be able to answer:

- What does the system know?
- Where did this claim come from?
- Which version of the source supports it?
- Which jurisdiction and population does it apply to?
- Is it working, disputed, promoted, superseded, or revoked?
- Who was eligible to review it?
- Which review and Smart Vote reading contributed to promotion?
- Which rule produced the result?
- Which language artifact rendered the explanation?
- Can the historical result be reproduced?

That audit trail is part of the knowledge architecture, not an afterthought.
