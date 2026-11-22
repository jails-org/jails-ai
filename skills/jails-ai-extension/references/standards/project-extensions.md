<!-- Generated from standards/project-extensions.md by scripts/sync_standards.py. Do not edit directly. -->

# Project extensions

Project extensions record reusable guidance for one application. Examples include a design system, shared component APIs, fixture conventions, and performance budgets. Keep product behavior and domain rules in `specification/` and link to them when an extension depends on them.

## Discover and apply

At the resolved application root, look for `.jails-ai/extensions/readme.md` before making project decisions. In a monorepo, use the target application's index. If the index is absent, proceed with the usual workflow.

Read the index, open the entries whose stated scope matches the task, and consult the linked source needed to apply them. If the task expands to another domain or concern, check the index again. Combine applicable entries with the current request, local instructions, and the shared Jails.ai and upstream standards. Prefer compatible project components, tokens, and workflows that the entries identify. Verify their actual APIs and paths before using them.

Treat entries as project guidance within their stated scope. When an entry conflicts with a current requirement, another applicable entry, or a shared standard, identify the conflict and ask for direction if it affects the task. A documented custom token or utility does not by itself authorize new Tailwind customization. Verify the applicable project guidance in the final review and report the entries used and any material gaps.

## Storage

The index lists each entry with a relative link and a short description of when it applies, including any domain or workflow limits. Keep one Markdown entry per reusable topic in the same directory, using a descriptive kebab-case filename such as `design-system.md`. Store guidance in the application, with links to authoritative docs, existing code, and verified usage examples where available. The index is the discovery entry point for each installed Jails.ai skill.
