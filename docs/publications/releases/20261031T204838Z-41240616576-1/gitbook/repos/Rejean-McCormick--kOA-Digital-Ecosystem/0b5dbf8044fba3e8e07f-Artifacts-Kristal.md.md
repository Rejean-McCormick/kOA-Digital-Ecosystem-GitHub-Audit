<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/90865538b0c16be08423843208f4c5e6785a7523/docs/1-Overview/Artifacts-Kristal.md | commit: 90865538b0c16be08423843208f4c5e6785a7523 | SHA-256: 65e118597eac326fed19046b61a3fc285e64a24c593b56ae5bd0b0d126a1b981 -->

# Kristal v6 artifacts

The kOA ecosystem consumes Kristal v6 artifacts without collapsing their distinctions between measurement, applicability, role, validation, recognition and actionability.

| Artifact / surface | Purpose |
|---|---|
| Kristal State | canonical atomic assertions with provenance, typed valuations, coordinates, applicability, roles and optional actionability |
| Validation / recognition records | scoped findings and authority decisions referenced by state |
| Reader Policy | controls which labeled material a consumer may read |
| Derived Runtime/query projection | deterministic read/runtime materialization tied to a source state |
| Consumer projection | owner-specific rebuildable view such as UCKK/Moodle/glossary/media |

`artifact_status`, validation and recognition are separate transitions. A state may be `working` or `under_review` without pretending to be reference material.

## What belongs in Kristal

Kristal is a portable knowledge/state artifact layer, not a shared application database. It is appropriate for information that benefits from atomic identity, explicit provenance/evidence, typed measurements or states, applicability, conflict/supersession, validation/recognition, Reader Policy and reproducible content addressing.

Kristal v6 also distinguishes data roles: an official rule can be represented as `authoritative_constraint`, a captured fact as `observed_state`, an internal policy as `organizational_rule`, and a derived conclusion as `derived_state`. These roles preserve distinctions; they do not create authority by themselves.

## Actionable knowledge

`actionability` describes whether a represented action is eligible for automation, requires human review/decision, is manual/prohibited, or lacks enough information. It is intentionally not an execution API. Operational owners still mutate only their own state after admission under an explicit boundary contract.

## Derived materializations

Tables, indexes, columnar stores, read-only databases and Runtime Packs remain derived and non-authoritative. They must be tied to a source state/content digest and rebuildable from declared inputs.
