<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Linux-Koali/wiki/Multilingual-Operation | commit: a014d6b410b475fe227e3f0153bbae6e54ef0520 | SHA-256: eb7afb228d449901d0a3d275c843ce21aeae1f1120b8b7fe2bd814e4df03fc01 -->

<!-- Explanatory wiki projection; not an independent normative authority. -->

# Multilingual Operation

> **Authority and status:** This wiki is an explanatory navigation layer. The repository contracts, accepted ADRs, normative documents, and executable validators remain authoritative for kOA-Linux Operating System. Public initkoa.org pages explain the wider kOA ecosystem and the product capabilities provided by its independently documented subsystems.

## More than interface translation

The multilingual objective is to preserve meaning across languages, not merely replace strings. A governance decision, role description, uncertainty label or knowledge assertion must not become stronger, weaker or less qualified because it is rendered in another language.

## Semantik Architect

Semantik Architect separates structured meaning from language-specific realization. It uses semantic frames, constructions, language-family engines, language profiles, lexicons, render profiles and regression tests to produce deterministic text.

It may render:

- role and mandate summaries;
- decision explanations;
- knowledge query results;
- civic process descriptions;
- multilingual cards, snippets, reports and notices;
- localized labels for Ariane-assisted navigation.

It must not invent facts absent from the selected structured input.

## Operational chain

```text
structured, policy-selected meaning
+ active language artifact
+ render profile
+ reader policy
= rendered text
+ trace metadata
```

## Language artifacts in kOA-Linux

The operating system verifies and activates compiled language artifacts. A user profile can load only the languages required for its context, while build systems produce and test heavier artifacts separately.

## Important limits

Multilingual capability depends on available lexicons, constructions, grammar resources and quality tests. A missing language resource must be exposed as a limitation; the system must not silently substitute unreviewed machine translation for a governed deterministic rendering.

## Sources

- [Semantik Architect](https://initkoa.org/technology/architect)
- [docs/02-system/13-language-system-boundary.md](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/02-system/13-language-system-boundary.md)
- [docs/06-lifecycle/09-language-artifacts.md](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/06-lifecycle/09-language-artifacts.md)
- [docs/contracts/subsystems/semantik-architect.subsystem.json](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/contracts/subsystems/semantik-architect.subsystem.json)
