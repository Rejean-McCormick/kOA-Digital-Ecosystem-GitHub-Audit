<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/wiki/Development-Guardrails | commit: f187a43fc9540ce7d443ff4d2ab26dfdc7a48bfe | SHA-256: ccdd5d3f2e889cf66d9748c8bc5da93d03c46ec2fb8f75854a07fbcdb840d5d1 -->

# Development Guardrails

These rules keep implementation work aligned with the architecture, including AI-assisted work.

## Mandatory

- preserve the dependency direction `adapters → application → domain`;
- preserve every communication obligation;
- keep PGF/GF types inside the GF adapter;
- keep product-specific models behind ACLs;
- keep language-specific behavior out of shared core branches;
- pin realization to immutable RuntimeSet identity;
- add/update tests when contracts change;
- change public/locked contracts explicitly and version them.

## Do not

- add a language-specific `if language == ...` branch to shared core;
- add a silent fallback language;
- add a template grammar to hide a GF gap;
- guess a missing lexeme in the deterministic production path;
- silently drop content to satisfy a style/length constraint;
- turn supporting metadata into a new factual obligation;
- make a remote service mandatory for canonical rendering;
- introduce distributed architecture patterns without a concrete requirement.

## Ambiguity rule

When the architecture does not resolve a choice, prefer the smallest implementation that preserves all existing contracts. Do not invent a new architectural layer solely to make one local change easier.
