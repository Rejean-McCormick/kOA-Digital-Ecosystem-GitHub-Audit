<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/wiki/Integrations | commit: f187a43fc9540ce7d443ff4d2ab26dfdc7a48bfe | SHA-256: 6e35719b3b59670c51591225b72bac36cd6dea98942c83762f7927a8af4f0133 -->

# Integrations

SemantiK Architect is designed as a transversal communication component. Integration does not transfer domain ownership to SA.

## Kristal

Kristal owns structured epistemic state, provenance, certainty/status/authority and canonical knowledge artifacts.

SA may verbalize those distinctions when they are obligations, but it does not create a competing truth ledger.

```text
Kristal projection → Kristal ACL → CommunicationRequest → SA
```

## SenTient

SenTient owns free-text ingestion/resolution/formalization in the ecosystem flow.

SA does not parse arbitrary prose as its canonical input.

```text
human/free text → SenTient → structured semantics/Kristal → SA
```

## Orgo

Orgo owns tasks, cases, assignments, urgency, deadlines, priority and ordering policy.

SA turns the selected Orgo semantics into communication without re-prioritizing them.

## eThikos

eThikos owns structured questions, propositions, argument graphs and interaction semantics.

SA articulates the graph in natural language so a person can confirm or refine the intended meaning. It does not decide which ethical position is correct.

## KeenKonnect / Konnaxion

These systems own exchange, matching and community state. SA can render structured prompts, notices, explanations and exchanges in participant languages.

## Wikidata / Wikimedia ecosystem

SA may use:

- Wikidata identifiers;
- local Wikidata mirrors;
- Wikidata Lexeme data;
- useful open-source offline components.

Live Wikimedia infrastructure is not required by the canonical runtime. Wikimedia-specific protocols remain behind adapters.

External structured-meaning protocols such as Ninai or ZObject-based representations may be supported through optional ACL/adapters when useful. They are interchange formats, not the canonical internal model.

## Integration rule

The preferred sequence is:

```text
reuse → wrap → extend → replace → rewrite
```

Move right only when there is a concrete technical benefit such as determinism, offline capability, semantic fidelity, performance or maintainability.
