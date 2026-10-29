# SEC-51 — Human Approval Is a Security Protocol

## Core principle

Human-in-the-loop is not automatically safe. Agents can frame, omit or overload information so a user approves a harmful action. Approval UX must bind the human decision to exact machine semantics.

## Security invariant

For high-impact agent actions, approval MUST show material target/scope/effect in a trusted UI generated from canonical structured data, not from model prose alone. Approval binds to a digest and expires.

## Senior architecture

Render a deterministic confirmation card from the typed proposal: operation, target, tenant, data affected, privilege/effect class, reversibility, expiry and key warnings. Keep model explanation separate and explicitly non-authoritative. On approval, sign/store the canonical proposal digest and revalidate policy at execution.

## Application to the supplied ecosystem

This mirrors Konfid approval/quorum semantics. Let AI assist with explanation, but Orgo/Konfid should own approval artifacts and policy. For release or emergency operations, require an independent trusted surface outside the agent conversation.

## Failure modes / anti-patterns

- “Are you sure?” in chat with hidden parameters.
- Model writes its own approval summary.
- User approves category “delete files” but agent chooses files later.
- Approval never expires.
- One click approves a batch whose membership can change.

## Evidence that proves the control

Mutation of proposal after approval invalidates execution. UI test derives critical fields from canonical data. Audit stores what was approved and by whom, distinct from model-generated rationale. Approval timeout and scope are enforced server-side.


## Reference anchors

- OWASP Top 10 for Agentic Applications 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- NIST AI 600-1 — Generative AI Profile: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- NIST SP 800-63-4 Digital Identity Guidelines: https://csrc.nist.gov/pubs/sp/800/63/4/final
