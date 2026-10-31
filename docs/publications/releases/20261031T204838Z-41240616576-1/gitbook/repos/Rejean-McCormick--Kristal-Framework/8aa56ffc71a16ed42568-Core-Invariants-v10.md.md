<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Core-Invariants-v10 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: aa607ffc9eb42a7845d08f5d483491bbc513e87f170e2c38b85039c5b6b936e8 -->

# Core Invariants — v10

Every invariant of [[Core-Invariants-v9]] remains in force. The hosted-network layer adds boundaries that deployments and tools must keep explicit.

```text
SEMANTIC STATE != HOSTING != PUBLICATION LOCATION != DISCOVERY DIRECTORY
HOST LOCATION != SEMANTIC IDENTITY
REPOSITORY != KRISTAL NODE
HOST BINDING != LOGICAL STATE
PUBLICATION RECORD != LOGICAL STATE
DIRECTORY != AUTHORITY
DISCOVERY != FEDERATION MEMBERSHIP
HOST ATTESTATION != EPISTEMIC AUTHORITY
AUTOMATION != AUTHORITY
HOST EVENT != LOGICAL MUTATION
MIRROR != LOGICAL REVISION
PUBLIC VISIBILITY != SEMANTIC AUTHORITY
PRIVATE LOCATION != SEMANTIC SECRECY
PROFILE != CORE
```

## Draft.3 GitHub reader boundary

```text
READ SURFACE != SEMANTIC STATE
COLLECTION INDEX != AUTHORITY
SYNC != PUBLICATION != ACTIVATION
```

Repack, compact, encrypt, rematerialize, reindex, synchronize or move bytes without changing semantic commitments **unless the domain logical content itself changes**. A derived index is not a second canon.

## Practical consequences

- Repository identifiers, URLs, workflow IDs, deployment IDs and tokens do not belong in v9 commitments, absent an explicit domain logical rule.
- A host may keep several mirror bindings for the same node.
- Directory omission is not a claim that a Kristal does not exist.
- Qualification proves contract behavior, not factual correctness or authority.
- Failed or unsupported guarantees must be represented honestly, not as successful validation.

See [[Architecture-v10]], [[Security-and-Confidentiality-v10]] and [[GitHub-Read-Surfaces-v10]].

*Normative source: Framework `spec/v10/Core-Invariants.md` and `spec/v10/01-core-spec/kristal-v10-core-spec.md`.*
