<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Version-Stack-v6-v7-v8-v9-v10-v11 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 9797f06582b2e5929c68e5d70cce9a1db6e71098e5f17606586adebba6b37d0c -->

# Version stack — v6 through v11

| Version | Capability added | Previous layer preserved? |
|---|---|---|
| **v6** | Portable epistemic state, provenance/assertions | Original form remains valid |
| **v7** | KQ/KP/KA/KS opaque semantic IDs, registries and mappings | Yes |
| **v8** | Language/lexical layers, exact query, read models | Yes |
| **v9** | Logical Artifacts, commitments, state snapshots and polymorphic storage | Yes |
| **v10** | Hosting nodes, publication, discovery, read surfaces | Yes |
| **v11 draft.4** | Strict canonical semantic identity, separated multilingual dictionary catalogs and Wikidata crosswalk + diK coverage/migration contracts | **Yes** (opt-in for new v11 canonical graphs) |

### Invariants across all layers

```text
IDENTITY != LABEL != EXTERNAL ID
LOGICAL COMMITMENT != PHYSICAL BLOB DIGEST
SEMANTIC STATE != HOST BINDING != DISCOVERY DIRECTORY
CANONICAL GRAPH != LEXICAL DICTIONARY != CROSSWALK
VALIDATION != DOMAIN TRUTH != PUBLICATION AUTHORITY
```

The versions have distinct machine formats and conformance profiles; this wiki does not pretend that a v6 word-based source *already conforms* to v11 canonical strict rules. An explicit migration can produce a new v11 revision **without deleting the old state**.

**Dive into:** [[Kristal-v11]] · [[Kristal-v10]] · [[Kristal-v9]] · [[Kristal-v8]].

**Draft.4 is an integration/tooling clarification**: its KQ/KP schema/TCK rules remain byte-identical to draft.3; this does not merge diK or Kit into Framework.
