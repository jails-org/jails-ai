# Page implementation workflow

Use this workflow within `jails-ai-spec` whenever creating or modifying a screen. Record requirements in the owning domain folder under the application-root `specification/`, with general/shared information in `specification/readme.md` and verify both visual and functional acceptance criteria.

## Inspect the application and starter examples

Locate the target application from the working directory and context. Ask for its path only if ambiguous. Read local instructions, package scripts, installed versions, routes, layouts, components, aliases, and styles. If no application exists, direct the user to `jails-ai-setup`; do not silently scaffold or replace a project.

Before implementing, read the examples already present in the scaffold created from [jails-org/Starter-Kit](https://github.com/jails-org/Starter-Kit). In the reviewed starter, useful examples include:

- `src/pages/index.astro` and `src/domain/home/index.astro`: route delegation and screen composition.
- `src/domain/home/components/hello-world/index.astro` and `index.ts`: markup, namespace registration, controller, model, event handlers, and state-to-DOM behavior.
- `src/shared/main.ts` and `src/shared/application.ts`: application registration, startup, and an existing `jails.stdlib/third-party` integration.
- The component's `test.unit.ts` and `test.integration.ts`: existing testing conventions.

These are navigation hints, not mandatory filenames for every project. Inspect their actual contents and neighboring implementations. If examples were moved or removed, locate equivalent project examples; consult the upstream starter when necessary and disclose that fallback. Do not pretend the starter demonstrates stdlib modules absent from its examples.

Reuse the scaffold's composition, registration, event, and lifecycle patterns where compatible with current contracts. Do not copy unrelated demo content, arbitrary Tailwind values, or incidental patterns that conflict with jails-ai standards. Do not add a second application startup or register a component twice.

## Load architecture and implementation guidance

Read [the upstream skill catalog](standards/upstream-skills.md), resolve and read `ui-clean-arch`, `jails`, and `jails-stdlib`, and load their task-relevant references. In particular, read the architecture specification, Jails mental model and component conventions, and references for each stdlib module used.

Read [the shared Tailwind standard](standards/tailwind.md) before creating or modifying styles. Use built-in classes; visual fidelity does not authorize customizations. If a required design detail conflicts with this standard, explain the constraint and obtain explicit developer direction before customizing.

Use `ui-clean-arch` for application organization, `jails` for component behavior, and `jails-stdlib` for module contracts. Check examples against installed package versions. If required guidance is inaccessible, follow the catalog's resolution procedure rather than inventing APIs.

## Shared SVG and icon convention

Read and apply [the shared SVG and icon standard](standards/icons.md) before creating or modifying UI. Inspect and reuse `src/shared/components/icon/index.astro` and `public/icons/` from the scaffold, or recreate the component using the base repository's pattern if absent. Render SVGs through that component. When adapting existing HTML, extract embedded SVGs into the corresponding asset files and replace them with Icon usages. Verify asset resolution and rendered appearance before delivery.

## Map the architecture before writing markup

Read and apply [the shared UI Clean Architecture acceptance criteria](standards/ui-clean-architecture.md). Reading the upstream `ui-clean-arch` skill and its architecture specification is a prerequisite to implementing the page; do not proceed with page code if those required sources are unavailable.

Before implementation, record a concise section-to-file map: the screen domain, each meaningful structural section, its component entrypoint, and the responsibilities requiring Store, Services, or Entities. Derive sections from context and purpose, not just visual containers. Resolve this decomposition from the inputs without asking the user to design the architecture.

Implement the page through these boundaries from the start. Do not build the entire screen in one Astro/HTML file as an intermediate shortcut and leave extraction for later. The route delegates, the domain index composes, and section Components own their markup and local behavior. A static page still requires structural decomposition; absence of JavaScript does not make section boundaries optional.

## Build the page

1. Implement the section-to-file map: create a folder and index entry for each structural Component, then import and render those Components in the domain entrypoint. Keep the route thin and the domain index focused on composition, following the application's Astro conventions. Reuse shared layouts and components where their contracts fit; do not move screen-exclusive resources into shared or import another domain.
2. Implement the layout, content hierarchy, responsive behavior, and assets from the inspected references using semantic markup and built-in Tailwind classes. Match observable spacing, typography, colors, and states within the shared styling constraint. Use existing assets when available; disclose placeholders rather than presenting invented assets or copy as supplied requirements.
3. Implement actual interactions with Jails using the scaffold's working patterns. Use native controls, accessible names, keyboard interaction, visible focus, and appropriate form feedback. Connect visible controls to the specified behavior rather than leaving decorative actions.
4. Keep purely local state in its component. For cross-component propagation or persistence, use the screen Store and architecture contracts. Keep external integrations in Services and data adaptation in Entities. Do not create empty layers merely to mirror a folder diagram. Apply the upstream rules for co-located TypeScript types.
5. Prefer suitable stdlib modules for the required behavior after reading their contracts. Import public subpaths, bridge Store subscriptions to component state explicitly, and release subscriptions, timers, and external resources on unmount. Do not add modules or infrastructure without a requirement.
6. Use existing integration contracts. If real data is unavailable, identify the missing contract; use an explicitly disclosed fixture only when suitable for the requested preview. Do not fabricate a working backend, authentication, persistence, or submission success.

