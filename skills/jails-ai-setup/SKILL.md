---
name: jails-ai-setup
description: Scaffold front-end applications from jails-org/Starter-Kit with jails-ai, UI Clean Architecture, Jails, and jails.stdlib. Use when setting up an application with this stack or when the user invokes jails-ai-setup.
---

# jails-ai Setup

Invoke this skill with `/jails-ai-setup` in GitHub Copilot Chat, or `$jails-ai-setup` in agents that support dollar mentions. The skill must be installed in a discovery location supported by the agent.

Prepare an executable foundation with UI Clean Architecture, Jails for interface behavior, and jails.stdlib for the required capabilities. This skill coordinates setup; technical contracts belong to the upstream skills.

## Shared jails-ai standards

Before creating or modifying interface styles, read and apply [the shared Tailwind standard](references/standards/tailwind.md). Include the shared Tailwind and SVG/icon conventions in the generated application's architecture or styling documentation.

When creating or modifying Jails UI, read and apply [the Jails component and rendering standard](references/standards/jails-rendering.md).

## Shared SVG and icon convention

Read and apply [the shared SVG and icon standard](references/standards/icons.md) before creating or modifying UI. Inspect and reuse `src/shared/components/icon/index.astro` and `public/icons/` from the scaffold, or recreate the component using the base repository's pattern if absent. Render SVGs through that component. When adapting existing HTML, extract embedded SVGs into the corresponding asset files and replace them with Icon usages. Verify asset resolution and rendered appearance before delivery.

## Ask where to create the project

Before creating files, ask: “Where would you like to create the project: in the current folder, at a specific path, or in a new folder inside the current directory?” Offer these three choices and collect the path or folder name when required. If the user already supplied an explicit destination in the request, treat it as their answer and do not ask again.

Resolve the destination against the original working directory:

- **Current folder:** use the current working directory itself.
- **Specific path:** use the supplied absolute path, or resolve a relative path against the current working directory.
- **New folder:** create the supplied folder name directly inside the current working directory.

Inspect local instructions and the destination before writing. Preserve existing files and repository metadata. If the destination contains files, compare them with the starter and ask how to handle conflicting files before copying; never overwrite or delete user work silently. This repository distributes skills: create an application here only if the user explicitly chooses it as the destination.

Check the chosen destination for [project extensions](references/standards/project-extensions.md) before scaffolding. Use relevant guidance for requested adaptations and preserve the project's extension files when copying the starter.

## Scaffold from Starter-Kit

Use [jails-org/Starter-Kit](https://github.com/jails-org/Starter-Kit) as the application source. Do not substitute a generic framework generator or recreate the template manually.

1. Obtain a fresh copy of the starter in a temporary directory, for example with `git clone --depth 1 https://github.com/jails-org/Starter-Kit.git <temporary-directory>`. Record its commit with `git rev-parse HEAD` before copying. If the source cannot be fetched, report the blocker rather than generating a replacement.
2. Inspect its README, package manifest, lockfile, and configuration. The reviewed starter includes Astro, TypeScript, Jails, jails.stdlib, Tailwind, Vitest, and Playwright. Preserve the fetched starter's stack, dependency versions, source structure, and configuration unless the user requests a change.
3. Create the chosen destination if needed, then copy the starter contents, including dotfiles, while excluding the clone's `.git` directory. Do not import upstream Git history or modify an existing destination repository's `.git`. Do not initialize a new Git repository unless requested.
4. Use the starter's package manager and lockfile. The reviewed starter provides `yarn.lock`; prefer Yarn unless the fetched starter or the user specifies otherwise. Install dependencies in the destination without upgrading them as part of setup.
5. Keep the starter's initial screen as the default scaffold. Apply product-specific changes only when requested. Record the source URL, fetched commit, development commands, and applicable skill references in the application's README.
6. Normalize Jails registration without changing the initial screen: if the starter imports or registers domain components in `src/shared/main.ts`, move each controller import and `register()` call to a `<script>` immediately before the custom element's opening tag in that Component's own `.astro` file. Keep shared startup domain-agnostic and ensure registrations run before `start()`, following the shared Jails rendering standard.

The source was reviewed at commit `a9708be56ee8c228d0fe205bfb2cb3dad7753292`. This identifies the inspected baseline, not a mandatory pin: use the fetched revision unless the user requests a particular one.

## Load upstream skills

Read [the references and resolution procedure](references/standards/upstream-skills.md) before implementation. Resolve `ui-clean-arch`, `jails`, and `jails-stdlib` by their exact names and read their `SKILL.md` files. Load additional references linked by each skill only when needed.

Their responsibilities complement each other:

- `ui-clean-arch`: screen/domain organization, Components, Store, Services, Entities, and dependency boundaries.
- `jails`: components, registration, directives, state, and interface lifecycle.
- `jails-stdlib`: contracts for the modules used, including Store when needed.

Do not turn optional Jails patterns into additional architectural rules. Use `ui-clean-arch` for application organization and the Jails skills for implementation. Preserve the user's explicit choices; if they conflict with the stack or architecture, clarify the incompatibility before generating the foundation.

## Apply the architecture and framework contracts

Each interactive Astro Component must import `register` from `shared/main`
and its colocated Jails controller as a namespace. Register its own
custom-element tag from a `<script>` in that Component's
`.astro` entrypoint, immediately before the custom element's opening tag. Keep `src/shared/main.ts` domain-agnostic: use it for
shared startup and genuinely shared registrations, never as a list of
screen-specific Components. Follow the [shared Jails rendering standard](references/standards/jails-rendering.md) and
ensure all registrations run before `start()`.

Review the scaffold with the upstream skills and [the shared UI Clean Architecture acceptance criteria](references/standards/ui-clean-architecture.md) before making any requested adaptations. Create only the abstractions required by the initial screen. Keep component-local state local; use the screen Store for propagation or persistence as specified by `ui-clean-arch`.

Register complete Jails component modules before `start()`. In SSR/SSG, initialize browser APIs only during the client phase. Connect subscriptions to state and release resources on unmount according to the upstream skills. Check the installed exports and versions before applying examples; a skill revision does not pin a JavaScript package version.

Do not reinstall packages already provided by the starter, add unused libraries, or perform an unrelated architectural migration during scaffolding.

## Verify and deliver

Apply the upstream catalog’s review to all Jails code changes. Run the build and relevant available checks from the destination. The reviewed starter provides `build`, `test:unit`, and `test:integration` scripts; use the fetched manifest as the source of truth. Run the available unit tests and the integration tests when the browser dependencies are available. When browser access is available, verify the initial screen: mounting, interaction, DOM updates, and cleanup where applicable. Review dependency boundaries according to `ui-clean-arch`. Verify styling against the shared Tailwind standard.

Report the resolved destination, starter URL and fetched commit, generated files, applied choices, references actually used, checks performed, and the command to start the application. State which checks could not be performed and why.
