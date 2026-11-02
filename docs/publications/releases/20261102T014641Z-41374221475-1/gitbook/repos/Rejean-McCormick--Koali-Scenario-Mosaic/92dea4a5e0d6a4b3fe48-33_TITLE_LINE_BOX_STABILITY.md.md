<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Scenario-Mosaic/blob/4ac4e787ef01295c9100c73d8b5bbf9a19d9ef03/docs/33_TITLE_LINE_BOX_STABILITY.md | commit: 4ac4e787ef01295c9100c73d8b5bbf9a19d9ef03 | SHA-256: e68579b9a0abe0b5a26f2335bc4c35941820a10fa7b7c2e0ed51a5d4f44f01d0 -->

# Title completeness and line-box stability — superseded

The v4.3.1 implementation reserved a fixed three-line title box and selected a
font size from the title's character count. That rule is superseded by the
current preview layout contract.

## Current rule

- The title has natural height and uses at most two visible lines.
- It starts at the normal display size.
- `preview-layout.ts` progressively reduces only the title font size until the
  text fits on two lines.
- The reduction stops at a readable minimum.
- If an extreme title still does not fit, the browser clamps it to two lines.
- `text-wrap: balance` improves the distribution of words.

The fit is measured from rendered dimensions rather than character count. It
is recalculated after scenario changes, width changes, browser zoom, and font
loading. No fixed one-, two-, or three-line height is reserved.

## Stability invariant

The title, summary, and example remain naturally packed at the top. A flexible
row absorbs the remaining height. The CTA and action palette stay anchored at
the bottom of block 2, so title fitting does not move the functional baseline.

See `PREVIEW_LAYOUT_INTERACTION_CONTRACT.md` for the active contract.
