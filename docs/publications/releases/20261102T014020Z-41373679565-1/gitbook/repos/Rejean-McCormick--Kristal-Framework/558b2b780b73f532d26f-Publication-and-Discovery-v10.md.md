<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Publication-and-Discovery-v10 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: dc186aa3c1fec7140861ea316f727b43f56f6ebffc13519c946f5fef6b584f87 -->

# Publication & Discovery — v10

V10 separates an exact semantic state from the operational facts of its publication and discovery.

## Verifiable Publication Record

A `kristal_publication` binds an exact v9 `state_ref` and State Commitment to a host binding, publication identity and retrievable bytes. For the baseline, each `resources[]` entry includes **role, locator, media type, exact byte size and SHA-256 blob digest**.

The reference non-normative bundle tool format `kristal.publication-bundle/1.0` contains, at minimum in the managed GitHub publication path:

```text
state-snapshot.json
bundle-manifest.json
publication.json
```

Before finalizing publication, validate the local bundle and verify the remotely downloaded bytes. A retry is idempotent **only** if the existing Publication Record and verified bundle are identical; otherwise report a conflict.

## Lifecycle

```text
BUILD → QUALIFY/VALIDATE → PUBLISH immutable bytes → optionally ACTIVATE
```

Publication is not activation. A GitHub Release may be the publication location; an Environment/deployment or other selected pointer may serve the activation plane when configured. A best-effort Environment is **not** a required approval gate.

## Discovery and exact federation

A `kristal_directory` is a **mutable** locator. It may advertise nodes, bindings and channels; it is not authoritative knowledge and omission is not negation. Exact federation uses pinned v9 `State Snapshot.references[]`.

See [[Directories-and-Federation-v10]], [[Workflow-GitHub-v10]] and [[Conformance-v10]].

*Normative source: Framework `spec/v10/Publication-and-Discovery.md`.*
