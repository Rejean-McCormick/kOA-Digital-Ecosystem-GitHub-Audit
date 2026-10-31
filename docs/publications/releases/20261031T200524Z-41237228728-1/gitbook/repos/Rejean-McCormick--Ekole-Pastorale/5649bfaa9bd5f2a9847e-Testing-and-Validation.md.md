<!-- Frozen source: https://github.com/Rejean-McCormick/Ekole-Pastorale/wiki/Testing-and-Validation | commit: 7c73b3852cf83a881cd83a14f345a78e163dc8c3 | SHA-256: 424c66de7ba9afedadbf2815e9c548342b2f89c206990b77da0a3c9ee9ded07d -->

# Testing and Validation

## What can be verified locally

The supplied project has repository-level tests that check manifest structure, course counts, prerequisite boundaries, derived-file consistency, teacher/learner separation, v11 workspaces, and representative state controls. The companion Ekole Core can verify that the content pack loads through its real interface.

**Passing tests demonstrates technical consistency, not ecclesiastical approval or verified historical truth.**

## Quick checks

From `ecole-pastorale/`:

```bash
python3 -m unittest discover -s tests -v
python3 demarrer_pastorale.py --verifier
```

The second command needs the sibling `../ekole/launcher.py` or a `--core`/`EKOLE_CORE_PATH` override.

To exercise the content projection:

```bash
python3 outils/projeter_ekole.py
```

This command may validate all source Kristals and their pinned builds. It should regenerate the same output if source content has not changed.

## Representative single-course checks

```bash
python3 kristals/lire-bible/tools/kristal.py check-v11 kristals/lire-bible
python3 kristals/lire-bible/tools/kristal.py check kristals/lire-bible
```

Only build an updated state after actual canonical changes and source review:

```bash
python3 kristals/lire-bible/tools/kristal.py build-v9 kristals/lire-bible
```

## Expected content invariants

- Manifest declares `ekole.content-pack/0.1` and `id: ecole-pastorale`.
- **32 courses**, **7 pathways**, and course IDs resolvable to files.
- **20** courses in the message branch and **12** in the miracles branch.
- Prerequisites are acyclic and do **not** cross the two branches.
- Teacher JSON may contain assessment and session plans; learner JSON omits teacher-only data.
- Derived content matches the logical state/build commitments.
- Publication authorization remains false until an actual review process grants it.

## Optional dependencies

The tests can use `jsonschema` for deeper schema validation if the package is installed. Runtime Core loading in the provided prototype was designed without a required extra Python package; do not assume the same for future Core versions.

## Known limitations

- Arketype overlays ARK-20 and ARK-21 are **candidate extensions**, not upstream standards.
- An older Arketype baseline snapshot had independent global-validation issues; successful extension-local tests do not resolve those upstream issues.
- The historical Catho bridge is **documentary** and not a complete v11 semantic federation.
- Not all referenced editions, translations, images, or theological claims have been reviewed.
- The course drafts do not constitute an accredited or ecclesiastically endorsed curriculum.

For the change workflow, see [Authoring and Projection](Authoring-and-Projection.md). For launch failures, see [Troubleshooting](Troubleshooting.md).
