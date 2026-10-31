<!-- Frozen source: https://github.com/Rejean-McCormick/Ekole-Pastorale/wiki/Architecture | commit: 7c73b3852cf83a881cd83a14f345a78e163dc8c3 | SHA-256: 7cfbd63a3e320783d4d31e66796943a1155f9f44110f7fb6a36957a7bd52e58e -->

# Architecture

## Design rule

**Ekole Core is a standalone, neutral learning engine.** It must not contain Catholic-specific logic, saints, miracles, or local curriculum rules. The same Core can consume `ekole-quebec` or `ecole-pastorale` as separate content packs.

```text
                        Content repositories

  ekole-quebec/                         ecole-pastorale/
  (separate school)                     (Catholic school)
                                       ┌───────────────────────┐
  Independent content                   │ 32 ARK-20 Kristals    │
                                       │ 1 ARK-21 witness      │
                                       │ Catho legacy bridge   │
                                       └───────────┬───────────┘
                                                   │
                                      validate / derive
                                                   │
                                       ┌───────────▼───────────┐
                                       │ pack.json + cours/    │
                                       │ publications/eleve/   │
                                       └───────────┬───────────┘
                                                   │
                        select a content pack      │
                                   ┌───────────────▼─────┐
                                   │      ekole/         │
                                   │ neutral Ekole Core  │
                                   └─────────────────────┘
```

## Responsibilities

| Layer | Owns | Must not own |
| --- | --- | --- |
| **Ekole Core** (`../ekole`) | Web servers, course loading, navigation, general student/teacher features | Catholic doctrine or site-specific curriculum |
| **Pastorale Kristal sources** (`kristals/`) | Canonical learning units, objectives, teaching sequence, assessments, namespace-scoped semantics | Other Kristals' primary historical sources |
| **Witness Kristals** (`kristals-temoins/`) | Sources and structured testimony about saints or witnesses | Automatic recognition of miracles, doctrinal authority |
| **Federation** (`federation/`) | Pinned documentary references and candidate links | Unreviewed v11 identity equivalences |
| **Ekole projection** (root `pack.json`, `cours/`, etc.) | Runnable, derived views for Core | Canonical source edits |

## Data flow

1. Write and review the **canonical learning-unit JSON** of one Kristal.
2. Validate its v11 graph, local workspace, and content quality.
3. Rebuild the v9 logical state commitment if canonical content has changed.
4. Run `outils/projeter_ekole.py` to regenerate the Core-facing files.
5. Verify the pack with `demarrer_pastorale.py --verifier`.
6. Open the school locally for testing.

## Two branches, no forced dependencies

The projector checks that a course prerequisite remains within its own branch. A mixed **pathway** may include materials from both branches, but no module in the message branch requires a learner to complete the miracles branch first.

Both branches are Catholic. Separation is an instructional design boundary, not a claim that religious teachings and miracles are doctrinally unrelated.

## Teacher and learner projections

- `cours/` contains the **teacher-oriented** generated JSON, including assessment fields and lesson guidance.
- `publications/eleve/` contains **learner-oriented** generated JSON; it omits private teacher rubrics and safeguarding notes.
- Learner views remain local demonstrations and explicitly indicate that publication is **not authorized**.

## Useful entry points

- `pack.json`: `ekole.content-pack/0.1` manifest.
- `demarrer_pastorale.py`: sibling-Core launcher.
- `outils/projeter_ekole.py`: strict content compiler/projector.
- `contracts/`: editorial schemas, **not** upstream v11 standards.
- `provenance-derivation.json`: generated provenance record.

Next: [Kristal Framework v11](Kristal-Framework-v11.md) and [Authoring and Projection](Authoring-and-Projection.md).
