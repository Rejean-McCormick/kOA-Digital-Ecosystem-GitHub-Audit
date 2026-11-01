<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Scenario-Mosaic/blob/4ac4e787ef01295c9100c73d8b5bbf9a19d9ef03/docs/VALIDATION_V4_2.txt | commit: 4ac4e787ef01295c9100c73d8b5bbf9a19d9ef03 | SHA-256: f6d9a2a7e4a6bc5d7ab064997a459835677fb0afca0a7f75680ba2d3eeb1aa89 -->


> koali-scenario-mosaic@4.2.0 validate
> npm run validate:mosaic && npm run validate:repo && npm run validate:images && npm run validate:copy && npm run validate:i18n && npm run validate:name


> koali-scenario-mosaic@4.2.0 validate:mosaic
> node scripts/validate-mosaic.mjs

✓ 120 assignments
✓ 150 slots / 30 reserved
✓ exact 20 × 6 regular honeycomb panorama
✓ 8 contiguous 5 × 3 category territories
✓ panoramic viewBox ratio 3.57:1

> koali-scenario-mosaic@4.2.0 validate:repo
> python scripts/validate-repo.py

120 shared scenarios; 240 localized documents; 20 × 6 panoramic honeycomb; bilingual EN/FR routes

> koali-scenario-mosaic@4.2.0 validate:images
> python scripts/validate-images.py

Scenario PNGs available: 31 / 120; SVG fallback: 89
Bilingual scenario image validation passed.

> koali-scenario-mosaic@4.2.0 validate:copy
> python scripts/validate-copy.py

Preview-copy validation: 240 localized scenario documents checked (120 EN + 120 FR)
Bilingual scenario preview-copy validation passed.

> koali-scenario-mosaic@4.2.0 validate:i18n
> python scripts/validate-i18n.py

Bilingual contract: 120 shared identities + 120 EN + 120 FR editorial documents
Bilingual routing, content separation, language switch, and offline previews validated.

> koali-scenario-mosaic@4.2.0 validate:name
> node scripts/validate-name.mjs

✓ canonical brand: Koali
✓ positioning: Koali, the Sociotechnical Operating System
✓ bilingual interface names: Koali Scenario Mosaic / Mosaïque de scénarios Koali
✓ brand color: #1e6864
