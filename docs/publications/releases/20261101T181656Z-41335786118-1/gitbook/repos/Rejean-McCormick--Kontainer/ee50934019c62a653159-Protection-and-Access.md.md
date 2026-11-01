<!-- Frozen source: https://github.com/Rejean-McCormick/Kontainer/wiki/Protection-and-Access | commit: c9674410bf4a3167240457a63ed37ddf51b76b25 | SHA-256: 2cd196e134f92404dde831582c0e909f6918af88113ad41671f8185ad679904c -->

# Protection and Access

Kontainer separates **access to bytes**, **proof of origin**, and **recovery**. These dimensions are complementary, not a single ladder of “more secure” modes. All cryptographic policies must be evaluated by a trusted reader application.

## Profiles available in 1.0.0rc1

| Profile | Confidentiality | Key access |
| --- | --- | --- |
| Open | None | No decryption required |
| Password | Yes | Passphrase via Argon2id |
| Password + secret | Yes | Passphrase **AND** a 32-byte factor secret |
| X25519 recipient | Yes | Any individually authorized recipient private key |
| Recovery key | Yes | Independent alternate key slot, configured at creation/rewrap |
| Ed25519 signature | Separate authenticity control | Verify against public keys obtained through a trusted external channel |

For encrypted files, a fresh random 32-byte content key protects the inner archive via libsodium XChaCha20-Poly1305 `secretstream`. Each access slot protects that content key. The password KDF profile is Argon2id, with 64 MiB memory, three passes, and parallelism four. Weak passphrases remain vulnerable to offline guessing: the container cannot enforce an honest offline rate limit.

## AND vs OR is essential

- **Inside the password-factor slot:** both password **AND** factor secret are cryptographically required. An authentication-screen-only second step would not meet this condition.
- **Between slots:** password, recovery, and recipient slots are **OR** alternatives. A recovery secret can unlock the file without the normal password.
- **Between recipients:** each listed X25519 recipient is an independent OR path.

The shipped second factor is a *copyable secret file*, not a hardware-backed authenticator. The Python `FactorProvider` interface is a possible integration point, but there is no certified FIDO2/WebAuthn/TPM implementation in this release.

## Signatures are not encryption

An Ed25519 signature covers the canonical manifest (file paths, sizes, SHA-256 hashes) with domain separation. A signature bundled with its own public key can be **cryptographically valid but untrusted**. The reader must supply the accepted signing keys independently. A verified manifest signature does **not** sign the entire outside encryption/access policy, establish a Logical Commitment, or authorize the execution of file content.

Use `--trust signer-public.json` or `trusted_signers=...` when signature provenance matters. Use `--require-encrypted` when the consuming policy requires confidentiality. Use a trusted external physical-file SHA-256 where rollback/substitution protection is required.

## Not implemented (do not claim support)

Native TPM device binding, WebAuthn PRF, managed KMS/Konfid issuance, post-quantum key establishment, cryptographic threshold recovery, and offline revocation are **not part of the shipped CLI**. They require independent adapters, infrastructure, deployment testing, and security review.

## Choosing a profile

Use **open + verified signature** only when disclosure is acceptable and provenance matters. Use **password + recovery** for autonomous encrypted files. Use **recipient keys** for independent authorized recipients. Use **password-factor** when both secrets will be stored separately and normal access needs both. Do not label a copyable factor as “hardware MFA”; do not promise remote revocation of already distributed offline copies.

See [Security Model](Security-Model), [Key Management and Recovery](Key-Management-and-Recovery), and [File Format](File-Format).
