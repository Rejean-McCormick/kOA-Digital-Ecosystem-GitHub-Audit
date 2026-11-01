<!-- Frozen source: https://github.com/Rejean-McCormick/Ekole-Pastorale/wiki/Authoring-and-Projection | commit: 7c73b3852cf83a881cd83a14f345a78e163dc8c3 | SHA-256: e11a5e6043f242c4201254afe68eee16e85a3362b19307b7394a142420f64e40 -->

# Authoring and Projection

This page describes the conservative workflow for changing a course without creating a divergence between its canonical Kristal state and the Ekole projection.

## 1. Choose the source of truth

Example unit: `kristals/lire-bible/`.

Its learning content lives at:

```text
kristals/lire-bible/canon/domain/pedagogie/unite.json
```

The generated teacher and learner JSON files, along with root `pack.json`, are **outputs**. Do not edit them directly to change course substance.

For a saint or witness record, consult `kristals-temoins/francois-assise/` and the ARK-21 profile rather than embedding another unaudited biography inside a course.

## 2. Edit and review

Before changing canonical content:

1. Confirm the course's objectives, branch, prerequisites, target learners, and planned evaluation.
2. Verify all Scriptural, historical, theological, and biographical references in reliable source editions.
3. Make explicit which text is Catholic doctrine and which is pastoral interpretation.
4. Check privacy, safeguarding, and non-coercion language for activities.
5. Check translations, quotations, and media rights.
6. Record the review state; **do not** mark a course approved unless an authorized review has actually occurred.

The two branches are independent: prerequisites must not silently cross from one branch to the other.

## 3. Validate the Kristal

From the repository root:

```bash
python3 kristals/lire-bible/tools/kristal.py check-v11 kristals/lire-bible
python3 kristals/lire-bible/tools/kristal.py check kristals/lire-bible
```

Resolve any errors before proceeding.

## 4. Rebuild the pinned state

After editorial and technical review:

```bash
python3 kristals/lire-bible/tools/kristal.py build-v9 kristals/lire-bible
```

The v9 state commitment binds the canonical payload used by the current projection pipeline. A changed canonical file with a stale build must be rejected rather than silently exported.

## 5. Regenerate the Ekole pack

```bash
python3 outils/projeter_ekole.py
```

This updates the **known derived outputs** at the root, including `pack.json`, `cours/`, `publications/eleve/`, and `provenance-derivation.json`. The projector reads the source Kristals and checks their relationship to pinned builds; it must not rewrite canonical teaching content.

The `--sans-preflight` mode, where available, is for narrowly scoped developer tests and **does not waive** state-content consistency requirements. Do not use it as a release shortcut.

## 6. Test in the real Core

```bash
python3 -m unittest discover -s tests -v
python3 demarrer_pastorale.py --verifier
```

Optionally start the interface:

```bash
python3 demarrer_pastorale.py --sans-navigateur
```

Inspect a course in both teacher and learner views. Confirm the learner file omits teacher rubrics, internal safeguarding instructions, and other private teacher-only material.

## 7. Review the build as a change set

A typical course edit may change the source Kristal, state snapshot, generated JSON, manifest and provenance. Review the changes together in version control. Do not publish solely because tests pass.

## Common pitfalls

| Problem | Why it happens | Safe response |
| --- | --- | --- |
| The projector rejects a changed canon | Source and state commitment differ | Review source; run validation and a new authorized `build-v9` |
| A prerequisite crosses branches | Two-branch curriculum invariant | Redesign the prerequisite, not the validator |
| Teacher notes appear in learner output | Projection/privacy boundary was violated | Block publication and correct the projection |
| A legacy Catho ID looks familiar | Labels and legacy IDs are not v11 identity proof | Use a reviewed crosswalk with recorded provenance |

Read [Testing and Validation](Testing-and-Validation.md) and [Governance and Safeguarding](Governance-and-Safeguarding.md) before publishing any content.
