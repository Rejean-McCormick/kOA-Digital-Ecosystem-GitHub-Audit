<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/06-surface-layer/06-implementation/43-definition-of-done-onboarding.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 514b2f75dd8193bd4ff78b9ed62a538bfcc7704555afbc4703b62ce7950dab85 -->

# 43. Definition of Done pour une application onboardée

Une application n'est considérée intégrée que si :

```text
[ ] stable module ID exists
[ ] valid module interface manifest exists
[ ] route contributions validate
[ ] local surface registration exists
[ ] runtime target resolves without arbitrary URL input
[ ] health/availability behavior is declared
[ ] framed mode works
[ ] immersive mode works if declared allowed
[ ] owner UI remains intact
[ ] owner navigation remains intact
[ ] no owner business code is copied into Koali
[ ] no owner secret is stored in manifest/browser state
[ ] auth behavior is documented
[ ] CSP/embed compatibility is explicit
[ ] offline/degraded behavior is explicit
[ ] negative security tests pass
[ ] build/runtime qualification passes
```

---
