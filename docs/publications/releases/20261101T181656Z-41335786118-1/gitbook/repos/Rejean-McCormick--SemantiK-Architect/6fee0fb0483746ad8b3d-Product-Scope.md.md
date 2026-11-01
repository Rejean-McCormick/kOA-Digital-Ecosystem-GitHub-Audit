<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/wiki/Product-Scope | commit: f187a43fc9540ce7d443ff4d2ab26dfdc7a48bfe | SHA-256: f26816f6edd03ca7db82864b9f2e1ef27309556f2d811a64eec4b022698ed135 -->

# Product Scope

## Product definition

SemantiK Architect transforms **structured semantic information selected by an upstream authority** into faithful, context-appropriate, multilingual human communication.

Its unit of work is a **bounded communication**, not necessarily one sentence. A result may contain several utterances, a question, a list, labels, notices, or a conventional greeting/closing.

## The ownership boundary

The central distinction is:

```text
content authority                 articulation authority
(upstream)                        (SemantiK Architect)

what is true                      how it is phrased
what must be communicated         how it is grouped
priority/order policy             sentence segmentation
workflow state                    register/politeness
epistemic status                  target-language construction
```

### SA may

- split dense meaning across several sentences;
- fuse compatible obligations into one utterance;
- render a homogeneous collection as a list;
- choose formal/informal forms;
- choose language-appropriate construction and word packaging;
- add non-factual discourse framing such as an authorized greeting;
- derive deterministic values such as a count when the derivation is explicit and traceable.

### SA must not

- invent missing facts;
- silently omit an obligation;
- decide which supplied fact is more important;
- rank tasks unless the ranking/order policy was supplied;
- convert uncertainty into fact;
- decide which ethical argument is better;
- use a hidden language fallback;
- duplicate GF morphology/syntax inside SA.

## Core use cases

### Operational systems

Orgo can provide ordered tasks, deadlines, machines, contacts and communication context. SA turns the supplied semantics into a natural operational communication without changing the task set.

### Structured thought

eThikos can provide a concept/argument graph. SA verbalizes that structure so a person can confirm whether the sentence matches the intended meaning.

### Multilingual exchange

KeenKonnect/Konnaxion can pass structured exchange semantics to SA for presentation in each participant's language.

### Semantic translation

Free text is first interpreted/formalized upstream. SA then re-realizes the resulting structured meaning in the target language. See [[Translation & Multilingual Use|Translation-and-Multilingual-Use]].

## Non-goals

SA is not:

- a truth engine;
- a knowledge base;
- a raw-text NLP parser;
- a workflow engine;
- an article generator;
- a recommendation/ranking engine;
- a second RGL;
- a best-effort grammar fallback system.
