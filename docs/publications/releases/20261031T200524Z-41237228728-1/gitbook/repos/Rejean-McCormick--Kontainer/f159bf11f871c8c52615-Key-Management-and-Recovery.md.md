<!-- Frozen source: https://github.com/Rejean-McCormick/Kontainer/wiki/Key-Management-and-Recovery | commit: c9674410bf4a3167240457a63ed37ddf51b76b25 | SHA-256: 21b26247a31780787cf1f06f5cbdb900254703ae72e9d75ee87a56d81e0cc442 -->

# Key Management and Recovery

A protected `.kristal` file is only useful if the intended users can still decrypt it **after** a lost password, lost factor, hardware failure, or staff turnover. Recovery is not automatic: it must be provisioned and tested.

## Recommended personal workflow

1. Generate a distinct recovery secret.
2. Package the file with both a normal opening method and a recovery slot.
3. Verify that a copy opens **using recovery alone**.
4. Store the recovery secret separately from the file and make an independent protected backup.
5. Document who may use recovery and how access rotation is handled.

```bash
python -m kristal_container keygen recovery emergency.ksecret
python -m kristal_container pack my-folder protected.kristal --mode password --recovery-key emergency.ksecret
python -m kristal_container verify protected.kristal --unlock-recovery emergency.ksecret
```

**Warning:** `.ksecret` recovery and factor files contain copyable bearer secrets in plaintext. Their filenames or JSON wrapping do not encrypt them. Anyone holding the correct recovery file can bypass the normal password/factor path. Do not email them, commit them, or package them in a `.kristal` alongside the protected content.

## Recover and rotate

When the normal credential is lost but the recovery key survives:

```bash
python -m kristal_container verify protected.kristal --unlock-recovery emergency.ksecret
python -m kristal_container rewrap protected.kristal rotated.kristal --unlock-recovery emergency.ksecret --mode password --recovery-key emergency.ksecret
python -m kristal_container verify rotated.kristal --password --require-encrypted
python -m kristal_container verify rotated.kristal --unlock-recovery emergency.ksecret
```

`rewrap` creates a **new** file with a new content key and fresh encryption, while preserving the exact inner ZIP bytes. The new envelope does **not** automatically inherit old recipient or recovery slots: explicitly supply every access path that should remain. Prefer also replacing a compromised recovery secret rather than reusing it.

## Shared access

For individual recipients:

```bash
python -m kristal_container keygen identity alice.kkey --public alice-public.json
python -m kristal_container keygen identity bob.kkey --public bob-public.json
python -m kristal_container pack my-folder team.kristal --mode recipient --recipient alice-public.json --recipient bob-public.json
python -m kristal_container verify team.kristal --identity alice.kkey
```

Both Alice and Bob can decrypt independently. Authenticate the public key material through an out-of-band trusted channel. Files signed with a trusted author key and files encrypted for a recipient solve different problems.

## Lost or compromised keys

- **Lost normal password or factor, valid recovery available:** unlock with recovery and rewrap to new credentials.
- **Lost every valid opening and recovery method:** the software cannot decrypt the file. There is no vendor backdoor.
- **Lost all copies of the `.kristal`:** the recovery key does not restore missing ciphertext; you also need a file backup.
- **Compromised credential/recipient:** make a new encrypted file with a new set of access slots and distribute it to remaining authorized users.
- **Compromised signing key:** remove trust in that signer; rewrapping does not re-sign the manifest.
- **Old copies in circulation:** changing keys for a *new* file does not erase, retroactively disable, or securely delete old ciphertext or already exported plaintext.

## Hardware and managed environments

The library exposes optional provider interfaces but **does not ship a native TPM, WebAuthn, or organization KMS implementation**. A future hardware lock should always have a proven alternative recovery route. An organization may govern access through Konfid and a separately deployed KMS/HSM, but that is an architecture boundary, not a supported mode of this release. An approval quorum is not equivalent to cryptographic threshold-secret sharing.

Related: [Protection and Access](Protection-and-Access), [Security Model](Security-Model), [Ecosystem Integration](Ecosystem-Integration).
