<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/wiki/Examples | commit: f187a43fc9540ce7d443ff4d2ab26dfdc7a48bfe | SHA-256: c922851bb11542ddb1af3c4f2f2d495baac7e24dbd3977b96a3c61744fa94b2a -->

# Examples

These examples illustrate ownership and flow. Exact surface wording is determined by the released target-language runtime.

## Orgo operational communication

### Upstream meaning

```text
recipient: Marcel
work item: repair machine 4356
before: 16:00
support contact: Gabriel
phone: 418 123-4567
register: operational
relationship: familiar
```

### SA responsibility

SA may decide to produce two utterances instead of forcing every fact into one sentence, while preserving all obligations.

A possible French realization is conceptually:

```text
Marcel, la machine 4356 doit être réparée avant 16 h.
Gabriel est disponible pour t'aider au 418 123-4567.
```

The wording is not the authority. The original structured content remains the authority, and coverage maps output units back to obligations.

## Task collection

If Orgo supplies four tasks and their authoritative order, SA may render:

```text
Bonjour Marcel. Ce matin, tu as quatre tâches à réaliser.

1. …
2. …
3. …
4. …
```

SA may choose a list because it is an appropriate presentation structure. It may not delete task 4 because the message is long.

## eThikos confirmation

A user constructs a graph:

```text
central claim
 ├─ supports → reason A
 ├─ conflicts with → reason B
 └─ depends on → condition C
```

SA turns that structure into a natural-language communication/question in the selected language so the user can confirm whether the graph represents the intended thought.

## Cross-language realization

The same obligations may produce two utterances in one language and three in another. That is valid if semantic coverage remains identical and both language/profile RuntimeSets are released.
