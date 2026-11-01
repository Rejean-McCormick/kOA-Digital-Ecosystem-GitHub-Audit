<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/wiki/Language-Profiles-and-Conformance | commit: f187a43fc9540ce7d443ff4d2ab26dfdc7a48bfe | SHA-256: 6e9aa48cf5d6a80c860295e8fdd5ab891cf3669060ec6f193d16c4996275dca9 -->

# Language Profiles & Conformance

SA releases **language/profile pairs**, not vague claims that a language is “supported”.

## Capability profile

A profile is a versioned workload contract, for example:

```text
sa-core-1
orgo-operational-1
ethikos-dialogue-1
keenkonnect-system-1
```

A profile defines:

- required SA↔GF operations;
- required register/politeness distinctions;
- required lexical classes;
- required output block kinds;
- locale/format requirements;
- conformance suite identity.

## Production status

Lifecycle states:

```text
DEVELOPMENT
CANDIDATE
RELEASED
RETIRED
```

Only `RELEASED` is callable by production policy.

A released profile is binary: every required capability passes, or the profile is not released.

## Conformance dimensions

Depending on the profile, suites can cover:

- positive/negative clauses;
- intransitive/transitive/ditransitive events;
- copular constructions;
- existence/location/possession;
- questions;
- directives;
- coordination and relatives;
- dates/deadlines;
- quantities;
- names/technical identifiers;
- agreement;
- address/formality;
- lists/fragments;
- semantic role, polarity, modality, time and quantity preservation.

## Release gate

A language/profile becomes `RELEASED` only after:

1. GF build succeeds;
2. immutable grammar artifact exists;
3. bridge contract compatibility passes;
4. lexical artifacts exist;
5. the profile suite passes completely;
6. golden/regression tests pass;
7. semantic/property tests pass;
8. failure-path tests pass;
9. RuntimeSet integrity passes;
10. evidence is recorded and hashed.

There is no production “mostly works” state.
