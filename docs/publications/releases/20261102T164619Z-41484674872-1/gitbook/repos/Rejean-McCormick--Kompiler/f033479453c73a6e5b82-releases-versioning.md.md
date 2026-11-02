<!-- Frozen source: https://github.com/Rejean-McCormick/Kompiler/blob/cf4836ccf2741b609c562254d09ba47d7e9a6187/docs/06-operations/releases-versioning.md | commit: cf4836ccf2741b609c562254d09ba47d7e9a6187 | SHA-256: 5fe1048065e8f38c721f50e8b9a7ff6e6020ddbb86d7f4ce762ae79480374659 -->

# Releases and Versioning

## Version domains

Kompiler versions four things separately:

1. application/runtime version;
2. protocol versions;
3. adapter versions;
4. compilation/ranking policy versions.

These MUST NOT be conflated.

## Semantic versioning

Runtime and adapters use SemVer.

Protocol identifiers carry a major/minor form such as `1.0`. Breaking wire/semantic changes require a major change.

## Breaking changes

Examples:

- renaming an operation ID;
- changing parameter meaning;
- changing a normalized field's semantics;
- changing default conflict handling;
- changing a deterministic ordering rule;
- changing the hash target.

## Additive changes

Examples that MAY be minor:

- new optional capability;
- new optional Context Pack field under a defined extension point;
- new adapter target;
- new error detail field.

## Release artifacts

A release SHOULD ship:

- package/wheel;
- lockfile or reproducible dependency metadata;
- protocol JSON Schemas;
- conformance vectors;
- changelog;
- migration notes for breaking changes.

## Compatibility gate

CI MUST run golden protocol vectors against every supported protocol major version before release.
