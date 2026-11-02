<!-- Generated from standards/tailwind.md by scripts/sync_standards.py. Do not edit directly. -->

# Tailwind portability

Compose components using only Tailwind's built-in utility classes and variants for the installed version. Components should remain portable to other projects using standard Tailwind without carrying project-specific styling configuration.

Create Tailwind customizations only when explicitly instructed by the developer. Without that instruction, do not add or extend theme tokens, custom colors or spacing scales, custom utilities or variants, plugins, or component classes built with `@apply`. Do not bypass this rule with arbitrary values, arbitrary properties or variants, inline styles, or custom CSS introduced to replace standard utilities.

Preserve the starter's Tailwind integration, but do not introduce dependencies on project-specific customizations when composing new components. If a requested design cannot be expressed with built-in classes, explain the constraint and ask whether the developer wants to authorize the required customization. A visual reference or general styling request alone is not explicit authorization.

When customization is explicitly requested, document its purpose and the configuration required to port affected components.
