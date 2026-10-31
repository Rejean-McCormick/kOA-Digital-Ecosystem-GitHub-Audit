<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/4ed4b8928665ebd723b68f8b3f2cb2f196d6374f/docs/2-Technical-Reference/40-integration/identity-oidc/oidc-profile.md | commit: 4ed4b8928665ebd723b68f8b3f2cb2f196d6374f | SHA-256: a90886b2785572d1946bb088f78403227b8ad195e17f126da425ce05ba1a990a -->

# kOA OIDC Profile

**Status:** Normative (kOA profile)  
**External normative reference:** OpenID Connect / OAuth specifications applicable to the selected client flow.

## 1) Required identity semantics

Applications implementing this profile MUST resolve users from the validated pair:

```text
issuer + subject
```

They MUST NOT resolve a federated identity from email alone.

## 2) Login resolution

```text
validate OIDC response
-> obtain issuer + subject
-> resolve local external-identity link
-> resolve local account
-> evaluate local authorization
```

If no local link exists, the application applies its own provisioning policy: deny, controlled linking, pre-provisioning, or approved JIT provisioning.

## 3) Token validation

Implementations MUST validate the security properties required by their OIDC client flow, including issuer, intended audience/client, signature, and expiry. Replay/CSRF protections applicable to the selected flow MUST be enabled.

## 4) Claims

Profile claims such as email, name, preferred username, and locale are attributes. They do not establish ecosystem identity and do not grant privileged roles by themselves.

## 5) Role claims

Mapping an IdP group/claim into a local role is OPTIONAL and MUST be explicit, allowlisted, tenant/context scoped, auditable, and locally revocable.

## 6) Token boundaries

A token issued for one application MUST NOT automatically be accepted by another application. Audience and client boundaries remain enforced.

Human SSO tokens MUST NOT be reused as business-bridge or service credentials.
