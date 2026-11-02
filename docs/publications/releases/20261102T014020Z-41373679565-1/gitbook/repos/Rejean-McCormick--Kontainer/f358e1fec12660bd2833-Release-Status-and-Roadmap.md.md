<!-- Frozen source: https://github.com/Rejean-McCormick/Kontainer/wiki/Release-Status-and-Roadmap | commit: c9674410bf4a3167240457a63ed37ddf51b76b25 | SHA-256: 662694aede0394b97d59bff4f882ecd1e13cba15170fe1f81071682180bd281e -->

# Release Status and Roadmap

## Current baseline: 1.0.0rc1

The supplied distribution includes Python source, typed file-format schemas, installable wheel/sdist, documentation, an example open container, a test suite, and a CI workflow. Its **dated validation report (11 October 2026)** describes the following **locally recorded** outcomes:

| Validation item | Recorded result |
| --- | --- |
| Tests, including adversarial and property-based coverage | 62 passing |
| Branch coverage | 82% |
| Local execution environment | Linux x86-64; Python 3.12.14 |
| Ruff lint and formatting | Passed |
| Wheel and source distribution build | Passed |
| Isolated wheel install and CLI smoke workflows | Passed |
| Dependency advisory check for pinned runtime packages | No known advisories found at the dated check |
| Synthetic 64 MiB packaging/opening check | Passed |

These are **claims from the provided delivery record**, not an independently rerun audit in this wiki. They do not prove that all advertised target OS/Python combinations passed remote CI. No independent cryptographic audit, FIPS certification, or high-assurance qualification is claimed.

## Capabilities that are intentionally absent

- Native TPM secure-element or device binding.
- WebAuthn PRF / hardware factor provider with real-world platform qualification.
- Live managed KMS/HSM/Konfid issuance and policy enforcement.
- Post-quantum or hybrid ML-KEM recipient/recovery profile.
- Cryptographic threshold (e.g., 2-of-3) recovery.
- Offline revocation of old copies or already exported plaintext.
- Direct partial-decryption/random-access encryption index without full verification.
- Desktop GUI and OS file association.
- Normative ratification of container v1 by Kristal Framework.

These must not be toggled on with a label or assumed to work because a provider protocol exists in Python.

## Gates before sensitive production

1. Independent security review of key-slot composition, header authentication, cryptographic framing, key files and recovery.
2. Executed CI across actual target Python versions and OS/filesystem combinations, especially Windows/NTFS controls.
3. Multi-GiB/ZIP64, power-loss, interrupted-write, disk-full, and hostile input testing on deployment hardware.
4. Supply-chain verification: fresh vulnerability review, reviewed dependency lock/hashes and provenance appropriate to releases.
5. Explicit Framework adoption, compatibility vectors, and independent interoperability reader/writer tests.
6. Key-recovery exercises using actual owners, backup storage, hardware, and organizational policies.
7. Real provider integration qualification for any TPM, WebAuthn, or managed key operations before advertising them.
8. Repository owner decisions on licensing and a private vulnerability-reporting channel before public distribution.

## Future directions — not release promises

Where a demonstrated use case warrants it: qualified hardware-/identity-based key providers; enterprise authorization through separate KMS infrastructure; hybrid classical/post-quantum recipient paths protecting **all relevant unlock routes**; and a separately designed secure partial-access profile for very large archives. A blockchain is **not** a baseline dependency: it does not solve the primary threats of copying, key loss, or decrypted-content leakage.

## Upgrade and compatibility policy

A format or cryptography change should create a reviewed profile/version with explicit tests and migration. Do not silently accept unknown slots, drop recovery access, overwrite existing files, or confuse ciphertext rotation with semantic changes. Keep validated backups until the new path and recovery route are tested.

See [Security Model](Security-Model) and source `docs/VALIDATION.md` / `docs/RELEASE.md`.
