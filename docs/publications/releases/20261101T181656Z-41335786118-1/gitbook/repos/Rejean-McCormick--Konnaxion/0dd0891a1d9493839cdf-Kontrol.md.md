<!-- Frozen source: https://github.com/Rejean-McCormick/Konnaxion/wiki/Kontrol | commit: 62c3bb451bacb4cfbbeb68181c1edfc7ba47a8f9 | SHA-256: 77c2df1b8dc7edc479b75b4fe682b6fe675bb7a7b34b7fd2fe3bb6c7b91901a1 -->

# Kontrol — Administration and Moderation

Kontrol is Konnaxion's administrative application surface.

Canonical backend:

```text
backend/konnaxion/kontrol/
```

## Current state

- `AuditLog`;
- `ModerationTicket`;
- `KonsensusConfig`.

The backend also exposes administration/reporting views for usage, performance and Smart Vote reporting.

## Current UI

```text
/kontrol/dashboard
/kontrol/audit-log
/kontrol/moderation/*
/kontrol/users/all
/kontrol/roles
/kontrol/konsensus
```

## Ownership rule

Kontrol may present and administrate multiple Konnaxion domains, but the existence of an admin screen does not transfer the underlying domain ownership to Kontrol.
