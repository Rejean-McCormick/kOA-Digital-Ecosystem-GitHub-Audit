<!-- Frozen source: https://github.com/Rejean-McCormick/Kontainer/wiki/CLI-Reference | commit: c9674410bf4a3167240457a63ed37ddf51b76b25 | SHA-256: b98af93e194e882294b2446adda76a175c70b63c5dd5a246fbcd6c576569c292 -->

# CLI Reference

Invoke commands with `python -m kristal_container` from the appropriate environment. Successful commands write **JSON** on standard output. Expected container/policy/access errors use JSON on standard error. The parser may display its own text for syntax errors.

## Commands

| Command | Purpose |
| --- | --- |
| `capabilities` | Report implemented/unsupported capabilities and audit status |
| `plan SOURCE` | Inventory an input selection, with no write |
| `keygen KIND OUTPUT` | Generate `identity`, `signing`, `recovery`, or `factor` key material |
| `pack SOURCE OUTPUT --mode MODE` | Create and verify a new `.kristal` |
| `inspect FILE` | Examine an **unverified** outer header |
| `verify FILE` | Fully verify integrity and the requested policies |
| `list FILE` | List members after successful full verification |
| `export FILE MEMBER OUTPUT --allow-plaintext` | Export one member into a new plaintext file |
| `extract FILE OUTPUT_DIRECTORY --allow-plaintext` | Extract all members into a new directory |
| `rewrap FILE OUTPUT --mode MODE` | Change protection and re-encrypt while preserving the inner ZIP |

## Protection modes used by `pack` and `rewrap`

| Mode | Required inputs | Meaning |
| --- | --- | --- |
| `open` | none | No encryption; never confidential |
| `password` | prompted passphrase or password FD | Password-protected content |
| `password-factor` | passphrase + `--factor-key` | Both secrets required for **normal** access |
| `recipient` | one or more `--recipient PUBLIC_KEY` flags | Every listed X25519 recipient can open independently |

`--recovery-key PATH` adds a distinct recovery slot to an encrypted mode. A recovery slot is an **alternative** way to open; it does not turn password/factor into a three-step AND policy. Recipient mode is explicit in the CLI; the Python API supports intentionally combining more kinds of slots.

## Access flags for reading commands

| Flag | Meaning |
| --- | --- |
| `--password` | Prompt for existing container passphrase; **not** a string value |
| `--password-fd N` | Read existing passphrase from an inherited descriptor |
| `--identity PRIVATE_KEY` | Recipient identity (private key file); a private-key password may be requested |
| `--key-password-fd N` | Descriptor for private-key passphrase |
| `--unlock-factor SECRET_FILE` | Supply a second secret for `password-factor` |
| `--unlock-recovery SECRET_FILE` | Use an independent recovery secret |
| `--trust PUBLIC_SIGNER` | Supply a trusted Ed25519 public key; may repeat; implies signature requirement |
| `--require-signature` | Require a trusted signer; with no trusted key this fails closed |
| `--require-encrypted` | Refuse open containers |
| `--expected-sha256 HEX` | Require a trusted **external** digest of the whole file |

Use `--new-password-fd` with `rewrap` to distinguish the new passphrase from the old one in automation. `--overwrite` permits replacing an existing *output*; it does not grant `--allow-plaintext`.

## Examples

```bash
# Exact selection, not wildcards
python -m kristal_container pack project output.kristal --mode open --include state/snapshot.json

# Identity-based sharing
python -m kristal_container keygen identity alice.kkey --public alice-public.json
python -m kristal_container pack project shared.kristal --mode recipient --recipient alice-public.json
python -m kristal_container verify shared.kristal --identity alice.kkey

# Strong explicit signature trust
python -m kristal_container keygen signing author.kkey --public author-public.json
python -m kristal_container pack project signed.kristal --mode open --signing-key author.kkey
python -m kristal_container verify signed.kristal --trust author-public.json

# Rotate a password; old password is requested first, new one next
python -m kristal_container rewrap old.kristal rotated.kristal --password --mode password
```

The private identity/signing key files use password-based encryption; the public key authenticity must be confirmed outside the container. New signing keys and identity keys require `--public` when generated. Recovery and factor key files are copyable plaintext bearer secrets.

## Input and output safety

- Without `--include`, recursive scanning selects regular files and refuses common secret/dev names. `--allow-sensitive` overrides the **name-based policy only**; it does not disable path and structural validation.
- Source entries must be regular files with portable relative paths; symlinks are refused.
- Destination files must not already exist unless `--overwrite` is given where supported; output must be outside the input source.
- `extract` writes to a new directory. A crash during extraction may leave partial plaintext; extraction is not a directory-level atomic transaction.
- Nothing performs GitHub synchronization, publication, shell execution, or automatic remote downloads.

## Exit codes

| Code | Meaning |
| --- | --- |
| `0` | Success |
| `2` | Format, integrity, access, policy, limit, or CLI parsing error |
| `3` | Environment/operation error |
| `130` | Cancelled |

Do not use `inspect` as a substitute for `verify`. Also see [Key Management and Recovery](Key-Management-and-Recovery) and [Troubleshooting and FAQ](Troubleshooting-and-FAQ).
