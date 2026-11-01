<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/90865538b0c16be08423843208f4c5e6785a7523/docs/2-Technical-Reference/30-artifacts/release-record.md | commit: 90865538b0c16be08423843208f4c5e6785a7523 | SHA-256: b44743934f009120fd83e27f755ac74a59dbdc0718e5bf262d80a0909cfa2180 -->

# Release Record v2 — deprecated compatibility projection

**Status:** Deprecated for authoritative release state.

The current kOA-Linux platform contract already defines **Release Set** as the artifact that binds compatible versions across independent release channels.

Digital Ecosystem must therefore not create a competing release authority.

If a legacy Release Record is retained for analytics, audit or migration, it MUST:

- identify itself as a non-authoritative projection;
- reference the authoritative `release_set_id`;
- reference owner-component activation/publication receipts;
- avoid inventing a second activation state;
- preserve the independent status of Kristal compile/validation/recognition and platform activation.

The former `schemas/release-record.schema.json` remains compatibility-only and should not be used for new authoritative writes.
