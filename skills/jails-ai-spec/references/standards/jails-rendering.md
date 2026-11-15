<!-- Generated from standards/jails-rendering.md by scripts/sync_standards.py. Do not edit directly. -->

# Jails initial rendering

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
