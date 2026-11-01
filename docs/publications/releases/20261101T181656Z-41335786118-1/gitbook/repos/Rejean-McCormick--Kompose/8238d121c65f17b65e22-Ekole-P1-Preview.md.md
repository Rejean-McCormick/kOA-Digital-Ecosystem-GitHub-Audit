<!-- Frozen source: https://github.com/Rejean-McCormick/Kompose/wiki/Ekole-P1-Preview | commit: ec94ee500739b0078a14ee9cf67d34d46d2087e4 | SHA-256: 6366b71ce01a60540b509d448393e25cdc5ca9836db7561c10f356eeef7c6ac2 -->

# Ekole Tandem P1 — Synthetic Teacher Preview Gate

KOMPOSE provides a **local, read-only JSON verifier**, not an Ekole server, Orgo client, permission check, or classroom workflow. The accepted format is exactly `ekole.tandem-teacher-preview/1.0` with `mode: synthetic` and `authority: orgo`.

## Verify the included fixture

```bash
PYTHONPATH=src python3 -m kompose.cli verify-ekole-preview \
  examples/integrations/ekole-fete-sorciere.synthetic.json
```

On Windows PowerShell, use `$env:PYTHONPATH='src'` followed by `py -m kompose.cli ...`.

The bundled synthetic input contains **11 tasks**, but none of them is an authenticated Orgo task. Valid output includes:

```json
{
  "format": "ekole.tandem-teacher-preview/1.0",
  "valid": true,
  "task_count": 11,
  "authority": "orgo",
  "mode": "synthetic",
  "runtime_admitted": false,
  "permissions_verified": false,
  "world_release_verified": false
}
```

## What is checked

- Required top-level keys and exact task keys; no extra fields (for example no names, marks, tokens, photos, or protected fragment bodies).
- Canonical nonzero UUID representation for tenant, World, and WorldRelease identifiers **only as syntax**.
- Allowed task states (`ready`, `waiting`, `in_progress`, `done`, `blocked`); unique valid references; 1–50 tasks; up to 8 unique fragment *references* per task.
- Local file size **at most 128 KiB**, strict UTF-8, no symlink, no duplicate JSON keys (including nested objects).

## What is NOT checked

No school identity, logged-in teacher, real tenant membership, permission, signed release, workflow existence, network request, fragment authorization, operational admission, or learning competency is verified. A syntactically acceptable `authority: orgo` label is **not** a token issued by Orgo.

**Sources:** `src/kompose/tandem_handoff.py`, `tests/test_tandem_ekole_handoff.py`, `docs/TANDEM_P1_ORGO_EKOLE_ALIGNMENT.md`, ADR 0008.

[[Home|← Home]] · [[Tandem-Orgo-Boundary|Operational authority]] · [[Project-Status|Status →]]
