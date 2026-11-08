# Visual reproduction from an image

Use this workflow when a screenshot or layout image defines the requested screen. The default target is at least 95% measured visual similarity at each supplied reference viewport. This is an acceptance target for the captured view, not a guarantee of identical behavior, responsive fidelity at unseen widths, or universal perceptual equivalence.

## Establish the reference

Inspect the actual image with available image tools before coding. Preserve its original file, dimensions, and aspect ratio. Record the source, route, visible state, image pixel dimensions, known CSS viewport, device scale factor, scroll position, and any browser chrome or crop. Image pixels do not necessarily equal CSS pixels. If viewport metadata is absent, use a documented working assumption and do not present it as observed fact. Exclude browser chrome from both captures consistently; never crop away application mismatches to improve the score.

Read the root specification index and store a concise visual contract in the owning domain document or linked topic file. Record:

- Section boundaries and bounding boxes, page/container widths, column proportions, alignment anchors, gaps, padding, repeated dimensions, and vertical rhythm.
- Visible text verbatim, line breaks and wrapping, font family candidates, weight, size, line height, letter spacing, and text width. Mark unreadable content as uncertain instead of inventing confirmed copy.
- Backgrounds, foreground colors, borders, radii, shadows, image aspect ratios, crop positions, icon shapes, and layering.
- Supplied assets, matching repository assets, missing assets/fonts, and confidence in inferred values.
- Reference viewports, comparison regions, metric configuration, threshold, and unresolved constraints.

Measure rather than substituting familiar design defaults. Inspect enlarged crops for typography and small details. Separate measured image coordinates from estimated CSS values. Map the same meaningful sections to structural Components using the page implementation workflow.

## Resolve fonts, assets, and styling constraints

Search supplied files and repository assets before choosing substitutes. Match the actual font and weight where available; verify font loading rather than accepting fallback text. Match image crop and object positioning, not only the image subject. Route SVG artwork through the shared Icon component. Do not replace distinctive artwork or logos with emoji, generic icons, or invented assets and describe them as faithful reproductions. Do not render the reference image as the page or use it as a background to simulate implementation.

Read the bundled Tailwind, icon, and architecture standards linked by the main skill. Choose the closest permitted built-in utilities by measurement. A screenshot alone does not authorize custom CSS, arbitrary values, custom tokens, or inline styles. If the permitted values cannot satisfy the target, document the concrete discrepancy and required customization, complete independent permitted work, and ask for explicit direction before introducing that customization. Report an unmet target honestly if the constraint remains. Do not silently redesign the reference to fit a preferred component library.

## Implement and capture under controlled conditions

Build geometry first, then typography and wrapping, assets, colors, and fine details. Reuse structural Components without flattening the screen into one file. Use layout relationships rather than absolute positioning every element; use absolute placement only where the reference's actual layering calls for it.

Use the project's available browser tooling to open the implemented route. Match the reference CSS viewport, device scale, zoom, scroll position, theme, content, and UI state as closely as evidence permits. Wait for fonts, images, and layout to settle. Disable animations and transitions during capture and fix time-dependent fixture data when appropriate, recording those controls. Capture at the reference dimensions without stretching either image. Compare a viewport screenshot to a viewport screenshot; compare full-page images only when both represent equivalent full-page content.

For multiple references, validate each independently. For an unseen mobile or desktop width, verify usability, overflow, content order, and interactions separately; label the resulting layout as inferred rather than claiming measured reference fidelity.

## Compare, correct, and verify

Use image-comparison tooling available in the environment. Save the reference, actual screenshot, a 50% opacity overlay, a difference heatmap, and a machine-readable report in the project's existing artifact location or a temporary output directory. Keep tool dependencies scoped to the available environment; do not replace project tooling merely to obtain a score.

Define the metric before tuning the implementation. Prefer an existing project visual-regression metric when it has a documented threshold. Otherwise use SSIM on equal-size, consistently decoded RGB images, with data range 255 and recorded library/version and parameters. Set similarity to `100 * SSIM`; the default passing threshold is 95. Do not call a raw pixel-match percentage, SSIM, and human judgment interchangeable measures of accuracy. If using a different metric, record its definition and justify its threshold rather than translating its score into SSIM.

Compute scores for the whole image and each meaningful section defined in the visual contract. Include critical small regions such as the main heading, primary action, logo, and navigation when present: large blank areas can hide significant errors in a global score. Keep region coordinates fixed to the reference and compare the same coordinates in the actual capture. With the default metric, require both global and each declared region score to reach 95. Do not lower thresholds, redefine regions after observing failures, downscale away detail, auto-align displaced content, or exclude static content to obtain a passing result.

Inspect the overlay and heatmap visually as well as the scores. Correct the largest discrepancies in this order when applicable: missing sections/assets, container geometry and placement, font and wrapping, spacing and dimensions, then colors/borders/shadows/icons. Re-capture and re-run comparison after corrections. Record each iteration's scores and remaining discrepancies. A score above threshold does not excuse visibly wrong text, missing controls, incorrect assets, clipping, or architecture violations.

Use masks only for genuinely unavoidable dynamic content, documenting coordinates and rationale before comparison. Report excluded area and do not claim fidelity for masked content. Do not mask mismatches caused by the implementation.

Continue while meaningful corrections are available. After three consecutive correction passes without measurable improvement, diagnose the blocker and report the remaining gap rather than endlessly tuning. Resume when a missing asset, font, permission, or environment capability becomes available. If browser capture, the reference file, or comparison tooling is unavailable, continue supported implementation work and report visual verification as incomplete; never manufacture a score or claim the 95% target was achieved.

## Completion evidence

Update the domain specification with the actual verification status. Report reference and actual capture paths, overlay/diff/report paths, viewport assumptions, metric and parameters, global and per-region scores, excluded areas, and unresolved discrepancies. State whether the target was met for each supplied viewport. Keep functional, accessibility, responsive, and structural architecture checks separate: a visual similarity score does not prove them.
