<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/4ed4b8928665ebd723b68f8b3f2cb2f196d6374f/docs/1-Overview/FAQ.md | commit: 4ed4b8928665ebd723b68f8b3f2cb2f196d6374f | SHA-256: 90d035a49c04ba6ca5e8ce8e3ca85a9c8fc4e67f20fcdfc4746ac7af69449d6b -->

# FAQ

## Is Orgo the global control plane?
No. Orgo owns workflow/operational state represented inside Orgo.

## Does every cross-system interaction already use Interaction Kernel?
No. IK is the target cross-system Profile layer. kOA-Linux already has canonical internal/component contracts; explicit adoption/mapping is required before calling those interactions IK-conformant.

## Must Kristal validation pass before compilation?
No. Kristal v6 may preserve a working Kristal State before final validation/recognition; artifact status, validation and recognition are separate.

## Who owns Runtime Pack activation on kOA-Linux?
`kristal_runtime` owns Runtime Pack verification/compatibility, active Runtime Pack state and activation/rollback receipts. kOA Node Agent performs the narrow privileged host transition when required by the active profile/contract.

## What does Release Set own?
Release Set binds compatible versions across platform release channels. It does not replace Kristal validation, `kristal_runtime` active state or Koali Space state.

## Is Koali Space activation the same as Runtime Pack activation?
No. Space activation changes presentation/application composition. Runtime Pack activation changes the active knowledge runtime state.

## Is Konnaxion's Koali pilot still pending?
The supplied Koali maturity report contains a later notice recording a successful Konnaxion pilot, although two Koali current-state reference pages still contain older “pilot pending” language. Digital Ecosystem treats those pages as product-documentation drift awaiting refresh.
