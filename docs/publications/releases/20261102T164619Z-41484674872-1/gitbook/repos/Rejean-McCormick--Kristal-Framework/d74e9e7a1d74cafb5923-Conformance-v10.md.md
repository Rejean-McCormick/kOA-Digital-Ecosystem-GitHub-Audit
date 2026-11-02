<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Conformance-v10 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 4279ef77a7e3f07ee11bcd6fbbbcae5881772ee0cc3a06e3d5bd178b08f0cfa9 -->

# Conformance & Qualification — v10

V10 conformance is **capability/profile-based**. A tool may support only some profiles; the optional GitHub host profile is not required for generic `V10-Full`.

| Profile | Core requirement |
| --- | --- |
| `V10-Node-Reader` | Validate node, binding, publication and directory structures |
| `V10-Publisher` | Preserve v9 semantics and exact published state, retain a Publication Record with verifiable bytes |
| `V10-Directory` | Keep discovery distinct from exact semantic federation |
| `V10-GitHub-Host` | Node Reader + `kristal.host/github/1.0` profile |
| `V10-Full` | Inherited `V9-Full` + Node Reader + Publisher + Directory (GitHub optional) |

The draft.3 GitHub read-surface support, **when advertised**, additionally validates read-surface, sync-manifest and collection-index contracts.

## Fail-closed qualification

- Malformed documents yield validation failures, not uncaught processing errors.
- Unsupported profiles must not be falsely marked verified.
- Publication resource byte sizes and SHA-256 digests must match, including remote retries.
- Host qualification, integrity and workflow attestations are **not** factual or epistemic authority.

## Independent examiner

KristalDiag independently verifies v9 commitments and v10 contracts (not by reusing the Framework JS verifier). The supplied KristalDiag README identifies **Framework `10.0.0-draft.2`** as its pinned target; this is **not a verified claim of draft.3 coverage**. Review its lock and actual test results before asserting draft.3 conformance.

See [[Status-v10]], [[Conformance-v9]], [[Security-and-Confidentiality-v10]].

*Normative source: Framework `spec/v10/Conformance.md`; examiner scope: KristalDiag `README.md` and locked resources.*
