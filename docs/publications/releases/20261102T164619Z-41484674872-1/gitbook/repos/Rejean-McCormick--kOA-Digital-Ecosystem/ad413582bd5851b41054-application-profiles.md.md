<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/2-Technical-Reference/40-integration/identity-oidc/application-profiles.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: 3890374849a7f5e40842abdad0d13a0aa2c652893d17549d6953802355c661ab -->

# Application Identity Profiles

**Status:** Normative boundary profile; implementation maturity differs by application.

## 1) Orgo

Orgo uses a local account and local authorization model. When OIDC is enabled, the target resolution is:

```text
issuer + subject
-> Orgo local user
-> organization memberships
-> Orgo roles/permissions
```

The current Orgo implementation already contains local auth, SSO/OIDC, and identity services; implementations SHOULD extend those primitives rather than create a parallel identity subsystem.

## 2) Konnaxion

Konnaxion MUST keep a local account and local authorization model. OIDC support and account-linking details are implementation-specific and MUST be verified in the active runtime before conformance is claimed.

The Orgo<->Konnaxion business bridge is not an identity provider and MUST remain separate from human authentication.

## 3) UCKK-Moodle

UCKK-Moodle MUST retain local users, enrolments, roles/capabilities, academic authority, and administrative recovery.

```text
issuer + subject
-> Moodle local user
-> enrolments / contexts
-> Moodle roles/capabilities
```

Identity federation does not transfer UCKK-local academic/publication permissions to Orgo or Konnaxion. Konnaxion/eThikos decision authority is a separate business-domain concern and is not derived from OIDC roles.

## 4) Service integrations

Konnaxion/eThikos→Orgo decision handoff, Orgo→Konnaxion impact/publication, workers, and callbacks use dedicated machine credentials/scopes rather than human SSO sessions. Optional UCKK publication/distribution integrations use their own service identity when needed.
