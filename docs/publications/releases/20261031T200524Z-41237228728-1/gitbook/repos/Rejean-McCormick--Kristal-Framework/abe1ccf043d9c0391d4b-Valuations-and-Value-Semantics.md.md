<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Valuations-and-Value-Semantics | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 6a90e216699fe14c7aef6ba51d296d121b65e44fb05d430ab9d99574d27dd832 -->

# Valuations & Value Semantics

> **v9 compatibility note:** This page documents the retained v6 portable-state semantics. V9 preserves the contract as a frozen substrate and may wrap/project it through Logical Artifacts without redefining it. See [[Version-Stack-v6-v7-v8-v9]].

Kristal v6 replaces the old assumption of one universal `certainty_level` with **typed valuations**.

A valuation answers two separate questions:

1. **Which dimension is being measured?**
2. **What kind of value represents that dimension?**

## Supported semantic families

Typical value semantics include:

| Semantics | Example |
|---|---|
| boolean | document received: true/false |
| categorical | native / introduced / cultivated |
| set | applicable dimensions: {energy, information} |
| ordinal | low < medium < high |
| scalar | wear = 0.72 |
| interval | expected pressure = 350–400 kPa |
| probability | P(cause \| observations) = 0.72 |
| distribution | competing diagnostic hypotheses |
| vector | support + severity + cost + testability |
| partial_order | alternatives incomparable without preferences |
| state | draft → review → approved |
| temporal | instant, interval, duration, recurrence |

## Value state is separate from value

These are not numbers:

```text
unknown
not_applicable
indeterminate
not_measured
```

In particular:

```text
unknown ≠ 0
not_applicable ≠ low
```

## Ordinal “grayscale”

The old certainty vocabulary was best understood as an ordinal grayscale: values were ordered, but distances were not necessarily equal.

In v6 an ordinal scale can still be used, but the dimension must be explicit. For example:

```text
dimension = diagnostic_support
value_semantics = ordinal
value = high
```

is not equivalent to:

```text
dimension = intervention_necessity
value = high
```

## Measurement is not policy threshold

A continuous or ordinal measurement should preserve nuance. Policy can later derive an action boundary:

```text
risk < 0.20       → automatic path allowed
0.20 ≤ risk < .60 → human review
risk ≥ .60        → specialist decision
```

The threshold belongs to policy/actionability. It does not redefine the underlying measurement.

## Avoid fake precision

Do not convert qualitative review into `0.83` just because a scalar field exists. Use a measurement type only when the domain has a defensible interpretation and method.

## Scaling and operational boundaries

A rich measurement may later be projected to a simple action boundary, but the measurement and the policy threshold remain separate. See [[Measurement-Scaling-and-Decision-Boundaries]] for binary projections, continuous measures, vectors, partial orders and legacy down-projection.
