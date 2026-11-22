<!-- Generated from standards/upstream-skills.md by scripts/sync_standards.py. Do not edit directly. -->

# Upstream skills and framework specifications

Use [Javiani/agent-skills](https://github.com/Javiani/agent-skills) as the sole reference for learning Jails behavior and conventions. Read the relevant guidance maintained in that repository. The upstream skills are distributed under the MIT license, copyright 2026 Eduardo Ottaviani Aragão.

| Skill | Entrypoint on the current default branch | References to read |
| --- | --- | --- |
| `ui-clean-arch` | [skills/ui-clean-arch/SKILL.md](https://github.com/Javiani/agent-skills/blob/HEAD/skills/ui-clean-arch/SKILL.md) | The linked architecture specification for application organization and boundaries. |
| `jails` | [skills/jails/SKILL.md](https://github.com/Javiani/agent-skills/blob/HEAD/skills/jails/SKILL.md) | The linked mental model and component conventions. |
| `jails-stdlib` | [skills/jails-stdlib/SKILL.md](https://github.com/Javiani/agent-skills/blob/HEAD/skills/jails-stdlib/SKILL.md) | The linked references for the modules used. |

## Load upstream guidance on demand

When a workflow requires upstream guidance, fetch it as part of the task. A workspace with only the Jails.ai skills installed is sufficient. Read upstream skill files directly as task references and keep any checkout in a temporary directory outside the destination project.

For a shell with Git and access to GitHub, use:

```bash
jails_upstream_dir="$(mktemp -d)" &&
  git clone --quiet --depth 1 https://github.com/Javiani/agent-skills.git "$jails_upstream_dir" &&
  git -C "$jails_upstream_dir" rev-parse HEAD
```

With repository-host access, resolve the default-branch commit and read the files directly at that commit. Use this route if Git or a temporary checkout is unavailable. Honor an explicit revision requested by the developer.

Read the required `skills/<name>/SKILL.md` entrypoints and their task-relevant references from the same revision. Reuse the resolved revision throughout the task and record it with the references read in the handoff.

If neither fetch route succeeds, use an accessible local copy as a fallback, disclose that freshness could not be verified, and identify its revision when possible. If required guidance is unavailable, report the specific access blocker and continue any independent work. A separate skill installation is unnecessary.

Check the application's manifest, lockfile, and installed package exports and types for compatibility before applying upstream examples. If the guidance describes an API unavailable in the installed version, report the mismatch. Preserve the application's dependency versions unless an upgrade is requested.

## Check for jails-stdlib reuse

Before creating or editing a Jails component, resolve and read `jails-stdlib` even if the component has no existing stdlib imports. Check its module table for the behavior being added or changed, including custom helpers and direct browser API usage in the affected code.

Read the reference for each candidate and confirm the installed public API covers the required behavior, runtime, and lifecycle. Reuse a compatible module when it reduces custom code and preserves required behavior. Keep a focused implementation when the available modules do not meet the requirement.

## Review Jails changes before delivery

Review additions, edits, and removals against the resolved `jails` conventions and the relevant module contracts. Inspect the actual diff and the resulting affected code. For removals, check remaining callers, registrations, and bindings where applicable. Correct introduced deviations and verify affected mounting, interactions, state updates, and cleanup as applicable.

For new or edited components, recheck the diff for custom behavior that a suitable stdlib module can replace. Report any replacements and explain why a plausible candidate was unsuitable if custom code was retained.
