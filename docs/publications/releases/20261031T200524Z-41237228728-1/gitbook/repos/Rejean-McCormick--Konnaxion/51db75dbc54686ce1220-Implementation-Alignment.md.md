<!-- Frozen source: https://github.com/Rejean-McCormick/Konnaxion/wiki/Implementation-Alignment | commit: 62c3bb451bacb4cfbbeb68181c1edfc7ba47a8f9 | SHA-256: b22b008db5b5fbe637f6cfcb8dfa53c6f3949c4c54b390adbb2e72bca53e9588 -->

# Konnaxion — Implementation Alignment

This page lists the current code areas that should change so implementation and architecture use the same ownership model. It is a technical reference, not a project-management log.

## 1. EkoH expertise taxonomy

`EthikosTopic.expertise_category` currently references a compatibility taxonomy under `kollective_intelligence`. New canonical references should use `ekoh.ExpertiseCategory`, with the required data/schema migration.

The EkoH-owned taxonomy is **UNESCO ISCED-F 2013 / CITE-F 2013**, with a default domain-bearing profile of **10 broad / 26 substantive narrow / 77 substantive detailed = 113 categories**. Do not recreate the old flat “26 ISO-based domains” list. See [[EkoH Expertise Taxonomy|EkoH-Expertise-Taxonomy]].

## 2. `kollective_intelligence` compatibility paths

The codebase still contains the `konnaxion.kollective_intelligence` package and compatibility vote APIs. New EkoH and Smart Vote functionality should use:

```text
konnaxion.ekoh
konnaxion.smart_vote
```

rather than creating new canonical state in the compatibility package.

## 3. Konsensus vote API

Current Konsensus frontend code still uses the compatibility `kollective/votes/` route and can submit `weighted_value`.

Target rule:

```text
source ballot
≠ derived reading weight
```

The client should submit source participation only. Smart Vote should calculate a contextual reading separately.

## 4. Smart Vote persisted weighted values

The current Smart Vote ballot path persists `Vote.weighted_value` and aggregates `VoteResult.sum_weighted_value`.

This path must be reconciled with the reading architecture so the source ballot and the derived contextual interpretation are not one authoritative object.

## 5. Preserve the ethiKos reading path

`smart_vote/services/reading_service.py` already follows the correct direction:

- reads ethiKos source stances;
- uses explicit `SourceConsultationBinding`;
- keeps baseline separate;
- hashes the lens;
- hashes EkoH contextual inputs;
- supports advisory-only exclusions without deleting source participation;
- filters participant detail through EkoH rating access.

Do not collapse this behavior back into ballot-level weighted state.

## 6. Durable reading snapshots

The current `snapshot_ref` identifies the EkoH inputs used for an on-demand reading. If a reading is treated as durable/published/replayable, add recoverable snapshot/materialized-reading storage so those exact inputs can be retrieved.

## 7. Consultation relevance validation

Validate the full `ConsultationRelevance` vector according to the lens policy: non-negative values plus the declared normalization/sum rule.

## 8. Remove global voting-power UI semantics

The current EkoH UI contains a `current-voting-weight` page that presents a person's global Smart Vote influence. Replace this with domain expertise or consultation-specific reading context. There is no universal personal Smart Vote weight in the aligned model.

## 9. Analytics/Pulse source typing

Do not mix ethiKos stances, Smart Vote source ballots and Smart Vote derived readings into one untyped participation source. Analytics should declare which source/event type it is counting.

## 10. External ecosystem adapters

No active Konnaxion adapter is present for Orgo, Kristal or SemantiK Architect in the supplied snapshot. Add dedicated boundary/adapters only when a concrete use case is implemented; do not import their internal persistence models into Konnaxion.
