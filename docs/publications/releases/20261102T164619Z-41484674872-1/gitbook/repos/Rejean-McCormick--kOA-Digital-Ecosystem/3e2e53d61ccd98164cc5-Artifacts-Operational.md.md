<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/wiki/Artifacts-Operational | commit: dd52671208ae86295bfcc5f896d236a20182faba | SHA-256: 19de417ad4cda4305d76dc559e52f2c275cc74dfff690ca62a94c383ad25eb19 -->

# Operational integration artifacts

## Build Record

A Build Record may remain as **ecosystem correlation/reproducibility evidence**. It must not replace Kristal artifacts, kOA-Linux Release Sets, component active-state records or lifecycle receipts.

It should keep independent statuses for compilation, validation, recognition, publication and activation and reference the owning artifacts rather than re-declaring them.

## kOA-Linux Release Set

Release Set is the platform release compatibility artifact. It binds versions across independent release channels and carries compatibility/activation metadata under the kOA-Linux contract.

Digital Ecosystem's former `Release Record v2` is deprecated as an authority. If retained for analytics/audit compatibility, it is only a projection that references `release_set_id` and owner receipts.

## Runtime Pack local state

For kOA-Linux deployments, `kristal_runtime` owns:

- Runtime Pack verification/compatibility record;
- active Runtime Pack record;
- activation receipt;
- rollback receipt;
- runtime health state.

kOA Node Agent may execute the narrow privileged host transition required by the profile. A receipt does not replace the owner component's active-state record.

## Koali Space state

Koali Space activation/rollback/deactivation belongs to Koali Spaces and is unrelated to Kristal Runtime Pack active state.
