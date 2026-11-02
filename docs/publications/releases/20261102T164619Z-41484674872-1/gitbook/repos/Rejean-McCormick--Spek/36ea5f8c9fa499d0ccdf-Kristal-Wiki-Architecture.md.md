<!-- Frozen source: https://github.com/Rejean-McCormick/Spek/wiki/Kristal-Wiki-Architecture | commit: 4eb78305f912b1e78e9caa5a9afd83b6a9e03253 | SHA-256: 9876688f947249f1381769aaf63b1dcaad33f5daffbbbcbfdd7ad0cdd0a05e97 -->

# Kristal Wiki Architecture

## Principle: content authority, articulation, composition and publication stay separate

A Kristal Wiki page is a **read-only, derived communication projection** of an approved set of Kristal assertions. It is not the canonical Kristal state, and an attractive template is never a license to publish or to alter the meaning.

```text
Canonical Kristals in locals/ (private; semantic authority)
      |
      v
Kristal-Manager / Framework (selection, provenance, eligibility, C3)
      |
      | explicit selected assertions and communication obligations
      v
SemantiK Architect (semantic -> short, bounded, traceable realizations)
      |
      | CommunicationResult / realization_key / runtime identity
      v
Spek (typed article + Arketype-compatible layout -> Wiki Markdown)
      |
      | PRIVATE markdown draft + SHA-256 manifest
      v
Separate scientific, linguistic, disclosure and C1/C2/C3 approval
      |
      v
kristal-public collection and GitHub Wiki (explicit, authorized push)
```

## Who owns what?

| Component | Responsibility | What it must not do |
| --- | --- | --- |
| Kristal and `locals/` | Canonical meaning, assertions, identifiers, provenance | Delegate semantic truth to formatting |
| Kristal-Manager | Explicit selection, intake, readiness, publication orchestration | Assume a layout or text generator grants C1/C2 permission |
| Kristal Framework / validators | Contracts and qualifying integrity checks | Infer absent evidence |
| Arketype | Content-structure archetype and compatible editorial layouts | Choose claims or forge missing mandatory slots |
| SemantiK Architect | Plan and realize **provided** communication obligations, traceably | Choose facts, write unrestricted articles, improvise fallback prose |
| Spek | Bind typed semantic units, frozen realization keys and layout slots | Invent sentences, claim authority or verify external signatures |
| `kristal-public` | Public, versioned *eligible derived* collection | Become a second canonical source |
| GitHub Wiki | Human-readable Markdown navigation and presentation | Substitute for a release gate |

## Versioned hand-offs

1. A trusted producer supplies `semantik.kristal-v6.communication-projection/1.0`, containing a portable Kristal v6-compatible state reference, selected assertions and a mapped `communication_request`. The SemantiK `KristalV6Acl` checks selected-assertion `source_refs` and maps to `CommunicationRequest`.
2. A released SemantiK RuntimeSet attempts realization in the selected language. `CommunicationResult` carries blocks, coverage, deterministic result identity, runtime/profile and source references. Failure is reported, **not** hidden with a template-generated sentence.
3. An upstream adapter binds approved results to the exact keys used by `kristal.layout-article-source/0.1` and `kristal.layout-realizations/0.1` (`channel: semantik_architect`).
4. The optional `spek.wiki-archetype-templates/1.0` registry admits the section layout for the selected Arketype. Spek validates slots and emits private `spek.wiki-draft/1.0` Markdown.
5. The collection stage can aggregate by C3 index and pin a Git revision; publication still requires independently checked authorization and a separate push.

**Compatibility note:** a v9 state snapshot is not directly the SemantiK v6 communication request. An upstream, provenance-preserving projection is required; merely changing a version string is not valid integration.

## Current implementation boundary

- **Spek baseline 0.5.0:** eight typed HTML/PDF/TeX layouts, not a GitHub Wiki generator.
- **Optional overlay:** Markdown draft renderer, 19 Arketype profiles, CLI and Manager/`kristal-public` private-draft integration.
- **Still missing:** automatic trusted assertion-to-request-to-realization-to-article mapping for the real Kristals, independent approval/attestation verification and final Wiki deployment.

See [[Wiki Templates by Archetype]], [[Wiki Draft Workflow]], [[SemantiK Integration]] and [[Epistemic and Security Boundaries]].
