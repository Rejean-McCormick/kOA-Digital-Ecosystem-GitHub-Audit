<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Query-Pagination-and-Capabilities | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: fa3a34101dc1afd1a3ef1844b9904ec2039e95d0fbf8c6f8097ac642f911e037 -->

# Query: Pagination & Capabilities

v8 processors advertise only the capabilities they actually implement. A consumer must not assume every engine supports every KQP mode, encoding, index or federation feature.

## Capability examples

- exact identity lookup;
- typed neighborhood/traversal;
- evidence closure;
- temporal/diff operations;
- lexical resolution;
- AI context compilation;
- `expanded_json` / `symbol_table_v1` output;
- local or remote federation;
- v6/v7 adapters.

Unsupported operations should fail explicitly rather than be guessed.

## Pagination

Pagination must preserve a stable semantic ordering. An opaque cursor should bind to:

- normalized query fingerprint;
- source snapshot/fingerprint set;
- ordering profile;
- last emitted position;
- expiry/validity policy where applicable.

If source state is incompatible with the continuation contract, resume must fail rather than silently continue against a different snapshot.

## Completeness

Every bounded/federated result should make clear whether its semantic/evidence/source coverage is complete, partial, not requested or unknown.

See [[Federation-Pagination-and-Continuations]].
