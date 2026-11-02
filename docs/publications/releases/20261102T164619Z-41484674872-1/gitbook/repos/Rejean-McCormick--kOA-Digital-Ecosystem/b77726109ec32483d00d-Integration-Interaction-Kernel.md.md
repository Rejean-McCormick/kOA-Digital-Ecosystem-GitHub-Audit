<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/wiki/Integration-Interaction-Kernel | commit: dd52671208ae86295bfcc5f896d236a20182faba | SHA-256: d4b7816fcfadac3fb915cba92fb2a053731f98c454332ac2a6775eed18f76a30 -->

# Integration — Interaction Kernel

Interaction Kernel (IK) is the **target system-of-systems interoperability protocol/Profile layer** for cross-product interactions such as Konnaxion↔Orgo and ecosystem↔Da’at.

## Status boundary

Digital Ecosystem must distinguish:

```text
IK target cross-system architecture
≠
kOA-Linux canonical internal/component communication contracts
```

The current kOA-Linux snapshot already defines its own registered command/query/event/job/artifact/receipt/gateway patterns. IK must not be described as having replaced those contracts until kOA-Linux and the product owners explicitly publish adoption/mapping.

## Target use

Planned/mapped Profiles include:

- `governance.decision.execute/1.0.0`;
- `accountability.impact.publish/1.0.0`;
- Kristal build/artifact/revision/distribution Profiles through Da’at.

## Rules

- Konnaxion↔Orgo is direct by default; no forced Kristal hop.
- Da’at remains the anti-corruption/mapping boundary for IK-facing Kristal work.
- Profile admission does not imply Kristal validation/recognition.
- Source-owned artifacts remain source-owned.
- Durable interactions preserve idempotency identity and reconciliation.

## Adoption claim

A product/platform may claim IK conformance only when its owning contracts and evidence identify the Profile/version and required behavior. General build/runtime qualification is not IK conformance evidence.
