<div align="center">
  <img width="280" alt="jails-logo" src="https://github.com/user-attachments/assets/b121dbd0-4221-4a48-92c6-2a9e4d8ede32" /><strong>.ai</strong><br/><br/>
  <p><strong>Build more. Keep every change understandable.</strong></p>
  <p>AI-assisted frontend development with a lightweight stack, clear architectural boundaries,<br />and the developer in control.</p>
  <p><a href="#quick-start">Quick start</a> · <a href="#the-skills">Skills</a> · <a href="#architecture-that-supports-review">Architecture</a> · <a href="#contributing">Contributing</a></p>
</div>

## Why Jails.ai

Code can be generated in seconds. Understanding it takes longer.

When code arrives faster than people can absorb it, review becomes the bottleneck: large diffs, unclear responsibilities, and changes whose impact is difficult to trace. Without a consistent architecture, each new feature can add another layer of uncertainty for the next developer.

Jails.ai applies the philosophy of the Jails microframework to AI-assisted application development: simplicity, modularity, performance, and long-term maintainability. It brings together a deliberate stack and shared engineering practices so generated code has a structure developers can inspect and evolve.

Simple, predictable code gives reviewers less context to reconstruct. Separation of concerns helps them understand what changed and where its effects belong. That supports a more sustainable pace of development as the application grows.

Jails.ai draws on more than 20 years of development experience across projects. Its purpose is to give developers more capacity to build while preserving technical judgment. You direct the work, inspect the result, and decide how the application evolves.

## What this repository provides

This repository is a collection of **Agent Skills**: instructions and on-demand references that guide a coding agent through specific development workflows. It follows the [Agent Skills specification](https://agentskills.io/specification) and works with the [skills CLI](https://github.com/vercel-labs/skills).

The skills coordinate application setup, specifications and implementation, mock responses, performance investigations, and project extensions. They compose the upstream `ui-clean-arch`, `jails`, and `jails-stdlib` skills.

The application foundation comes from [jails-org/Starter-Kit](https://github.com/jails-org/Starter-Kit): Astro, TypeScript, Jails, jails.stdlib, Tailwind, Vitest, and Playwright. This distribution repository itself does not contain a generated application or a `jails-ai` terminal executable.

## Quick start

You need Git, Node.js with `npx`, and a coding agent that supports Agent Skills. The generated application's package manager and runtime requirements come from the fetched Starter-Kit.

### 1. Clone the skills repository

```bash
git clone https://github.com/jails-org/jails-ai.git
```

### 2. Install into your target workspace

From the project or workspace where you want the skills available, run:

```bash
npx skills add /absolute/path/to/jails-ai --skill jails-ai-setup jails-ai-spec jails-ai-mock jails-ai-performance jails-ai-extension
```

Replace `/absolute/path/to/jails-ai` with the absolute path to your clone and select your coding agent. The agent fetches the required guidance from Javiani/agent-skills on demand. Installing those upstream skills separately is unnecessary. See the [upstream catalog](standards/upstream-skills.md#load-upstream-guidance-on-demand) for the fetch procedure.

To inspect the local catalog before installation:

```bash
npx skills add /absolute/path/to/jails-ai --list
```

Cloning the repository is not enough to make its skills available to an agent. Run installation from each target workspace where you need them.

### 3. Ask your agent to create an application

In agents supporting dollar mentions:

```text
$jails-ai-setup Create the application foundation in ./my-app.
```

In GitHub Copilot Chat:

```text
/jails-ai-setup Create the application foundation in ./my-app.
```

These are **agent chat instructions**, not shell commands. Invocation syntax and autocomplete depend on the client.

The setup skill fetches the Starter-Kit, installs its dependencies, and verifies the application. Use the generated application's README for its exact development and verification commands.

## The skills

| Skill | Use it to | Primary output |
| --- | --- | --- |
| [jails-ai-setup](skills/jails-ai-setup/SKILL.md) | Create an application foundation from the Starter-Kit. | A scaffold with its stack, architecture, and source revision documented. |
| [jails-ai-spec](skills/jails-ai-spec/SKILL.md) | Specify and build screens or behaviors, or document an existing application. | A cumulative `specification/` directory and implementation when requested. |
| [jails-ai-mock](skills/jails-ai-mock/SKILL.md) | Model dynamic screen data and create response fixtures. | Valid JSON under `public/mocks/<domain>/`. |
| [jails-ai-performance](skills/jails-ai-performance/SKILL.md) | Investigate and improve loading, responsiveness, and visual stability. | Evidence-based findings and verified, focused fixes. |
| [jails-ai-extension](skills/jails-ai-extension/SKILL.md) | Save reusable project guidance for the other Jails.ai skills. | An application-local index and topic files under `.jails-ai/extensions/`. |

The following examples use Copilot's `/` syntax. Use `$` instead in clients that support dollar mentions.

### Set up the foundation

```text
/jails-ai-setup Create the application foundation in ./my-app.
```

Setup asks where to create the application unless you already supplied a destination. It fetches the Starter-Kit, copies its contents including dotfiles without importing Git metadata, and installs dependencies using the starter's lockfile. Existing files are preserved; conflicts are resolved with you before copying.

The starter's stack and initial screen remain in place unless you request changes. Setup records the fetched starter commit in the generated README and runs the relevant available checks. The fetched package manifest is the source of truth for build and test commands.

### Specify and build screens or behavior

Provide descriptions, PRDs, documentation, images, or reference URLs, including Figma links.

```text
/jails-ai-spec Build an orders page from the attached PRD and layout image.
```

For a focused behavior change:

```text
/jails-ai-spec When the category filter changes, update the results and summary without reloading. Reset the filter when leaving the page.
```

For documentation of an existing project:

```text
/jails-ai-spec Extract a PRD from this application. Organize specification/ into shared information and domain/page folders. Do not change application behavior.
```

The skill keeps requirements cumulative and scoped:

```text
specification/
├── readme.md              # Overview, shared rules, decisions, domain/page index
└── <domain>/
    ├── readme.md          # Domain requirements and implementation mapping
    └── <topic>.md         # Additional linked topics when useful
```

Stable rule IDs, acceptance criteria, relative links, and implementation mapping keep requirements traceable without duplicating them. Existing `specification.md` content is migrated without losing rules or evidence.

Documentation extraction traces routes, behavior, tests, and available runtime evidence. It distinguishes confirmed requirements, observed behavior, and inferred intent, and records areas that have not been inspected. Extraction alone does not authorize implementation changes.

### Create mock responses

```text
/jails-ai-mock Create an orders response for the dynamic order list and summary totals. Propose a contract because the API schema is not defined yet.
```

The skill first checks whether a response contract exists. With a contract, it uses the supplied schema. Without one, it asks focused questions about fields, relationships, types, and scenarios before proposing the structure.

Fixtures live in `public/mocks/<domain>/`. For example, `public/mocks/home/summary.json` is served at `/mocks/home/summary.json` with the default base path.

The skill previews the saved JSON, explains important fields and assumptions, and reports validation. Connecting a fixture to the application requires a separate request and follows the Service boundary.

### Investigate performance

```text
/jails-ai-performance The application feels slow, but I do not know where to start. Explore the main pages and interactions, prioritize the causes, and implement focused improvements.
```

The skill starts with the reported symptom, or explores representative journeys if the cause is unclear. It investigates Largest Contentful Paint (LCP), Interaction to Next Paint (INP), and Cumulative Layout Shift (CLS), using available field evidence, browser traces, targeted audits, and source attribution.

Scrolling and animation smoothness are investigated separately from Core Web Vitals. Findings are prioritized by user impact and supporting evidence. Improvements require verification under comparable conditions.

For font-related layout shifts, the skill preserves the intended design and does not automatically choose `font-display: optional`.

### Record project conventions

```text
/jails-ai-extension Document our existing design system so future screens reuse its components and tokens. Use docs/design-system.md and the shared components as sources.
```

The skill saves the guidance in the application, for example in `.jails-ai/extensions/design-system.md`, and registers it in `.jails-ai/extensions/readme.md`. Setup, specification, mock, and performance workflows check that index and load entries relevant to their work. Install the updated versions of those skills to use this behavior in an existing workspace. See the [project extensions standard](standards/project-extensions.md).

Jails.ai also captures confirmed conventions shared during ordinary work. If you say “All forms in this app use the shared Field component” while requesting a screen, the workflow records the convention and continues building the screen. Instructions scoped to a single task stay with that task.

## Architecture that supports review

A clear architecture gives both the agent and the reviewer a shared map of the application.

| Layer | Responsibility |
| --- | --- |
| **Astro** | HTML generation, page structure, and server-side rendering. |
| **Jails** | Modular interface behavior and lifecycle. |
| **Tailwind** | UI composition with reusable utility classes. |
| **Jails.ai skills** | Workflow, architectural conventions, and verification across those pieces. |

Use the [upstream skill catalog](standards/upstream-skills.md) to resolve the architecture specification and Jails conventions. The [screen implementation review](standards/ui-clean-architecture.md) records how Jails.ai skills verify the implemented boundaries before delivery.

## Shared implementation conventions

### Portable Tailwind

Use built-in utilities and variants supported by the installed Tailwind version. Project-specific tokens, utilities, variants, plugins, `@apply` component classes, and styling shortcuts require explicit developer instructions. A visual reference alone does not authorize customization.

See [the Tailwind standard](standards/tailwind.md) for the full portability contract.

### SVGs and icons

Store SVG assets in `public/icons/` and render them through the Starter-Kit's shared `src/shared/components/icon/index.astro` component. Inspect the actual component API before using it. When adapting HTML, extract inline SVGs into asset files and reuse the shared component.

See [the SVG and icon standard](standards/icons.md) for rendering and accessibility requirements.

### Upstream skills

| Skill | Owns |
| --- | --- |
| `ui-clean-arch` | Application organization and dependency boundaries. |
| `jails` | Component behavior, registration, state, and lifecycle contracts. |
| `jails-stdlib` | Utility module and Store contracts. |

The [upstream catalog](standards/upstream-skills.md) designates Javiani/agent-skills as the sole reference for Jails behavior and conventions. Resolve the current upstream default-branch commit for each task and check API contracts against the application's installed package versions.

## VS Code and GitHub Copilot

Install from your target workspace using the commands above and select GitHub Copilot. Workspace skills are discovered in `.github/skills/`; this repository distributes their source from `skills/`.

Open the workspace where the skills were installed and enter `/jails-ai-setup` in Copilot Chat. If it is missing:

1. Confirm installation completed in that workspace.
2. Run **Developer: Reload Window**.
3. Check the Skills section in Agent Customizations.
4. Use a VS Code and Copilot version with Agent Skills support.

See the [official VS Code documentation](https://code.visualstudio.com/docs/agent-customization/agent-skills) for discovery locations and invocation support.

## Repository layout

```text
standards/                         # Canonical shared standards and upstream catalog
scripts/sync_standards.py           # Bundles standards into each skill
skills/
├── jails-ai-setup/
├── jails-ai-spec/
├── jails-ai-mock/
├── jails-ai-performance/
└── jails-ai-extension/
```

Each skill contains a `SKILL.md`, optional OpenAI client metadata in `agents/openai.yaml`, and self-contained references. Detailed references are loaded on demand. The `jails-ai-` folder name and skill `name` stay consistent and use kebab-case.

The repository-level [AGENTS.md](AGENTS.md) governs authoring here. Installed skills receive shared rules and the on-demand upstream fetch procedure through bundled references.

## Contributing

Write instructions, documentation, metadata, and examples in English. Keep shared rules in `standards/` and workflow-specific guidance in the corresponding skill. Skills that create or modify UI must link to their bundled standards and load them before implementation.

After changing shared standards or adding skills, synchronize the bundled copies:

```bash
python3 scripts/sync_standards.py
```

Then verify they are current:

```bash
python3 scripts/sync_standards.py --check
```

Edit canonical standards rather than generated copies in `skills/*/references/standards/`. Keep upstream source links and the resolution procedure current.

---

**Build for the first release. Leave a foundation for the changes that follow.**
<img width="271" height="123" alt="jails-logo" src="https://github.com/user-attachments/assets/83f2cb5a-d430-4c4d-8125-10ee054a4cc8" />
