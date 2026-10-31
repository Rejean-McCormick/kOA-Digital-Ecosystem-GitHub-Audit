<!-- Frozen source: https://github.com/Rejean-McCormick/kristal-public/blob/9a017c89e5fabb6d21f2a97fbe2f55cebd5cb2fd/docs/STAGING_INTAKE.md | commit: 9a017c89e5fabb6d21f2a97fbe2f55cebd5cb2fd | SHA-256: 0acfd16ac4b9fb52f69c03a2f3bf41e121e8e31cebaaccdc66c131b976f72313 -->

# Staging intake — exact hosted Kristal surfaces

**Status:** proposed, non-destructive integration runbook. Not a public publication instruction.

## Preconditions

- Confirm the exact Framework `10.0.0-draft.3.1` contract-set / immutable SHA, Authoring Kit 3.2.4+ version and Manager implementation in use. A ZIP snapshot name is not a commit pin.
- Choose an isolated, private staging directory and a **synthetic or explicitly approved nonsensitive** Kristal. Do not assume Zoology is approved for public exposure.
- Capture the original workspace `state_ref`, v9 commitments and source coverage. Build/check on a copy; never rewrite the canonical state to match an index.
- Assign read-surface ownership to the Kit and Manager, not to this repository's C3 validator.

## Controlled offline procedure

1. With the actual, verified Authoring Kit, run `check`, `build-v9`, `build-ai`, `check-ai`, and `read-surface --require-ready --compact` *according to that Kit's real CLI*, on an approved workspace copy. This is a **derived reader projection**, not semantic qualification.
2. Have the actual Manager generate an exact staging read surface and `kristals/<slug>/.kristal/sync-manifest.json` from the Kit output. The exact list, sizes, hashes, state reference, and surface digest must agree.
3. On **that isolated staging copy only**, use `python tools/c3_collection.py --repo <staging> build-index` to preview the projected index. After verification, `build-index --write` can write a **local candidate** index — not an approval to push.
4. Run `python tools/c3_collection.py --repo <staging> validate-index` and `candidate --slug <slug>`; verify the same state reference and state commitment as the workspace. Test missing files, altered bytes, duplicate slugs/state identities and unexpected files.
5. Obtain **independent** C1 qualification and a separate authentic, revocable C2 authorization at the exact digest/commit and approved destination, before **any** public GitHub write.
6. Have Bootstrap reconcile its managed-file drift with an owner-reviewed plan. Configure genuine GitHub branch/Environment protections and a trusted verifier outside the untrusted candidate tree.
7. Only after these gates and explicit operator approval may Manager synchronize an authorized public surface. Immutable release publication and activation are **separate** operations with separate policy and evidence.

## Fail-closed current state

The shipped Zoology surface contains a v9 snapshot but lacks its Manager manifest and AI reader entrypoint. **Do not manufacture these missing files or treat the collection root's genesis state as Zoology.** `validate-index` must remain blocked until the real producer outputs exist.

A local test fixture can pass structural validation without becoming a source of truth. No fixture output should be committed as real Zoology data.
