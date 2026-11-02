<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Integration-Pack/wiki/Legacy-Kompiler-Bridge | commit: 949de422daed28c0b84684b509e675807ac9c48b | SHA-256: ae1eae4b20c85c6d77929cecfe0a8696aa31dd43ed6739d9c9fa65595e86b178 -->

# Legacy Kompiler Bridge

This separate compatibility path uses a **local Kompiler HTTP server**. It is not equivalent to reading or validating a v11 semantic graph.

## Run the bridge CLI

With an operator-controlled local Kompiler service (for example `http://127.0.0.1:7788`):

```bash
export KOMPILER_URL=http://127.0.0.1:7788
node tools/kristal-bridge.mjs doctor
node tools/kristal-bridge.mjs run \
  --query examples/kristall-surface.query.json \
  --out ./results/context-pack.json
node tools/kristal-bridge.mjs project \
  --pack ./results/context-pack.json \
  --out ./results/projection
```

`doctor` reports the service's **real supported target IDs**; do not assume that a query example will be available. `run` validates the query plan before execution and writes a new Context Pack. `project` requests `POST /v1/projections/v6` only when an appropriate v7 Surface can be materialized. If it cannot, the projection fails rather than inventing missing semantics.

## Data and provenance

A successful `project` creates a new output directory with:

- `kristal-projection-v6.json` — derived state.
- `konstellation-backend.json` — reader configuration with source hash.
- `bridge-receipt.json` — source Context Pack ID, hashes and source state refs.

A Context Pack or projection may omit source material. Inspect its source and coverage metadata; do not treat a projection as a new logical or state commitment.

## Network restrictions

The CLI allows **loopback HTTP only**, no embedded URL credentials, a bounded response (8 MB), timeouts, no redirects and a strict endpoint allowlist. Where supported, an upstream token is supplied via `KOMPILER_TOKEN`, not included in repository docs or configuration files.

## Historical evidence

A local Kompiler `0.8.0-alpha.1` / Framework `10.0.0-draft.3.1` C5 test is retained as **historical evidence**. A new full Konstellation app/browser qualification has not been performed for this Pack release.

See [[Konstellation-Overlay]], [[Security-and-Trust-Boundaries]], and [[Qualification-and-Testing]].
