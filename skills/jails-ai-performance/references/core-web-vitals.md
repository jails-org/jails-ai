# Core Web Vitals investigation method

Use a hypothesis-driven loop: discover the symptom, collect a baseline, attribute the delay or instability, change the responsible code, and repeat the same journey. An audit recommendation is an investigation lead, not proof of a root cause.

## Choose evidence and tools

1. Inspect existing real-user monitoring or supplied reports when available. Public production URLs may have PageSpeed Insights or CrUX data. Distinguish route-level data from origin aggregates, mobile from desktop, and reporting windows. Lack of field data is not a blocker and does not imply good performance. Do not add telemetry or transmit private routes to external services without the appropriate authorization.
2. Build and preview the application using its documented commands. Use the available browser Performance panel or equivalent tracing for loading and actual interactions. Record network requests, main-thread tasks, layout/paint activity, and attribution to source where supported.
3. Use Lighthouse or existing audit tooling to discover loading and stability opportunities when useful. Complement load-only audits with real interaction recordings; do not use the overall Lighthouse score as the sole target.
4. Prefer standard metric tooling, such as existing web-vitals instrumentation, over a homemade metric calculator. Temporary diagnostic instrumentation should not become a permanent production dependency by accident. Report tool limitations instead of inventing unavailable capabilities.

Record the route, build mode, viewport, browser, CPU/network settings, cache state, dataset, and journey. Capture cold and warm visits where relevant. Under general exploration, include a mobile viewport and realistic throttling. Repeat noisy scenarios enough to identify variability; report the observed range or aggregate and sample count instead of cherry-picking a run.

## Diagnose loading: LCP

Identify the actual largest contentful element in the trace; do not assume it is the hero image. Break down the delay into server response, resource discovery/load, and element render delay where applicable.

Trace candidates in the application: slow document/data responses, serial request chains, render-blocking resources, oversized or poorly sized images, critical content hidden behind JavaScript, late font discovery, and main-thread work delaying rendering. Inspect assets and bundle output to confirm the trace, not to declare every large file a bottleneck.

Choose a targeted change: earlier discovery or appropriate priority for the actual critical resource, correctly sized/compressed media, removal of an unnecessary waterfall, or reduced work delaying content. Do not lazy-load the actual above-the-fold LCP resource as a generic image optimization or preload every asset. Preserve data freshness and application contracts when changing fetch/cache behavior.

## Diagnose responsiveness: INP

Exercise representative clicks, taps, and keyboard interactions: opening menus/dialogs, typing into search, filtering, changing tabs, and relevant form actions. Separate input delay, handler processing, and presentation delay using available traces.

Inspect long main-thread tasks, excessive synchronous computation, repeated Store reactions, broad DOM updates, forced layout, expensive rendering, duplicate listeners, and third-party execution. Attribute the slow interaction to actual source before changing it. For Jails, inspect subscriptions, selective reactions, state-to-DOM updates, and cleanup against the installed contracts.

Reduce unnecessary work, limit updates to affected sections, or split/defer noncritical work where safe. Preserve immediate feedback and correct results. Do not debounce every action or postpone visible feedback merely to move work out of a measurement. A slow network operation and a slow next paint are different problems; investigate both when the UX requires it.

INP needs interactions. A load-only Lighthouse audit reports TBT as a diagnostic proxy, not measured INP. A controlled browser interaction trace is lab evidence for that journey, not the site's real-user percentile. No interaction samples means INP is unavailable, not zero.

## Diagnose visual stability: CLS

Record shifts during loading and the relevant post-load journey, including content insertion and data updates. Identify the source of displaced content, reserve appropriate space, and follow [the detailed layout-shift workflow](layout-shift.md), including verification that intended fonts render.

Use standard CLS aggregation and input exclusions. Do not report every motion as CLS or declare stability from a final screenshot.

## Investigate perceived fluidity beyond the three metrics

Trace dropped frames, expensive scrolling/animations, layout thrashing, oversized DOM work, and delayed visible feedback when the symptom warrants it. Label frame timing, long tasks, request duration, or time-to-feedback as supplementary observations. Smooth scrolling is not measured by INP alone, and good LCP/INP/CLS values do not prove every interaction feels fluid.

## Prioritize and validate

Summarize findings with the affected journey, observed symptom, metric or signal, source attribution, confidence, proposed change, and trade-off. Separate confirmed offenders from source-only hypotheses. Prefer shared causes affecting important journeys, but keep changes within scope.

Repeat the same scenarios after each coherent fix. Check that improvements do not regress other metrics, readability, functionality, or design. If measurements are unchanged or worse, investigate, revise, or revert the unsuccessful change rather than claiming success. Do not disable required features to obtain a better score.

Use a compact before/after table when comparable data exists, and state when it does not. Field compliance depends on real-user distributions; a single local measurement does not establish it. Finish with actual findings and changes, remaining risks, tested coverage, and unavailable evidence.

## Authoritative references

- [Web Vitals](https://web.dev/articles/vitals): metric definitions and field/lab distinctions.
- [Core Web Vitals workflows with Google tools](https://web.dev/articles/vitals-tools): selecting diagnostic tooling.
- [Why lab and field data can be different](https://web.dev/articles/lab-and-field-data-differences): interpreting evidence.
- [Optimize LCP](https://web.dev/articles/optimize-lcp) and [optimize INP](https://web.dev/articles/optimize-inp): detailed attribution and mitigation.
