<!-- Frozen source: https://github.com/Rejean-McCormick/Kompose/wiki/Quick-Start | commit: ec94ee500739b0078a14ee9cf67d34d46d2087e4 | SHA-256: 45200c7b7195dd46c36706e54b0f184dda6c24631db608da4391d84b404fcdac -->

# Quick Start — Local Examples Only

**Requirements:** Python 3.10+, the KOMPOSE source checkout. There is no web server and no live Orgo integration in this package.

## Test and validate the reference capsule

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
PYTHONPATH=src python3 -m kompose.cli validate examples/capsule-rivieres
PYTHONPATH=src python3 -m kompose.cli demo-flow examples/capsule-rivieres
PYTHONPATH=src python3 -m kompose.cli quota 20
```

Windows PowerShell: run `$env:PYTHONPATH='src'` first; then replace `PYTHONPATH=src python3 -m` with `py -m`.

Optional development install: `python3 -m pip install -e '.[dev]'`; the `kompose` CLI then becomes available as a console command.

## Read a fictional Kristal answer

```bash
PYTHONPATH=src python3 -m kompose.cli read \
  examples/capsule-rivieres/kristals.json KR-ARCHIVES TERRITOIRE OCCUPANTS --demo
```

`--demo` permits explicitly **fictional** content. It never authorizes a real child or certifies a historical source.

## B6 bakery scenario preview (no Orgo calls)

```bash
PYTHONPATH=src python3 -m kompose.cli preview-kontexte \
  examples/kontexte-boulangerie/data/missions/boulangerie.json \
  examples/kontexte-boulangerie/data/roles
```

The output is a **non-executable** plan. Optional role/fallback/mock-replay flags and their restrictions are explained in [[Kontexte-B6-Preview]].

## P1 synthetic teacher-preview check (no authorization proof)

```bash
PYTHONPATH=src python3 -m kompose.cli verify-ekole-preview \
  examples/integrations/ekole-fete-sorciere.synthetic.json
```

The accepted fixture returns `runtime_admitted: false`, `permissions_verified: false`, and `world_release_verified: false`; see [[Ekole-P1-Preview]].

## Troubleshooting and limits

- Run commands from the source root, where `examples/` is present. Install the package or set `PYTHONPATH=src` if imports fail.
- A wiki checkout is optional and separate (`../Kompose.wiki/`). Missing wiki tests are **skipped**, not passed.
- All demonstration data are fictional. Passing local tests does not prove school SSO, permission enforcement, real event delivery, or release validation.

[[Home|← Home]] · [[Testing-and-Validation|Testing]] · [[Tandem-Orgo-Boundary|Authority →]]
