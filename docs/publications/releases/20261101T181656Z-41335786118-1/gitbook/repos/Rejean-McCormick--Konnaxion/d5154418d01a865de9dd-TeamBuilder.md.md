<!-- Frozen source: https://github.com/Rejean-McCormick/Konnaxion/wiki/TeamBuilder | commit: 62c3bb451bacb4cfbbeb68181c1edfc7ba47a8f9 | SHA-256: 5844cb8450a89de3cf05913dadb8e2ef1a484a192adfa64b464d84413d59a3e0 -->

# TeamBuilder — Problem and Team Formation

TeamBuilder is a Konnaxion application/domain capability for problem framing, builder sessions and team formation.

Canonical backend:

```text
backend/konnaxion/teambuilder/
```

## Current core models

- `Problem`;
- `ProblemChangeEvent`;
- `BuilderSession`;
- `Team`;
- `TeamMember`.

## Current UI

```text
/teambuilder
/teambuilder/create
/teambuilder/problems/*
/teambuilder/[sessionId]
/teambuilder/humans/*
```

## Orgo boundary

A TeamBuilder `Problem`, `BuilderSession` or team is not an Orgo Case/Task by identity. A future integration may create Orgo-governed work through an explicit boundary, but the Konnaxion objects keep their own semantics.
