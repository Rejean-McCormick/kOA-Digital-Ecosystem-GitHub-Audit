<!-- Frozen source: https://github.com/Rejean-McCormick/Kontainer/wiki/Architecture | commit: c9674410bf4a3167240457a63ed37ddf51b76b25 | SHA-256: b90f50cb23d6ccaba059f2541f40a73f2479b7df9987269f68a4407e0229246e -->

# Architecture

Kontainer is a **single reusable engine** for the physical packaging of Kristal bytes. Its repository boundary exists to avoid reimplementing key handling and archive verification separately in Authoring Kit, Manager, and readers. No server is required for local open/password/recipient workflows.

## Internal module map

| Module | Responsibility |
| --- | --- |
| `api.py` | `pack`, verified `Container` reader, rewrap, extract |
| `archive.py` | File selection, strict ZIP64 STORE, manifest, signature verification |
| `crypto.py` | Encryption, key slots, KDF, authenticated stream |
| `staging.py` | Encrypted temporary spool supporting random reads |
| `filesystem.py` | Safe source inspection, links/path checks, atomic file publication |
| `keys.py` | Typed key-file handling and private-key protection |
| `integration.py` | Local Kit projection adapter |
| `providers.py` | Application-injected provider interfaces |
| `cli.py` | User-facing command parsing and JSON reports |

## Write pipeline

```text
source directory / approved file selection
    → inventory and reject unsafe members
    → read and verify stable source snapshot
    → write strict uncompressed ZIP to encrypted temporary staging
    → verify ZIP + manifest + content digests
    → optionally sign manifest
    → optionally encrypt the full ZIP payload with new content key
    → flush and publish new .kristal atomically
```

Output is outside the source; creation does not delete or modify source files. A concurrently changing source is detected by pre/post checks where possible, but a fully hostile local process can defeat ordinary metadata-based validation; a real filesystem snapshot is a separate prerequisite for that threat model.

## Read pipeline

```text
.kristal file
    → read header as untrusted input
    → acquire an allowed decryption key when needed
    → decrypt/copy into encrypted temporary staging
    → require authenticated final frame
    → fully validate ZIP layout and every manifest entry
    → enforce optional trusted-signature/encryption/digest policy
    → expose a verified, read-only member view
```

Verification is **O(total bytes)** before the first private member is made available. This cost is deliberate. ZIP random access is provided only after verification, from encrypted staging. The implementation neither launches scripts nor renders arbitrary content.

## Transactionality and storage

The engine uses 1 MiB encrypted staging blocks and seeks over this local protected spool. It aims to avoid a complete plaintext temporary copy, but RAM, swap, crash dumps, and a compromised live process are outside the claimed protections. Ordinary closure removes the temporary file; after an abrupt failure, remaining temporary bytes are encrypted.

A new file is prepared beside its destination. No-overwrite publication requires filesystem support for the atomic hardlink path; explicit overwrite uses replacement semantics. Directory extraction, in contrast, is not an atomic transaction — an abrupt interruption can leave partial plaintext.

## Representation vs identity

Open archives have deterministic construction for identical paths/bytes/signature. Encrypted archives intentionally differ for each build. `rewrap` regenerates encryption and access slots while preserving **the inner ZIP bytes**, including its manifest signature, not Framework semantic validation or an automatically refreshed signature.

The container must not be treated as a general-purpose knowledge authority, an operational database, a live synchronization system, or a Runtime Pack activation command.

See [File Format](File-Format), [Security Model](Security-Model), and [Ecosystem Integration](Ecosystem-Integration).
