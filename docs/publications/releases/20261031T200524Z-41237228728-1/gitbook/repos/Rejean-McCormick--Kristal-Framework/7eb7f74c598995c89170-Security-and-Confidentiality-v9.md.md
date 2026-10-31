<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Security-and-Confidentiality-v9 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 5924cc7310b2b8a6a972a4d982a2c999ad9646064fc0bdc25941548ad311056a -->

# Security and Confidentiality — v9

## Threat classes

V9 distinguishes at least:

- accidental corruption;
- incomplete writes/crashes;
- concurrent publishers;
- malicious storage;
- unauthorized readers;
- unauthorized publishers/activators;
- epistemically untrusted sources.

Different controls address different threats.

## Commitment visibility

A deterministic Logical Commitment need not be globally public. For low-entropy sensitive data, public hashes may leak equality or enable guessing attacks.

V9 therefore keeps commitment security profile-driven. The baseline does not invent custom cryptography.

## Encryption

Re-encryption may change physical blob bytes while preserving logical content:

```text
new key / nonce / ciphertext
→ new Blob Digest
→ same Logical Commitment
```

when the applicable security profile permits logical comparison.

## Privilege separation

```text
STORE WRITE != PUBLISH AUTHORITY != ACTIVATE AUTHORITY
```

A deployment may separate these privileges.

## Remote content

Retrieved manifests and blobs are untrusted input until validated.

```text
RETRIEVED CONTENT != INSTRUCTION AUTHORITY
```

The existence of data in a package cannot grant itself execution, mutation or activation permission.
