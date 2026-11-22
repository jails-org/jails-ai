---
name: jails-ai-extension
description: Save and update reusable guidance in a Jails.ai application. Use automatically when the developer introduces or corrects durable project-specific knowledge during another task, such as design system usage, component conventions, tooling, or performance budgets. An explicit save request is optional.
---

# jails-ai Extension

Select this skill automatically when the developer shares confirmed project guidance that should be reused in future tasks. Capture it as part of the current task and continue the original work. For explicit use, invoke with `/jails-ai-extension` in GitHub Copilot Chat or `$jails-ai-extension` in agents supporting dollar mentions.

Read [the project extensions standard](references/standards/project-extensions.md) for implicit capture, storage, and discovery across the Jails.ai skills.

## Inspect the project and sources

Resolve the target application root from the request, workspace, manifest, and local instructions. Ask which application to use if the target remains ambiguous. Read the extension index and related entries if present, then inspect the supplied materials and the relevant project documentation, source, and configuration. Keep the extensions in that application so teammates and future sessions can use them.

Capture explicit developer decisions and guidance supported by authoritative project sources. If existing code only suggests a convention, verify its intended scope before recording it as a requirement. Keep proposed changes separate from established practices. When recording a design system, locate its supported components, import paths, tokens, variants, accessibility guidance, and examples relevant to the request. Link to the owning files so later agents can check them.

## Save and verify

1. Create or update the relevant topic file in `.jails-ai/extensions/`. Reuse or refine a matching entry to avoid overlapping rules. Write its scope, actionable guidance, and source references. Record usage or verification steps where they help someone apply the guidance.
2. Update `.jails-ai/extensions/readme.md` with the relative link and the tasks or domains that should load the entry. State the scope clearly enough that a later skill can select it from the index alone.
3. Reopen the index and follow its links as a consuming skill would. Verify that a relevant task can find the entry and that the entry points to existing files or supplied sources. Report what was saved, when it applies, and any missing evidence.

Recording an extension changes the project's reusable guidance. If the request also asks to implement a missing capability or apply the guidance to a screen, follow the relevant implementation workflow for that work. Apply [the Tailwind standard](references/standards/tailwind.md) before styling, [the SVG/icon standard](references/standards/icons.md) for UI, and [Jails rendering](references/standards/jails-rendering.md) and [UI Clean Architecture](references/standards/ui-clean-architecture.md) where applicable.
