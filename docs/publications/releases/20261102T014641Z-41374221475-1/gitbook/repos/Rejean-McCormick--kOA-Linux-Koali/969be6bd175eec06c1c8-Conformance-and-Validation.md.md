<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Linux-Koali/wiki/Conformance-and-Validation | commit: a014d6b410b475fe227e3f0153bbae6e54ef0520 | SHA-256: 32c7540ec9a1f7d0b3999623bce15f31b747caf6745003ef1dd94738b18ef4e8 -->

<!-- Navigational projection. Normative authority remains in the repository docs/ corpus. -->

# Conformance and Validation

> **Authority notice:** This wiki is a readable navigation layer. Source contracts, accepted ADRs, normative documents, and executable validators in the repository remain authoritative.

## Complete pipeline

Run from the repository root:

```bash
python docs/tools/validate_docs.py
```

The pipeline runs the specialized documentation controls before a documentation release can be considered valid.

## Specialized validators

| Validator | Purpose |
| --- | --- |
| `check_ai_boundary.py` | AI and external-integration authority boundaries |
| `check_artifact_contracts.py` | Artifact schemas and examples |
| `check_canonical_ownership.py` | Canonical ownership uniqueness |
| `check_component_boundaries.py` | Component and subsystem separation |
| `check_decision_closure.py` | Decision closure and unresolved choices |
| `check_document_graph.py` | Document identities and dependency graph |
| `check_generated_blocks.py` | Generated blocks inside source documents |
| `check_generated_content.py` | Deterministic generated outputs |
| `check_greenfield_architecture.py` | Active architecture constraints |
| `check_interfile_locks.py` | Cross-file alignment locks |
| `check_language.py` | Active documentation language policy |
| `check_no_unresolved_state.py` | Unresolved authority or placeholder states |
| `check_normative_language.py` | Normative language use |
| `check_profile_inheritance.py` | Profile and overlay composition |
| `check_release_sets.py` | Release-set and channel compatibility |
| `check_subsystem_alignment.py` | Subsystem boundary contracts and mounts |
| `check_traceability.py` | Decision, requirement, test, and evidence traceability |

## Generated-content rebuild

```bash
python docs/tools/build_indexes.py
python docs/tools/build_ai_context.py
python docs/tools/check_generated_content.py
```

## Subsystem mounts

Normal validation permits reserved paths to remain unmounted:

```bash
python docs/tools/check_subsystem_alignment.py
```

After all six official documentation trees are linked, require their presence:

```bash
python docs/tools/check_subsystem_alignment.py --require-mounted
```

## Evidence model

Conformance claims require traceable requirements, tests, and evidence. Architectural prose alone is not sufficient for an implementation claim.

## Sources

- [`docs/09-conformance/00-conformance-model.md`](../blob/main/docs/09-conformance/00-conformance-model.md)
- [`docs/09-conformance/01-requirement-identification.md`](../blob/main/docs/09-conformance/01-requirement-identification.md)
- [`docs/09-conformance/02-requirement-traceability.md`](../blob/main/docs/09-conformance/02-requirement-traceability.md)
- [`docs/09-conformance/05-test-evidence.md`](../blob/main/docs/09-conformance/05-test-evidence.md)
- [`docs/09-conformance/06-release-evidence.md`](../blob/main/docs/09-conformance/06-release-evidence.md)
- [`docs/09-conformance/19-release-gates.md`](../blob/main/docs/09-conformance/19-release-gates.md)
- [`docs/09-conformance/20-subsystem-documentation-alignment.md`](../blob/main/docs/09-conformance/20-subsystem-documentation-alignment.md)
- [`docs/09-conformance/21-generated-navigation-rebuild.md`](../blob/main/docs/09-conformance/21-generated-navigation-rebuild.md)
- [`docs/tools/validate_docs.py`](../blob/main/docs/tools/validate_docs.py)
