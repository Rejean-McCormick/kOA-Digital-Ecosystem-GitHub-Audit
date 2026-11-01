<!-- Frozen source: https://github.com/Rejean-McCormick/Ekole-Pastorale/wiki/Troubleshooting | commit: 7c73b3852cf83a881cd83a14f345a78e163dc8c3 | SHA-256: c49e070f8f9ddb95936ff43f1ac31a1d8f09590b67e8769bec50ef8afe8452cf -->

# Troubleshooting

## Ekole Core was not found

The launcher's default path is `../ekole/launcher.py` relative to `ecole-pastorale/`. Verify the sibling layout:

```text
projects/
├── ekole/launcher.py
└── ecole-pastorale/demarrer_pastorale.py
```

Or pass an explicit location:

```bash
python3 demarrer_pastorale.py --core /absolute/path/to/ekole --verifier
```

You can also use the `EKOLE_CORE_PATH` environment variable.

## The content pack is not loading

Start with:

```bash
python3 demarrer_pastorale.py --verifier
```

Check that `pack.json` exists at the **root** of `ecole-pastorale/` and has the format `ekole.content-pack/0.1`. The content pack is currently expected to contain **32 courses and 7 pathways**.

If you have both `ekole-quebec/` and `ecole-pastorale/` installed, explicitly use the Pastorale launcher or Core's `--contenu` argument; do not rely on auto-discovery to choose the intended school.

## Windows double-click closes or shows an error

Run `LANCER_PASTORALE.bat` from a command prompt so you can read the output. Ensure `py -3` or `python` resolves to Python 3.10 or later.

## Server port is already in use

Select another pair:

```bash
python3 demarrer_pastorale.py --port 8875 --port-editeur 8876
```

Use different ports for learner and teacher applications.

## Browser does not open

If the server continues running, open `http://127.0.0.1:8775/` manually. To avoid automatic opening altogether, use `--sans-navigateur`.

## Cannot access the teacher application

Ekole displays a **private teacher URL** in the terminal. Do not assume that visiting port 8776 directly is sufficient. The editor is read-only unless you deliberately use `--edition`.

## Projector says canonical content changed

Do not bypass the guard. Recheck your source edit and rebuild the correct committed state:

```bash
python3 kristals/lire-bible/tools/kristal.py check-v11 kristals/lire-bible
python3 kristals/lire-bible/tools/kristal.py check kristals/lire-bible
python3 kristals/lire-bible/tools/kristal.py build-v9 kristals/lire-bible
python3 outils/projeter_ekole.py
```

Adjust the unit path to match the edited Kristal. See [Authoring and Projection](Authoring-and-Projection.md).

## Historical Catho references are unresolved

That is expected. `federation/catho-legacy-bridge.json` is a **hash-pinned legacy inventory**, not an authorized Framework v11 semantic crosswalk. See [Catho Reference Integration](Catho-Reference-Integration.md).

## Tests fail because Core is not next to Pastorale

Some integration tests exercise the real Core when a sibling checkout is present. The core-independent repository tests can still run; to test the full launching path, install Core next to Pastorale or set the explicit Core path supported by the launcher.

## Course content is in French

The **learning pack is currently fr-CA by design**. Only the GitHub-facing README and wiki documentation were translated to English. An English curriculum would be a separate authoring and localization project.
