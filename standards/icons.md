# SVG and icon rendering

Use the Starter-Kit's shared Icon component to render SVG artwork in the interface. This convention applies to every jails-ai skill that creates or modifies UI, including conversions of existing HTML.

## Inspect and reuse the base implementation

Read the target project's Icon component and existing SVG assets before implementation. The reviewed [jails-org/Starter-Kit](https://github.com/jails-org/Starter-Kit) at revision `a9708be56ee8c228d0fe205bfb2cb3dad7753292` provides:

- Component: `src/shared/components/icon/index.astro`.
- SVG files: `public/icons/<name>.svg`.
- Props: `name`, `color`, and `class`.
- Loading: a raw SVG import from `public/icons/${name}.svg?raw`, rendered inside a span.

Use the actual implementation as the API source of truth if the project has evolved. If the component is absent, create it following the base repository's implementation and location rather than introducing a competing icon system. Preserve the existing shared component when it is present.

For the reviewed contract, an SVG stored at `public/icons/search.svg` is rendered as follows, using the project's configured import alias:

```astro
---
import Icon from 'shared/components/icon/index.astro'
---

<Icon name="search" class="inline-flex text-slate-600" />
```

Pass the basename without the `.svg` extension or directory prefix. Only use props supported by the actual component; the reviewed implementation does not forward arbitrary attributes to its span. Prefer standard Tailwind classes and SVG `currentColor` where suitable instead of adding custom styling configuration. The existing `color` prop is not a reason to introduce arbitrary colors contrary to the Tailwind standard.

## Extract embedded SVGs

When adapting existing HTML or components containing inline `<svg>` elements:

1. Inventory the SVGs in the requested screen and check for equivalent files already in `public/icons/`.
2. Extract each distinct SVG into a descriptively named `.svg` file in that directory. Preserve its root SVG element, namespace, viewBox, geometry, and required fill, stroke, mask, gradient, and definition relationships. Reuse identical assets instead of duplicating files for every occurrence.
3. Replace the embedded SVG markup in the page or section with the shared Icon component referencing that file. Keep interaction handlers and accessible control names on their owning controls.
4. Verify dimensions, inherited colors, alignment, and accessibility against the original. Check repeated instances of SVGs with internal IDs for conflicting references. Do not assume passing a class to the wrapper automatically resizes the SVG; inspect the component and asset sizing behavior.

Do not leave SVG bodies embedded directly in screen markup, store SVG markup strings in controllers, or use ad hoc raw-HTML rendering outside the Icon component as a shortcut. Apply this to the screen being created or modified without rewriting unrelated pages.

## Accessibility and verification

Decorative icons must not replace accessible labels on buttons or links. Supply accessible names through supported markup; do not assume the Icon component forwards ARIA props. Preserve meaningful SVG titles or descriptions where applicable, checking their behavior when reused.

Before delivery, check that SVG files resolve through the component, that extracted assets render correctly, and that no inline SVG implementations remain in the affected page or structural components. The shared Icon component may render SVG markup internally; that is the intended rendering boundary.
