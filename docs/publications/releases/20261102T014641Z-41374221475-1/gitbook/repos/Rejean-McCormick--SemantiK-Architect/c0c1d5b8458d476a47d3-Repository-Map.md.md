<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/wiki/Repository-Map | commit: f187a43fc9540ce7d443ff4d2ab26dfdc7a48bfe | SHA-256: 0f0fef2f91d49fd96d03ae8567c224b5ae1596c7e02d276e4b228fd54fe8475b -->

# Repository Map

The implementation follows the locked dependency structure.

```text
semantik-architect/
├── src/semantik_architect/
│   ├── domain/
│   │   ├── semantics/
│   │   ├── communication/
│   │   ├── language/
│   │   └── errors.py
│   ├── application/
│   │   ├── ports/
│   │   ├── planning/
│   │   ├── validation/
│   │   └── use_cases/
│   ├── adapters/
│   │   ├── inbound/
│   │   │   ├── python_sdk/
│   │   │   ├── cli/
│   │   │   └── http/
│   │   ├── ecosystem/
│   │   ├── lexical/
│   │   ├── realization/gf/
│   │   ├── runtime/filesystem/
│   │   ├── locale/
│   │   └── output/
│   ├── conformance/
│   ├── bootstrap/
│   └── observability/
├── schemas/
├── tests/
├── tools/
├── docs/
└── runtime/
```

## Import direction

- `domain` is framework-independent;
- `application` depends on domain + port abstractions;
- adapters depend inward on application/domain contracts;
- PGF imports stay under the GF realization adapter;
- HTTP details stay under inbound HTTP;
- ecosystem adapters do not import one another.

## Where to change what

| Need | Location |
|---|---|
| new semantic structure | domain + schema + ADR/lock |
| new application orchestration | application/use_cases |
| new product integration | adapters/ecosystem |
| new lexical source | adapters/lexical behind port |
| new realizer backend | adapter behind `RealizerPort` |
| new language | external GF/runtime artifacts, not core branch |
| new output projection | adapters/output |
