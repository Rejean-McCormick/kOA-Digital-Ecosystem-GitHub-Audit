<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Integration-Pack/wiki/Framework-v11-Reader | commit: 949de422daed28c0b84684b509e675807ac9c48b | SHA-256: 5e26ea2546db42f946fc6496c11043d8d372d402b4819812e0b9545d8520f338 -->

# Framework v11 Reader

`tools/v11_integration.py` is the authoritative **reader-side interface** in this Pack. It loads the **verified** Framework `11.0.0-draft.4` Python validators; it is not a replacement validator.

## Commands

| Operation | Inputs | Output | Effect |
| --- | --- | --- | --- |
| `check` | Framework, registry, graph, crosswalk, catalog | `kristal.integration.v11-check/v1` | Validates input structure and dictionary audit |
| `coverage` | Same, optional `--locales fr-CA,en` | Framework `kristal_dik_coverage_report` | Counts direct, fallback and missing lexical coverage |
| `view` | Same, required `--locale fr-CA` | `kristal.integration.read-view/v11.0-draft.1` | Produces a **derived**, non-canonical reading view |

All four semantic input files are required for this tool. A `catalog.json` may refer to lexical JSONL layers, which must stay available beside it at their declared relative paths.

## Bash example

```bash
FW=/path/to/Kristal-Framework-v11.0.0-draft.4
S="$FW/examples/v11"
ARGS=(--framework "$FW" --registry "$S/identity-registry.example.json" \
  --graph "$S/semantic-graph.example.json" \
  --crosswalk "$S/external-crosswalk.example.json" \
  --catalog "$S/dictionaries/catalog.json")

python tools/v11_integration.py check "${ARGS[@]}"
python tools/v11_integration.py coverage "${ARGS[@]}" --locales fr-CA,en
python tools/v11_integration.py view "${ARGS[@]}" --locale fr-CA --out ./view.json
```

For Node, the equivalent entry point is `node tools/kristal-bridge.mjs v11 --operation check|coverage|view ...` with the same named input options. See [[CLI-Reference]].

## Failure and non-overwrite behavior

- An unexpected Framework version or changed pinned file **fails closed**.
- An invalid namespace, mismatched identities or modified lexical-layer digest **fails validation**.
- The tool does not use a label or Wikidata Q/P as a substitute for KQ/KP.
- An existing `--out` destination is not overwritten.
- The derived view is **not** a signed commitment, semantic migration, publish action or license to serve data beyond the user's authorized scope.

See [[Derived-Views-and-Coverage]] and [[Dictionary-and-Wikidata-Rules]].
