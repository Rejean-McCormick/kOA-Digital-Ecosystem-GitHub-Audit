<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/wiki/Communication-Request | commit: f187a43fc9540ce7d443ff4d2ab26dfdc7a48bfe | SHA-256: df62dab8bd9bcda300370ddb606e9e08545e8a88afe59e79c64eba8edea90676 -->

# Communication Request

`CommunicationRequest` is the canonical public input aggregate.

## Shape

```text
CommunicationRequest
  schema_version
  semantic_graph
  obligations
  supporting_context
  context
  constraints
  capability_profile
  runtime_selector?       # optional explicit RuntimeSet pin
  request_id?             # operational
  deadline?               # operational
```

## Example

```json
{
  "schema_version": "1.0",
  "request_id": "example:repair-4356",
  "semantic_graph": {
    "graph_id": "graph:repair-4356",
    "nodes": [
      {
        "id": "marcel",
        "kind": "entity_ref",
        "external_ref": "orgo:user/marcel",
        "labels": {"fr": "Marcel"}
      },
      {
        "id": "machine",
        "kind": "entity_ref",
        "external_ref": "orgo:machine/4356",
        "labels": {"fr": "machine 4356"}
      },
      {
        "id": "repair",
        "kind": "concept_ref",
        "concept_ref": "local-concept:repair"
      }
    ],
    "statements": [
      {
        "id": "repair_statement",
        "predicate_ref": "local-predicate:repair_event",
        "arguments": [
          {"role_ref": "semantic-role:agent", "value_id": "marcel"},
          {"role_ref": "semantic-role:patient", "value_id": "machine"},
          {"role_ref": "semantic-role:event_type", "value_id": "repair"}
        ],
        "polarity": "positive"
      }
    ]
  },
  "obligations": [
    {
      "obligation_id": "repair_task",
      "semantic_refs": ["repair_statement"],
      "force": "DIRECT"
    }
  ],
  "context": {
    "target_language": "fr",
    "target_locale": "fr-CA",
    "formality": "informal",
    "register": "operational"
  },
  "constraints": {
    "allowed_block_kinds": ["utterance", "list"],
    "opening_policy": "allowed",
    "closing_policy": "allowed",
    "list_policy": "allowed",
    "output_format": "structured"
  },
  "capability_profile": "orgo-operational-1"
}
```

## CommunicationContext

Context may control wording, pronouns, register, politeness and segmentation, but it must not alter the obligation set.

Typical fields:

- target language/locale;
- speaker and recipient;
- relationship;
- formality;
- politeness;
- register;
- tone profile;
- channel;
- bounded discourse context.

## PresentationConstraints

Constraints describe permitted presentation forms:

- allowed block kinds;
- opening/closing policy;
- list policy;
- terminology profile;
- optional maximum length;
- output format.

A hard constraint that can only be met by deleting required meaning makes the request unsatisfiable.
