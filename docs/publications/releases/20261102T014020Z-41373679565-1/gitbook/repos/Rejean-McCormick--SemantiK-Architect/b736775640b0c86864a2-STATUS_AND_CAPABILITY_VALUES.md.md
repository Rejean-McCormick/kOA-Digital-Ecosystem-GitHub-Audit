<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/blob/74b07c42811dae0c68549d8554c00bc44a04298d/docs/reference/STATUS_AND_CAPABILITY_VALUES.md | commit: 74b07c42811dae0c68549d8554c00bc44a04298d | SHA-256: bf0519b8c42113eb5ce1afcbf9a2c1b80adf7a7215fa7f75959086231acdf4f4 -->

# Status and Capability Values

Status: **normative registry**

## Language/profile lifecycle

```text
DEVELOPMENT
CANDIDATE
RELEASED
RETIRED
```

Only `RELEASED` is callable by production policy.

## Ordering state

```text
FIXED
POLICY
FREE
```

## Communicative force

```text
ASSERT
ASK
DIRECT
PRESENT
```

Additions require versioned registry change.

## Runtime integrity state

```text
UNKNOWN
VALID
INVALID
```

`UNKNOWN` is never production-ready.

## Capability declaration

A capability entry is either present in a released profile or absent. Runtime does not expose “best effort”, “partial”, “maybe” or “fallback” as successful capability states.
