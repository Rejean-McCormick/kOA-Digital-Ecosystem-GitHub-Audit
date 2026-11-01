<!-- Frozen source: https://github.com/Rejean-McCormick/Spek/wiki/Standalone-Architecture | commit: 4eb78305f912b1e78e9caa5a9afd83b6a9e03253 | SHA-256: 4ebaa1d493f16dbd87614748587efa2db617ab90f9f10c9508e650a5b77209f4 -->

# Standalone Architecture

**Spek is an independent local-first publishing product**, not a Konstellation plug-in. It needs only Python and local article/realization/layout files. Optional connectors can import data from separate Kristals, Konstellation or other source systems.

Knowledge authority remains upstream. Spek accepts explicitly mapped reader-visible exports, composes typed layouts, and produces derived publications. It never commits to a Kristal state or grants publication approval.

```text
Kristal A  ─┐
Kristal B  ─┼─→ approved export / Spek native input ─┐
Other APIs ─┘                                        │
Konstellation → ResultSet 0.2 → Spek bridge adapter ─┤
                                                     ↓
SemantiK Architect ───────┐            Spek Document Model
                          ├──→ short expressions → layouts → HTML/PDF/LaTeX
Preconstructed AI text ──┘            + Source Explorer
```

**One channel per phrase:** `semantik_architect` OR `ai_preconstructed`; legacy v0.3 fixtures remain labeled `legacy`. A static publication can carry provenance, but cannot automatically enforce a remote reader policy.

See [Source Connectors](Source-Connectors) and [Language Channels](Language-Channels). More precise source code: `docs/STANDALONE_AND_CONNECTORS.md`.

## Optional Kristal Wiki orchestration

Spek remains a standalone publishing product; in a Kristal deployment it is an invoked presentation component, **not** a subordinate knowledge authority. Arketype selects compatible editorial profiles, SemantiK supplies bounded language realizations, and the Manager coordinates eligibility and public deployment. None of these services are implicitly invoked by the shipped Spek 0.5 command `build`. See [[Kristal Wiki Architecture]].
