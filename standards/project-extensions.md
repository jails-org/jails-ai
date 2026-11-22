# Project extensions

Project extensions record reusable guidance for one application. Examples include a design system, shared component APIs, fixture conventions, and performance budgets. Keep product behavior and domain rules in `specification/` and link to them when an extension depends on them.

## Discover and apply

At the resolved application root, look for `.jails-ai/extensions/readme.md` before making project decisions. In a monorepo, use the target application's index. If the index is absent, proceed with the task and create it when there is reusable guidance to capture.

Read the index, open the entries whose stated scope matches the task, and consult the linked source needed to apply them. If the task expands to another domain or concern, check the index again. Combine applicable entries with the current request, local instructions, and the shared Jails.ai and upstream standards. Prefer compatible project components, tokens, and workflows that the entries identify. Verify their actual APIs and paths before using them.

Treat entries as project guidance within their stated scope. When an entry conflicts with a current requirement, another applicable entry, or a shared standard, identify the conflict and ask for direction if it affects the task. A documented custom token or utility does not by itself authorize new Tailwind customization. Verify the applicable project guidance in the final review and report the entries used and any material gaps.

## Capture guidance during other tasks

When the developer supplies or corrects a confirmed project-specific practice that should carry across tasks, invoke `jails-ai-extension` internally in the same task. Check the initial request, follow-up messages, and decisions confirmed during the work. An explicit request to save the knowledge is optional. For example, “All new forms in this app use the shared Field component” is reusable guidance; “Use Field on this form while we test the layout” is scoped to the current task.

Use the resolved application and the developer's confirmed scope. Skip temporary choices, hypothetical proposals, guesses from existing code, and sensitive data such as credentials or personal records. If an ambiguity would materially change what future tasks inherit, clarify it before saving. Respect requests to keep the work read-only or to avoid recording the guidance.

If direct skill invocation is unavailable, load the installed `jails-ai-extension/SKILL.md` and follow it. If the skill is not installed, use the bundled storage procedure below. Save confirmed guidance before making dependent decisions when practical and check for later corrections before delivery. Continue the original task and mention any entry created or updated in the handoff.

## Storage

The index lists each entry with a relative link and a short description of when it applies, including any domain or workflow limits. Keep one Markdown entry per reusable topic in the same directory, using a descriptive kebab-case filename such as `design-system.md`. Store guidance in the application, with links to authoritative docs, existing code, and verified usage examples where available. The index is the discovery entry point for each installed Jails.ai skill.

Read existing relevant entries before writing. Update the matching topic in place, or create a topic and index entry when needed. Record the confirmed guidance, its scope, and available sources. Reopen the index and verify the topic link and its scope from the perspective of a later task.
