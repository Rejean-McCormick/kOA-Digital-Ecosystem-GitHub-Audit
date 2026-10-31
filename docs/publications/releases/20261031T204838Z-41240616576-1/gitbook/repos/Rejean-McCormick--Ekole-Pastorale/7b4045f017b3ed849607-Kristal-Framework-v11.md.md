<!-- Frozen source: https://github.com/Rejean-McCormick/Ekole-Pastorale/wiki/Kristal-Framework-v11 | commit: 7c73b3852cf83a881cd83a14f345a78e163dc8c3 | SHA-256: 9d44aaa68ceec1ada0bfb89ea75da15420e7e89307a37db6a2012993eabc1190 -->

# Kristal Framework v11

Ekole Pastorale is organized around independently owned **Kristal** workspaces. The version declared in the supplied sample is **Kristal Framework 11.0.0-draft.3**. Do not confuse the framework's draft contract with the separate version numbers of Ekole Pastorale or Arketype.

## Why use Kristals?

A learning unit should be identifiable, reviewable, auditable, and projectable into different applications. The Ekole content pack is a *derived view*, not the intellectual home of everything it displays.

```text
Kristal workspace (canonical + registered semantic objects)
             │
             ├── validation: check-v11 / check
             ├── state build: build-v9
             ▼
     outils/projeter_ekole.py
             ▼
      Ekole content-pack/0.1
             ▼
         Ekole Core
```

## Identity and lexical separation

Framework v11 uses namespace-scoped semantic identities, including:

- **KQ:** a concept or entity;
- **KP:** a property or predicate;
- **KA:** an assertion;
- **KS:** a source or evidence reference.

A readable label is *not* a global identity. The same label in two Kristals does not prove those entities are the same. A historical `urn:kristal:catho:...` identifier is not automatically a v11 `KQ` identity.

## Anatomy of a course workspace

An instance such as `kristals/lire-bible/` includes:

```text
kristals/lire-bible/
├── kristal.workspace.json
├── canon/
│   └── domain/
│       ├── pedagogie/unite.json   # Canonical course source
│       └── v11/                  # Semantic graph, registry, mappings, lexicon
├── build/v9/                     # Built logical state and snapshot
├── sources/                      # Source records
├── docs/                         # Workspace design contract
└── tools/kristal.py              # Local Kristal CLI
```

The `v9` label refers to the **logical state commitment/build mechanism** used alongside the **v11** semantic structures. It does not mean this is a v9-only project.

## Minimum local workflow

```bash
python3 kristals/lire-bible/tools/kristal.py check-v11 kristals/lire-bible
python3 kristals/lire-bible/tools/kristal.py check kristals/lire-bible
python3 kristals/lire-bible/tools/kristal.py build-v9 kristals/lire-bible
```

Perform the build **only after** reviewing a real canonical change. The project refuses to project changed canonical content that no longer matches the recorded build state.

## Boundaries

- A course Kristal owns **learning design**; it need not own the primary text of Augustine or a biography of Francis.
- Witness Kristals own **structured documentation about persons, virtues, and sources**; they do not independently certify sainthood or miracles.
- The existing historical Catho repository is inventoried by exact hashes but has **not** been automatically converted into a trustworthy v11 crosswalk.
- Local checks establish **technical consistency**, not accuracy of every theological claim or ecclesial authorization.

For the specific profiles, continue to [Arketypes ARK-20 and ARK-21](Arketypes-ARK-20-and-ARK-21.md). For source changes, see [Authoring and Projection](Authoring-and-Projection.md).
