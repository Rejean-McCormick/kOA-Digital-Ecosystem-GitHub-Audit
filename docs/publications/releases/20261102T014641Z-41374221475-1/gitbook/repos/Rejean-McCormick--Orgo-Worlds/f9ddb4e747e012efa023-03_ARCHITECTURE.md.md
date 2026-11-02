<!-- Frozen source: https://github.com/Rejean-McCormick/Orgo-Worlds/blob/c2445db8abf78afcb647f22615ad3b9dd132bde8/docs/Technical-Reference/Worlds/03_ARCHITECTURE.md | commit: c2445db8abf78afcb647f22615ad3b9dd132bde8 | SHA-256: a429ea2153195ec1a156ad7728e9cd629e4f9954a603e81ed99240528e163f55 -->

# Architecture

```text
Browser / Orgo World Manager
        │
        └── /api/control/worlds/...
                     │
               WorldsService
                     │
      World / Release / Membership
                     │
        runtime/orgo-worlds-state.json
```

`Orgo_Worlds` is now a standalone World control/routing package. It does not
import the Orgo operational runtime and does not own `Signal`, `WorkflowVersion`,
`Case`, `Task`, `IntegrationOperation`, Outbox or provider adapters.

Cross-system Interaction Kernel traffic terminates in the main `Orgo` product.
World identifiers may be carried as routing/provenance metadata, but the Worlds
repository must not recreate the operational engine.
