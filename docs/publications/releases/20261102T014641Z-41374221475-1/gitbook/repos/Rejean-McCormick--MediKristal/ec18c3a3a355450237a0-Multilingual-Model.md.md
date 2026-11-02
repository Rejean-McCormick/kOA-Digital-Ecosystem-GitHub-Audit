<!-- Frozen source: https://github.com/Rejean-McCormick/MediKristal/wiki/Multilingual-Model | commit: 93fba2ff54b0d2066bc5f3ba8afecf16ec10590c | SHA-256: fcb3c1af0242f79d945a02ea7e89451528bb8680d9c97190247773e09e4ba58b -->

# Multilingual Model

MediKristal is intended to make medical knowledge multilingual **by structure**, not merely by translating pages of prose.

## Meaning before wording

```text
Validated medical meaning
          ↓
Structured representation
          ↓
Language-specific realization
```

This makes language a rendering layer over governed knowledge rather than the place where medical authority lives.

## SemantiK Architect

The wider kOA architecture provides [SemantiK Architect](https://github.com/Rejean-McCormick/SemantiK_Architect) for deterministic realization of structured meaning.

- [SemantiK Architect Wiki](https://github.com/Rejean-McCormick/SemantiK_Architect/wiki)
- [Multilingual operation in kOA-Linux](https://github.com/Rejean-McCormick/kOA-Linux/wiki/Multilingual-Operation)
- [Multilingual knowledge networks](https://github.com/Rejean-McCormick/kOA-Linux/wiki/Multilingual-Knowledge-Networks)

A MediKristal concept should keep one underlying identity while supporting multiple validated labels, definitions, instructions, and explanations.

## Official terminology first

Where an authoritative source already provides French and English terminology — for example Canadian terminology resources — MediKristal should preserve those official labels rather than regenerate them unnecessarily.

## Language metadata

A language-dependent artifact should retain:

```text
language
locale / region
source or language authority
version
validation status
relationship to the underlying concept/assertion
```

## Translation is not medical promotion

```text
medical approval ≠ language validation
```

A medically approved assertion can still be rendered badly. Conversely, a perfect translation does not promote an unapproved medical claim.

Both states should remain explicit.

## Hospital use without required generative AI

A practical target is a multilingual hospital or clinic where short, validated instructions can be rendered without requiring cloud AI.

```text
Structured medical substance
        + patient/context selection
        + validated language artifact
        ↓
Language-specific clinical presentation
```

Examples can include short instructions, explanations, navigation, medication statements, or validated educational sequences.

Generative AI may assist later, but it is not required for canonical output.

## Safety boundary

```text
Validated information presentation
≠ Automated clinical decision
```

The system should reject unsupported linguistic constructions rather than silently improvise beyond its validated language coverage.
