<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/wiki/HTTP-API | commit: f187a43fc9540ce7d443ff4d2ab26dfdc7a48bfe | SHA-256: 12b0fe8650da0a8dd86ed51dc623ea1fe6c0c511d45b4bdc0f68cf3066106f98 -->

# HTTP API

The built-in HTTP surface is intentionally minimal. It is a transport adapter over the same application use cases used by the SDK and CLI.

## Endpoints

### `GET /health`

Process liveness.

### `GET /ready`

Runtime readiness. A deployment is ready when at least one configured RuntimeSet validates successfully.

### `GET /v1/capabilities`

Lists available RuntimeSets/language-profile capability data.

### `POST /v1/validate-request`

Validates a canonical request without performing grammatical realization.

### `POST /v1/explain`

Returns planning/runtime diagnostics.

### `POST /v1/render`

Executes the canonical semantic-to-language pipeline.

## Error behavior

Semantic/application failures are returned as the stable SA error envelope. Malformed transport/input errors are mapped to `SA-REQ-001`.

## Production note

The built-in server is a thin reference transport. Production deployment may place SA behind another service host or gateway as long as the canonical application contracts remain unchanged.
