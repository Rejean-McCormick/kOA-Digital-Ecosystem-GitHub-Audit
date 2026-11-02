<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/wiki/Architecture | commit: f187a43fc9540ce7d443ff4d2ab26dfdc7a48bfe | SHA-256: 10e609950b13ff7f91250c864b8ded28ec11b7a645d964082e5fb656426d3d3e -->

# Architecture

SemantiK Architect is a **hexagonal modular monolith**.

The architecture is intentionally simple: one canonical render path, strict ports/adapters boundaries, immutable runtime artifacts, and explicit failures when semantic or linguistic correctness cannot be guaranteed.

## Canonical runtime path

```text
Driving adapter
   │
   ▼
ACL / canonical request mapper
   │
   ▼
CommunicationRequest
   │
   ├── request validation
   ▼
CommunicationPlanner
   │
   ▼
CommunicationPlan
   │
   ├── lexical knowledge preflight
   ▼
LanguagePlanner
   │
   ▼
LanguagePlan
   │
   ├── lexical binding
   ▼
RealizerPort
   │
   ▼
GF bridge adapter
   │
   ▼
GF / PGF runtime
   │
   ▼
Output assembly
   │
   ├── coverage validation
   ▼
CommunicationResult
```

## Dependency rule

```text
adapters  →  application  →  domain
              ↑      │
              │      ▼
            ports  pure policies
```

The domain/application core does not import PGF, HTTP frameworks, databases, Wikidata protocols or product-specific models.

## One canonical path

There is no parallel grammar engine, family renderer, emergency template engine or automatic fallback language.

If a requested released language/profile cannot realize the request correctly, generation fails.

## Anti-Corruption Layers

External systems end at explicit adapters:

```text
Kristal      ─┐
Orgo         ─┤
eThikos      ─┼─→ ACL → CommunicationRequest
KeenKonnect  ─┤
other systems ─┘
```

The core never needs to know an Orgo task schema or a Kristal wire format.

## Runtime immutability

A request is pinned to one immutable RuntimeSet. Grammar, lexical data, bridge contract and conformance identity cannot change mid-request.

See [[RuntimeSets]].
