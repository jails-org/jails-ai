# Extract a PRD or application documentation

Use this workflow when the developer asks to extract, reverse-engineer, or document an existing project. The deliverable is an evidence-backed PRD or documentation inside the application-root `specification/` directory, alongside existing specifications. Do not require a separate PRD file or change application behavior merely to document it.

## Establish scope and inspect

Identify the application and whether the request covers the whole project, selected domains/pages, or a particular flow. Use the stated scope; ask if ambiguous. For a whole-project extraction, inventory all routes and domains before investigating them in manageable batches. Record the revision inspected when identifiable.

Read `specification/readme.md` and the relevant domain readmes/topic files first. If the legacy `specification.md` exists, migrate it using the organization guide without losing rules or evidence. Inventory routes, layouts, structural components, controllers, Stores/actions, Services, Entities, tests, fixtures, and supplied product documents. Use the upstream `ui-clean-arch` guidance to interpret responsibility boundaries, but describe the actual implementation even if it does not follow that architecture. Do not manufacture missing abstractions or silently refactor the application.

Trace each scoped page through its significant user journeys:

- Purpose, actors, entry/exit points, navigation, and prerequisites.
- Visible sections, content, responsive behavior, accessibility behavior, and available actions.
- Input validation, state transitions, cross-section effects, and persistence.
- Data contracts and external integrations, including loading, empty, error, and success handling.
- Observable restrictions, calculations, defaults, and acceptance scenarios supported by the evidence.

Inspect runtime behavior with available browser tools where useful, using representative non-destructive journeys. Do not send messages, submit real transactions, or change external records just to discover a rule. When runtime access is absent, describe the code path and mark it as source-inspected rather than tested.

Tests show intended assertions but do not prove they currently pass. Fixtures show sample shapes, not guaranteed production contracts. Names, UI labels, comments, and apparent product purpose do not establish hidden business intent. Do not reproduce secrets or production personal records in the documentation.

## Record evidence and uncertainty

Keep requirement authority separate from implementation evidence:

- **Confirmed requirement:** explicitly supplied or confirmed by the developer or an authoritative project specification.
- **Observed behavior:** directly traced in source or runtime; not automatically an approved product requirement.
- **Inferred intent:** a plausible explanation that needs confirmation, clearly separated from established rules.
- **Open question:** insufficient or conflicting evidence; record what must be clarified.

Attach relevant repository-relative source/test paths, symbols, supplied document references, or runtime scenarios to each substantial extracted rule. Record verification separately: source-inspected, runtime-observed, test-passed, or not verified, with accurate scope. Do not label a source-only observation as runtime-verified or a legacy defect as a confirmed requirement.

For conflicting evidence, preserve the existing confirmed specification, document the discrepancy and its impact, and ask the developer when a product decision is needed. A missing frontend permission check does not prove unrestricted backend access, and client-side validation does not prove server enforcement.

## Produce an organized PRD in specification/

Follow [the specification organization guide](specification-organization.md). Update project-wide overview and shared information in `specification/readme.md`, and scoped domain/page documentation in `specification/<domain>/` with goals supported by evidence, journeys, functional rules, data contracts, acceptance scenarios, implementation mapping, and open questions. Record nonfunctional requirements only when supported; do not invent performance targets, SLAs, personas, or business objectives.

Merge extracted behavior into matching entries rather than duplicating them. Preserve explicit distinctions between desired and implemented behavior. Acceptance scenarios derived from observations describe current behavior; they do not approve it as a future requirement without confirmation.

For large projects, maintain the route/domain coverage index in the root readme after every batch. Mark each area as documented, partially inspected, or not inspected, stating remaining routes and paths to investigate. Keep a short durable continuation note with completed domains, unresolved questions, and next inspection points so later work can resume without rereading the entire application. Do not claim complete extraction when any requested area remains uninspected.

## Deliver documentation without implicit implementation

Review identifiers, links, coverage, evidence labels, and consistency with existing rules. Verify that only requested documentation changed. Report the root readme and affected domain/topic paths, documented domains/pages, observed versus confirmed rules, inspected evidence, unresolved discrepancies, and remaining coverage.

If implementation is also explicitly requested, finish documenting the evidence and intended changes first, resolve material ambiguities, then use the implementation workflow in `SKILL.md`. Extraction alone never authorizes fixing every discrepancy found.
