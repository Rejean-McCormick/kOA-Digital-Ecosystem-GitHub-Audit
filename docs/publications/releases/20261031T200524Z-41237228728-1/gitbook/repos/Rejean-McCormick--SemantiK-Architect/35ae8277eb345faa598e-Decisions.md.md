<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/wiki/Decisions | commit: f187a43fc9540ce7d443ff4d2ab26dfdc7a48bfe | SHA-256: c0855b1d06ae17771e09d7067148abf216ce1409d4c96ba69e9083200cae7f1d -->

# Decisions

This page summarizes the architectural decisions that should remain stable across implementation work.

## Locked v1 decisions

1. **SA owns articulation, not content selection.**
2. **Canonical meaning is a typed semantic graph plus explicit communication obligations.**
3. **Communication planning precedes target-language planning.**
4. **There is one canonical `LanguagePlan`; no extra general-purpose construction IR is required.**
5. **GF/RGL owns grammar; SA reaches it through a versioned bridge contract.**
6. **There is no hidden runtime language fallback.**
7. **Lexical resolution is two-phase: planning knowledge, then exact binding.**
8. **RuntimeSets are composed, immutable and content-addressed.**
9. **Languages are released by capability profile and conformance evidence.**
10. **The core is a hexagonal modular monolith.**
11. **Live external services are optional; offline/local operation is first-class.**
12. **Semantic correctness fails closed.**
13. **AI assists development; deterministic artifacts decide production release.**
14. **The 300th language must not require a new core-language branch.**

## Change discipline

Changes to locked boundaries require an explicit architectural decision, corresponding schema/contract updates and tests before code behavior is changed.

Additive growth such as a new lexeme, language RuntimeSet, capability profile, ecosystem ACL or output adapter should use existing extension points instead of redesigning the core.
