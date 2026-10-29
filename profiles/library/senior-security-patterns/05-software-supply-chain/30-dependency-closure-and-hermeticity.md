# SEC-30 — Dependency Closure and Hermeticity

## Core principle

Pinning top-level dependencies does not pin the build if resolvers can choose transitive versions, mutable indexes, build backends or system packages at build time. Reproducibility requires controlling the dependency closure.

## Security invariant

A production build should be able to prove the exact dependency graph and fetch only from approved, integrity-verified sources. Network access during release builds is minimized or mediated by trusted mirrors.

## Senior architecture

Use lock/constraint files with hashes where ecosystem supports them, internal mirrors or artifact proxies, pinned base image digests, isolated build environments and reproducible dependency resolution. Quarantine newly published packages when risk warrants it.

## Application to the supplied ecosystem

Konfid's constraints file reduces drift but its own docs correctly note that it is not artifact hashes or a package mirror. Promote this into an ecosystem build policy: hash-lock production dependencies, pin container bases by digest, and record dependency material in provenance.

## Failure modes / anti-patterns

- Version pins without hashes.
- Build downloads directly from public index during release.
- Base image tag floats.
- Build backend/plugins are unpinned.
- SBOM generated after resolver drift already occurred.

## Evidence that proves the control

Rebuilding same source under controlled inputs yields equivalent dependency graph/artifact. Provenance lists dependency materials. Build fails if dependency hash/source differs. Network policy shows only approved mirrors are reachable during trusted build stages.


## Reference anchors

- SLSA Specification v1.2: https://slsa.dev/spec/v1.2/
- NIST SP 800-218 SSDF 1.1 (final): https://csrc.nist.gov/pubs/sp/800/218/final
