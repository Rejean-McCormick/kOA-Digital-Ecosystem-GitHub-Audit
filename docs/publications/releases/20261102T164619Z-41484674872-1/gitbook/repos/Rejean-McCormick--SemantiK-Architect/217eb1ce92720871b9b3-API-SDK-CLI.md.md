<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/wiki/API-SDK-CLI | commit: f187a43fc9540ce7d443ff4d2ab26dfdc7a48bfe | SHA-256: 7431de9f70faa6bb4afa55836d16d8be893de05e3e9391b0895c4c42d583dc4e -->

# API, SDK & CLI

SA exposes the same canonical use cases through multiple driving adapters.

## Core use cases

- `RenderCommunication`
- `ValidateRequest`
- `ListCapabilities`
- `ValidateRuntime`
- `ExplainGeneration`

## Python SDK

Conceptually:

```python
from semantik_architect import SemantikArchitect

sa = SemantikArchitect.from_runtime_root("runtime")

sa.validate_request(request)
sa.render(request)
sa.explain(request)
sa.capabilities()
sa.validate_runtime("runtime-set-id")
```

`render()` accepts either a canonical `CommunicationRequest` or its public mapping/JSON shape.

## CLI

```text
semantik-architect --runtime-root runtime validate-request request.json
semantik-architect --runtime-root runtime render request.json
semantik-architect --runtime-root runtime explain request.json
semantik-architect --runtime-root runtime capabilities
semantik-architect --runtime-root runtime validate-runtime <runtime-set-id>
semantik-architect --runtime-root runtime conformance suite.json
semantik-architect --runtime-root runtime serve --host 127.0.0.1 --port 8765
```

Use `-` instead of a request filename where supported to read JSON from standard input.

## Explain generation

`explain` is a diagnostic view of planning/runtime choices. It is **not** an epistemic authority and does not replace the original structured content.

## Stable errors

Application failures use a machine-readable error envelope with:

```text
code
category
stage
message_safe
retryable
request_id?
runtime_set_id?
details?
```

See [[Errors & Troubleshooting|Errors-and-Troubleshooting]].
