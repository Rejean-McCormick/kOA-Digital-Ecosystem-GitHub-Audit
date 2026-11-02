<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/wiki/Operations-and-Release | commit: f187a43fc9540ce7d443ff4d2ab26dfdc7a48bfe | SHA-256: 7cc7598f4e8ec92b3af647d8fc91428b8a0adec5a8067bf0ba88fb925bb95030 -->

# Operations & Release

## Repository validation

The repository includes validation tooling for:

- Python compilation;
- test suite execution;
- JSON Schema validation;
- architecture boundaries;
- contract/integration/failure-path tests.

## Build a RuntimeSet manifest

A release helper can construct a manifest from artifact paths, calculate SHA-256 hashes and pin capability/conformance artifacts.

The release process must never edit an already released artifact in place.

## Runtime validation

`validate-runtime` checks, among other things:

- artifact presence;
- hashes;
- SA version compatibility;
- bridge contract version;
- capability manifest identity;
- capability profile artifacts;
- conformance evidence;
- grammar/bridge completeness for released profiles.

## Activation

`activation.json` resolves ambiguity when several released RuntimeSets serve the same language/profile.

Example shape:

```json
{
  "schema_version": "1.0",
  "bindings": {
    "sq|sa-core-1": "runtime:sq:2026-09"
  }
}
```

## Health model

- **liveness**: process/event loop is alive;
- **readiness**: at least one configured RuntimeSet is integrity-valid and usable.

Optional telemetry failures do not make semantic generation succeed incorrectly or alter output.

## Rollback

Rollback is activation of a previous immutable known-good RuntimeSet/application version, not an in-place repair of the released files.
