<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Migration-v10-to-v11 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 75b657bbf621592e54349f3c187ae5dbda503426a0847c57012cc34e85f5bfa2 -->

# Migrating to v11 without destroying historical state

**v11 is additive:** preserving valid v9 logical state and v10 hosting remains the default. A v10 hosted node does **not** need its v9 state or published bytes rewritten merely because v11 exists.

## Choosing a path

**Path A — Existing legacy Kristal:** leave its historic contract intact. Inventory source identity strings and older labels; use [[Legacy-Migration-v11]] only when adopting a strict v11 semantic graph is explicitly desired. Build new logical artifacts/revisions, never mutate the old committed ones.

**Path B — New strict-v11 Kristal:** allocate namespace-scoped KQ/KP/KA/KS with the internal authority; create a graph, dictionaries and Wikidata crosswalk, register artifacts in Authoring Kit 4 and enable v11 checks. `Q…` never replaces `KQ…` in the graph itself.

**Path C — Arketype design scaffold:** `create --authoring v11` yields an empty Kit 4 workspace and readiness guide, not a compliant graph. Finish authoring and register real artifacts before opting into strict conformance.

## Source audit and migration gates

1. Pin original source hashes, commitments and the old schema/version.
2. Distinguish legacy semantic identifiers from textual/literal content.
3. Generate candidate KQ/KP resolution proposals; review ambiguity and provenance.
4. Publish reviewed crosswalk and dictionary layers as separate immutable versions.
5. Only after approval produce a **new** canonical graph and Logical Artifact commitments.
6. Run the Framework TCK and Kit-specific tests; preserve original snapshots and explicit rollback route.

An absent Wikidata Q or a missing translation does not invalidate an existing internal KQ. The same graph can be rendered in many languages as dictionaries evolve without creating new semantic identities.

**See also:** [[Compatibility-v9-v10]] · [[Conformance-v11]] · [[Wikidata-Crosswalk-v11]].
