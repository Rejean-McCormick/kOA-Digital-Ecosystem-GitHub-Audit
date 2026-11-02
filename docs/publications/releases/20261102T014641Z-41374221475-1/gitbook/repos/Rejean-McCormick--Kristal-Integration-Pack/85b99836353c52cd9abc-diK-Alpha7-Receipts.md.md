<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Integration-Pack/wiki/diK-Alpha7-Receipts | commit: 949de422daed28c0b84684b509e675807ac9c48b | SHA-256: a42ecbf23ca2107df2c14e8c61b7154a18964d24fe45bfd6e91e870d6b5f6844 -->

# Checking diK Alpha.7 Import Receipts

When supplied with `--dik-job`, the handoff checks the actual `dik-job.json` profile **`dik.large-import/1.0-candidate`**. The receipt is expected next to `catalog.json` in the **content-addressed** publication directory.

## Fields inspected

`tools/v11_handoff.py` compares:

1. Receipt profile and catalog SHA-256.
2. Registry and crosswalk SHA-256 from `source_pins` against the files being reviewed.
3. Namespace, language list and source snapshot against the catalog.
4. The advertised transformation `wikidata-large-import-1.0.0-alpha.7` and 64-character source dump digest.
5. The `upstream_verified` flag in the receipt and source pins.
6. The SHA-256 idempotency key, recomputed from `source_pins`, including the requirement that the enclosing snapshot directory is named after that key.

The Framework preflight independently checks catalog and layer structure. **Passing both checks is still only a reader-side preflight.**

## What a receipt does not establish

- The original dump file's current availability or complete content: the handoff reads the receipt and catalog, not the raw dump.
- The authenticity of Wikidata sources: a file hash can ensure consistency without proving provenance.
- An approved Wikidata `exactMatch` that has not been separately reviewed and recorded.
- Human authorization to import, activate or publish.
- Full-scale import performance or recovery after power loss.

`--dik-job` **requires** `--kit-import-candidate`; otherwise the tool refuses the operation. Outputs written with `--out` must not preexist.

See [[diK-to-Authoring-Kit-Handoff]], [[Dictionary-and-Wikidata-Rules]], and [[Security-and-Trust-Boundaries]].
