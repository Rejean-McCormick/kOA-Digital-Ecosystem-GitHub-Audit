<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Workflow-Federation-and-Curation | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 6c5ab6e632b20e2dda855b9094e3be6c78eba1a8725fe5d5f451185d194c31c1 -->

# Workflow: Federation & Curation

V9 federation composes independently governed states/artifacts without erasing source identity, disagreement or uncertainty.

## Pin exact children

A parent State Snapshot references exact child commitments, not mutable `latest` aliases.

## Preserve authority

```text
REFERENCE != OWNERSHIP TRANSFER
STATE COMPOSITION != AUTHORITY MERGE
```

A parent can compose a child without becoming the child's epistemic authority.

## Preserve semantic distinctions

Do not merge material merely because rendered text looks similar. Differences may exist in semantic ID, valuation, applicability, record role, validation/recognition, temporal scope or source authority.

## Shards and segments

A semantic shard may be independently curated/versioned. Its physical materialization may contain many segments.

```text
SHARD != SEGMENT
```

## Federated query

The v8 query coordinator preserves shard/source provenance and parent budgets. Unavailable child state/shards yield explicit partial/unknown coverage instead of silent absence.

## Lexical federation

Semantic and lexical federation remain orthogonal. A domain state can be rendered through several lexical stacks without changing the state commitment.

See [[Federation-and-Coverage-v9]] and [[Federation-Pagination-and-Continuations]].
