<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Universal-Structure-and-Transposition | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 1166923249956f989386106af4df29fadb5e5f843629c983ed3c3411f6a06c79 -->

# Universal Structure & Transposition

> **v9 compatibility note:** This page documents the retained v6 portable-state semantics. V9 preserves the contract as a frozen substrate and may wrap/project it through Logical Artifacts without redefining it. See [[Version-Stack-v6-v7-v8-v9]].

Kristal is universal **not because every domain has the same ontology**, but because very different domains repeatedly require the same structural capabilities:

```text
stable identity
    +
atomic assertions
    +
context / applicability
    +
typed measurements or states
    +
provenance / evidence
    +
validation / recognition
    +
conflict / succession / lineage
    +
reader projections
    +
actionability boundaries
```

The domain supplies the meaning. Kristal supplies the durable structure around that meaning.

## One substrate, many data structures

The same Kristal semantics can be materialized in several implementation forms.

### Property graph

Natural for traversing relations, dependencies, causal paths, taxonomies and provenance.

```text
(subject)-[predicate {valuations, applicability}]->(object)
```

### Relational model

Natural for deterministic joins, reporting and transactional integrations.

```text
referents
assertions
valuations
coordinates
applicability
provenance
validation
```

### Document / JSON model

Natural for portable artifacts, content addressing, exchange and nested domain payloads.

### Event-sourced model

Natural when observations, decisions, supersession and derived state must be reconstructed over time.

### Analytical / columnar model

Natural for bulk projections, statistics, coverage analysis and high-volume valuation queries.

### Vector / retrieval indexes

Useful as **derived search surfaces**, but not as the canonical authority layer. Embeddings may help locate related material; they do not replace identity, provenance or applicability.

## The canonical meaning is more important than storage shape

Kristal does not require every application to use the same physical database. A graph store, SQL database, document store and data lake can all participate if they preserve the same semantic boundaries.

The invariant is the meaning of the record and its traceability, not the vendor or storage engine.

## Why this matters for AI

AI work becomes durable when the useful result is converted from transient prose into structured, attributable state.

```text
AI reads / extracts / reasons
        ↓
structured assertions
        ↓
evidence + applicability + valuations
        ↓
Kristal State
        ↓
human correction / new evidence / new rule
        ↓
updated Kristal State
```

The next agent can start from the accumulated work rather than reproducing it.

## Domain examples

The same structural substrate can represent:

- proof closure and formal dependencies in mathematics;
- cross-scale biological interactions;
- historical technology trajectories;
- institutional pathways and administrative requirements;
- recipe identity and ingredient necessity;
- automotive diagnostic hypotheses;
- botanical taxonomy and occurrence confidence;
- organizational rules and observed operating state;
- food products, formulations, nutrients and regulatory claims.

The structure is reusable precisely because the **semantic dimension is declared instead of assumed**.

## A practical test

A domain is a good Kristal candidate when useful work must survive beyond one application session and the following questions matter:

1. What is this about?
2. What exactly is being asserted?
3. Under which conditions does it apply?
4. How strong / necessary / likely / compatible / mature is it?
5. Where did it come from?
6. Who validated or recognized it?
7. What conflicts with or supersedes it?
8. What can be derived from it?
9. What can be automated, and what still needs a human?
