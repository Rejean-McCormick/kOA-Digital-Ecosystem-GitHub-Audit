<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/wiki/Integration-External-systems | commit: dd52671208ae86295bfcc5f896d236a20182faba | SHA-256: 28e449a9c768760dfaafc8965d9749f2c8393a273ad6386821783daf58416878 -->

# Integration — External systems

External systems integrate through explicit adapters/contracts, source-owned exports/references and adopted cross-system Profiles where applicable. Shared mutable state is not an integration contract.

## Safe entry patterns

- command: explicit intent to the owning receiver;
- query: read/projection without ownership transfer;
- event: fact already committed by the publisher;
- artifact: immutable/versioned content with identity/integrity/provenance;
- durable external effect: idempotency + retry/outbox + terminal reconciliation.

## Knowledge-source pattern

External knowledge providers such as Wikidata, Project Gutenberg, VIAF, Wikisource or archive services enter through source-owned discovery/acquisition flows. External identifiers are anchors for matching and provenance; they do not automatically become Kristal authority or UCKK identity.

EncyKlopedia owns the acquisition side of this boundary before Da’at/Kristal handoff.

## kOA-Linux artifact boundary

When an external artifact is adopted by kOA-Linux, use the registered artifact class/release channel and Release Set compatibility rules. Runtime Pack local verification/active state belongs to `kristal_runtime`; privileged node operations use kOA Node Agent only where required.

## Koali

External/product applications may contribute presentation surfaces to Koali Spaces through its admission/registration contracts. Presentation registration or Space activation does not grant product, policy or host authority.
