<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Query-Basics | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: ff3184796f76e0a8f52cf06dd4cce2ea11f01426479846739ebd155c1c3bec54 -->

# Query Basics

v8 querying starts from **semantic identity**, not from a blob of rendered prose.

## Basic flow

1. Select source Kristal/Kristall material or a declared read model.
2. Resolve query roots to stable identities.
3. Validate typed scope, filters, capabilities and budget.
4. Execute exact traversal/assertion/evidence operations.
5. Return completeness, unresolved/conflict state and continuation metadata.
6. Optionally resolve lexical forms and compile an AI context bundle.

## Discovery is not semantic answer

Approximate lexical/vector search may propose candidates, but exact query begins only after identity resolution.

```text
FUZZY DISCOVERY != SEMANTIC ANSWER
```

If identity remains ambiguous, return candidates/conflict instead of silently selecting one.

## Direction matters

Traversal is not implicitly bidirectional. `out`, `in` and `both` are explicit. Following an incoming edge is not the same as asserting the inverse semantic relation.

## v6 dimensions remain valid

When querying v6 portable state, preserve semantics such as:

- subject / predicate / object;
- assertion status / record role;
- valuation dimension / value semantics / value state;
- coordinates / applicability;
- actionability;
- source/evidence;
- validation/recognition;
- conflict/supersession/lineage.

Do not flatten a valuation such as `high` without its dimension, and do not collapse `unknown` into `not_applicable` or zero.
