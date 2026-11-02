# Investigate and mitigate layout shift

Preserve the intended font, content, and design. Preventing the intended font from rendering, hiding content, or removing necessary UI is not a successful fix for instability.

## Before changing code

1. Inspect how fonts are declared and loaded: global and component CSS, `@import`, `@font-face`, fallback stacks, document `<head>` links, preconnects, preloads, `font-display`, requested families/weights/styles/subsets, and framework configuration. Trace the actual network discovery path, including duplicate or late requests and failed font responses.
2. If a browser is available, reproduce the affected page with a cold cache and throttled network. Install recording or observation before navigation where the tooling supports it, so early shifts are captured. Identify moving elements and timing through a performance trace, layout-shift tooling, or equivalent instrumentation. Inspect upstream causes as well as the displaced element: a heading can move because content above it grows.
3. Confirm the intended font loads **and renders** on the affected text. Inspect font requests and rendered-font information where available, including relevant weights and glyphs. A computed `font-family`, a successful download, or a resolved font-loading promise alone does not prove the visible text uses that face. If tooling cannot establish actual rendering, state that limitation.
4. Check competing CLS causes: images or embedded media without reserved dimensions, asynchronously inserted content, banners, late components, and changes in content size after data arrives. Do not attribute every shift to fonts solely because custom fonts exist.

When numeric CLS is available, use browser tooling or a standard metric implementation. Do not label a raw sum of every layout-shift entry as CLS: input exclusions and session-window aggregation matter. Observe the relevant loading and interaction period; a screenshot after everything settles cannot establish absence of earlier shifts. Record repeated runs when results vary, and retain their range rather than selecting only a favorable result.

If no browser is available, finish the source review before changing code, explain what remains unverified, and choose only mitigations justified by the available evidence. Do not claim reproduction or runtime success.

## Choose a mitigation based on the cause

Consider these options only where applicable:

- Move a late font stylesheet into the document `<head>` and preconnect early to the actual font origins. Avoid duplicate stylesheet requests and unnecessary connections.
- Self-host fonts when appropriate for the project and permitted by their license. Preserve the intended family, weights, styles, and required glyph coverage.
- Preload only truly critical font files with matching URLs, types, and cross-origin settings. Verify requests are reused instead of downloading twice. Do not preload every weight or compete unnecessarily with other critical resources.
- Keep a suitable fallback stack. When metrics differ materially, consider a dedicated fallback face with justified `size-adjust`, `ascent-override`, `descent-override`, and, when needed, `line-gap-override`. Derive values from the actual font pairing; do not copy arbitrary percentages from another project. Check browser support and rendering at relevant weights and widths.
- Reserve space for images, embeds, asynchronous content, banners, and late components using dimensions, aspect ratios, or appropriate existing layout patterns. Preserve responsive behavior and avoid clipping or excessive blank space.

Do not apply `font-display: optional` automatically. It can avoid a late swap by leaving the fallback visible for the visit. If selected, verify whether the intended font actually appears during the relevant cold-cache, slow-network, and repeat-visit conditions. If it does not satisfy the intended typography requirement, choose another strategy rather than presenting a lower shift score as sufficient.

Do not mask instability by permanently retaining the fallback, delaying all content until fonts arrive, or removing content. Evaluate readability and resource-loading trade-offs alongside layout stability.

## Validate the change

Run relevant build and existing checks. Add or adapt regression coverage for the actual failure where suitable: critical font request success, eventual intended-font rendering, stable content geometry through loading, or reserved media/content space. Use the available tools' rendered-font evidence when possible; geometry checks and font-loading promises are supporting evidence, not substitutes for it.

Repeat cold-cache and throttled-network checks at the affected viewport and a mobile viewport when possible. Include warm-cache behavior where font strategy changes it. Wait long enough to see delayed font swaps and asynchronous content. Preserve text readability, required glyphs, weights/styles, and relevant page behavior. Compare the same scenarios before and after.

Separate configuration checks from measured UX. Report any unavailable browser capabilities or unexecuted tests. Even a measured zero in a particular lab run is not proof of zero CLS in every session.

## Authoritative references

Consult current documentation when implementation or browser-support details require verification:

- [Optimize Cumulative Layout Shift](https://web.dev/articles/optimize-cls).
- [Optimize web fonts](https://web.dev/learn/performance/optimize-web-fonts).
- [Ensure text remains visible during webfont load](https://developer.chrome.com/docs/lighthouse/performance/font-display).
