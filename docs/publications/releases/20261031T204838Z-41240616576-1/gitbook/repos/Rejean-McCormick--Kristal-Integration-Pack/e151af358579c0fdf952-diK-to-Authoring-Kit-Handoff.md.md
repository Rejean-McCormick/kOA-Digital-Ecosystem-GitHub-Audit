<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Integration-Pack/wiki/diK-to-Authoring-Kit-Handoff | commit: 949de422daed28c0b84684b509e675807ac9c48b | SHA-256: 782d602b87429dc3bf5da6b97c589b9bbdabfb69a9af4210570dabc2051caf9b -->

# diK → Authoring Kit: Read-only Handoff

`tools/v11_handoff.py` is an optional preflight for incoming diK dictionary artifacts. **It does not import, register, select, activate, publish, or migrate anything.** It calls the pinned Framework draft.4 `tools/v11/interop_preflight.py` and rejects an unexpected result profile or input digests.

## Mode 1: inspect an existing v11 catalog

```bash
FW=/path/to/Kristal-Framework-v11.0.0-draft.4
S="$FW/examples/v11"
python tools/v11_handoff.py \
  --framework "$FW" \
  --catalog "$S/dictionaries/catalog.json" \
  --registry "$S/identity-registry.example.json" \
  --crosswalk "$S/external-crosswalk.example.json" \
  --graph "$S/semantic-graph.example.json" \
  --locales fr-CA,en
```

`--locales` requires `--graph`. Without either, the preflight can focus on catalog and identity metadata without computing graph coverage.

## Mode 2: review an incoming diK alpha.7 snapshot

Use the unmodified `catalog.json` and `dik-job.json` **inside the same content-addressed snapshot directory**, with registry and crosswalk inputs matching the job receipt:

```bash
python tools/v11_handoff.py \
  --framework "$FW" \
  --catalog /snapshots/KEY/catalog.json \
  --registry /workspace/identity-registry.json \
  --crosswalk /workspace/external-crosswalk.json \
  --kit-import-candidate \
  --dik-job /snapshots/KEY/dik-job.json \
  --out ./preflight.json
```

`--kit-import-candidate` requires incoming dictionary layers of kind `wikidata` only. The optional receipt check binds the catalog and inputs to a specific diK alpha.7 import; this is **not** proof that a human has approved the source data or match.

Node equivalent:

```bash
node tools/kristal-bridge.mjs v11-handoff \
  --framework "$FW" --catalog /snapshots/KEY/catalog.json \
  --registry /workspace/identity-registry.json \
  --crosswalk /workspace/external-crosswalk.json \
  --kit-candidate yes --dik-job /snapshots/KEY/dik-job.json
```

**Node uses `--kit-candidate yes`; Python uses `--kit-import-candidate`.** Do not interchange the flags.

## Mode 3: only after separate review, use the Kit

In the **Authoring Kit** repository, not in this Pack:

```bash
python tools/kristal.py import-dik-catalog /workspace \
  --catalog /snapshots/KEY/catalog.json \
  --revision reviewed-001 --register \
  --artifact-id urn:reviewed:dictionary:001 \
  --contract-id project.dictionary.v11

# Use the returned catalog revision path after checking the result:
python tools/kristal.py select-v11-catalog /workspace \
  --catalog /path/returned/from/import
python tools/kristal.py check-v11 /workspace
```

The Authoring Kit owns state registration, catalog selection and recovery (`recover-v11`). A `preflight_pass` response is **not** a selection decision.

See [[diK-Alpha7-Receipts]], [[Architecture-and-Ownership]] and [[Qualification-and-Testing]].
