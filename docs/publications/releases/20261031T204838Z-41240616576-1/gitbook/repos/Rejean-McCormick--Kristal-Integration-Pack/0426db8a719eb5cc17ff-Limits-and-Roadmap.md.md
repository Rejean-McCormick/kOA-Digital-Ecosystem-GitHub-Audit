<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Integration-Pack/wiki/Limits-and-Roadmap | commit: 949de422daed28c0b84684b509e675807ac9c48b | SHA-256: 1df0883ed7a9a70fd62ac78a3bd9daaedae29058ff3135533cdf71db52a8f4b5 -->

# Limits and Roadmap

## Current release boundaries

- The Pack is a **candidate** read-only v11 adapter and a separately guarded legacy Konstellation/Kompiler overlay.
- No canonical KQ/KP mutation, schema migration, dictionary activation, authoring registration, or publication is performed by the v11 path.
- The old v6 projection requires a compatible v7 Surface; it cannot generally convert v9, v10 or v11 semantic states.
- The real diK alpha.7 executable and a production-size Wikidata dump have **not** been qualified end-to-end in this Pack release.
- Full Konstellation build, browser tests, multiuser policy enforcement and live Kompiler HTTP integration are still separate.
- No production signatures, reviewer authentication or C1/C2/C3 release gates are implemented here.

## Priorities for a future stable integration

1. Re-run the handoff against the **exact distributed diK alpha.7 artifacts**, using representative and permissioned source data.
2. Qualify the Authoring Kit and Framework on common reviewed pins, including crash recovery and registered catalog revisions.
3. Complete Konstellation owner integration and enforce per-principal Reader Policies across all Kompiler requests; only then consider shared deployment.
4. Perform source and browser tests on the actual host at its supported Node version, plus failure and authorization negative tests.
5. Qualify C3 and any public/private distribution through the responsible owner systems; avoid new navigation or publishing authorities.
6. Review and version the contract manifests whenever a Framework validator or semantic schema changes.

The architecture should remain **non-canonical at the Integration Pack boundary**. Stabilization is an evidence and integration effort, not an invitation to infer identities from labels.

See [[Qualification-and-Testing]] and [[Architecture-and-Ownership]].
