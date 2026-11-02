<!-- Frozen source: https://github.com/Rejean-McCormick/kristal-public/blob/88d3e2035d1eedc9234d5c7c2c4bc6694a07311a/docs/C123_SIGNED_GATE.md | commit: 88d3e2035d1eedc9234d5c7c2c4bc6694a07311a | SHA-256: 6fead9cfae5e721ebb196a8e1c708d912e2638f4fe47034c24640804fbaa6671 -->

# Offline signed C1/C2 evidence gate — review-only candidate

**Status: reference verification code; no C1 issuer, C2 authorization, GitHub release, or public synchronization is enrolled.**

The supplied repository is intentionally **BLOCKED**: its `kristals/index.json` and real Zoology read surface are absent, and the five Bootstrap-managed file hashes drift. **Never create a fabricated index, signed test receipt, or trust policy in the public checkout to make the gate pass.**

## What is implemented

`tools/c123_offline.py` checks all the following *locally*:

1. The checkout is a **clean Git worktree** and its `HEAD` resolves to an exact 40-hex SHA-1 commit (not an unverified user argument). No untracked or changed files.
2. The existing strict `c3_collection.validate_index` verifies **all** hosted members, the exact index and each source byte; selected slug is present.
3. An independently supplied external trust policy has different active **Ed25519** public keys for roles C1 and C2, with local key/receipt revocation records.
4. C1 and C2 receipts are **both signature-verified** over the exact canonical UTF-8 JSON object (sorted keys, compact separators, original Unicode); absent or ambiguous fields and duplicate JSON keys are rejected. This serialization is a local versioned reference profile, **not** claimed to be general RFC 8785 JCS.
5. Receipt signatures bind the **same exact repository, slug, Git commit, index digest, source surface digest, semantic state reference and state commitment**.
6. The C2 receipt binds **the exact signed C1 receipt digest**, public visibility and an explicit complete set of allowed public paths (every file in that member's approved C3 surface, sync manifest and shared index).
7. Issuance, validity windows, explicit local key/receipt revocation and signer independence are checked.

Outputs never say `authorized_to_publish=true`. A matching local check reports `SIGNED_EVIDENCE_MATCHES_LOCAL_POLICY` with **`public_exposure_authorized=false`**. It does not know whether the trust roots are legitimate or revocations are fresh, whether the initial public upload was authorized, or whether GitHub has published a truly immutable release.

## Usage — controlled private staging checkout only

Install the optional verifier dependency, preferably in a disposable virtual environment:

```powershell
py -3.12 -m pip install -r requirements-security.txt
py -3.12 -B tools/c123_offline.py --repo . --slug zoology `
  --trust C:\secure\kristal\policy.json `
  --c1 C:\secure\kristal\signed-c1.json `
  --c2 C:\secure\kristal\signed-c2.json
```

`--trust`, `--c1` and `--c2` **must** be actual protected external files *outside this public repository*. These paths are only examples; the files are not included here. The script runs without network access and performs no write, signing or deployment. Exit code **3** means BLOCKED; exit code **0** means only local evidence consistency, **not publication clearance**.

### External trust policy shape (illustration only)

```json
{
  "format": "kristal-public.local-trust-policy/1.0",
  "repository": "Rejean-McCormick/kristal-public",
  "keys": [
    {"key_id":"c1-independent","role":"C1","status":"active","public_key_base64":"<32-byte Ed25519 public key in RFC 4648 base64>"},
    {"key_id":"c2-domain-owner","role":"C2","status":"active","public_key_base64":"<different public key>"}
  ],
  "revoked_keys": [],
  "revoked_receipts": []
}
```

This is a **configuration shape**, not a trusted policy. The authentic trust administrator must secure it independently of the candidate repository and attest its provenance; don't commit keys, private evidence, tokens or authorization records here. Public keys alone do not prove that a signer is entitled to C1/C2 authority.

### Signed receipt shape

C1 contains exactly: `format=kristal.c1-qualification/1.0`, `issuer_key_id`, `decision=qualified`, `subject`, `issued_at`, `not_before`, `expires_at`, `signature`.

C2 contains exactly: `format=kristal.c2-public-authorization/1.0`, `issuer_key_id`, `decision=approved`, the identical `subject`, timestamps, `c1_receipt_digest`, `allowed_paths` (sorted exact list), `visibility=public`, `signature`.

Both subject values are JSON objects with keys: `repository`, `slug`, `source_commit`, `index_digest`, `surface_digest`, `state_ref`, `state_logical_commitment`.

Dates use **UTC** `YYYY-MM-DDTHH:MM:SSZ`. Signatures are RFC 4648 base64 Ed25519 signatures of exactly the UTF-8 bytes produced by:

```python
json.dumps({k: v for k, v in receipt.items() if k != 'signature'},
           sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode('utf-8')
```

C2 `c1_receipt_digest` is `sha256:` + SHA-256 of the canonical **entire signed C1 object including its `signature`**. The signer/owner tools that issue actual receipts live **outside this public repository**. Test private keys are generated **ephemerally in memory** by unit tests; no real receipts or signers are shipped.

## Security and release boundaries that remain CLOSED

- A public push/PR reveals bytes **before** an in-repository GitHub Action can authorize them. A trust gate inside this repo, even with verified signatures, cannot authorize first exposure. Public sync must be gated **upstream in private staging**, with external trusted enforcement and a refreshed revocation registry.
- Source trust cannot be established by the candidate tree itself (including scripts/workflows). Require independently managed C1/C2 roots and an operator-reviewed exact destination/visibility/scope before synchronizing any bytes.
- This program does not implement live checks of GitHub branch protections, signer revocations, online trust registries, audience restrictions, licenses, or the publication actor's permissions.
- **An immutable publication is not demonstrated by a commit hash alone.** Qualified release requires verified GitHub Release/attestation bound to exact archive hash and tag/commit, protected against tag replacement and asset replacement, followed by a separately validated C4 intake. The current managed `kristal-publish.yml` remains read-only and deliberately fails.
- Framework v10 validation is still independently required, and the existing pin disagreement must be resolved before any production trust verdict.
- Do not use the return code of this offline tool directly as an authorization switch or in a public write workflow.

## Safe next steps

1. Real Kit+Manager produce an approved read surface and accurate index in private staging; C3 validates it.
2. C1 owner issues genuine independent signed qualifications; C2 domain owner issues independent scoped public-exposure approval, including a maintained live revocation mechanism.
3. Bootstrap reconciles its five managed-file drifts under explicit ownership review.
4. Design and test external **pre-public** push controls and a separate irreversible/append-only release workflow with externally validated attestations, GitHub protected tags and verification of published bytes.
5. Only then qualify a non-sensitive test release and separately authorize C4/EncyKlopedia intake.
