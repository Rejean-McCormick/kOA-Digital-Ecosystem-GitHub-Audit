<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/2-Technical-Reference/30-artifacts/konnaxion-state.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: 31ac893dff29f990e911748033a4378f355b4899d7479116fbc6e3cff687b337 -->

# Konnaxion State — historical compatibility note

The former Konnaxion State artifact assumed Konnaxion universally owned Runtime Pack verification/activation/rollback.

That assumption is not valid in the current architecture.

For kOA-Linux deployments:

- Konnaxion may own civic/product desired selection or application intent;
- `kristal_runtime` owns Runtime Pack verification and active-state records;
- kOA Node Agent performs narrow privileged node-local transitions where required;
- Release Set/channel compatibility belongs to kOA-Linux platform contracts.

Do not emit new Konnaxion State records as authoritative Runtime Pack activation state.
