<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/blob/74b07c42811dae0c68549d8554c00bc44a04298d/docs/reference/REFERENCE_BASIS.md | commit: 74b07c42811dae0c68549d8554c00bc44a04298d | SHA-256: a54e5cc5cc517932539a65d94e7745765184141c12d8bd2613ded34ffc5be094 -->

# Reference Basis

Status: **informational**

This architecture lock was produced from the supplied project context and design review, including:

- the previous SemantiK Architect repository snapshot, used only to identify valuable concepts and failure modes rather than as a compatibility target;
- the supplied `senior-architecture-patterns` catalog, especially Hexagonal Architecture, Anti-Corruption Layer, Modular Monolith, Idempotency, Immutable Infrastructure, health checks, observability, timeout budgets and bounded graceful degradation;
- the user's stated product requirements: SA does not select/drop content, supports bounded multi-block communication, owns register/articulation, depends on well-developed GF languages, fails explicitly during language development, works throughout Orgo/eThikos/KeenKonnect/kOA, and operates from structured semantics/Kristal rather than direct free-text translation;
- the current GF language-development direction, including full Albanian/RGL work and the intent to scale to many mature languages;
- GF Wordbench/Observatory boundaries already present in the wider ecosystem.

The architecture intentionally excludes frame-family engines and safe-mode grammar paths.
