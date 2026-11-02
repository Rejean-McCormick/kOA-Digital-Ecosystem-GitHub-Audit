<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Integration-Pack/wiki/Prerequisites-and-Pinning | commit: 949de422daed28c0b84684b509e675807ac9c48b | SHA-256: 5403bdad35a318f07121a424cee69f83f664e3e394bce256c9758ed7e2ac4c57 -->

# Prerequisites and Framework Pinning

## Required tools

- Python 3.11+ with the Framework's `jsonschema` runtime dependency.
- Node.js 22+ for the stand-alone CLI; use Node 24.15+ when reproducing the historical Konstellation release environment.
- Exact local Framework `11.0.0-draft.4` for v11 checks and handoff.
- Optional Kompiler service for **legacy** commands only, reachable on a local loopback interface.

## What the v11 pin protects

`contracts/v11-framework-pin.json` specifies the profile `kristal-integration-framework-pin/v11.0-draft.4`, exact Framework version and SHA-256 of **13** consumed files: `VERSION`, eight v11 schema files and four v11 Python tool files. The list includes `tools/v11/interop_preflight.py`.

Before importing or running Framework validators, `tools/v11_integration.py` checks the exact version and content hashes. A different Framework checkout is a **review requirement**, not a reason to force execution.

```bash
python tools/v11_integration.py check \
  --framework /absolute/path/to/Kristal-Framework-v11.0.0-draft.4 \
  --registry /path/registry.json --graph /path/graph.json \
  --crosswalk /path/crosswalk.json --catalog /path/catalog.json
```

For historical **Kompiler v10** live tests, `contracts/contract-set.json` is a different source with a different trust model. Its SHA-256 must be obtained and approved independently for the actual Framework checkout; do **not** copy a digest from an old C5 report as a universal production value.

## Files deliberately not bundled

- Framework checkout and upstream executable dependencies.
- Authoring Kit and diK runnable distributions.
- Real Wikidata snapshots, secrets, local Kristal collections, and production Reader Policies.

See [[Verification-and-Release]] and [[Security-and-Trust-Boundaries]].
