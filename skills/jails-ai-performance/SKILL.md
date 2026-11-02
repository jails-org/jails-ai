---
name: jails-ai-performance
description: Diagnose and improve front-end performance and perceived fluidity using Core Web Vitals (LCP, INP, and CLS). Ask about the problem or explore the application when the developer does not know where to start; implement and verify focused fixes.
---

# jails-ai Performance

Invoke with `/jails-ai-performance` in GitHub Copilot Chat or `$jails-ai-performance` in agents supporting dollar mentions.

Investigate technical causes of poor UX, implement focused improvements, and verify their effects using Core Web Vitals and actual user journeys. Preserve intended design, content, and behavior. Do not expand a targeted request into unrelated optimizations or redesigns.

## Ask what the developer wants to solve

Start by asking: “What would you like to improve: initial loading, slow interactions, visual shifts, scrolling or animation smoothness, or a general investigation because you are not sure where to start?” Treat a specific issue already described in the request as the answer; do not ask it again.

For a known symptom, establish the affected route or journey and relevant conditions: device, browser, cold versus repeat visit, network, action, expected response, and observed delay. Ask only about missing details that matter; inspect available project context first.

If the developer does not know, says the application feels slow, or asks for a general review, proceed with exploratory diagnosis. Do not require them to name a metric, identify a root cause, or supply an audit report. If no answer has arrived, begin independent source and tooling discovery without treating silence as authorization for unrelated changes.

## Explore and establish a baseline

Locate the target application and affected routes from context. Read local instructions, package scripts, build configuration, relevant source, and existing performance tooling. Inspect `specification/readme.md` and the relevant domain/topic documents when present to preserve required behavior.

Read [the Core Web Vitals investigation method](references/core-web-vitals.md) before making code changes. Use its field-evidence, reproducible browser journey, source-attribution, and prioritization process. Load [the detailed CLS and font workflow](references/layout-shift.md) when visual instability or font loading is relevant, rather than assuming fonts are always the cause.

For a general exploration, inspect the entry route and a small representative set of routes selected from actual project structure: a content-heavy page and an interaction-heavy page when they exist. Exercise the key interactions rather than running a load-only audit. Expand coverage when findings indicate a shared cause or another important journey; report the scope actually explored.

Prefer production build and preview when available. Keep before/after conditions comparable: route, build, browser, viewport, data, cache state, network/CPU throttling, observation window, and interactions. Use existing tools first and choose the smallest set that answers the question; do not install a large audit stack or production telemetry by default.

If runtime tools are unavailable, complete source investigation and clearly separate suspected causes from verified ones. Prioritize concrete, traceable risks and disclose the missing baseline. Do not invent measurements, diagnose a metric from source alone, or describe a source review as a reproduced bug.

## Prioritize and improve

Connect each finding to an affected user action, metric or supplementary fluidity signal, evidence, owning source, and proposed fix. Prioritize user impact, strength of evidence, affected journeys, implementation risk, and expected benefit; do not chase the highest generic audit score.

For a general review, implement the highest-confidence improvements within the requested scope after explaining the findings briefly. Do not stop at a list of recommendations when implementation was requested. For an audit-only request, deliver findings without changing code. Investigate uncertain causes further rather than applying speculative fixes. Clarify product or design trade-offs only when existing requirements do not resolve them.

## Preserve jails-ai conventions

Apply [the shared architecture criteria](references/standards/ui-clean-architecture.md) when changing screen code. Resolve `ui-clean-arch` and relevant Jails skills through [the upstream catalog](references/standards/upstream-skills.md) when changing their abstractions or behavior. Preserve section ownership and existing application patterns; performance work does not authorize architectural replacement.

Read [the Tailwind standard](references/standards/tailwind.md) before styling changes and [the SVG/icon standard](references/standards/icons.md) when working with SVGs. Use built-in utilities for layout reservations where suitable and preserve the base Icon rendering boundary.

The supplied font workflow explicitly permits justified font-loading configuration and fallback metric descriptors such as `size-adjust`, `ascent-override`, and `descent-override`. Keep these scoped to the font-loading fix; this does not authorize unrelated Tailwind theme extensions, custom utilities, or visual redesign. Document any portability requirements introduced by the chosen font configuration.

## Verify and deliver

Make the smallest change supported by the investigation. Add or update meaningful regression checks for the changed behavior and configuration using existing tooling. Verify the affected loading or interaction journey, layout stability, readability, and any relevant font rendering; tests that only match configuration strings do not establish those outcomes. Run available checks, then repeat the relevant browser scenarios under comparable conditions.

Report the root cause and supporting evidence, files changed, chosen mitigation and trade-offs, verification results, and limitations. Distinguish measurements, visual observations, and hypotheses. Provide before/after values only when collected, identifying lab scope; do not claim field Core Web Vitals improved from a local run. Include explored routes, prioritized findings, remaining issues, and actual measurement conditions; report unmeasured metrics as unavailable, not zero. Do not claim CLS was eliminated or performance improved without measurement supporting that statement.
