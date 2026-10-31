<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/4ed4b8928665ebd723b68f8b3f2cb2f196d6374f/docs/1-Overview/Integration-External-systems.md | commit: 4ed4b8928665ebd723b68f8b3f2cb2f196d6374f | SHA-256: 58c07344c1b13c7664d9e50908d62e1dcb1f8ab836c9871a26167b4376ca3890 -->

# Integration — External systems

External systems integrate through explicit adapters/contracts, source-owned exports/references and adopted cross-system Profiles where applicable. Shared mutable state is not an integration contract.

## Safe entry patterns

- command: explicit intent to the owning receiver;
- query: read/projection without ownership transfer;
- event: fact already committed by the publisher;
- artifact: immutable/versioned content with identity/integrity/provenance;
- durable external effect: idempotency + retry/outbox + terminal reconciliation.

## Knowledge acquisition

EncyKlopedia is the source-discovery/acquisition boundary for the current knowledge pipeline. It hands immutable evidence and referent candidates to Da’at/Kristal through `encyklopedia.corpus-harvest-handoff/1.0.0`. External providers and identifiers never become the Kristal authority.

## kOA-Linux artifact boundary

When an external artifact is adopted by kOA-Linux, use the registered artifact class/release channel and Release Set compatibility rules. Runtime Pack local verification/active state belongs to `kristal_runtime`; privileged node operations use kOA Node Agent only where required.

## Koali

External/product applications may contribute presentation surfaces to Koali Spaces through admission/registration contracts. Presentation registration or Space activation does not grant product, policy or host authority.

## UCKK directional interchange and projection

kOA-Linux defines separate `publish_to_uckk` and `import_from_uckk` contracts. They preserve source/destination authority and do not imply shared databases or background bidirectional synchronization.

Separately, `uckk.univers-cite-projection/1.0.0` defines a rebuildable consumer projection over pinned Kristal state. Moodle/campus state remains UCKK-owned; the projection does not become the epistemic canon.

## SemantiK / GF tooling boundary

GF Wordbench, SemantiK Architect, SemantiK Runtime Orchestrator, LevelUpDiag and GF Observatory retain separate ownership. Release orchestration may coordinate them through external filesystem/process contracts, but does not transfer grammar, semantic, diagnostic or observation authority.
