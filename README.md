# jails-ai

A collection of Agent Skills for building front-end applications with lightweight technologies and architectural conventions. It follows the open [Agent Skills specification](https://agentskills.io/specification) and the `skills/<name>/` structure used by [Javiani/agent-skills](https://github.com/Javiani/agent-skills), compatible with the [Vercel skills CLI](https://github.com/vercel-labs/skills).

## Available skills

| Skill | Responsibility |
| --- | --- |
| [jails-ai-setup](skills/jails-ai-setup/SKILL.md) | Scaffold an application from jails-org/Starter-Kit with UI Clean Architecture, Jails, and jails.stdlib. |
| [jails-ai-spec](skills/jails-ai-spec/SKILL.md) | Specify and build pages and rules, or extract a PRD from an existing project. |
| [jails-ai-mock](skills/jails-ai-mock/SKILL.md) | Create JSON response fixtures for dynamic screen data and explain their structure. |
| [jails-ai-performance](skills/jails-ai-performance/SKILL.md) | Diagnose and improve loading, responsiveness, and stability using Core Web Vitals and user journeys. |

## Install and use

From the project where you want to use the skills, install jails-ai using its absolute local path:

```bash
npx skills add /absolute/path/to/jails-ai --skill jails-ai-setup jails-ai-spec jails-ai-mock jails-ai-performance
npx skills add Javiani/agent-skills --skill ui-clean-arch jails jails-stdlib
```

Select your agent in the installer. To inspect the local catalog before installing:

```bash
npx skills add /absolute/path/to/jails-ai --list
```

In agents that support `$` invocation, use:

```text
$jails-ai-setup Create the application foundation in ./my-app.
```

The stable name `jails-ai-setup` enables discovery in the agent's skill selector. Autocomplete and invocation syntax depend on the client; in Codex clients supporting `$` mentions, look for `$jails-ai-setup`. The skill does not create a terminal executable. Keeping files in `skills/` alone does not install them in an agent.

## VS Code and GitHub Copilot

Install the skills into your target workspace with the skills CLI and select GitHub Copilot. Copilot discovers workspace skills in `.github/skills/`; the distribution source remains in `skills/`.

Open the jails-ai root folder in VS Code, then type `/jails-ai-setup` in Copilot Chat. If it does not appear, run **Developer: Reload Window** and check the Skills section of Agent Customizations. Use an up-to-date VS Code and Copilot version with Agent Skills support.

Run installation from each project where you want the skills to be available. Merely cloning this distribution repository does not install its skills in the agent.

See [the official VS Code Agent Skills documentation](https://code.visualstudio.com/docs/agent-customization/agent-skills) for discovery locations and slash command support.

## Setup workflow

`jails-ai-setup` first asks where to create the application: the current folder, a specific path, or a new folder inside the current directory. An explicit destination already supplied in the request counts as the answer.

It then fetches [jails-org/Starter-Kit](https://github.com/jails-org/Starter-Kit), copies the template including dotfiles without its Git metadata, installs dependencies using its lockfile, and verifies the generated application. Existing files are preserved, and conflicts are resolved with the user before copying.

The starter supplies Astro, TypeScript, Jails, jails.stdlib, Tailwind, Vitest, and Playwright. Setup retains its stack and initial screen unless changes are requested, and records the fetched starter commit in the generated README.

## Page and behavior specification workflow

Use `/jails-ai-spec` or `$jails-ai-spec` for pages, screens, behaviors, and business rules. Supply descriptions, documentation, PRDs, images, or URLs pointing to Figma, written requirements, layout images, or reference pages. The same entrypoint handles both a complete new screen and a focused rule change.

The skill maintains a cumulative `specification/` directory at the target application root. `specification/readme.md` holds the project overview, structural decisions, shared rules, and a domain/page index. Each `specification/<domain>/` folder contains only that domain's requirements, evidence, acceptance criteria, and implementation mapping, starting with its own `readme.md` and splitting into linked topic files when useful. Stable rule IDs, relative links, summaries, and focused retrieval keep context manageable without duplicating rules. Existing `specification.md` content is migrated without losing rules or evidence.

It implements the specification with `ui-clean-arch`, `jails`, and `jails-stdlib`, inspecting the application's Starter-Kit examples first. Page construction requires a section-to-file map, separate structural Components, shared Tailwind/icon standards, and visual and functional verification. A behavior-only request remains scoped to that behavior without unnecessarily rebuilding the page.

```text
/jails-ai-spec Extract a PRD from this existing application and organize specification/ into general information and domain/page folders. Do not change application behavior.
/jails-ai-spec Build an orders page from the attached PRD and layout image.
/jails-ai-spec When the user changes the category filter, update results and summary without reloading. Reset the filter when leaving the page.
```

For documentation extraction, the skill inventories routes and traces implemented behavior, tests, and available runtime evidence. It records findings in the appropriate general or domain documents under `specification/`, distinguishes confirmed requirements from observed behavior and inferred intent, and tracks uninspected areas. Extraction alone does not authorize application changes; implementation remains a separate mode or an explicitly combined request.

## Mock data workflow

Use `/jails-ai-mock` or `$jails-ai-mock` to describe which screen data is dynamic. The skill first asks whether a response contract exists. If it does, it requests the pasted or attached contract; otherwise it asks focused questions about dynamic fields, relationships, types, and relevant scenarios before proposing a structure. It then creates valid JSON in the application's `public/mocks/<domain>/`, using the screen's actual domain name. For example, home screen responses belong in `public/mocks/home/summary.json` and are served at `/mocks/home/summary.json` with the default base path.

It previews the saved JSON in chat, explains important fields and assumptions, and reports validation. Application integration is performed only when requested; future consumption follows the UI Clean Architecture Service boundary.

```text
/jails-ai-mock Create an orders response for the dynamic order list and summary totals. Propose a contract because the API schema is not defined yet.
```

## Performance workflow

Use `/jails-ai-performance` or `$jails-ai-performance` to investigate technical UX and performance problems. It first asks what the developer wants to solve, unless the symptom is already specified. If the developer does not know where to start, it explores representative pages and interactions independently.

The investigation follows LCP, INP, and CLS using available field evidence, production-preview browser traces, targeted audits, and source attribution. It also investigates scrolling and animation smoothness without mislabeling those signals as Core Web Vitals. Findings are prioritized by user impact and evidence, then focused fixes are verified under comparable conditions.

The detailed font-loading workflow remains available for CLS issues. The skill preserves the intended design, does not automatically use `font-display: optional`, and never claims improvement without supporting measurements.

```text
/jails-ai-performance The application feels slow, but I do not know where to start. Explore the main pages and interactions, prioritize the causes, and implement focused improvements.
```

## Structure

```text
standards/                  # Canonical shared rules and upstream catalog
scripts/sync_standards.py    # Bundle shared references into every skill
skills/
├── jails-ai-setup/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/standards/
├── jails-ai-spec/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
│       ├── extract-project.md
│       ├── page-implementation.md
│       ├── specification-organization.md
│       └── standards/
├── jails-ai-mock/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/standards/
└── jails-ai-performance/
    ├── SKILL.md
    ├── agents/openai.yaml
    └── references/
        ├── core-web-vitals.md
        ├── layout-shift.md
        └── standards/
```

Each skill uses the same folder name and `name`, in kebab-case. Use the `jails-ai-` prefix for skill names. `SKILL.md` describes applicability and workflow. Detailed references are loaded on demand. `agents/openai.yaml` provides optional metadata for OpenAI clients; the core format remains agent independent.

All project content, including skill instructions, metadata, documentation, and examples, must be written in English.

## SVG and icon convention

All UI skills follow the [shared SVG and icon standard](standards/icons.md). Render SVGs through the Starter-Kit's `src/shared/components/icon/index.astro`, storing SVG files in `public/icons/`. When adapting existing HTML, extract inline SVGs into those files and replace them with the Icon component. If the component is missing, recreate the base repository's pattern.

## Shared standards

Architecture and implementation conventions shared by all jails-ai skills live in `standards/`. The [UI Clean Architecture acceptance criteria](standards/ui-clean-architecture.md) require a section-to-file map, separate structural Components, and a source-level architecture review before delivery. The [Tailwind portability standard](standards/tailwind.md) requires built-in classes and explicit developer instructions for customizations.

[AGENTS.md](AGENTS.md) defines how contributors and agents apply these standards to existing and future skills. Skills that create or modify UI must link to their bundled Tailwind reference and read it before styling.

Each skill includes a generated copy under `references/standards/` so it remains self-contained when installed separately. Edit the canonical files in `standards/`, then synchronize and check the bundled copies:

```bash
python3 scripts/sync_standards.py
python3 scripts/sync_standards.py --check
```

The repository-level `AGENTS.md` guides authoring here; installed skills obtain the rules through their own references without depending on files outside their installation directory.

## Composing upstream skills

- `ui-clean-arch` defines application organization and boundaries.
- `jails` defines interface behavior contracts.
- `jails-stdlib` defines utility module and Store contracts.

`jails-ai-setup` coordinates these responsibilities without copying their manuals. The [reference catalog](standards/upstream-skills.md) records paths, the reviewed revision, and the resolution procedure when skills are not installed. The Starter-Kit supplies the default build tools, language, and rendering configuration; changes require an explicit application requirement.

Installation through `Javiani/agent-skills` follows the upstream source; the documented revision makes the content reviewed during jails-ai's creation traceable. The CLI does not resolve these dependencies merely because they are mentioned in the instructions.
