<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/90865538b0c16be08423843208f4c5e6785a7523/docs/1-Overview/Non-goals.md | commit: 90865538b0c16be08423843208f4c5e6785a7523 | SHA-256: c35a218b8f10b3cb6bbdfd4f21a9ca3a5cde7d7b450060593b230cdd057f541c -->

# Non-goals

This page defines what kOA (and this wiki) intentionally does **not** try to be. These boundaries prevent drift, “best effort” correctness, and accidental duplication of external contracts.

## 1) Not a restatement of Kristal

- This wiki does **not** restate or re-implement Kristal’s normative artifact definitions (schemas, canonicalization, hashing, signing targets).
- When Kristal details are needed, we **link** to the pinned Kristal v6 source and kOA’s integration pointers.

## 2) Not a schema catalog for boundary artifacts

- We do not list field-by-field schemas for Claim-IR, Resolved Claim-IR, Validation Report, Exchange, Runtime Pack, Render Bundle, etc.
- We describe where each artifact sits in the lifecycle and what kOA requires at the boundary (gates, verification, determinism), not the artifact internals.

## 3) Not product marketing or a user manual

- No product marketing, UX copy, or end-user documentation for specific applications built on top of kOA.
- Only ecosystem-level behavior, responsibilities, and operational expectations.

## 4) Not a deployment/topology specification

- No cloud-vendor specifics, infrastructure wiring, or full deployment topology.
- Ops content focuses on portable procedures (release/rollback/incident response), not “how to run it on Vendor X”.

## 5) Not an “always-available” system that trades correctness for uptime

- No “best effort” integrity checks at truth-compilation or activation boundaries.
- If declared verification cannot be completed, the correct behavior is to **stop/deny/rollback**, not to proceed.

## 6) Not a mutable truth store

- Published/reference Kristal artifacts are not hot-edited during incidents or runtime; changes produce new governed artifacts/versions.
- Fixes happen by creating new governed work and producing new versions, not patching canon in place.

## 7) Not an ungoverned execution platform

- Nothing executes “just because it can.”
- Execution is expressed as governed work with recorded inputs/outputs and auditability.

---

## If you were looking for…

- **Kristal schemas/contracts:** see **Integration → Kristal v6** (pinned dependency + contract pointers).
- **What kOA does cover:** see **Architecture**, **How it works (Lifecycle)**, **Components**, **Artifacts**, and **Operations**.
- **Operational safety rules:** see **Operations → Incident response**.