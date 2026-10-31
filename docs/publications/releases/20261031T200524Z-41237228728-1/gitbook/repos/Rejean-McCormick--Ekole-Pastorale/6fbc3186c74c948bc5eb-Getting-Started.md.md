<!-- Frozen source: https://github.com/Rejean-McCormick/Ekole-Pastorale/wiki/Getting-Started | commit: 7c73b3852cf83a881cd83a14f345a78e163dc8c3 | SHA-256: 7445a6f4181d794bbf0faf725d908ddaf37feab9442d166b67b2960954e5aaf1 -->

# Getting Started

This guide runs **Ekole Core + Ekole Pastorale** as two independent sibling repositories. You do **not** copy pastoral content into the Core repository or modify the Core source.

## Prerequisites

- Python **3.10+** available from the command line.
- A compatible `ekole/` checkout containing `launcher.py`.
- This repository extracted or cloned as `ecole-pastorale/` next to `ekole/`.
- Free local TCP ports **8775** and **8776** (or select replacements).

```text
projects/
├── ekole/                # General-purpose engine
├── ekole-quebec/         # Optional independent curriculum
└── ecole-pastorale/      # This Catholic content repository
    ├── pack.json
    ├── demarrer_pastorale.py
    ├── LANCER_PASTORALE.bat
    └── lancer-pastorale.sh
```

The content directory is named `ecole-pastorale`, not `ekole-pastorale`, to remain consistent with the current pack ID and content discovery convention.

## Windows

1. Open `ecole-pastorale/` in File Explorer.
2. Double-click **`LANCER_PASTORALE.bat`**.
3. Keep the terminal window open; closing it stops the servers.
4. Open the learner portal at **http://127.0.0.1:8775/** if the browser does not open automatically.

Run a preflight check without starting the servers:

```bat
LANCER_PASTORALE.bat --verifier
```

`LANCER.bat` is kept as a compatibility alias.

## macOS / Linux

```bash
cd ecole-pastorale
./lancer-pastorale.sh
```

Or start with Python explicitly:

```bash
python3 demarrer_pastorale.py
```

Verify first:

```bash
python3 demarrer_pastorale.py --verifier
```

`lancer.sh` is kept as a compatibility alias.

## Launch options

| Argument | Purpose |
| --- | --- |
| `--verifier` | Validate loading using the real Ekole Core, then exit |
| `--sans-navigateur` | Do not open browser windows automatically |
| `--sans-editeur` | Run only the learner portal |
| `--edition` | Enable local editing in the teacher application (read-only by default) |
| `--port 8875` | Change the learner portal port |
| `--port-editeur 8876` | Change the teacher application port |
| `--core ../ekole` | Specify a different Core location |

Alternatively, set `EKOLE_CORE_PATH` to the directory holding Ekole Core. The default launcher path is `../ekole/launcher.py` relative to this repository.

Equivalent direct Core command:

```bash
python3 ../ekole/launcher.py --contenu . --port 8775 --port-editeur 8776 --ouvrir
```

The teacher application uses its own local port. **Use the private URL displayed by Ekole in the terminal**; do not assume that the bare port URL is its protected entry point. Do not expose the local editor to the internet.

## What to expect

- **32 draft courses** and **7 pathways** in the content pack.
- Two distinct branches (message/tradition and miracles/mysteries).
- A learner-facing view with draft-status warnings.
- A separate teacher view; editing remains disabled unless explicitly enabled.

If loading fails, start with [Troubleshooting](Troubleshooting.md). For boundaries between the two repositories, read [Architecture](Architecture.md).
