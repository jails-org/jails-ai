# jails-ai authoring conventions

Write all project content in English.

Application specifications live in a root `specification/` directory. `specification/readme.md` contains general/shared information and a domain/page index; `specification/<domain>/` contains only that domain's rules, with a local `readme.md` and optional topic files. Skills reading specifications must retrieve the root index and relevant domain documents rather than assume a single `specification.md` file. The jails-ai-spec organization guide defines migration of legacy files.

All skills that create or modify UI must read `standards/icons.md` and link to its bundled copy at `references/standards/icons.md`. Render SVGs through the base repository's shared Icon component, and extract inline SVGs from existing HTML into the base template's SVG asset directory.

Shared architecture and implementation standards belong in `standards/`, independently of any individual skill. Read and apply `standards/tailwind.md` when creating or modifying interface styles.

Skills that create or modify screens must also read and apply `standards/ui-clean-architecture.md`, link to its bundled copy, and verify actual structural component boundaries before delivery. Do not treat visual completion or a passing build as proof of architectural compliance.

When creating or updating a skill that generates or modifies UI, link its `SKILL.md` to `references/standards/tailwind.md` and instruct the agent to read it before styling. Keep task-specific workflow in the skill and shared rules in the canonical standard.

Run `python3 scripts/sync_standards.py` after changing shared standards or adding skills. It bundles the standards inside every skill so individual installations remain self-contained. Do not edit generated copies in `skills/*/references/standards/` directly. Run `python3 scripts/sync_standards.py --check` to verify that the copies are current.
