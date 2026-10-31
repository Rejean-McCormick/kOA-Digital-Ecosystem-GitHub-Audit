<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/4ed4b8928665ebd723b68f8b3f2cb2f196d6374f/docs/2-Technical-Reference/40-integration/tandem-vps-capsule-agent/evidence-ledger.md | commit: 4ed4b8928665ebd723b68f8b3f2cb2f196d6374f | SHA-256: a7682bd7c6e64fe8a906e170caad58f1b8c6c283e0fda8bbdb06681403344279 -->

# Evidence ledger — snapshot and operator-reported (2026-10-18)

| Evidence | Grounding | Scope | Classification |
|---|---|---|---|
| `IK-FAKEPLANT-20261018` | Operator's PowerShell log: FINALISER_TANDEM_IK_FAKEPLANT, decision 1, Orgo Workflow V2, impact Neon 2, duplicate counts=1, `complete=true` | Local Windows/Neon/Orgo Docker FakePlant; synthetic | **USER_REPORTED_LOCAL_E2E_VERIFIED**, not production |
| `LOT1A-20261018` | Operator's PREVIEW/INSTALL/VERIFIER LOT1 logs: SHA-256 matched, 40 targeted tests; backup created | Local Capsule Manager source only | **USER_REPORTED_LOCAL_TESTED**, remote Agent not updated |
| `LOT1B-20261018` | Operator's PREVIEW/INSTALL/VERIFY KDiag logs: SHA-256 matched, 71 tests; rollback backup created | Local KonnaxionDiag 4.2.5 source only | **USER_REPORTED_LOCAL_TESTED**, Agent invocation pending |
| `PROFILE-20261018` | User choice: first final environment VPS Linux Docker/Capsule Agent | Deployment *intent*, no VPS attestation | **USER_DECIDED** |
| `LOT1C` | Capsule Agent measured ReleaseSet + owner PEP call on exact VPS | No execution or source update shown | **NOT_INTEGRATED** |

**Source limitations:** reference ZIP `kOA_Digital_Ecosystem_Code_snapshot(1).zip` is a user-supplied repository snapshot, not live Git HEAD. No exact owner commit SHA, key fingerprint, domain, host identity, OCI image digest, certificate, actual deployment receipt or active VPS inventory is established here. Files under `docs/2-Technical-Reference/40-integration/tandem-vps-capsule-agent/` record C0 coordination only; they are not signed release evidence.

**Privacy:** do not commit `.env` secrets, bearer tokens, private keys, human identities, infrastructure IP addresses or database contents into this ledger. Later evidence imports must be redacted and hashed and located outside public documentation if sensitive.
