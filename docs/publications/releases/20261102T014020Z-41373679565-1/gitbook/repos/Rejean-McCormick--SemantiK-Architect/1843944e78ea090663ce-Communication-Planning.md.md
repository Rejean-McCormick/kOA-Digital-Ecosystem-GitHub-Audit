<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/wiki/Communication-Planning | commit: f187a43fc9540ce7d443ff4d2ab26dfdc7a48bfe | SHA-256: 0cb028fa2df822e01b921e2edb22024556f42fb5ffcd6127a78c538a2f2da019 -->

# Communication Planning

`CommunicationPlanner` organizes all submitted obligations into a language-neutral `CommunicationPlan`.

It answers **how the supplied content should be organized**, not how a particular language spells or inflects it.

## Planner freedoms

When permitted by constraints, the planner may:

- group compatible obligations;
- preserve or apply supplied ordering constraints;
- split dense material into several communication units;
- identify list-worthy collections;
- add an authorized greeting or closing;
- preserve discourse sequence relationships.

## Planner prohibitions

The planner must not:

- delete an obligation because it seems unimportant;
- rank content unless an upstream ordering policy exists;
- infer business urgency from linguistic wording;
- summarize by silently dropping meaning;
- invent missing facts.

## Ordering states

- `FIXED` — supplied order is meaningful and must be preserved;
- `POLICY` — a supplied ordering policy/result is authoritative;
- `FREE` — presentation order may change for communicative naturalness.

`FREE` permits presentation order, not a new business ranking.

## CommunicationPlan

A `CommunicationPlan` contains obligation grouping, sequencing and presentation intent.

It does **not** contain:

- PGF objects;
- language-specific morphology;
- arbitrary GF functions;
- final language-specific sentence structure.

Those decisions belong to [[Language Planning|Language-Planning]].
