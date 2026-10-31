<!-- Frozen source: https://github.com/Rejean-McCormick/Karacter/blob/c50db0afda429e4be45e41f67658061e49e9282f/docs/decisions/ADR-002_EXPLAINABLE_SIMULATIONS.md | commit: c50db0afda429e4be45e41f67658061e49e9282f | SHA-256: 8b3c180f391d039419d842401db618653467bcf23a3928a329aea7e98ca84175 -->

# ADR-002: Explanation-first scenario simulation

**Status:** Proposed for v6.

## Decision

Use a deterministic, locally executable scenario engine that generates multiple **plausible hypotheses** grounded in a frozen snapshot. Every suggestion has an explanation linking to actual supplied character/context data. The user can edit or reject any suggestion.

## Why

The existing v5 heuristic output can feel repetitive and unconvincing. A black-box AI prediction could overstate psychological certainty and create privacy dependencies. A transparent engine is easier to test and refine.

## Consequences

- Maintain versioned rules and example fixtures.
- Treat narrative/story constraints as important as numerical preferences.
- Support low information gracefully instead of hallucinating history.
- Reject moral ranking and simulated certainty percentages.
- Optional model-provider integration is future scope only.

See [simulation engine](../domain/05_SIMULATION_ENGINE.md).
