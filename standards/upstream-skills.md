# Upstream skills and framework specifications

Use [Javiani/agent-skills](https://github.com/Javiani/agent-skills) as the sole reference for learning Jails behavior and conventions. Read the relevant guidance maintained in that repository. The upstream skills are distributed under the MIT license, copyright 2026 Eduardo Ottaviani Aragão.

| Skill | Entrypoint on the current default branch | References to read |
| --- | --- | --- |
| `ui-clean-arch` | [skills/ui-clean-arch/SKILL.md](https://github.com/Javiani/agent-skills/blob/HEAD/skills/ui-clean-arch/SKILL.md) | The linked architecture specification for application organization and boundaries. |
| `jails` | [skills/jails/SKILL.md](https://github.com/Javiani/agent-skills/blob/HEAD/skills/jails/SKILL.md) | The linked mental model and component conventions. |
| `jails-stdlib` | [skills/jails-stdlib/SKILL.md](https://github.com/Javiani/agent-skills/blob/HEAD/skills/jails-stdlib/SKILL.md) | The linked references for the modules used. |

## Resolve the current guidance for each task

1. Resolve the current default-branch commit of the upstream repository at the start of the task. Use a fresh shallow clone in a temporary directory, or resolve remote HEAD through Git or the repository host and read the files at that commit. Use one commit for the skill entrypoints and their relative references throughout the task. Honor an explicit revision requested by the developer.
2. Read the required `SKILL.md` files by their exact names and read their task-relevant references within the same repository. Reuse installed copies when their contents match the resolved upstream files. Record the upstream commit and references actually read in the handoff.
3. If upstream freshness cannot be verified, disclose that limitation. Use accessible installed copies as a fallback and identify their revision when possible. If required guidance is unavailable, report which files or references need access before implementing the affected work.
4. Check the application's manifest, lockfile, and installed package exports and types for compatibility before applying upstream examples. If the guidance describes an API unavailable in the installed version, report the mismatch. Preserve the application's dependency versions unless an upgrade is requested.

## Optional installation

To install the current upstream skills into the destination project, run from that project:

```bash
npx skills add Javiani/agent-skills --skill ui-clean-arch jails jails-stdlib
```

Select the target agent and preserve the installer lockfile when applicable. Resolve freshness again when using an installed skill on a later task. This catalog provides source links and a resolution procedure. Skill installation is a separate operation, and `dependencies.tools` in `agents/openai.yaml` is reserved for MCP tools.
