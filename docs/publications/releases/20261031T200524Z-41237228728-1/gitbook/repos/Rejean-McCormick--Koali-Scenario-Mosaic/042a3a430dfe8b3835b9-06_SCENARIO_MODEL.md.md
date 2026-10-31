<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Scenario-Mosaic/blob/4ac4e787ef01295c9100c73d8b5bbf9a19d9ef03/docs/06_SCENARIO_MODEL.md | commit: 4ac4e787ef01295c9100c73d8b5bbf9a19d9ef03 | SHA-256: cae92d7f1b733dd5fa04a12d73a414521cb32550ffe792b3a755f319d04c6078 -->

# Scenario card model v2 — English edition

## Why this schema

The scenario model separates human intent, scale, environment, technical properties, domain, and evidence status. It also adds two layers of traceability:

- `pattern_family` — reusable editorial abstraction;
- `canon_refs` / `signature_patterns` — links to the Koali capability canon.

## Frontmatter

```yaml
id: SCN-001
title:
primary_category: CAT-01
pattern_family: PAT-01
palette: []
components:
  kristal: 0..5
  konnaxion: 0..5
  orgo: 0..5
  uckk: 0..5
secondary_components: []
entry_trigger:
scales: []
settings: []
properties: []
domains: []
signature_patterns: []
canon_refs: []
transfer_domains: []
derivation: EXPLICIT | COMPOSED | DERIVED | FUTURE-DESIGN
runtime_evidence: DOCUMENTED | VALIDATED | PARTIALLY-VALIDATED | UNVERIFIED
pattern:
continuity_gap:
```

## Facets

**scales** — individual, team, organization, inter-organizational, community, public-institution.

**settings** — enterprise, research, education, culture, field, crisis, public-service, community.

**properties** — offline, multilingual, local-first, sensitive-data, ai-optional, public-facing, high-consequence, intermittent-connectivity, role-routing.

**domains** — professions and sectors; useful as secondary indexes, never as the primary information architecture.

## Quality rule

A scenario belongs in the Atlas when a reader can recognize the problem without knowing Koali; the use crosses at least two meaningful steps; Koali’s role is continuity rather than a generic isolated feature; the pattern transfers to other domains; authority boundaries remain intact; and the wording matches the evidence level.
