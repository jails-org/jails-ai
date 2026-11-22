<!-- Generated from standards/ui-clean-architecture.md by scripts/sync_standards.py. Do not edit directly. -->

# Screen implementation review

Resolve `ui-clean-arch` and read its architecture specification through [the upstream catalog](upstream-skills.md). Use the upstream skill for architectural contracts and source-level verification.

Before writing markup, record a short map of the screen's meaningful sections, their responsibilities, and their owning component files. In a Starter-Kit application, use Astro entrypoints and follow [the Jails rendering standard](jails-rendering.md) for colocated behavior. Update the map if the design changes.

Before delivery, reconcile the map with the actual source. Check that each mapped section lives in its owning component and that the domain index imports and renders it. Inspect the route and domain index for misplaced section implementations. Correct violations in the affected screen and report the structural component files and the applicable Store, Service, and Entity responsibilities. Verify these boundaries in source even when the build and visual checks pass.
