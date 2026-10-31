<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Linux-Koali/wiki/AI-and-External-Integrations | commit: a014d6b410b475fe227e3f0153bbae6e54ef0520 | SHA-256: 4ee1e217fa4ab5962cfe490e14db2362886392b28b9e0a51897c559fe4af30e1 -->

<!-- Navigational projection. Normative authority remains in the repository docs/ corpus. -->

# AI and External Integrations

> **Authority notice:** This wiki is a readable navigation layer. Source contracts, accepted ADRs, normative documents, and executable validators in the repository remain authoritative.

## Baseline rule

AI is optional, capability-scoped, attributable, and unable to create invisible authority. Core operation remains deterministic and does not require native generative AI.

External outputs remain non-authoritative unless an explicit review and admission process transfers accepted facts into an authoritative owner.

## Declared integrations

| Integration | Type | Role | Authority | Availability | Contract |
| --- | --- | --- | --- | --- | --- |
| Ariane Voice | external_voice | Optional voice-input surface for Ariane. | non_authoritative | optional | [contract](../blob/main/docs/contracts/integrations/ariane-voice.integration.json) |
| ChatGPT | external_ai | Approved candidate metadata and analysis surface. | non_authoritative | optional | [contract](../blob/main/docs/contracts/integrations/chatgpt.integration.json) |
| Gamma | external_media_service | Optional external presentation surface. | non_authoritative | optional | [contract](../blob/main/docs/contracts/integrations/gamma.integration.json) |
| Suno | external_media_service | Optional external media-generation surface. | non_authoritative | optional | [contract](../blob/main/docs/contracts/integrations/suno.integration.json) |

## Boundary rules

- explicit user or system authorization;
- declared capability and data scope;
- no silent provider substitution;
- no direct mutation of authoritative state;
- privacy, consent, disclosure, and cultural-rights controls;
- bounded failure and safe degradation when the provider is unavailable.

## Sources

- [`docs/02-system/09-ai-boundary.md`](../blob/main/docs/02-system/09-ai-boundary.md)
- [`docs/02-system/10-external-ai-surfaces.md`](../blob/main/docs/02-system/10-external-ai-surfaces.md)
- [`docs/02-system/16-external-integrations.md`](../blob/main/docs/02-system/16-external-integrations.md)
- [`docs/07-security/11-ai-boundaries.md`](../blob/main/docs/07-security/11-ai-boundaries.md)
- [`docs/07-security/12-external-integration-classification.md`](../blob/main/docs/07-security/12-external-integration-classification.md)
- [`docs/contracts/integration-types.contract.json`](../blob/main/docs/contracts/integration-types.contract.json)
