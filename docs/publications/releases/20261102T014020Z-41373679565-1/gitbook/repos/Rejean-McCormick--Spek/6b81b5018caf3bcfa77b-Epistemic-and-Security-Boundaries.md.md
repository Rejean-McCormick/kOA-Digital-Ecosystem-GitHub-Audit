<!-- Frozen source: https://github.com/Rejean-McCormick/Spek/wiki/Epistemic-and-Security-Boundaries | commit: 4eb78305f912b1e78e9caa5a9afd83b6a9e03253 | SHA-256: bd8464740d3ae4be4e9760c74d250c860e8db11f8bbc9ee6b9644d9033647178 -->

# Epistemic and Security Boundaries

## Distinctions that must remain separate

| Operation | Responsibility |
| --- | --- |
| Canonical state authoring | Kristal upstream authority, not Spek |
| Evidence and claim qualification | Scientific/Framework governance |
| Per-language sentence realization | SemantiK or reviewed supplier |
| Arketype profile selection | Upstream editorial / structure owner |
| GitHub Wiki Markdown composition | Spek optional Wiki renderer |
| Layout composition | Spek's typed slot compiler |
| Public disclosure consent | Authorized owner/release process |
| Pages deployment | Explicitly protected GitHub workflow |
| Kristal activation | Separate upstream activation controller |

## What the validator does

Spek checks mandatory slots, allowed unit kinds, evidence links, language availability, input status declarations, HTML/LaTeX escaping, build hashes and path integrity. Production preflight can check that a supplied state reference matches metadata in a supplied snapshot.

## What it does not do

No verification of JCS commitment from canonical source bytes, no scientific peer review, no detection of misinformation, no grammatical certification, no translation equivalence proof, no cryptographic signature authentication, no permission to disclose, and no C1/C2/C3/C4 release authorization. The demonstration article is fictional.

## Security hygiene

Never place raw private state dumps, credentials, unapproved research material, or PII in `published-site/`, reports, or public wiki pages. Protect the `public-pages` environment with required reviewers and minimal workflow permissions.

## Specific Wiki cautions

- An Arketype label or a successful Spek template verification never authorizes a claim or creates evidence.
- A SemantiK `qualified` field in `realizations.json` is not a cryptographic RuntimeSet attestation.
- Markdown Wiki drafts may contain identifying or confidential rendered text even if internal source IDs and locators are omitted. Human disclosure review remains necessary.
- The `kristal-public` collection, Spek's own software wiki, and the `kristal-public.wiki.git` publishing repository are **different locations**. Never push a private draft to any of them without separate review and approval.
