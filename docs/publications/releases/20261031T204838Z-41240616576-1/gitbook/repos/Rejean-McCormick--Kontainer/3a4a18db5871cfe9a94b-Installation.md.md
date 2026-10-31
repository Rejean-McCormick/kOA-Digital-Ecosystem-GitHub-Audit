<!-- Frozen source: https://github.com/Rejean-McCormick/Kontainer/wiki/Installation | commit: c9674410bf4a3167240457a63ed37ddf51b76b25 | SHA-256: 63521aefb00fbcf3019b082a9321b4f7d92e31771d06557e73bf50c3f1990dac -->

# Installation

Kontainer is distributed in the provided archive as a **Python library plus CLI** (`kristal_container`). Version **1.0.0rc1** targets Python **3.11–3.14**. The delivery report records local execution on Linux x86-64/Python 3.12.14; the included CI workflow targets Linux, Windows, and macOS, but is **not evidence that all those CI jobs ran** for this delivery.

## Install from the source repository

From the extracted `Kristal-Container` directory:

```bash
python -m venv .venv
.venv/bin/python -m pip install -c constraints.txt .
.venv/bin/python -m kristal_container capabilities
```

On Windows PowerShell:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -c constraints.txt .
.\.venv\Scripts\python.exe -m kristal_container capabilities
```

The `constraints.txt` file pins qualified **runtime** dependency versions. It is not a complete reproducible, cross-platform lockfile with hashes. Review dependencies in your own deployment pipeline.

## Install the built wheel

The supplied distribution includes `dist/kristal_container-1.0.0rc1-py3-none-any.whl`. With a separate project environment, install the wheel using your deployment's reviewed dependency constraints; do not assume the wheel alone includes every dependency or that its existence proves a production review.

## Developer setup

```bash
python -m pip install -c constraints.txt -e ".[dev]"
python -m pytest
python -m ruff check src tests tools
python -m ruff format --check src tests tools
python -m build
```

These commands reproduce the repository's development workflow on an appropriately prepared host. Before distributing externally, review `docs/RELEASE.md`, `LICENSE`, and `SECURITY.md` in the source repository.

## Operating-system notes

- **No bundled GUI:** Manager/Konstellation are separate application layers.
- **No automatic file association:** double-click opening is not installed by this package.
- **Filesystem controls:** the writer uses a prepared output and atomic publication. Filesystems without required hardlink support can fail closed in no-overwrite mode.
- **Windows:** POSIX-style file permission modes are not a replacement for appropriate NTFS DACLs. Test protected staging, backups, antivirus interactions, and destination permissions on the actual target system.
- **Cross-platform conformance:** Python/OS support targets must be qualified through your own CI and integration environment.

## Confirm installed features

```bash
python -m kristal_container --version
python -m kristal_container capabilities
```

The JSON capability response identifies available profiles and explicitly unsupported native TPM/WebAuthn/KMS/post-quantum modes. Do not infer hardware assurance from the presence of an abstract provider interface.
