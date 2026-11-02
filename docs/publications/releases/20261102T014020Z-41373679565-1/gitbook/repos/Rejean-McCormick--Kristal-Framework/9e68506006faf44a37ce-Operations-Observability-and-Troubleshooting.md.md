<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Operations-Observability-and-Troubleshooting | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: ef1a5f1dbc70a3480dd075d1b0f5826b1444b425a77980cddd5137c3dfda2739 -->

# Operations: Observability & Troubleshooting

## Identity / integrity failures

Check standard/schema version, inherited canonicalization profile, content boundary, byte hash/signature inputs and — when used — the declared semantic-fingerprint profile. Do not compare a semantic fingerprint as if it were an inherited byte hash.

## Query returns unexpected material

Check:

- resolved semantic roots;
- normalized query plan;
- traversal direction and property constraints;
- source/shard scope;
- v6 applicability / valuation / record-role filters where relevant;
- evidence policy;
- query-index source fingerprints;
- conflicts / unresolved identities.

## Query appears to say “nothing exists”

First verify completeness. A `partial` result, exhausted budget, unavailable shard or continuation requirement cannot be treated as a negative factual answer.

```text
PARTIAL RESULT != NEGATIVE RESULT
BUDGET EXHAUSTION != ABSENCE
```

## Continuation fails

Check that the cursor still matches the normalized query, source fingerprint/snapshot set and ordering profile. A safe implementation should fail rather than resume against incompatible source state.

## Missing / wrong lexicalization

Check requested BCP 47 locale, lexicon-stack order, explicit fallback policy and conflicting equal-precedence entries. If no term resolves, preserve the semantic ID; do not synthesize a canonical label.

## AI context seems incomplete

Inspect the context bundle's source fingerprints, semantic/evidence closure, omissions, selection policy and byte/token budgets. Verify that semantic atoms preserve the identities/provenance needed to interpret each selected claim/edge.

## Automation unexpectedly blocked or attempted

Check `actionability.mode`, human-validation requirements, missing inputs and downstream owner admission/authority policy. A valuation such as `high` never means “execute,” and model output does not grant execution authority.

## Projection / index drift

Rebuild the derived projection/index from the pinned source state and declared transform/profile. Derived stores should be disposable/reproducible where their contract promises determinism.
