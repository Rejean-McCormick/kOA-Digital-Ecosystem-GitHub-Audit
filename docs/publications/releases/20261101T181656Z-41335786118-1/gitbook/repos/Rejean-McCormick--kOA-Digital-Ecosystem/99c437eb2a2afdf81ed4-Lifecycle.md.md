<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/wiki/Lifecycle | commit: dd52671208ae86295bfcc5f896d236a20182faba | SHA-256: cafb148a1d4b02a3728de77e35af20210366b4dabce4eda0b0389e9ef8eda9ac -->

# Lifecycle

kOA coordinates several independent lifecycles.

## Cross-system interaction

Where Interaction Kernel is adopted:

```text
sender-owned state
→ versioned Profile/Envelope
→ receiver authentication/authorization/admission
→ receiver-owned mutation/read
→ Receipt / Event / QueryResult
→ reconciliation
```

Current kOA-Linux internal/component communication remains governed by its own canonical contracts until explicitly mapped to IK.

## Konnaxion decision → Orgo work

```text
Konnaxion deliberation/readings
→ finalized DecisionRecord
→ target cross-system handoff/Profile
→ Orgo Signal / WorkflowVersion / Case / Tasks
```

## Kristal v5 epistemic lifecycle

```text
source / structured input
→ Structured Epistemic State
→ Working Exchange
→ review / validation
→ authority recognition when applicable
→ Reference Exchange when recognized
→ Runtime Pack under policy
```

## kOA-Linux release and Runtime Pack lifecycle

```text
Runtime Pack candidate
→ knowledge release channel
→ Release Set compatibility
→ kristal_runtime verification/compatibility
→ activation eligibility
→ active_runtime_pack_record transition
→ activation receipt / runtime health
→ rollback receipt + last-valid restore when required
```

A kOA Node Agent operation is used only for the privileged host-facing transition required by profile/contract.

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
