# Navigation refactor — guide-architecture-interfaces-ia-v2

This refactor applies the supplied `senior-interface-ux-patterns-v2` guide,
particularly `AI_INGESTION.md`, UX-01, UX-05, UX-08, and UX-15–UX-18.
The guide calls for workflows organized by user intent, not by technical modules.

## Daily journey (dominant)

**Select an application → inspect categories and checked sources → read evidence →
open its technical profile if needed → consult the corresponding dated campaign.**

The dashboard now has three independent spaces:

1. **Validations** — the first screen; source-checked, scope-limited documentary
   proof, CI historical observations, and review criteria. Only verifiable
   documentary claims receive green ticks.
2. **Applications** — the system dossier and measured Engineering Profiles.
   Kristal's map is a contextual subview, not an independent competing home.
3. **Campagnes** — separate current-state coverage from immutable past captures,
   with original private reports available only on the loopback server.

The Windows launcher also has only four major tabs: **Pilotage**, **Dossiers des
systèmes**, **Campagnes datées**, and **Outils avancés**. The ten original
capabilities are retained in nested workspaces. Publishing, remote audits,
diagnostics and configuration are accessed via advanced tools. The daily
launch action is not duplicated in advanced settings.

## Old → new navigation mapping

| Previously top-level | Now |
|---|---|
| Écosystème | Pilotage (open dashboard) |
| 49 dépôts | Dossiers des systèmes → Registre des 49 |
| Preuves 245 | Dossiers des systèmes → Preuves et sources |
| Certification | Dossiers des systèmes → Qualification et profils |
| Campagnes | Campagnes datées |
| Rapports | Outils avancés → Rapports |
| Audit local | Outils avancés → Audit local |
| Vérification | Outils avancés → Vérification |
| GitHub | Outils avancés → GitHub |
| Historique | Outils avancés → Diagnostics historiques |
| Kristal source / publication | Outils avancés → Sources et publication |

The dashboard keeps old `#apps`, `#cartographie`, `#qualification` and
`#historique-campagnes` deep links working. When switching applications and
proof categories, selection remains in context. The 53 security and 33
architecture criteria are progressively disclosed rather than showing all
86 rows by default.

## Sources of truth and preserved safety

- `koa_audit.validation_board` is still the only source for green documentary
  ticks, bound to verified original SHA-256 evidence and explicit scope.
- A successful historical CI workflow is not interpreted as a complete test
  suite pass or security certification.
- The 245 stage conclusions do not change dated campaigns retroactively.
- Only the local launcher serves private evidence APIs; the published site
  never receives these responses.
- There are no new Git scans, background checks or extra network calls.
- Source clones, Git history, existing evidence and public publishing
  controls are unchanged.

## Acceptance scenarios

1. Launch → choose Konnaxion → Tests → open historical E2E source;
   its dates and limited scope remain visible.
2. Switch to Sécurité → inspect catalogue; no unsupported green check.
3. Open Applications → Engineering Profile → select Kristal map → return to
   same application dossier.
4. Open Campagnes → read date and latest frozen snapshot; on public Pages
   the private campaign link is hidden and explained as unavailable.
5. Open Windows **Dossiers** → select a repo in the registry → navigate
   directly to its qualification editor.
6. Open **Outils avancés** and confirm local audits, diagnostics and
   explicit GitHub publishing are still available with the original safeguards.
