<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Linux-Koali/blob/8f70441f18a259023a4c0a643bff82d731634cf5/docs/04-components/subsystems/konnaxion.md | commit: 8f70441f18a259023a4c0a643bff82d731634cf5 | SHA-256: a44779637d927b3749cee99435f0c7c7c13500f35b220e32a80fbc653252cbf9 -->

<!-- KOA:DOC-META:BEGIN GENERATED
{
  "doc_id": "DOC-SUB-KONNAXION",
  "document_class": "explanatory_markdown",
  "status": "active",
  "language": "en",
  "layer": "subsystem_boundaries",
  "scope": [
    "global"
  ],
  "canonical_refs": [
    "contracts/subsystems/konnaxion.subsystem.json"
  ],
  "decision_ids": [],
  "requirement_ids": [],
  "lock_ids": [],
  "exception_ids": [],
  "depends_on": [],
  "tags": [
    "subsystem",
    "konnaxion",
    "integration-boundary"
  ]
}
KOA:DOC-META:END -->

# Konnaxion Subsystem Boundary

## Purpose

This page defines the **kOA-Linux host boundary** for Konnaxion. Konnaxion remains an independently owned ecosystem system. This page does not reproduce or redefine its internal documentation.

## Official documentation

The official documentation mount is `subsystems/konnaxion/` and remains authoritative for Konnaxion internals.

## Host role

Within kOA-Linux, Konnaxion is an **integrated subsystem**. kOA-Linux can own/mediate deployment-profile membership, process lifecycle, resource envelope, trust boundary, network/storage exposure, artifact admission, health integration, backup coordination, safe degradation, and declared cross-system interactions.

Konnaxion itself owns its civic/public domain model, internal workflows/state machines, API semantics, validation logic, application behavior, and user interfaces.

```text
ecosystem scope: Konnaxion = ecosystem system
host scope:      Konnaxion = integrated subsystem
```

No direct cross-system authoritative writes are permitted.


## User-interface boundary

Konnaxion owns its product pages, navigation semantics, commands, workflows, and standalone application entry point. It can use shared Koali shell and PageShell primitives without transferring Konnaxion business ownership to Koali.

When integrated with kOA Spaces, Konnaxion can contribute declarative surfaces, routes, navigation, commands, contextual inspectors, and widgets. The integrated host renders one outer frame; Konnaxion renders its business pages inside the active workspace. When kOA Spaces is absent, Konnaxion can render the same shared shell primitives itself and remain functional as a standalone product.

Konnaxion SHALL NOT become a mandatory UI runtime for Orgo or another product. Generic shell behavior belongs in the shared Koali UI contract or a compatible reusable library, not in private cross-product imports.
