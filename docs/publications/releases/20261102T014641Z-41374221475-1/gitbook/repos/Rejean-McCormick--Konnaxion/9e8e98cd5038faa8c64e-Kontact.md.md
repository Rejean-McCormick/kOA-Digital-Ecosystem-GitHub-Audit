<!-- Frozen source: https://github.com/Rejean-McCormick/Konnaxion/wiki/Kontact | commit: 62c3bb451bacb4cfbbeb68181c1edfc7ba47a8f9 | SHA-256: 69ebd975e5bc96d7e7d2a305b6943c0b51659b9256a38fb347ba609e2b6f0cee -->

# Kontact — Networking and Opportunities Surface

Kontact is a **Konnaxion application/interface capability**, not a separate ecosystem system.

The current snapshot contains a frontend module under:

```text
frontend/modules/kontact/
```

with profile/opportunity UI including:

- `ProfileCard`;
- `OpportunityList`;
- `ConnectCenter`;
- `PublicProfile`;
- profile/opportunity hooks.

## Architecture rule

Kontact is a presentation/interaction surface. It must use the authoritative Konnaxion owner for profile, opportunity, project or EkoH data rather than creating a parallel backend truth simply because the UI groups those concepts.

If a dedicated backend capability is added later, its ownership must be declared explicitly rather than inferred from the frontend module name.
