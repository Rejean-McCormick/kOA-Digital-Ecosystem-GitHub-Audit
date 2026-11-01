<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/90865538b0c16be08423843208f4c5e6785a7523/docs/1-Overview/Operations-Incident-response.md | commit: 90865538b0c16be08423843208f4c5e6785a7523 | SHA-256: e11825798d9a0098e3919fa352d531b9a3fff4920f6e27cc305745f630012889 -->

# Incident response

Incidents are handled by the owner of the affected state.

- **Konnaxion:** civic/governance state and DecisionRecords.
- **Orgo:** workflow/work state, IntegrationOperations, outbox/retries.
- **Kristal/Da’at:** epistemic artifacts, validation/recognition/reference semantics and mapping boundary.
- **kristal_runtime:** Runtime Pack verification/compatibility, active Runtime Pack state, activation/rollback receipts and runtime health.
- **kOA Node Agent:** privileged node-local lifecycle operation failures/receipts.
- **kOA-Linux Release Set/channels:** release compatibility/admission failures.
- **Koali Spaces:** Space activation, presentation routing, runtime registration/readiness and rendering failures.
- **Interaction Kernel:** adopted Profile/protocol conformance and delivery issues.

## Runtime Pack incidents

Inspect `kristal_runtime` owner records first. If the failure is in the privileged host transition, inspect the corresponding kOA Node Agent receipt. Do not create a parallel Runtime Activation State in Digital Ecosystem or Konnaxion.

## Koali incidents

A Space/surface readiness failure is not a Runtime Pack activation failure unless the underlying runtime owner actually reports one.
