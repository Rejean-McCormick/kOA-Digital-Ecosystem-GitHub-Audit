<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Integration-Pack/wiki/Getting-Started | commit: 949de422daed28c0b84684b509e675807ac9c48b | SHA-256: f054f2dadacd835b17ad089acf21cf1dca4633a9d8f0afe7a9cf7d520e1760fc -->

# Getting Started

Use this guide from the **root of the extracted Kristal Integration Pack 0.3.0-alpha.1**. Examples use Bash and a separately checked-out Framework; adjust paths for your operating system.

## Prerequisites

- Python 3.11+ and the Framework's `jsonschema` dependency for v11 tools.
- An **exact** Kristal Framework `11.0.0-draft.4` checkout, with its `VERSION`, schemas and tools intact.
- Node.js 22+ for the standalone bridge; the historical Konstellation release environment calls for **Node 24.15+**.
- For the legacy Kompiler commands only: an authorized, local Kompiler service. No network is required for the v11 path.

The Pack **does not install or vend** Framework, diK or the Authoring Kit. An incompatible Framework checkout is refused, even when its API looks similar.

## First read-only check

```bash
FW=/absolute/path/to/Kristal-Framework-v11.0.0-draft.4
S="$FW/examples/v11"

python tools/v11_integration.py check \
  --framework "$FW" \
  --registry "$S/identity-registry.example.json" \
  --graph "$S/semantic-graph.example.json" \
  --crosswalk "$S/external-crosswalk.example.json" \
  --catalog "$S/dictionaries/catalog.json"
```

`check` validates the graph, identities, crosswalk, catalog and lexical layers by calling the **pinned Framework scripts**. It reads inputs only; it never changes the canonical graph.

## Optional coverage and presentation

```bash
python tools/v11_integration.py coverage \
  --framework "$FW" --registry "$S/identity-registry.example.json" \
  --graph "$S/semantic-graph.example.json" \
  --crosswalk "$S/external-crosswalk.example.json" \
  --catalog "$S/dictionaries/catalog.json" \
  --locales fr-CA,en --out ./coverage.json

python tools/v11_integration.py view \
  --framework "$FW" --registry "$S/identity-registry.example.json" \
  --graph "$S/semantic-graph.example.json" \
  --crosswalk "$S/external-crosswalk.example.json" \
  --catalog "$S/dictionaries/catalog.json" \
  --locale fr-CA --out ./view-fr-CA.json
```

**Important:** `--out` creates a *new* file; it does not overwrite an existing file. `direct`, `fallback`, and `missing` are different coverage results, not interchangeable translation statuses.

## Next steps

- [[Framework-v11-Reader]] for CLI semantics.
- [[diK-to-Authoring-Kit-Handoff]] to review an incoming dictionary catalog.
- [[Security-and-Trust-Boundaries]] before using the legacy HTTP bridge.
- [[Verification-and-Release]] to verify the delivered files.
