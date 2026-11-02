<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Measurement-Scaling-and-Decision-Boundaries | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 2d246070eea85778758cb5c5fbbe6c9c819dcfbe783e1eb83bc172f0003a0832 -->

# Measurement Scaling & Decision Boundaries

> **v9 compatibility note:** This page documents the retained v6 portable-state semantics. V9 preserves the contract as a frozen substrate and may wrap/project it through Logical Artifacts without redefining it. See [[Version-Stack-v6-v7-v8-v9]].

Kristal v6 separates the **shape of a value** from the **decision derived from that value**.

A binary action does not imply that the underlying world is binary.

## Value shapes

Kristal valuations may use several semantic forms:

| Shape | Example |
|---|---|
| boolean | document received: true / false |
| categorical | native / introduced / cultivated |
| set | applicable dimensions = {energy, information} |
| ordinal | low < medium < high |
| scalar | wear = 0.72 |
| interval | pressure = 350–400 kPa |
| probability | P(cause \| observations) = 0.72 |
| distribution | {cause A: .55, B: .30, C: .15} |
| vector | support + severity + cost + testability |
| partial order | A cheaper, B faster; no universal winner |
| state machine | draft → review → approved |
| temporal | instant / interval / duration / recurrence |

## Binary is often a projection, not the source data

For example:

```text
risk = 0.37
```

may be mapped by policy to:

```text
< 0.20        automatic
0.20–0.60     human_review
> 0.60        human_decision
```

The thresholds belong to policy. The scalar remains the measured representation.

## Ordinal grayscale

The historical Kristal certainty scale was an ordinal grayscale rather than a true continuous analog value.

```text
unknown / speculative / low / medium / high / established
```

The important property was ordering, not equal numerical distance.

In v6 this becomes explicit:

```text
dimension = diagnostic_support
value_semantics = ordinal
value = high
```

A different family might use:

```text
dimension = constitutive_necessity
value = high
```

Same ordinal shape, different semantic dimension.

## Meta-states are not low values

These must remain outside the measured scale:

- `unknown` — dimension applies, value unresolved;
- `not_applicable` — dimension does not apply;
- `indeterminate` — available information cannot produce a stable value;
- `not_measured` — dimension applies but has not been measured.

Never map these blindly to zero.

## Multi-dimensional values

Many operational decisions should not be collapsed into one score.

Example diagnostic candidate:

```text
support      = 0.82
severity     = 0.95
testability  = 0.60
cost_of_error= 0.90
```

The policy may use all four to route work. A single “health score” or “risk score” can hide important tradeoffs.

## Partial order and incomparability

Some alternatives are not naturally rankable without organizational preferences.

```text
A = cheaper, slower
B = faster, more expensive
```

Kristal should preserve that incomparability instead of forcing an arbitrary total score.

## Scaling without semantic breakage

A valuation scales safely when:

1. the dimension remains explicit;
2. units / semantics remain stable;
3. unknown states are preserved;
4. projections are documented;
5. thresholds live in policy rather than being baked into observations;
6. richer values can be down-projected for legacy consumers without changing high-stakes meaning.

## Actionability is a derived boundary

```text
nuanced state
    ↓
measurements / categories / rules
    ↓
policy
    ↓
actionability
    ↓
automatic | human_review | human_decision | prohibited
```

This lets Kristal preserve a nuanced world while still making operations simple where they genuinely are simple.
