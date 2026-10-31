<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Reference-Runtime-v10 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 91c7c2d94f5bbee10cf141151ab47fdafc6d20fbf6443e3fa51c875a823e56bc -->

# Reference Runtime & Verification — v10

The Framework includes a **non-normative JavaScript reference implementation**. Normative authority remains with the Framework specification, schemas, machine contracts and relevant test vectors.

The v10 reference covers hosted-network contracts and GitHub reader/publication surfaces while continuing to verify inherited v9 Logical Artifacts and State Snapshots. Host locations and reference implementation behavior must not redefine semantic commitments.

## Complementary verification planes

- **Framework JS:** reference operations and contract verification for the implemented baseline.
- **KristalDiag Python:** independent examination of targets and evidence; do not assume it has qualified Framework draft.3 merely because it is a v10 examiner.
- **GitHub collection ingest:** checks exact derived reader surfaces and hosted state linkages; this is operational integrity verification, not epistemic certification.

For exact profiles consult [[Conformance-v10]], [[Reference-Runtime-v9]], [[GitHub-Read-Surfaces-v10]] and [[Status-v10]].

*Sources: Framework `reference/js/src/v10/`, `spec/v10/Conformance.md`; KristalDiag `README.md`.*

## Optional reader inspector (draft.3.2)

The CLI implements `inspect-reader-discovery <local-dir> [--verify-files]` for the Kit 3.3.0 triple. It checks metadata relations, byte sizes and SHA-256 of registered files when requested, and returns non-executable reader suggestions. There is no simdjson binding or authorization engine here. See [[Reader-Discovery-and-Arketype-v10]].
