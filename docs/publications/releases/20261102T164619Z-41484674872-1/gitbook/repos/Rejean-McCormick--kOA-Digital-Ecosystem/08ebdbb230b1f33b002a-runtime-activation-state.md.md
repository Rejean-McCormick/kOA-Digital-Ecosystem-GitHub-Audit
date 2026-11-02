<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/2-Technical-Reference/30-artifacts/runtime-activation-state.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: 3194d2d1a0df6d483c631914fc867f30a1cd73ab9502497811ea577b4c7d5728 -->

# Runtime Activation State — deprecated compatibility artifact

**Status:** Deprecated for kOA-Linux Runtime Pack activation.

The current kOA-Linux contracts already assign authoritative Runtime Pack state to `kristal_runtime`, including:

- `runtime_pack_verification_record`;
- `active_runtime_pack_record`;
- activation receipts;
- rollback receipts;
- runtime health state.

Digital Ecosystem MUST NOT create another authoritative Runtime Activation State beside those records.

kOA Node Agent may execute the narrow privileged node-local transition when required, but its receipt does not replace `kristal_runtime`'s active-state record.

For standalone deployments outside kOA-Linux, the deployment may define another owner, but that owner remains deployment-specific rather than a universal Digital Ecosystem artifact.

The former `schemas/runtime-activation-state.schema.json` is retained only for migration readers.
