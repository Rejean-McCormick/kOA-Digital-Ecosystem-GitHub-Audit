<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/2-Technical-Reference/40-integration/orchestration-c0/decisions-and-gates.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: d16f34c50ba3a15f7666f41b39d0ca7a597750b7e2f7a1bf9b01c6a6689c7118 -->

# C0 — Publication and authority gates

**D-001 — Accepted policy (user decision).** After an **initial human authorization for one specific Kristal**, future revisions may publish automatically **within that authorization's explicit public scope**, provided **every revision passes qualification**. This is a policy decision, **not an implemented mechanism**.

**D-002 — Preserve ownership.** EncyK acquires evidence; Médiathèque stores durable sources; Da’at maps/admission where explicitly adopted; Kristal controls semantics; Authoring builds; KristalDiag independently verifies; Manager synchronizes; Bootstrap qualifies/publishes/activates; Konstellation explores; Kompiler compiles read-only context. C0 only coordinates interface evidence.

**D-003 — No silent v1/v2, v6/v9/v10 upgrade.** Historical knowledge projection JSON stays frozen. EncyK v2 source-storage handoff is not equivalent to historical v1. v10 hosting is distinct from v9 semantic identity.

**D-004 — Pilot Zoology.** Zoology is the test fixture. Its local structural tests passed in C0 investigation. Independent qualification and *specific publication authorization* have not yet been supplied. Do not expose additional Zoology bytes publicly merely because state metadata already exists publicly.

## Minimum release gating sequence (proposal; not deployed)

```text
candidate built in private / local context
   -> owner validation, coverage and source rights checked
   -> independent qualification against EXACT inputs/commit and bytes
   -> per-Kristal authorization active AND exact files within allowed scope
   -> publish immutable release at pinned commit (no silent overwrite)
   -> verify release, record receipt
   -> authenticated downstream rebuild of Konstellation Light catalogue
   -> smoke test site; on failure preserve previously valid site

Activation = separate explicit decision; never inferred from publication.
```

**Critical security property:** writes or pull requests to a *public* GitHub repository expose their contents. Therefore approval + qualification must occur **before any public push/PR**, not just before creating a GitHub Release. On new file categories or expanded audience, require renewed human authorization. If an approval is revoked, stop future releases; already-published bytes are not secret again.

## Mandatory reject cases

- Missing, expired or revoked per-Kristal authorization; scope path mismatch; new unreviewed data category.
- Missing independent qualification, or any mismatch between verified bytes/commit and publish candidate.
- Unsigned / unverifiable / ambiguous source refs where integrity is required by the owner contract.
- Inconsistent release tag/content; divergent replay; publication callback untrusted or unpinned.
- Missing required manifest or mismatching digests for Konstellation and Kompiler reads.
- Redacted/private source content reachable from a public artifact.

**Current gate status for Zoology:** blocked for new public content. General policy decision is approved; *specific Zoology authorization and qualified release evidence remain pending*.

## D-005 — Global navigation decision (2026-10-12)

Konstellation is the sole Kristal fleet and in-Kristal navigator. Manager is the operational instance-inventory owner, Arketype the non-normative archetype/pattern library, and Kompiler a read-only context producer. Implementation has **not** been qualified and does not relax any C1/C2/C3 or Reader Policy gate. See [decisions and blockers](../kristal-v10-alignment/decisions.md).
