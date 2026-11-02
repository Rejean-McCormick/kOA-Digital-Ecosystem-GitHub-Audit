<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Operations-Compatibility | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 8b31004110509dbc1ec8bdb3a5ebb0ab478a5f83976036fe7065c7c36aae6878 -->

# Operations: Compatibility

Kristal v9 is additive over v6/v7/v8. Operational compatibility must preserve inherited semantics while allowing v9 state/materialization capabilities to be adopted independently.

## Stable expectations

Consumers should version-gate changes to:

- v6 canonicalization/hash boundaries and `kristal_state` semantics;
- v7 KQ/KP/KA/KS identity semantics;
- valuation/value-state meaning;
- record-role/actionability meaning;
- validation/recognition meaning;
- lexical stack resolution policy;
- KQP query/result contracts;
- semantic-fingerprint profiles;
- compact encoding profiles.

## Additive evolution

Deployments may add optional lexicons, query indexes, context compilers, encodings and specialized query modes when capability negotiation makes support explicit.

## Breaking evolution

Treat as breaking unless explicitly versioned:

- redefining an existing semantic ID or property;
- turning a label into semantic identity;
- changing inherited content-hash boundaries;
- silently promoting a derived read model to canonical truth;
- treating `partial` as negative/complete;
- changing lexical precedence without declaring stack/profile changes;
- changing semantic-fingerprint projection under the same profile ID.

## Upgrade principle

Prefer machine-readable capabilities, adapters and validation over heuristic compatibility. See [[Compatibility-v6-v7-v8]].
