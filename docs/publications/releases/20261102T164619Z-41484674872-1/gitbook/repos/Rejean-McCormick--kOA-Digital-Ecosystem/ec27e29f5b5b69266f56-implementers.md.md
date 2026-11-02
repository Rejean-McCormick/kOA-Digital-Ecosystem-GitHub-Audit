<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/2-Technical-Reference/60-guides/implementers.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: 7e8bc3f14c2d06810d12e734573fd942e8c9b2dbc3dfc9165b6b3449c789c177 -->

# Implementer guide

Implementers should preserve these separations:

```text
transport/delivery status ≠ domain status
domain status             ≠ epistemic status
compile                    ≠ validate
validate                   ≠ recognize
publish                    ≠ activate
```

## Orgo implementers

Reuse Signal/Workflow/Case/Task and IntegrationOperation/outbox infrastructure. Do not absorb provider models into Orgo core.

## Konnaxion implementers

Keep source events/readings/DecisionRecord in Konnaxion. Cross-system adapters should use explicit boundaries and must not write Orgo/Kristal/kOA-Linux stores directly.

## Da’at/Kristal implementers

Emit Kristal State or explicitly supported Kristal-native inputs. Never treat validation as a universal compile blocker. Keep source artifact status and recognition metadata explicit.

## Runtime/platform implementers

Provide one authoritative activation state, atomic activation, deterministic rollback, revocation/downgrade checks and complete evidence.
