<!-- Frozen source: https://github.com/Rejean-McCormick/Konnaxion/wiki/CertifiKation | commit: 62c3bb451bacb4cfbbeb68181c1edfc7ba47a8f9 | SHA-256: 7f05825c00c1637aca55b20a1670d0d4b4530c75c1a1071f46c193ae05f76aae -->

# CertifiKation — KonnectED Certification Capability

CertifiKation is the certification/credential capability inside **KonnectED**. It is not a separate ecosystem system.

Canonical backend:

```text
backend/konnaxion/konnected/
```

## Current model families

- `CertificationPath`;
- `Evaluation`;
- `PeerValidation`;
- `Portfolio`;
- `InteropMapping`.

## Responsibilities

- define certification/learning paths;
- record evaluation attempts/results;
- support peer validation;
- maintain user portfolio evidence;
- map internal certification concepts to external systems when required.

## Current UI

Certification surfaces live under:

```text
/konnected/certifications/*
```

including programs, exam preparation/registration and result dashboards.

## Ownership

Certification state remains KonnectED-owned. An external attestation or interoperability mapping can be referenced without becoming a second source of certification truth.
