<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/What-is-Kristal | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 87e286c6aa4d566ab3939825f4a45af7b4fdbf4273400754e502b6a80285b095 -->

# What is Kristal?

Kristal is a portable, deterministic architecture for structured knowledge, epistemic state and reproducible knowledge artifacts.

It is not one database format or one ontology model.

**Current snapshot:** v10 `10.0.0-draft.3.2` adds a hosted-network layer to unchanged v9 semantic state; see [[Kristal-v10]].

## Five accumulated generations

- **v6** defines portable epistemic state and independently addressable assertions;
- **v7** adds stable semantic identity, registries, factorization and orchestration;
- **v8** externalizes language and adds exact semantic query/read models;
- **v9** separates logical state from build, physical materialization and runtime access;
- **v10** adds nodes, host bindings, publication and discovery without changing v9 commitments.

## The inherited v9 semantic-state model

```text
what knowledge means
        ↓
Logical Artifact(s)
        ↓
immutable State Snapshot
        ↓
Derivations + Materializations
        ↓
Exchange / Runtime / Query / AI views
```

## What Kristal tries to preserve

- identity without label coupling;
- provenance and evidence;
- applicability and value-state distinctions;
- explicit disagreement and unknowns;
- authority boundaries;
- reproducible build lineage;
- representation independence;
- explicit completeness/partial-result semantics;
- deterministic publication and rollback.

## What it deliberately avoids

Kristal does not require all knowledge to be triples, rows, graph edges or documents. It standardizes the envelope and lifecycle around domain-native structures.

The most compact v9 principle is:

```text
KNOWLEDGE != BUILD != MATERIALIZATION != READ MODEL
```
