<!-- Frozen source: https://github.com/Rejean-McCormick/Kontainer/wiki/Ecosystem-Integration | commit: c9674410bf4a3167240457a63ed37ddf51b76b25 | SHA-256: aa74a94427568e5d93c4425af363681f6d4bea3f1240fdb3a1734461699b03d9 -->

# Ecosystem Integration

Kontainer is the **physical container engine**, not the authority over Kristal semantics or cross-system business state. The supplied kOA Digital Ecosystem reference describes **Kristal v6** as a portable knowledge/state artifact layer, separate from runtime materializations and operational owners.

## Clear ownership

| Owner | Responsibility relative to Kontainer |
| --- | --- |
| **Kristal Framework** | Normative Kristal schemas, Logical Commitments, validation/recognition/Reader Policy; must explicitly adopt any physical format profile |
| **Kristal Authoring / Local Kit** | Build and validate Kristal data; select the authorized read surface passed to Kontainer |
| **Kontainer** | Select/package physical files; verify structure and bytes; provide encryption, signature, key access, and recovery primitives |
| **Manager / Konstellation** | GUI workflow, user prompts, display of verified state, explicit plaintext export, and transfer |
| **Kompiler / readers** | Consume authorized content and apply reader/application policies before projection or presentation |
| **Konfid** | Organizational access decisions, not local human password storage |
| **KMS/HSM (separately deployed)** | Enterprise key custody and issuance if a qualified provider is integrated in future |
| **Interaction Kernel** | Explicit admission, bounded operations and receipts across an adopted contract; not semantic verification |
| **kOA / other operational owners** | Their own release, activation, workflow, and mutable state boundaries |

## Intended data flow

```text
Kristal v6 state / validated Authoring Kit output
           |
           v
Local Kit read-surface/1.0 projection
           |   path, size, sha256, ready, errors
           v
Kontainer pack_read_surface()  →  .kristal
           |                         |
           | verified byte selection | transport / storage (opaque when encrypted)
           v                         v
Authorized reader/application → Framework semantic + Reader Policy checks
           |
           v
Derived projection / read-only view (not a second authority)
```

The Local Kit adapter requires `ready=true` and an empty `errors` list, copies exactly the selected files, and rechecks their sizes/digests against the selection. The caller must establish the provenance of the projection. The adapter **does not** independently recompute Framework Logical Commitments or validate Kristal v6 epistemic status.

## Difference between a Kristal State and a `.kristal` file

- A **Kristal State** is a structured semantic artifact with provenance, typed valuations, applicability, validation/recognition, roles, actionability and Reader Policies according to the relevant Kristal standard.
- A **`.kristal` container** is an outer physical representation that transports selected bytes with optional confidentiality and provenance-of-bytes checks.
- A **Runtime Pack or index** is a derived, rebuildable consumption artifact whose authority remains with its source and owning runtime processes.

In the supplied kOA ecosystem snapshot, the active Kristal semantic boundary is v6; **that does not automatically ratify the proposed `kristal.container/1` file-format contract.** Framework adoption and interoperability testing are separate decisions.

## Safe Manager and synchronization behavior

Manager should display at least: open vs encrypted; signature absent / valid-but-untrusted / trusted; physical verification vs Framework semantic validation; normal unlock vs recovery path. `inspect` alone is not validation. When moving an encrypted file to a repository or another system, move the **opaque ciphertext** unless explicit policy and user action authorize plaintext export. A GitHub private repo alone is not a cryptographic security boundary.

Reader Policies must be enforced downstream; the current container decrypts access to the **whole archive**, not different permissions for different members. Use separate packages/key domains if multiple audiences cannot share the same readable content. Protect previews, caches, AI indexes, logs and temporary derivatives as carefully as the original protected content.

## Deployment reality

The adapter and provider interfaces are implemented in the supplied library; direct Manager integration, live Konfid/KMS service authorization, TPM/WebAuthn unlocking, and full end-to-end semantic validation are **not claimed to be working integrations** in this candidate release.

References: repository `docs/INTEGRATION.md`; supplied kOA Digital Ecosystem overview and Kristal v6 integration material.
