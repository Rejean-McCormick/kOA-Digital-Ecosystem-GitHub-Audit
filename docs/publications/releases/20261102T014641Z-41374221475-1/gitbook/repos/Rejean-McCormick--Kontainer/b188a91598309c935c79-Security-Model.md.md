<!-- Frozen source: https://github.com/Rejean-McCormick/Kontainer/wiki/Security-Model | commit: c9674410bf4a3167240457a63ed37ddf51b76b25 | SHA-256: 7b3c7556c6041b367ec92c40fe5ea978a526c42d9e4b657cfaff80831d1998c4 -->

# Security Model

**Status: release candidate, no independent cryptographic security audit.** This document explains design intent and shipped controls, not certification. For precise threat statements and invariants, consult source `docs/THREAT_MODEL.md` and `SECURITY.md`.

## Threats and controls

| Threat | Mitigation | Limit |
| --- | --- | --- |
| A stolen encrypted container | Random content key, XChaCha20-Poly1305, Argon2id for passwords | Weak passwords can be guessed offline |
| Truncation / modification / reordering | Header-bound authenticated frames with final marker | Authorized key holders can produce new valid files |
| Hostile ZIP members | Strict STORE-only parser, bounded entries, portable path rules | Malicious content can remain unsafe to render |
| Unknown signature origin | External trusted Ed25519 signer keys | The embedded key does not bootstrap trust |
| Temporary plaintext copies | Encrypted staging spool | Memory/swap/host compromise remains possible |
| Lost opening secret | Preconfigured independent recovery slot | No recovery without a surviving authorized key |
| Rollback to an old copy | Trusted `expected_sha256` from external policy | The file itself cannot know the newest version |
| Downgrade to an open representation | Consumer `require_encrypted` policy | A manifest signature does not sign the encryption policy |

## Hard boundaries

- **No implicit execution:** files inside `.kristal` are untrusted data, including embedded instructions aimed at a model or rendering engine.
- **No secret parameters on CLI:** do not put passphrases in process arguments, shell history, logging, or CI environment variables. Use interactive input, guarded descriptors, or the application API.
- **No transparent export:** plaintext export/extraction is explicit. Manager and integrations must preserve this rule, including private GitHub repositories and indexing/caching systems.
- **No quiet downgrade:** missing factors, unsupported providers, untrusted signatures when required, and unrecognized profiles fail closed.
- **No hidden universal recovery:** recovery is an owner-provided alternate capability, and should be protected accordingly.
- **No automatic physical-device security claims:** neither MAC/system ID nor a copyable factor file equals a TPM-backed nonexportable key.

## Confidentiality scope

Encrypted inner filenames, manifest metadata, and file content are protected. The outer header and file length still expose useful metadata including access-slot types and recipient identifiers; this release does **not** include padding. Files opened by an authorized process can be copied by that process. Files already leaked in plaintext cannot be cryptographically recalled.

The engine does **not** provide digital-rights management, malware scanning, secure erase guarantees, runtime sandboxing, per-file ACLs, or a foolproof defense against a malicious administrator or rooted endpoint.

## Authenticity and authorization are separate

`verify` checks byte-level integrity and any required external signature policy. The results cannot establish that an assertion is true, that a Kristal State is `recognized` or `reference`, or that a specific reader is authorized under a Kristal **Reader Policy**. Applications must still enforce their own policy *before* viewing, indexing, searching, quoting, exporting, or activating derived materializations.

## Production review checklist

Use a strong unique passphrase; maintain protected backups; rehearse independent recovery; pin external trusted signer keys; specify `require_encrypted` where needed; review dependencies; run real multi-OS tests; validate filesystem behavior and protected caches; arrange independent cryptographic review before production-critical deployment.

See [Release Status and Roadmap](Release-Status-and-Roadmap) for gaps and [Troubleshooting and FAQ](Troubleshooting-and-FAQ) for operational answers.
