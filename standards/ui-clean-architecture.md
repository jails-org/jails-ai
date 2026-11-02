# UI Clean Architecture acceptance criteria

Apply these criteria together with the actual `ui-clean-arch` skill and its specification, resolved through [the upstream catalog](upstream-skills.md). This checklist makes the required structure explicit; it does not replace the upstream specification.

## Decompose before implementing

Identify the screen's meaningful sections from the requirements and layout before writing its markup. Map each section to a structural Component with a responsibility and destination file. Keep this map as a short implementation note, and update it if the design changes. Architectural decomposition is part of implementation, not an optional cleanup after visual completion.

A structural Component represents a meaningful screen section, independent of desktop/mobile arrangement. A grid, flex wrapper, or responsive column does not define a Component by itself. Buttons, icons, and individual list rows do not automatically become structural Components.

## Required composition boundaries

- A screen owns a domain. Its root `index` imports structural Components and composes the screen.
- Each structural Component owns a folder under `domain/<screen>/components/<section>/` with an `index` entry using the framework's extension. In the Starter-Kit this is normally `index.astro`, with a colocated Jails controller when behavior is needed.
- Put section markup and section-local behavior in its structural owner. Do not implement several meaningful sections as inline blocks in the route or domain index. Naming HTML blocks, adding comments, or creating empty component files does not establish these boundaries.
- The route delegates to the domain screen using the framework's conventions. The domain index may contain layout wrappers and composition markup, but must not become the implementation of all sections.
- Extracted atomic components remain inside their structural owner's folder. Atomic extraction is optional; do not create a file for every element or impose a minimum component count. A genuinely single-section screen can have one structural Component, while still preserving route, screen composition, and section ownership.
- Keep screen-exclusive resources in the domain. Use shared resources for cross-domain reuse; never import another domain or let shared import a domain.

Illustrative Astro mapping for an orders screen with three meaningful sections:

```text
src/pages/orders.astro                       # Delegates to the domain screen
src/domain/orders/index.astro               # Composes sections and layout
src/domain/orders/components/summary/index.astro
src/domain/orders/components/filters/index.astro
src/domain/orders/components/results/index.astro
```

The section names and number of sections come from the actual screen. Do not reproduce this tree mechanically.

## Place behavior in the correct abstractions

- Components own markup and behavior confined to their section without persistence.
- Cross-component propagation or persistence uses the screen Store and actions. Follow the upstream single-Store, complete-state notification, and selective reaction contracts; do not replace screen coordination with direct updates between sections.
- External integrations belong in stateless Service functions with a single object input and Promise-of-object-or-list output. Components and Stores do not call fetch or storage APIs directly.
- Entities perform pure, synchronous, stateless adaptation of received data. Follow the upstream destructured-object input and semantic output conventions.
- Keep Stores, Services, and Entities independent of the UI framework. Put TypeScript definitions in context-owned `types.ts` files, preserving dependency boundaries.
- Create abstractions for actual responsibilities, not empty folders or pass-through files to satisfy a diagram. Direct access to inner layers remains allowed by the upstream dependency rules.

## Completion review

Inspect the actual source and imports before declaring the page complete:

1. Match every identified structural section to its owning component file and confirm the domain index imports and renders it.
2. Inspect the route and domain index for section implementations that should have been extracted. A visually correct page or passing build does not satisfy architecture if those sections remain in one file.
3. Trace state propagation, persistence, integrations, and data adaptation to their owning abstractions. Explain genuinely inapplicable abstractions rather than generating placeholders.
4. Check dependency directions, domain/shared separation, type placement, and source readability.

Correct violations within the requested screen before delivery. Report the domain, structural component files, and applicable Store, Service, and Entity responsibilities so the implementation is reviewable.
