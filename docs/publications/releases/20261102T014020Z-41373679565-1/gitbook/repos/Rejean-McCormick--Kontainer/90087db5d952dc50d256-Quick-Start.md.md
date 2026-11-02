<!-- Frozen source: https://github.com/Rejean-McCormick/Kontainer/wiki/Quick-Start | commit: c9674410bf4a3167240457a63ed37ddf51b76b25 | SHA-256: 8f0a2fc8eccec9739636b9d34f1bcd3a9c166a53f281ef66984f2f27d4ff472b -->

# Quick Start

These examples use the source tree from **Kristal-Container 1.0.0rc1** and assume Python 3.11–3.14, an activated virtual environment, and the repository's working directory.

## 1. Install locally

```bash
python -m venv .venv
# macOS/Linux: activate the environment, or invoke .venv/bin/python explicitly
.venv/bin/python -m pip install -c constraints.txt .
.venv/bin/python -m kristal_container --help
```

On Windows PowerShell:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -c constraints.txt .
.\.venv\Scripts\python.exe -m kristal_container --help
```

In the remaining examples, `python` means the environment's interpreter. No daemon, account, network service, file association, or permanent system installation is required for open/password-based operation.

## 2. Plan what will be included

```bash
python -m kristal_container plan examples/demo
```

`plan` returns JSON with selected files and byte counts, without writing an archive. A directory scan is recursive; suspicious source names (including `.git`, `.env*`, private keys, and virtual environments) are rejected rather than silently omitted. Prefer **explicit selection** where you know the intended content:

```bash
python -m kristal_container plan examples/demo --include state/example.json
```

Each `--include` is a **single exact relative file**, not a glob or directory. The output file must be outside the source directory.

## 3. Make an open container

```bash
python -m kristal_container pack examples/demo demo.kristal --mode open
python -m kristal_container verify demo.kristal
python -m kristal_container list demo.kristal
```

Open means **no confidentiality**, not that integrity and structural checks are skipped. A `.kristal` is **not** directly a standard ZIP file: it has a versioned outer envelope even when unencrypted.

## 4. Make an encrypted container

```bash
python -m kristal_container pack examples/demo private.kristal --mode password
python -m kristal_container verify private.kristal --password --require-encrypted
```

The CLI prompts for the new phrase during creation and for the existing phrase during verification; it never takes a literal `--password mysecret` argument. Use a long, unique passphrase. `--require-encrypted` is an **external consumer policy** that rejects open containers.

## 5. Add recovery before you need it

```bash
python -m kristal_container keygen recovery rescue.ksecret
python -m kristal_container pack examples/demo protected.kristal --mode password --recovery-key rescue.ksecret
python -m kristal_container verify protected.kristal --unlock-recovery rescue.ksecret
```

`rescue.ksecret` is a **bearer secret stored in plaintext**: possession permits opening through the recovery slot. Store it in a separate protected location, with a separately protected backup. Never place it in the directory you package. Test the recovery path while you still have normal access.

## 6. Read or export

```bash
python -m kristal_container inspect protected.kristal
python -m kristal_container list protected.kristal --password
python -m kristal_container export protected.kristal state/example.json example.json --password --allow-plaintext
```

`inspect` returns **unverified** public header information only. `list`, `verify`, `export`, and `extract` validate before exposing content. `export` produces plaintext; do not point it at an untrusted or publicly synchronized location. Extraction of all files requires a **new** output directory and an explicit `--allow-plaintext` flag.

## Next

Read [CLI Reference](CLI-Reference) for all commands, [Protection and Access](Protection-and-Access) for access models, and [Security Model](Security-Model) before using sensitive data.
