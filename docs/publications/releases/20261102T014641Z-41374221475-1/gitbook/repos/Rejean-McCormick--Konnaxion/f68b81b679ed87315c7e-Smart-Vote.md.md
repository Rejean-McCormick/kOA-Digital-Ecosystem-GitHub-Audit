<!-- Frozen source: https://github.com/Rejean-McCormick/Konnaxion/wiki/Smart-Vote | commit: 62c3bb451bacb4cfbbeb68181c1edfc7ba47a8f9 | SHA-256: a018384fb077e9c6fec23ba5127c9878dac8b6b05a195cf4c47afe866d410713 -->

# Smart Vote — Contextual Readings

Smart Vote owns **declared derived readings**, lens semantics and related aggregation. It does not own the source facts it interprets.

Canonical backend:

```text
backend/konnaxion/smart_vote/
```

## Core rule

```text
source participation
≠ baseline
≠ contextual reading
```

For ethiKos:

```text
EthikosTopic + EthikosStance
        ↓ source facts
baseline aggregation
        ↓
SourceConsultationBinding
ConsultationRelevance
EkoH context
        ↓
Smart Vote advisory reading
```

## Current API

```text
POST /api/v1/smart-vote/cast/
GET  /api/v1/smart-vote/readings/ethikos-topic/<topic_id>/
```

The reading endpoint exposes a baseline and a separate `ekoh_weighted_v1` reading when a binding exists.

## Current reading metadata

The reading service produces, among other fields:

- `reading_key`;
- `lens_hash`;
- `snapshot_ref`;
- `computed_at`;
- result payload;
- participant-level trace/detail when allowed by rating-access policy.

## Contextual weight

A Smart Vote weight is specific to the declared consultation/lens/context. It is **not a permanent global voting power attached to the user**.

## Advisory exclusions

A declared advisory exclusion can set a participant's reading weight to zero while leaving the source stance in the baseline. This preserves source history and makes the advisory transformation explicit.

## Reproducibility

The current service hashes the EkoH input snapshot used for a reading. If a reading is treated as durable/published/replayable, the corresponding inputs must also be recoverable; a hash alone identifies data but does not store it.

## Implementation alignment

The older ballot path still contains `Vote.weighted_value` and `VoteResult.sum_weighted_value`. These should not become the architecture model for source participation. See [[Implementation Alignment|Implementation-Alignment]].
