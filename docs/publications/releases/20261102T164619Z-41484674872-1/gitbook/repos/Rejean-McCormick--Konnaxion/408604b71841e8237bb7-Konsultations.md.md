<!-- Frozen source: https://github.com/Rejean-McCormick/Konnaxion/wiki/Konsultations | commit: 62c3bb451bacb4cfbbeb68181c1edfc7ba47a8f9 | SHA-256: 9ddae0a14418c0b48891c1ec31c3d3cda976645abf09620843735e514d30b0db -->

# Konsultations — Consultation and Formal Participation

Konsultations is Konnaxion's logical consultation/intake/formal-participation boundary.

The current snapshot contains a dedicated frontend `konsultations` module and ethiKos demo-import structures for consultations and consultation votes. The architecture rule is more important than physical placement: **formal source participation must remain distinct from Smart Vote derived readings and from Korum topic stances.**

## Responsibilities

Konsultations covers product capabilities such as:

- consultation intake and listing;
- consultation detail;
- suggestions;
- formal participation/vote capture where the protocol calls for it;
- result presentation;
- impact/accountability timeline.

## Source ownership

A formal consultation ballot is a source fact of its consultation protocol.

```text
consultation ballot
≠ EthikosStance
≠ Smart Vote reading
≠ Orgo Task
```

## Smart Vote relationship

A consultation can be bound to Smart Vote through an explicit source/consultation mapping. Smart Vote may calculate a contextual reading, but the reading does not overwrite the source ballot.

## Orgo relationship

No active Orgo adapter is implemented in the current Konnaxion snapshot. A future workflow integration must treat Orgo Case/Task as external workflow objects, not as aliases for Konnaxion consultations.
