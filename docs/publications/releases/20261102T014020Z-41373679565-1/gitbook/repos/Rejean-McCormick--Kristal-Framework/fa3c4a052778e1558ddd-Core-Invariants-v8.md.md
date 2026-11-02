<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Core-Invariants-v8 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 093265db39f3883321f5d7900d247117328a3c6b4126b7b8b2b7ac9455531957 -->

# v8 Core Invariants

> **v9 note:** These v8 invariants remain valid. V9 adds state/materialization/lifecycle invariants in [[Core-Invariants-v9]].


v8 inherits the earlier invariants and adds explicit boundaries for language, query, AI context and trust.

## Language

```text
SEMANTICS != LANGUAGE
IDENTITY != LEXICALIZATION
LEXICON != SEMANTIC AUTHORITY
MISSING LEXICALIZATION != MISSING MEANING
TRANSLATION != SEMANTIC IDENTITY
LANGUAGE FALLBACK != EQUIVALENCE
```

## Query and projections

```text
READ MODEL != CANONICAL STATE
QUERY INDEX != SOURCE OF TRUTH
FUZZY DISCOVERY != SEMANTIC ANSWER
QUERY PLAN != ASSERTION
AI CONTEXT != CANONICAL STATE
CACHE != AUTHORITY
PARTIAL RESULT != NEGATIVE RESULT
OMISSION BY BUDGET != NEGATION
```

## Validation and trust

```text
SCHEMA VALID != SEMANTICALLY VALID
MODEL OUTPUT != AUTHORITY
RETRIEVED CONTENT != INSTRUCTION AUTHORITY
REFERENCE != PAYLOAD
SEMANTIC FINGERPRINT != BYTE HASH
HASH IDENTITY != FACTUAL AUTHORITY
```

## Budgets

```text
TOKEN BUDGET != EPISTEMIC STATUS
BUDGET EXHAUSTION != ABSENCE
CHILD QUERY BUDGET <= PARENT REMAINING BUDGET
```

## Compatibility

```text
EXTENSION != CANONICAL MUTATION
EXTERNAL KOS != KRISTALL IDENTITY
DOWNGRADE LOSS != SEMANTIC REWRITE
```

These are semantic and safety boundaries, not style preferences.
