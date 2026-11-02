<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/2-Technical-Reference/20-nodes/yesod-compiler.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: 11517dea5565bf12db12ec9a779f5dd1f9de63aa4158ba9f8cc17dd19332883a -->

# Yesod — compilation coordination role

Yesod is a conceptual kOA role for coordinating deterministic compilation work. Kristal remains the owner of Kristal compilation semantics and artifact schemas.

## Kristal v6 rule

Compilation and validation are separate. A policy may allow:

```text
Kristal State
→ compile
→ Working Exchange
```

before validation or authority recognition is complete.

Therefore Yesod/Orgo must not implement a universal “no compile on fail” assumption.

## Stage-specific gates

A deployment/profile may instead gate specific later transitions, for example:

- eligibility for Reference Exchange status;
- publication to a reference channel;
- distribution;
- production activation;
- Reader Policy visibility.

Build evidence must record the actual status of each transition separately.
