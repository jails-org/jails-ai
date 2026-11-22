<!-- Generated from standards/jails-rendering.md by scripts/sync_standards.py. Do not edit directly. -->

# Jails component registration and initial rendering

## Write and review Jails controllers

Before creating or modifying a Jails controller, resolve the current `jails` skill from Javiani/agent-skills through [the upstream catalog](upstream-skills.md). Read its mental model, [component conventions](https://github.com/Javiani/agent-skills/blob/HEAD/skills/jails/references/component-conventions.md), and Component API at the same resolved revision. Apply the upstream conventions to the controller, including controllers adapted from existing examples.

Before delivery, inspect each created or modified controller against the conventions you read. Check the default function declaration and named export order, placement of initialization values and closure-bound arrow helpers around `main`, and the ordering of event registration and helper calls inside `main`. Review the absence of declarations and branching inside `main`, external placement of pure utilities and data, and formatting of `model` and object updates passed to `state.set`. Use the upstream reference for the full set of conventions.

Correct deviations in the affected code and report the upstream revision and component files reviewed. Verify mounting, interaction, state-to-DOM updates, and cleanup where applicable.

## Keep behavior registration with its Astro component

Each interactive Astro Component owns the Jails behavior for its section. Its
own `.astro` entrypoint must import the colocated controller module and
register the matching custom-element tag in an Astro `<script>` placed
immediately before the custom element’s opening tag in that same file.

```astro
<script>
	import * as WeatherSearch from './index'
	import { register } from 'jails-js'

	register('weather-search', WeatherSearch)
</script>

<weather-search>
	<!-- Markup content -->
</weather-search>
```

Keep the shared startup entrypoint domain-agnostic. It may expose `start()` and
register genuinely shared components, but it must not import or register
screen-specific controllers. For example, `src/shared/main.ts` should not
contain a list of domain component modules. The layout remains responsible for
calling `start()` after the screen has composed its Components.

This boundary keeps domain imports with their owning Components and prevents
shared code from depending on a screen. Verify that every interactive
Component registers exactly once and that its registration script runs before
Jails `start()`; an integration test that checks mounting and interaction is a
useful confirmation.

## Prevent initially closed UI from flashing

In server-rendered or static HTML, Jails directives such as `html-if` and `html-class` are not applied by the browser before Jails initializes. A modal, backdrop, or empty styled notice can therefore appear briefly even when its initial Jails state is closed or empty.

Keep the registered component host in the document so Jails can initialize it, but put initially hidden visual content inside a native `<template>` within that host. Jails processes the template when rendering the component; the browser does not display its contents before initialization. Apply conditional visibility to the rendered content, not to an initially visible overlay on the host.

For example, with a registered `app-modal` whose model starts with `open: false`:

```html
<app-modal>
  <template>
    <div data-modal-overlay class="modal-overlay" html-class="open ? 'visible' : 'hidden'">
      <div role="dialog" aria-modal="true">
        <!-- Modal content and close control -->
      </div>
    </div>
  </template>
</app-modal>
```

The classes are illustrative: use the application's existing styles and ensure the closed state actually hides the overlay. Keep the backdrop, dialog, and any visible styling inside the template; an overlay on the component host can still flash. If backdrop dismissal previously compared the click target with the host, update it to compare with the rendered overlay instead. Preserve opening, closing, focus handling, keyboard behavior, and cleanup.

The same approach applies to conditionally displayed styled notices: put the element carrying `html-if` inside the component's template rather than relying on `html-if` alone to hide server-rendered markup.

Verify the initial HTML with JavaScript disabled or delayed: the overlay, dialog, and conditionally hidden notices must not appear. Then enable JavaScript and test the initial closed state and the relevant open, close, backdrop, keyboard, and focus interactions. Check the installed Jails version and component patterns before applying this approach.
