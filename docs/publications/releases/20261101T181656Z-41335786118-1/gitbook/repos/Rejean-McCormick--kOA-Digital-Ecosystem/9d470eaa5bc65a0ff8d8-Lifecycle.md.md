<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/90865538b0c16be08423843208f4c5e6785a7523/docs/1-Overview/Lifecycle.md | commit: 90865538b0c16be08423843208f4c5e6785a7523 | SHA-256: ed825273cf010774ac866e9e746e1409bbecf8efe19fa6b2229ceb973cb932c7 -->

# Lifecycle

kOA coordinates several independent lifecycles.

## Cross-system interaction

Where Interaction Kernel is adopted:

```text
sender-owned state
→ explicit versioned Profile
→ receiver authentication/authorization/admission
→ receiver-owned mutation/read
→ Receipt / Event / QueryResult
→ reconciliation
```

## Konnaxion decision → Orgo work

```text
Konnaxion deliberation/readings
→ finalized DecisionRecord
→ governance.decision.execute/1.0.0
→ Orgo Signal / WorkflowVersion / Case / Tasks
→ accountability.impact.publish/1.0.0 when applicable
→ Konnaxion impact/accountability state
```

## Knowledge acquisition → canon → projection

```text
source/provider discovery
→ EncyKlopedia acquisition evidence + referent candidates
→ encyklopedia.corpus-harvest-handoff/1.0.0
→ Da’at mapping / ACL
→ Kristal Referent Registry + Kristal State
→ Working Exchange
→ validation / authority recognition as applicable
→ Reference Exchange when recognized
→ Runtime Pack and/or UCKK consumer projection
```

Acquisition, validation/recognition and consumer projection are separate lifecycles.

## kOA-Linux release and Runtime Pack lifecycle

```text
Runtime Pack candidate
→ knowledge release channel
→ Release Set compatibility
→ kristal_runtime verification/compatibility
→ activation eligibility
→ active-state transition
→ activation receipt / runtime health
→ rollback + last-valid restore when required
```

kOA Node Agent is used only for the privileged host-facing transition required by profile/contract.

## Koali Space lifecycle

```text
Space definition
→ application/module admission
→ runtime registration/readiness
→ Space activation
→ surface resolution/rendering
→ rollback/deactivation
```

Koali Space activation is presentation lifecycle state and is not Runtime Pack activation.
