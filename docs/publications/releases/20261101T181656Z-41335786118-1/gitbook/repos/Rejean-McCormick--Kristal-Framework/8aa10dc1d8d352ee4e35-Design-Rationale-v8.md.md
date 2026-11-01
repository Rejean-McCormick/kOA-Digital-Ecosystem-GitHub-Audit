<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Design-Rationale-v8 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 6292804ea037c90b5c19d127a844d627041173269f9fa14e5b829a87e3f3d36f -->

# v8 Design Rationale

> **v9 note:** V8 rationale remains relevant for language/query boundaries. V9 extends the architecture with logical-state/materialization separation; see [[Kristal-v9]].


v8 deliberately applies established architecture/security patterns only where they protect Kristal's semantic contracts.

## Patterns used in the standard

- **Anti-Corruption Layer** → v6/v7/external-KOS adapters isolate legacy/foreign models.
- **CQRS/read-model separation** → canonical state remains authoritative while query indexes and AI projections are derived.
- **Sharding / Data Mesh** → semantic and lexical universes can be federated with domain stewardship under shared contracts.
- **Claim Check** → large source/evidence payloads can be referenced first and expanded on demand.
- **Graceful Degradation** → missing lexicons, shards or indexes become explicit states, not fabricated answers.
- **Timeout/agentic budgets** → deterministic limits live outside the model and propagate to child queries.
- **Canonical Semantic Fingerprints** → versioned semantic digests remain distinct from byte hashes.
- **Layered validation** → schema validity is not semantic validity or authorization.
- **Model is an Untrusted Planner** → model proposals pass deterministic gates.
- **Prompt/Context Taint** → retrieved context keeps provenance/trust classification.
- **Independent Tamper Anchor** → high-assurance deployments may externally anchor release/snapshot roots.

## Patterns intentionally left outside the semantic standard

Deployment-specific mechanisms such as blue/green rollout, Kubernetes service mesh, DLQ, CDN, transactional outbox or a particular database remain implementation/operations choices.

The standard defines **what semantic/query boundaries must hold**, not one infrastructure topology.
