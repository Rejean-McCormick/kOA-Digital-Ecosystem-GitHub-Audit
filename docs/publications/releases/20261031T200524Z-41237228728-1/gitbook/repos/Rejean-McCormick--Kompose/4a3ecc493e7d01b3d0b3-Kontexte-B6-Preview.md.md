<!-- Frozen source: https://github.com/Rejean-McCormick/Kompose/wiki/Kontexte-B6-Preview | commit: ec94ee500739b0078a14ee9cf67d34d46d2087e4 | SHA-256: f656cc6210063a7515421d12918118d586f69e4abb76ebad358067fc9c8912de -->

# Kontexte B6 — Non-Executable Bakery Scenario Preview

KOMPOSE can compile **explicitly synthetic** Kontexte `kontexte.mission/1` and `kontexte.role/1` source definitions into a local `kompose.kontexte-preview/1` plan. It does not create a Case/Task in Orgo, enroll students, send messages, grant fragment access, or grade a pupil.

## Run the bundled fixture

From the KOMPOSE source root:

```bash
PYTHONPATH=src python3 -m kompose.cli preview-kontexte \
  examples/kontexte-boulangerie/data/missions/boulangerie.json \
  examples/kontexte-boulangerie/data/roles
```

Windows PowerShell: set `$env:PYTHONPATH='src'` and run `py -m kompose.cli ...` with the same arguments.

### Optional flags

| Option | Result | Constraint |
|---|---|---|
| `--role ROLE_ID` | Restricted fictional role projection | No hidden clues or unrelated roles |
| `--absent-role ROLE_ID` | Proposed absence fallback | Teacher-level planning only; **no reassignment** |
| `--replay FILE` | Ordered replay of fictional Orgo receipts | Teacher-level output; rejects real or unreviewed receipts |
| `--out FILE` | Writes result JSON locally | Never sends a network request |
| `--target-course ID` | Annotates target course separately | **Does not remap** source curriculum IDs |

`--role` cannot be combined with `--absent-role` or `--replay`.

## Fixture and safety details

The bakery fixture has **3 roles, 3 dependent steps requiring human review, and 2 referenced fragments**. The source mission identifies `qc-pri-ma-006`; the default target option is `qc-pri-ma-008`, but the compiler does **not** silently equate them. A pedagogical reviewer must decide whether any mapping is acceptable.

The replay source must be `orgo_mock_fixture` with `synthetic: true`. Its sequence and duplicate event checks are **pure local** checks. Flags such as `human_reviewed` and `teacher_authorized` are fictional fixture claims; no Orgo receipt or teacher account has been verified. Fragment *identifiers* may be reported, not protected fragment contents.

**Sources:** `src/kompose/kontexte_preview.py`, `src/kompose/mission_replay.py`, `tests/test_kontexte_preview_b6.py`, `docs/b6/ARCHITECTURE.md`.

[[Home|← Home]] · [[Tandem-Orgo-Boundary|Who owns runtime?]] · [[Ekole-P1-Preview|P1 verifier →]]
