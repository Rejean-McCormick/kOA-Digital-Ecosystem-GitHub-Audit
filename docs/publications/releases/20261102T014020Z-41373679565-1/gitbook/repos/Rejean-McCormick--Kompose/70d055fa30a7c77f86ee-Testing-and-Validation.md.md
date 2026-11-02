<!-- Frozen source: https://github.com/Rejean-McCormick/Kompose/wiki/Testing-and-Validation | commit: ec94ee500739b0078a14ee9cf67d34d46d2087e4 | SHA-256: 3246831e2f8ad6c550482b73b39aa0f0a95d715f8da8081331296b367936db0e -->

# Testing — What Has Actually Been Checked

The `0.2.0` source includes Python unit tests for local demonstration rules and additional B6/P1 safety gates. **Passing local tests does not make KOMPOSE production-ready or authorize real Orgo operations.**

## Reproduce the checks

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
PYTHONPATH=src python3 -m kompose.cli validate examples/capsule-rivieres
PYTHONPATH=src python3 -m kompose.cli demo-flow examples/capsule-rivieres
PYTHONPATH=src python3 -m kompose.cli preview-kontexte examples/kontexte-boulangerie/data/missions/boulangerie.json examples/kontexte-boulangerie/data/roles
PYTHONPATH=src python3 -m kompose.cli verify-ekole-preview examples/integrations/ekole-fete-sorciere.synthetic.json
```

Set `$env:PYTHONPATH='src'` first for PowerShell and invoke `py -m ...`. Optional schema check dependencies: `python3 -m pip install -e '.[dev]'`.

## Verified classes of behavior

- Reference capsule cross-references, source/publication safeguards, non-generative Kristal reader and prompts.
- Example Entry Door preconditions, simulated lifecycle, phase and mission dependencies, controlled transfer proposals.
- B6 Kontexte synthetic-only preview, no silent curriculum remapping, restricted role views, cycle checks and non-executable output.
- Synthetic Orgo receipt replay guards: sequencing, duplicate handling, human-review fixture assertions, no protected fragment leakage.
- Ekole P1 file gate: exact JSON shape, synthetic mode, unknown/secret field rejection, canonical UUID syntax, duplicate JSON key rejection, valid task IDs/states, file-size/UTF-8/symlink restrictions.
- English wiki navigation/link tests **only when the separate wiki checkout exists**.

## Explicit gaps

- No authenticated teacher, school SSO, operational Orgo/Worlds instance, permission decision, real dispatch or network fallback.
- No full role-allocation solver, psychometric assessment validation, audited learner records, or certified educational content.
- A fixture's `teacher_authorized` or `authority: orgo` field is **not independent evidence**.
- If the wiki checkout is absent, wiki tests are **skipped**; do not count skipped checks as passing checks.

[[Home|← Home]] · [[Project-Status|Status]] · [[Ekole-P1-Preview|P1 security gate →]]
