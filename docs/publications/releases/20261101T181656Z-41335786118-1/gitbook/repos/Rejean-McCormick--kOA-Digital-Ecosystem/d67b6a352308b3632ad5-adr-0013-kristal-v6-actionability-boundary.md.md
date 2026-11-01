<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/90865538b0c16be08423843208f4c5e6785a7523/docs/2-Technical-Reference/90-reference/adr/adr-0013-kristal-v6-actionability-boundary.md | commit: 90865538b0c16be08423843208f4c5e6785a7523 | SHA-256: f987a472daa814a57f89e1d96918d42eaddd00a64e40279eb0cfa174251485d3 -->

# ADR-0013: Kristal v6 generalized state and actionability boundary

- **Status:** Accepted
- **Date:** 2026-10-01
- **Scope:** ecosystem interpretation of Kristal Standard 6.0.0

## Decision

Adopt Kristal v6 `kristal_state`, typed `valuations[]`, `coordinates`, `applicability`, `record_role` and `actionability` across the active knowledge boundary.

`actionability` is descriptive/policy metadata. It may be used to select an automation route, but it never authorizes a cross-system mutation by itself. The receiving owner contract, identity/authority check and admission rules remain mandatory.

`record_role` similarly does not create authority: an `authoritative_constraint` must retain a provenance/authority chain to the actual external authority; an `observed_state` remains a snapshot of the source owner's state; an `organizational_rule` remains scoped to the declaring organization.

## Consequence

The ecosystem can automate deterministic work with minimal friction while preserving human review/decision for cases where expertise or authority is required. Completed actions and human decisions can return as traceable records, allowing the knowledge corpus to improve over time without turning Kristal into a central operational database or orchestrator.
