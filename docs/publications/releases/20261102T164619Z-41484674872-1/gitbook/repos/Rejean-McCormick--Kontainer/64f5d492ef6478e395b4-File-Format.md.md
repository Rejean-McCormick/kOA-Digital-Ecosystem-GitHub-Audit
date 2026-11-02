<!-- Frozen source: https://github.com/Rejean-McCormick/Kontainer/wiki/File-Format | commit: c9674410bf4a3167240457a63ed37ddf51b76b25 | SHA-256: 76a0b2128c7a6534d26bf5c705d51b06688d0b17777c350a89a1c3b00fdf0319 -->

# File Format — Proposed Container v1

**Status:** the `kristal.container/1` physical format is implemented by **Kristal-Container 1.0.0rc1** but is a **proposal for Kristal Framework adoption**, not an already adopted ecosystem standard. The repository's `docs/FORMAT.md` and schema files in `contracts/` contain the precise authoritative *implementation contract*; this wiki is an overview.

## The outer envelope

```text
Offset      Field
0..7        ASCII "KRISTAL" + byte 0x01
8..11       Canonical JSON header length, unsigned big-endian uint32
12..        Canonical UTF-8 JSON header (1..65,536 bytes)
remaining   Raw ZIP64 STORE payload (open) OR framed authenticated ciphertext
```

An open file has the canonical JSON header `{"format":"kristal.container/1","mode":"open"}`. An encrypted header declares `mode=encrypted`, the `xchacha20poly1305-secretstream-v1` profile, a random container ID, stream header, and a bounded list of key slots. Header JSON has strictly defined serialization and rejects unknown normative fields and duplicate keys. **It does not claim full RFC 8785/JCS compliance.**

The outer envelope means that `.kristal` **cannot be treated directly as an ordinary ZIP**, even in open mode. Use the Kontainer reader or explicitly verified tools that understand the container protocol.

## Inner archive

The payload is a tightly constrained **ZIP64 STORE (no compression)** archive containing regular files, followed by `_kristal/manifest.json`:

```text
example.kristal
  ├─ Kristal envelope + public header
  └─ ZIP64 STORE payload (possibly encrypted)
       ├─ state/snapshot.json
       ├─ docs/README.md
       └─ _kristal/manifest.json
```

The manifest records each member's relative path, byte length, and SHA-256 digest, with an optional Ed25519 signature. Entries use canonical portable UTF-8 NFC paths with `/` separators. The parser rejects absolute/traversal paths, links, reserved Windows names, case collisions, unknown compression, and mismatched ZIP structures. ZIP CRC32 is **not** a cryptographic authenticity check; the manifest's hashes and authenticated encryption/signature policies have different roles.

A directory's empty directories, original timestamps, ACLs, POSIX permissions, and extended attributes are **not preserved**. This is a portable content package, **not** a filesystem-image backup.

## Encrypted profile

The inner ZIP is encrypted as a whole by libsodium **XChaCha20-Poly1305 secretstream**, using a fresh random 32-byte content key. The file uses length-prefixed frames, normally with 1 MiB plaintext chunks, an authenticated outer header, and a mandatory final authenticated frame. This detects tampering and truncation. Opening validates the full stream and archive before exposing member names or contents.

Password access uses **Argon2id** (64 MiB / 3 passes / parallelism 4), HKDF-SHA256, and an authenticated wrapping slot. Recipient access uses X25519 sealed boxes. Recovery and dual-secret slots are distinct. **Slots are OR alternatives**; within password-factor access, password **AND** factor are combined cryptographically.

Encrypted headers still expose the total file size, encryption mode, access-slot types/counts, and recipient public-key identifiers; this profile has **no padding**. Private filenames and inner manifest are encrypted, not the existence and approximate size of the file.

## Default resource limits

| Limit | Default |
| --- | ---: |
| Member count | 10,000 |
| Member size | 8 GiB |
| Total member content | 16 GiB |
| Manifest | 8 MiB |
| Central directory | 16 MiB |
| Direct API `read()` | 16 MiB |

Applications can set `Limits` in Python; raising them increases resources committed to untrusted input. For large members, prefer `copy_to()` rather than `read()`.

## Semantic boundaries

The physical manifest attests to **bytes and paths**, not Kristal's Logical Commitment, Reader Policy, provenance, recognition, or epistemic meaning. The kOA ecosystem's **Kristal v6** semantic contracts remain owned by Kristal Framework. Its canonicalization rules (including RFC 8785/JCS in Kristal v6) must not be confused with the separate proposed envelope-JSON profile described here.

See [Architecture](Architecture), [Protection and Access](Protection-and-Access), and [Ecosystem Integration](Ecosystem-Integration).
