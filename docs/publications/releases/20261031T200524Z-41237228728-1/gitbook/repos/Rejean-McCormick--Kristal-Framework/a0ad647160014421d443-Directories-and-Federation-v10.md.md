<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Directories-and-Federation-v10 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 5d20cf2941d29eb9792b7b24da0cfbd4470468273c058d8c27b5ea64e381396e -->

# Directories & Federation — v10

Two artifacts serve fundamentally different purposes:

```text
private root node
├── directory.json             # mutable discovery / routing
└── v9 federation State Snapshot  # exact pinned child commitments
```

- **Directory:** Where is a node currently advertised? It may change after a rename/move without semantic revision.
- **Pinned federation:** Which exact external state commitment participates in the parent state? It changes only by an explicit logical state update.

```text
DIRECTORY != AUTHORITY
DISCOVERY != FEDERATION MEMBERSHIP
REFERENCE != OWNERSHIP TRANSFER
```

## Visibility

For mixed public/private networks, keep the full directory private. A public directory may advertise a deliberately filtered set of public nodes; it **must not** disclose confidential node locations without an explicit disclosure decision. Repository visibility alone is not a secrecy guarantee.

## Hierarchy & scaling

Directory entries may point at other directory nodes. Hierarchy is an operational navigation graph, not semantic containment. Large collection repositories can add a derived `kristals/index.json` navigation index for local members without becoming a normative federation directory.

See [[Nodes-and-Collections-v10]], [[GitHub-Read-Surfaces-v10]] and [[Security-and-Confidentiality-v10]].

*Normative source: Framework `spec/v10/Directories-and-Federation.md`.*
