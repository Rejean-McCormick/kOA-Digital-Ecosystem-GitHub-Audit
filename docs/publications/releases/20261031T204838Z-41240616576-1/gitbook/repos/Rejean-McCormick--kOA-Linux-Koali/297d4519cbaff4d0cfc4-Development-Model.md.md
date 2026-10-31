<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Linux-Koali/wiki/Development-Model | commit: a014d6b410b475fe227e3f0153bbae6e54ef0520 | SHA-256: 2c289d145f037fd4b1ea4c305886dab879e21baa47af99fc652f7f08c67686ec -->

<!-- Navigational projection. Normative authority remains in the repository docs/ corpus. -->

# Development Model

> **Authority notice:** This wiki is a readable navigation layer. Source contracts, accepted ADRs, normative documents, and executable validators in the repository remain authoritative.

## Workspace isolation

A development workspace is the isolation unit for one application, branch, or worktree. Each workspace receives its own identity, mutable dependency environment, service state, ports, secrets, databases, volumes, and resource budget.

Shared content-addressed download and build caches may be reused. Mutable installed environments and runtime state are not shared.

## Python toolchain

UV is the declared Python dependency and environment manager. Workspaces use versioned `pyproject.toml` and `uv.lock` files with a workspace-local virtual environment.

## Service isolation

- rootless service containers where applicable;
- workspace-specific networks, sockets, volumes, and databases;
- explicit port allocation;
- no shared mutable secrets or application state;
- bounded CPU, memory, I/O, queues, and concurrency.

## Publication boundary

Development output is a candidate until it passes build, test, schema, provenance, evidence, and release admission controls. A local workspace cannot directly activate a production artifact.

## Sources

- [`docs/05-development/00-development-model.md`](../blob/main/docs/05-development/00-development-model.md)
- [`docs/05-development/02-workspace-identity.md`](../blob/main/docs/05-development/02-workspace-identity.md)
- [`docs/05-development/03-workspace-isolation.md`](../blob/main/docs/05-development/03-workspace-isolation.md)
- [`docs/05-development/04-dependency-isolation.md`](../blob/main/docs/05-development/04-dependency-isolation.md)
- [`docs/05-development/05-python-uv.md`](../blob/main/docs/05-development/05-python-uv.md)
- [`docs/05-development/06-service-containers.md`](../blob/main/docs/05-development/06-service-containers.md)
- [`docs/05-development/07-ports-networks-and-sockets.md`](../blob/main/docs/05-development/07-ports-networks-and-sockets.md)
- [`docs/05-development/08-volumes-and-persistent-data.md`](../blob/main/docs/05-development/08-volumes-and-persistent-data.md)
- [`docs/05-development/09-secrets-and-local-identities.md`](../blob/main/docs/05-development/09-secrets-and-local-identities.md)
- [`docs/05-development/14-build-test-and-validation.md`](../blob/main/docs/05-development/14-build-test-and-validation.md)
- [`docs/05-development/15-artifact-publication.md`](../blob/main/docs/05-development/15-artifact-publication.md)
- [`docs/contracts/toolchains/python-uv.toolchain.json`](../blob/main/docs/contracts/toolchains/python-uv.toolchain.json)
