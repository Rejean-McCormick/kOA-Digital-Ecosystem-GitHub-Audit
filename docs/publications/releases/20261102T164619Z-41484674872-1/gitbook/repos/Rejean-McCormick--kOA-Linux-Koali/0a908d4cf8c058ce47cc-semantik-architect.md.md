<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Linux-Koali/blob/8f70441f18a259023a4c0a643bff82d731634cf5/docs/04-components/subsystems/semantik-architect.md | commit: 8f70441f18a259023a4c0a643bff82d731634cf5 | SHA-256: 2f142bf33dfd75ef2d87da941e304ee7d1d8369cc6b90cb8a922fd01b2a8e330 -->

<!-- KOA:DOC-META:BEGIN GENERATED
{
  "doc_id": "DOC-SUB-SEMANTIK-ARCHITECT",
  "document_class": "explanatory_markdown",
  "status": "active",
  "language": "en",
  "layer": "subsystem_boundaries",
  "scope": [
    "global"
  ],
  "canonical_refs": [
    "contracts/subsystems/semantik-architect.subsystem.json"
  ],
  "decision_ids": [],
  "requirement_ids": [],
  "lock_ids": [],
  "exception_ids": [],
  "depends_on": [],
  "tags": [
    "subsystem",
    "semantik_architect",
    "integration-boundary"
  ]
}
KOA:DOC-META:END -->

# SemantiK Architect Subsystem Boundary

## Purpose

This page defines the **kOA-Linux host boundary** for SemantiK Architect. SemantiK Architect remains one independently owned planner-centered multilingual NLG ecosystem system.

## Official documentation

The official documentation mount is `subsystems/semantik-architect/` and remains authoritative for Architect internals.

## Host role

Within kOA-Linux, SemantiK Architect is an **integrated subsystem**. kOA-Linux can own/mediate:

- deployment-profile membership;
- process/service lifecycle;
- resource envelope;
- identity/trust boundary;
- network and storage exposure;
- artifact admission/verification;
- local activation state when a declared artifact contract requires it;
- health/readiness integration;
- backup coordination;
- safe degradation.

SemantiK Architect owns:

- request normalization;
- planner behavior;
- `PlannedSentence`;
- `ConstructionPlan`;
- lexical resolution;
- renderer selection and backend behavior;
- `SurfaceResult`;
- the public generation contract.

GF/PGF is a supported backend/tooling family inside Architect, not a separate ecosystem system and not the architecture center.

```text
ecosystem scope: SemantiK Architect = ecosystem system
host scope:      SemantiK Architect = integrated subsystem
```
