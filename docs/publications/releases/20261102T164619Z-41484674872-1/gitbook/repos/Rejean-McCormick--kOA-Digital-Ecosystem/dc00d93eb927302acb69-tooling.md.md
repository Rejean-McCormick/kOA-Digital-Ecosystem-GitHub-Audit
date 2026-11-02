<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/2-Technical-Reference/60-guides/tooling.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: c9a5801a8f5a2a2c014219139bb3e1d7ce55e65bd2ab145f9fb31150c987a7ec -->

# Tooling guidance

Expected tooling capabilities include:

- validate owner-system contracts and references;
- verify exact Kristal pin/canonicalization;
- validate Kristal State and Kristal manifests;
- inspect Working/Reference status and Reader Policy refs;
- emit/validate Build Record correlation evidence when used;
- validate/read kOA-Linux Release Set and release-channel compatibility;
- inspect `kristal_runtime` verification/active-state/activation/rollback receipts;
- invoke kOA Node Agent only through its narrow authorized lifecycle contract when required;
- inspect Koali Space/runtime-registration/readiness state separately from Runtime Pack state;
- redrive durable cross-system operations without changing logical idempotency identity.

Do not create new Digital Ecosystem Release Record or Runtime Activation State authorities when owner contracts already exist.
