<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/blob/74b07c42811dae0c68549d8554c00bc44a04298d/docs/reference/GF_BRIDGE_SPEC.md | commit: 74b07c42811dae0c68549d8554c00bc44a04298d | SHA-256: a74e86cf6fbcfc6c6d855e9718f9f80249567871b5512f23cc2ebfbbbaae98c3 -->

# GF Bridge Specification

Status: **normative adapter format for v1**

A RuntimeSet contains exactly one hashed `other` artifact whose ID begins with `sa-gf-bridge`. The artifact maps SA↔GF operation IDs to expressions accepted by the exact PGF artifact.

Example:

```json
{
  "schema_version": "1.0",
  "contract_version": "1.0",
  "feature_values": {
    "polarity": {
      "positive": "positivePol",
      "negative": "negativePol"
    }
  },
  "operations": {
    "clause.transitive_event": {
      "variants": [
        {
          "requires": ["agent", "predicate", "patient"],
          "when": {"polarity": "negative"},
          "expression": "SA_Transitive {agent} {predicate} {patient} {feature.polarity}",
          "consumes_features": []
        }
      ]
    }
  }
}
```

## Fidelity rule

For a variant to be admissible:

1. all declared `requires` must be available;
2. every expression placeholder must be bound;
3. **every lexical slot in the `RealizationUnit` must appear in the expression**;
4. every semantic feature must either appear as `{feature.<name>}` or be explicitly declared in `consumes_features`;
5. every `when` condition must match exactly.

If no variant satisfies these rules, realization fails with `SA-GF-001`. Extra semantic material is never silently ignored.

`feature_values` may map canonical feature values to GF expressions/constructors. Values without an encoder are represented as deterministic GF string/primitive literals and therefore must be accepted intentionally by the bridge expression.
