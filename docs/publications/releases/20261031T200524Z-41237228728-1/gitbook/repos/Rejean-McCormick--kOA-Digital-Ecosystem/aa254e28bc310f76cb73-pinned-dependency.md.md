<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/4ed4b8928665ebd723b68f8b3f2cb2f196d6374f/docs/2-Technical-Reference/40-integration/kristal-v5/pinned-dependency.md | commit: 4ed4b8928665ebd723b68f8b3f2cb2f196d6374f | SHA-256: d192d44882ce88c1eba4112de7683ff4095ef8064a5074cdc2cc162a671ff23d -->

# Kristal dependency and contract baselines

kOA integrations must distinguish a **contract baseline** from an **immutable release pin**.

## Historical v5 knowledge-contract baseline

```text
version                  5.0.0-rc.3
status                   release-candidate
referent registry        kristal.referent-registry/1.0.0
knowledge-model bundle   sha256:07fe0527ab29a4b40870efdd0c9e0c67c91de919e5428047245b2a2c04f8ea98
canonicalization         kristal.v5:jcs-rfc8785 / 1
```

The supplied rc.3 release metadata declared tag `v5.0.0-rc.3` but did **not** resolve it to an immutable commit SHA (`commit: null`). This historical boundary therefore froze the contract set without claiming rc.3 was a fully resolved published release. The active ecosystem baseline now uses Kristal Standard `6.0.0` pinned by content digest.

## Existing immutable downstream locks

Some downstream integrations may still pin an older immutable Kristal release. Those locks remain valid for their own scope until the owning integration explicitly updates and requalifies them. The new knowledge-projection baseline must not silently rewrite unrelated locks.

## Rule

For any conformance or release claim:

1. identify the exact integration scope;
2. identify the exact Kristal contract/release used by that scope;
3. reject floating references such as `main`, `latest` or `5.x`;
4. require tag + immutable commit for claims that depend on a published immutable release;
5. record the contract-set/model digest where the boundary defines one.
