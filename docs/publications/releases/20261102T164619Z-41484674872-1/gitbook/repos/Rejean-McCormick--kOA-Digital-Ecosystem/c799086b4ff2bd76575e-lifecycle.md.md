<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/2-Technical-Reference/10-system/lifecycle.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: 7f7520dcfea2cb512b6f2e04fc1bd17f79df82bd83df9259cd6445b20cbb875d -->

# Lifecycle model

The ecosystem has multiple independent lifecycle axes.

## Kristal epistemic lifecycle

```text
Kristal State
→ Working Exchange
→ validation/review
→ authority recognition when applicable
→ Reference Exchange when recognized
→ Runtime Pack as permitted by policy
```

## kOA-Linux release lifecycle

```text
artifact production
→ registered artifact contract
→ release channel
→ Release Set compatibility
→ admission / authorization / resource checks as applicable
→ owner-component activation
→ receipt/evidence
```

## Runtime Pack local lifecycle

In kOA-Linux:

```text
candidate Runtime Pack
→ kristal_runtime validation/verification record
→ activation eligibility
→ atomic active_runtime_pack_record replacement
→ activation receipt
→ runtime health
→ rollback to last valid runtime when required
```

A kOA Node Agent transition is used only for the privileged host-facing part required by the active profile/contract.

## Koali Space lifecycle

```text
Space definition
→ application/module admission
→ runtime registration/readiness
→ Space activation
→ surface resolution/rendering
→ rollback/deactivation
```

This is presentation/application composition and must not be merged with the Runtime Pack lifecycle.

## Interaction delivery

Where IK is adopted, command/query/event delivery status remains separate from target-domain status. Existing kOA-Linux internal/component interactions remain governed by their canonical platform contracts until mapped/adopted explicitly.
