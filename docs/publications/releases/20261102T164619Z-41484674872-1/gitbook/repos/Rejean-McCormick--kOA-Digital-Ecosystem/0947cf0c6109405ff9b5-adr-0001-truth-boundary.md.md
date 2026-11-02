<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/2-Technical-Reference/90-reference/adr/adr-0001-truth-boundary.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: d53209d437657f91602dadb35d0063f76f1208f2ed43482a50beb4b38de5c92d -->

# ADR-0001: Truth Boundary (historical)

**Status:** Superseded by ADR-0008 on 2026-09-16  
**Historical date:** 2026-02-27

This ADR captured the former Kristal v4-oriented model in which validation gated compilation and one canonical Exchange represented the truth boundary.

It is retained for decision history only. It is **not** the active architecture. ADR-0008 subsequently replaced the v4 truth-boundary model for the v5 era; the active v6 interpretation is now defined by:

- `adr-0013-kristal-v6-actionability-boundary.md`
- `../../40-integration/kristal-v6/`

The retained historical assumptions that are no longer normative include:

- universal `Claim-IR → Resolved Claim-IR → validation → compile` ordering;
- universal “no compile on fail”;
- a single “canonical truth” status;
- treating validation, reference status and publication as one boundary.
