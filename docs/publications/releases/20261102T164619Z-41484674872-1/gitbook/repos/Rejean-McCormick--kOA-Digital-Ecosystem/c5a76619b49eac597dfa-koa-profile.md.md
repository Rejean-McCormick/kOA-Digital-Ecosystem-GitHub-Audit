<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/2-Technical-Reference/40-integration/kristal-v6/koa-profile.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: 1a9bb0fe69aa30539f91b2b58a059015567726ca9f82def5f0dd79be4a9e0771 -->

# kOA profile for Kristal v6

The kOA profile keeps Kristal's representation semantics separate from ecosystem execution policy.

## Automation rule

A represented action with `actionability.mode = automatic` may be routed automatically only when all of the following hold:

- required inputs are complete;
- the relevant owner contract/profile exists;
- the caller possesses required authority;
- the receiving owner admits the request;
- no declared human review/decision requirement applies;
- no local safety/governance policy blocks it.

The receiving owner remains the only writer of its operational state. Human review and decisions should be returned as traceable decision/observed records when they materially affect future reasoning.
