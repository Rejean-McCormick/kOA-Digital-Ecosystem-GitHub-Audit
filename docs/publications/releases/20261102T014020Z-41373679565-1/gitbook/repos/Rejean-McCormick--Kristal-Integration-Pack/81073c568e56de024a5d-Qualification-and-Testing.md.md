<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Integration-Pack/wiki/Qualification-and-Testing | commit: 949de422daed28c0b84684b509e675807ac9c48b | SHA-256: 9ae7e23860d6bb0813dc106d83781a3f9d9a0f402979245307612b6fbd4a6af9 -->

# Qualification and Testing

**Local qualification record: October 17, 2026 · Integration Pack 0.3.0-alpha.1**

The supplied qualification report records **29 passing Python tests and 15 passing Node tests** with locally available, pinned Framework draft.4 and Authoring Kit draft.3 sources. It also records a successful **temporary demo-workspace** sequence: Framework preflight → Kit `import-dik-catalog --register` → Kit `select-v11-catalog` → `check-v11`. The original graph was unchanged.

These are **recorded results for the source release**, not a claim that the wiki creation step repeated all cross-repository testing.

## Reproduce unit and integration checks

```bash
export KRISTAL_FRAMEWORK_ROOT=/absolute/path/to/Kristal-Framework-v11.0.0-draft.4
export KRISTAL_AUTHORING_KIT_ROOT=/absolute/path/to/Kristal-Authoring-Kit-4.0.0-draft.3
python -m unittest discover -s tests -p 'test_*.py' -v
node --test tests/*.test.mjs
python tools/verify_manifest.py
```

A GitHub Actions CI workflow exists at `.github/workflows/ci.yml`, with read-only tests and checksum verification. The published record **does not establish that a remote GitHub run has occurred**. Unit-only execution without external Framework/Kit sources does not establish the same cross-repository qualification.

## Specific negative gates recorded

- Wrong Framework version, schema/tool drift and malformed semantic identities.
- Modified dictionary layer digest, invalid namespace and incompatible lexical candidate layers.
- Unknown diK receipt, source pins / catalog digest mismatch, unrecognized transform, idempotency mismatch, and output overwrite attempts.
- Host overlay reinstall safeguards and legacy CLI restrictions.

## Explicitly not qualified

- Running the delivered executable **diK alpha.7** to generate the source receipt being checked. The recorded receipt tests used **synthetic contract-conforming fixtures**.
- Real massive Wikidata dumps, authenticated human review, multiuser Konstellation Reader Policies, public HTTP/browser flows, and Astro/Svelte full build.
- Production publishing, Kubernetes deployment, Manager/Bootstrap/C1/C2/C3 approvals, disaster recovery, or complete v11/diK TCK certification.
- An Authoring Kit draft.4 pin update: Kit draft.3 still carries its reviewed draft.3 baseline.

Read [[Limits-and-Roadmap]], [[Verification-and-Release]], and [[Compatibility-Matrix]] before declaring an environment ready.
