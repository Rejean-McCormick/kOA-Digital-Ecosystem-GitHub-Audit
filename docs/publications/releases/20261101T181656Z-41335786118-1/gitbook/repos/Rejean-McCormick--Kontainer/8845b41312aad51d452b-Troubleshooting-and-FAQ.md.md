<!-- Frozen source: https://github.com/Rejean-McCormick/Kontainer/wiki/Troubleshooting-and-FAQ | commit: c9674410bf4a3167240457a63ed37ddf51b76b25 | SHA-256: 6cc444b0b96dc4278d3ad0b1dfbae38ad78ac1da5cdeb243f9bc90acda160ef1 -->

# Troubleshooting and FAQ

## Why can't I open `.kristal` in a normal ZIP program?

The file begins with a **Kristal-specific versioned envelope**; only its *inner* payload is ZIP64 STORE. For encrypted files, the inner ZIP is fully encrypted. Use the Kontainer reader and complete verification.

## Why does `inspect` show a file even when `verify` fails?

`inspect` parses **unverified public header claims only**. Its reported metadata must not be trusted as proof of integrity, correct credentials, or origin. `verify` checks the entire container and the requested signature/encryption policy.

## I have a valid signature. Why does the reader say `valid-untrusted`?

The signature checks against a public key carried in the file but that key is not trusted simply because it is embedded. Pass an externally authenticated signer public key with `--trust` or `trusted_signers`. A `--require-signature` setting with no trusted keys intentionally fails.

## My password is correct, but decryption fails.

Access errors can also arise from a missing factor, wrong key, damaged envelope, or policy mismatch. The API intentionally does not promise to distinguish a wrong secret from tampered ciphertext. Check which slot is required, verify your recovery method, and keep the original file intact.

## Can I recover after losing my password and recovery file?

Only if another legitimate opening path still exists (for example, a valid recipient identity). Without any remaining authorized key, there is no built-in backdoor or magic recovery procedure. Back up **both** your encrypted container and a separately protected recovery method.

## Does `password-factor` provide hardware-bound MFA?

No. The shipped factor is a **copyable 32-byte secret**. Both password and factor are required for that slot, but it is not proof of physical hardware presence. Native TPM/WebAuthn providers are not shipped.

## Does `rewrap` revoke access to earlier files?

No. It creates a new, freshly encrypted output and replaces the new file's access slots. Old copies and already-exported plaintext remain potentially accessible with the previous keys.

## Why does `extract` need `--allow-plaintext`?

Extraction deliberately releases decrypted content from the protected file. The explicit flag prevents accidental unprotected copies. Extracting to a new directory is required; a crash can leave partial plaintext files there.

## Why was my `.env`, key file, symlink, or `.git` content rejected?

The default input policy rejects common sensitive/development names and unsafe filesystem types to reduce accidental leakage. Use explicit `--include` selection. `--allow-sensitive` only overrides common-name filtering and **does not bypass** other path/format safety controls. It is not a comprehensive secret scanner.

## Why did a large file take time to open before listing members?

The engine fully verifies ciphertext, ZIP structures, manifest and hashes **before** exposing any content. This is intentionally an O(total-size) check. It uses encrypted temporary staging, not speculative streaming of untrusted file members.

## Does Kontainer guarantee semantic correctness or reader authorization?

No. It verifies **physical bytes** and configured cryptographic policies. Kristal Framework validation, Reader Policy enforcement, release compatibility, and execution/activation are separate responsibilities.

## What is the stability and audit status?

The supplied build is `1.0.0rc1`; its release report documents tests performed on Linux/Python 3.12.14, not an independent crypto audit or production qualification. See [Release Status and Roadmap](Release-Status-and-Roadmap).
