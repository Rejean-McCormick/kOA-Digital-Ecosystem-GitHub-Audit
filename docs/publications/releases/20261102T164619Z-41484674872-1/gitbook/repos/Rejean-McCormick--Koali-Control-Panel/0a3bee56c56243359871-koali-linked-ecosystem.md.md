<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Control-Panel/blob/7b476c20de7ac71332762a6e4e23cdde98f29148/docs/koali-linked-ecosystem.md | commit: 7b476c20de7ac71332762a6e4e23cdde98f29148 | SHA-256: be0a896ba8c84846581608e1d72c0abac2dd18d1c8177fc1129ee153e2a43f7b -->

# Koali linked ecosystem integration

The Control Panel delegates presentation composition to Koali Spaces and supplies local repository hints for the non-diagnostic snapshot components.

This integration does **not** change the existing `core_stabilization` qualification scope. It adds a linked-ecosystem inventory under `workflow.linked_ecosystem` and projects repository paths into the Koali Spaces process environment.

Diagnostics are not onboarded as Koali applications by this change. Existing diagnostic facilities in the Control Panel remain untouched as verification tooling.

Kristal Framework is provided to Koali Spaces only as a `reference_only` repository hint. Koali does not import Kristal theory or derive runtime semantics from the framework repository.

Owner applications remain autonomous. Orgo and Orgo Worlds are admitted as separate owner applications. SemantiK Architect, Konfid, and Kor are supervised headless services. Médiathèque kOA is admitted through its own `koali.integration.json` as a web owner surface while its `mediatheque-blank` content instance remains a separate qualified data root. Interaction Kernel, SemantiK Runtime Orchestrator, kOA Linux and the kOA Digital Ecosystem are linked as protocol/infrastructure/source repositories. Kristal Framework remains reference-only.
