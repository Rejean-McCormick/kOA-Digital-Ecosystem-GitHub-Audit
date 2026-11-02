<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/wiki/Errors-and-Troubleshooting | commit: f187a43fc9540ce7d443ff4d2ab26dfdc7a48bfe | SHA-256: b6acd245623938f162bc6122500644a0ac0d75c2d960a67eb628016976127355 -->

# Errors & Troubleshooting

SA fails closed on semantic, language and runtime correctness.

## Error envelope

```json
{
  "schema_version": "1.0",
  "code": "SA-LEX-002",
  "category": "LEXICAL_BINDING_FAILED",
  "stage": "lexical_binding",
  "message_safe": "...",
  "retryable": false,
  "request_id": "...",
  "runtime_set_id": "...",
  "details": {}
}
```

## Stable v1 codes

| Code | Meaning |
|---|---|
| `SA-REQ-001` | invalid request |
| `SA-SEM-001` | semantic content cannot be mapped |
| `SA-SEM-002` | obligation/semantic coverage failure |
| `SA-CON-001` | unsatisfiable presentation constraint |
| `SA-LANG-001` | language unavailable |
| `SA-LANG-002` | capability profile unavailable/not admitted |
| `SA-LANG-003` | language planning failed |
| `SA-LEX-001` | lexical knowledge missing/invalid |
| `SA-LEX-002` | exact lexical binding failed |
| `SA-GF-001` | SA↔GF contract/bridge incompatibility |
| `SA-GF-002` | GF realization failed |
| `SA-RUN-001` | RuntimeSet missing |
| `SA-RUN-002` | runtime integrity failed |
| `SA-RUN-003` | runtime not ready/ambiguous |
| `SA-ADP-001` | adapter contract failed |
| `SA-OPS-001` | deadline exceeded |
| `SA-OPS-002` | request cancelled |
| `SA-INT-001` | internal invariant broken |

## Common diagnosis path

### Language/profile unavailable

Check the capability manifest and release state. Production calls require `RELEASED`.

### Runtime integrity failed

Recompute/check artifact hashes. Do not patch a released runtime in place.

### Lexical binding failed

The semantic concept has no exact admitted lexical binding for the requested runtime/language. Fix the lexical artifact and release a new RuntimeSet.

### GF contract failure

The bridge does not support the selected operation or does not consume all semantic slots/features. Fix the bridge/grammar and reconform.

### Constraint unsatisfiable

The requested format/length cannot be honored without semantic loss. Change the request constraints; SA will not truncate required meaning silently.
