<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Nodes-and-Collections-v10 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: a433a5fa6f6112a7e648a8218d7a9d5373666c0e168f7284cb8551edff8d7886 -->

# Nodes & Collections — v10

A **Kristal node** is an operational endpoint with a stable `node_id`, described by `kristal_node_manifest`. It can expose one or more states and related services. A hosting repository is an operational boundary, not automatically a single Kristal.

## Node roles

- `collection`: one or many related independent Kristal states.
- `directory`: advertises nodes and their host locations.
- `publisher`: publishes immutable state representations.
- `gateway`: exposes read/query access without necessarily owning the state.

A node may have several roles. A collection boundary reflects ownership, confidentiality, lifecycle or scale, and **does not merge semantic authority**.

## Reference GitHub layout

```text
account or organization
├── private root directory (recommended for mixed visibility)
├── public collection repository
│   └── kristals/<slug>/
└── private collection repository
    └── kristals/<slug>/
```

Use a new collection repository when permissions, governance, retention or publication lifecycle actually diverge. Many small Kristals can coexist in one repository with independent State Snapshots.

See [[GitHub-Reference-Profile-v10]], [[GitHub-Read-Surfaces-v10]] and [[Directories-and-Federation-v10]].

*Normative source: Framework `spec/v10/Nodes-and-Collections.md`.*
