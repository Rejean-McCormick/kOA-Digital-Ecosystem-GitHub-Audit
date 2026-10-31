<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Scenario-Mosaic/blob/4ac4e787ef01295c9100c73d8b5bbf9a19d9ef03/docs/48_SOFT_MAGNETIC_MOTION.md | commit: 4ac4e787ef01295c9100c73d8b5bbf9a19d9ef03 | SHA-256: 5e46634f435aa1404175c567364a2f534bb1892bbab5abff63ae201525bae1b2 -->

# Soft magnetic motion — v4.3.5

The territory-label interaction keeps proximity repulsion but removes the conspicuous repeated bounce that could read as visual flicker.

## Motion tuning

- Influence radius: `104px` (broader, gentler field)
- Maximum displacement: `11px` (was 15px)
- Force exponent: `1.95`
- Spring: `0.085` (was 0.15)
- Damping multiplier: `0.56` (was 0.77; substantially stronger damping)
- Pointer smoothing: `0.34`
- Per-axis velocity cap: `1.35px/frame`
- Settle distance: `0.06px`
- Settle velocity: `0.05px/frame`

The pointer position is low-pass filtered while moving. Character velocity is capped before integration. Together these changes preserve the magnetic deformation but make the return read as a soft settling motion rather than an oscillating bounce.

The same tuning is implemented in both the Astro/GSAP runtime and the zero-install offline preview.
