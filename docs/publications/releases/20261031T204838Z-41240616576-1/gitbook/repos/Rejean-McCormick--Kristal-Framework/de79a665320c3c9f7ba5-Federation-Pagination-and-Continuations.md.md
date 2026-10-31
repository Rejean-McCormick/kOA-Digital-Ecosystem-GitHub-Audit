<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Federation-Pagination-and-Continuations | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 42270790a987d7c4897dc5ad468f948cdcaef3b6e76a9252fe4052d188759491 -->

# Federation, Pagination and Continuations

## Federation

A logical Kristall may span many shards/operators. Federated query must preserve:

- semantic identity namespace;
- source/shard provenance;
- snapshot/source fingerprints;
- unresolved or missing shard state;
- parent budget accounting.

A timeout or unavailable shard yields `partial` unless policy explicitly requires fail-closed behavior.

## Pagination

Every paginated operation must declare or derive a stable ordering key. Cursor state is opaque to clients and should bind to the normalized query and source state.

## Continuation safety

A continuation should fail rather than silently resume against incompatible source state when snapshot consistency is required.

## Streaming

Streaming transport is optional. Every emitted page/atom still belongs to the same query/source state, and early termination must remain explicit when the transport supports it.

## Unknown outcome

If a federated subquery's completion state is unknown, the coordinator records that uncertainty instead of inferring success or absence.
