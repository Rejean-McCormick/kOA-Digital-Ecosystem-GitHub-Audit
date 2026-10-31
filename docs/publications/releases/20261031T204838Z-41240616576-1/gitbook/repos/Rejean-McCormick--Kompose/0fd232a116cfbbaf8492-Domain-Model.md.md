<!-- Frozen source: https://github.com/Rejean-McCormick/Kompose/wiki/Domain-Model | commit: ec94ee500739b0078a14ee9cf67d34d46d2087e4 | SHA-256: c2a367a6fda73ca61c2f6fb9d2955511b60eba7779a4fa762f56910dd45c1386 -->

# Domain Model and Invariants

> These entities describe the **KOMPOSE reference model**, not canonical operational Orgo Case/Task/Signal aggregates. See [[Tandem-Orgo-Boundary]].

| Object | Identity and responsibility |
|---|---|
| `Capsule` | Versioned scenario referencing roles, missions, and Kristals |
| `Session` | Execution of a capsule for a group, with state and version |
| `Participant` | Opaque identifier scoped to one session |
| `Role` | Narrative function with required skills and capacity |
| `DiagnosticBlueprint` | Questions, dimensions, and planned accommodations |
| `DiagnosticResult` | Sensitive result and private summary |
| `TeacherConstraint` | Private hard rule or preference, with lifetime and rationale |
| `Assignment` | Participant-to-role assignment, version, supervised decision |
| `Kristal` | Content immutable for each `(id, version)` |
| `Custody` | Temporary guardianship of a Kristal |
| `AccessGrant` | Scoped, revocable permission to consult it |
| `MissionProgress` | Minimal mission-completion state |
| `Phase` | Shared milestone with prerequisites |
| `PromptDefinition` | Conditional message for an authorized audience |
| `Event` | Versioned, traceable domain fact |
| `IntegrationManifest` | Client application's authorized capabilities |

## Cross-cutting invariants

1. In a unit-capacity configuration, a participant has at most one active role.
2. Neither private relationships nor raw scores are exported through public events.
3. Changing guardians **never** changes the Kristal's editorial version.
4. A session uses **pinned versions** of knowledge.
5. Session transitions and mission updates remain consistent and auditable.
6. Missing documented answers produce an explicit unavailable result, never improvisation.

## Schemas

Authoritative structural definitions live in `contracts/schemas/` (JSON Schema 2020-12), with semantic checks in `src/kompose/validation.py`. Schema validity alone cannot guarantee all business invariants.

[[Home|← Home]] · [[Architecture|Architecture →]]
