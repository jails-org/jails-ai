# Organize the specification directory

Keep `specification/` at the application root as the canonical home for project specifications and extracted documentation. It is a directory, not a single Markdown file. Use the lowercase filename `readme.md` consistently.

## Directory structure

```text
specification/
├── readme.md
├── home/
│   └── readme.md
└── orders/
    ├── readme.md
    ├── filtering.md
    └── checkout.md
```

The domains and topic files above are illustrative. Reuse actual domain/page directory names from the application, create only scoped documentation, and do not invent pages or empty files to reproduce the tree.

### Project entrypoint: specification/readme.md

Keep general and project-wide information here:

- Project overview, scope, and supported product goals.
- Structural decisions and conventions affecting the whole application.
- Shared application rules, global requirements, and cross-page contract semantics.
- An index linking each domain/page directory, its routes, key rule IDs, and documentation/inspection coverage.
- Project-wide open questions and a concise coverage/continuation summary when needed.

Do not put full page-specific rules here. Reference them through domain links. A cross-page rule has one canonical definition here; domain documents link to its ID instead of duplicating it. Preserve the distinction between confirmed requirements, observed behavior, and inferred intent.

### Domain entrypoint: specification/<domain>/readme.md

Each domain/page folder contains only that domain's requirements and evidence. Its entrypoint describes purpose, routes, scope, meaningful sections, key journeys/UI states, local rules and acceptance criteria, data contracts, implementation mapping, references, and local open questions. Include only applicable headings.

Keep a concise summary and links to any topic documents in the same folder. Split a large domain into meaningful topics such as `filtering.md` or `checkout.md` when it improves retrieval. Do not create a file per sentence or a deep hierarchy without need. The folder owns its page-specific rules; do not copy other pages' rules into it. Cross-page dependencies link to their canonical definitions.

Multiple route variants of one screen may share a domain folder when their differences are documented. If screen ownership is unclear, inspect source and ask only when a product/domain decision remains unresolved.

## Stable rule records and links

Preserve existing identifiers. For new entries, use unique searchable IDs, for example `HOME-RULE-001`, without renumbering unrelated rules. For each rule, record applicable scope, trigger/preconditions, expected or observed behavior, acceptance criteria, persistence/propagation, integrations, implementation mapping, and evidence. Track requirement authority separately from implementation/verification status.

Use relative Markdown links between documentation files, with durable anchors where a particular rule is referenced. Resolve source/asset references relative to the document containing the link; moving a rule into a domain folder changes that base path. Keep root and domain indexes current when files or rules move.

## Focused retrieval and updates

- Start with `specification/readme.md`, then read only the relevant domain entrypoint, linked topic files, and applicable shared or cross-domain rules. Search by routes, IDs, and source paths rather than loading the entire directory.
- Summaries aid navigation; preserve full rule details, exceptions, evidence, and acceptance criteria in their owning documents.
- Store each rule once. Link to maintained schemas, fixtures, and source instead of copying large code blocks or logs into the specification.
- Edit the smallest relevant file and update indexes when necessary, preserving unrelated domains.
- Save findings after each domain batch during extraction. Keep local continuation details with their domain and a brief project-level coverage summary in the root readme. Record exact remaining paths/IDs, not an investigation transcript.

## Migrate the legacy specification.md

If an application still has a root `specification.md`, inspect it before creating or merging the new directory. If both formats exist, reconcile them rather than choosing one silently.

1. Inventory its overview, shared rules, domain/page rules, identifiers, evidence, open questions, and incoming links.
2. Move project-wide content to `specification/readme.md` and domain-specific content to its owning folder, preserving IDs, authority, verification status, and complete rule details. Ask when ownership or conflicting versions cannot be resolved from context.
3. Merge with existing directory documents without overwriting newer content or duplicating rules. Update relative source links, anchors, and in-scope consumers that reference the old file.
4. Verify every legacy section has a destination and all links resolve before removing `specification.md`. If unresolved material prevents safe migration, retain it temporarily and report the remaining work; do not leave two competing canonical versions or claim migration complete.

## Review

Check that all documented domains have root index entries, every topic is discoverable from its domain readme, IDs are unique, links resolve, and source mappings exist where claimed. Verify that the root readme contains general/shared information and domain folders contain only their own rules. Preserve discrepancies instead of silently rewriting confirmed requirements. Do not imply coverage that was never inspected.
