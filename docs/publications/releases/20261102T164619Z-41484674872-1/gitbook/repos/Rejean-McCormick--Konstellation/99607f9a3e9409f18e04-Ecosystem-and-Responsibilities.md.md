<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/wiki/Ecosystem-and-Responsibilities | commit: 01bfc9126e06db9560d1c84e4b315026a28690af | SHA-256: ef74482b8d8cf35314a251c65245b9fef206d98b0036a4387f300aa73f1f3a7e -->

# Ecosystem and Responsibilities

| Component | Responsible for | Must not claim to do |
| --- | --- | --- |
| **Kristal Framework v10** | Standards, contracts, commitments, hosting profiles | Grant publication permissions to a specific instance |
| **Kristal Authoring Kit** | Local builds, derivations, Discovery, authoring checks | Act as an independent qualifier |
| **Arketype** | `ARK-xx` structure catalog, `PRF-xx` usage profiles, presentation conventions | Certify content, access the canon, or infer authority from a name |
| **Kristal Manager** | Inventory and operational checks; future strictly authorized synchronization | Replace C1/C2/C3 or grant access merely because an entry is inventoried |
| **KristalDiag / C1** | Independent qualification of a candidate | Authorize publication beyond its mandate |
| **Bootstrap / C2** | Policy and authorization decisions | Change a Kristal's logical content |
| **Hosting / C3** | Publication and host-related checks | Replace C1/C2 with the mere existence of a GitHub repository |
| **Konstellation** | Reading, selection, navigation, queries, projection, visualization | Mutate canon, assert truth, or publish |
| **Interaction Kernel** | Typed exchanges, envelopes, references, interaction profiles | Become a domain-specific Kristal reader |
| **Daat** | Controlled mappings and bridges between IK systems/profiles | Require changes merely to enable local reading |

## Arketype: structure is not truth

Arketype is a **nonnormative design library**. Its archetypes, usage patterns, and profiles can help Konstellation choose a view **when the mapping to the instance is explicit and attributable**. A parser, renderer, or Arketype suggestion is neither executable code that should be loaded automatically nor an epistemic validation.

## Interaction Kernel and Daat

The snapshot used for this integration retains existing IK interoperability and compatibility locks. No IK or Daat protocol change was shown to be necessary for opening a local Kristal in Konstellation. Evolving IK would require profile negotiation and a dedicated conformance suite.

## Separation of duties

```text
Define logical truth: Kristal + Framework
Build: Authoring Kit
Qualify: C1
Authorize: C2
Host/publish: C3, subject to the required evidence
Inventory/observe: Manager
Explore: Konstellation
Transport interactions: Interaction Kernel / Daat
```

References: Framework `docs/28_V10_ECOSYSTEM_ALIGNMENT.md`, Arketype `arketype/docs/ECOSYSTEM_ALIGNMENT.md`, and Konstellation `docs/33-kristal-v10-local-reader.md`.
