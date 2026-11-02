<!-- Frozen source: https://github.com/Rejean-McCormick/Interaction-Kernel/blob/1d0598456fe8203625f9831ec00c32225422631d/docs/envelope.md | commit: 1d0598456fe8203625f9831ec00c32225422631d | SHA-256: 180e17f972afbbf8e847b555aa7374c03b1cf22c058c77114be34cf5b4feab67 -->

# Interaction Envelope

Normative schema: [`contracts/schemas/envelope.schema.json`](../contracts/schemas/envelope.schema.json).

Core fields include `specversion`, `id`, `class`, `time`, `profile`, `source`, `target`, `subject`, `operation`, `correlation_id`, `causation_id`, `idempotency_key`, `authority`, `data_schema`, `data`, `artifact_refs`, `governance`, `response`, `trace`, `evidence`, and `extensions`.

Durable Command/Query records require a concrete target before durable emission. Correlation, causation and technical trace are distinct.
