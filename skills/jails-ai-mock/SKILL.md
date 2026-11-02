---
name: jails-ai-mock
description: Create JSON response fixtures organized by screen domain under public/mocks/ from instructions identifying dynamic screen data. Follow a supplied schema or propose a service-ready contract, then show the developer the resulting JSON structure.
---

# jails-ai Mock

Invoke with `/jails-ai-mock` in GitHub Copilot Chat or `$jails-ai-mock` in agents supporting dollar mentions.

Create mock response files for the dynamic data identified by the developer. The primary deliverable is valid JSON in the target application's `public/mocks/<domain>/` directory, plus a readable explanation of its contract. Do not wire the mock into the application or replace existing data sources unless requested.

## Ask about the contract first

Before generating or writing a fixture, ask: “Do you already have a response contract or schema for this data?” Do not repeat the question if the developer has already supplied a contract or explicitly stated that none exists.

- **Yes:** ask the developer to paste or attach the contract, schema, or example response. If it was already supplied or referenced, read it instead of requesting it again. Wait for access to the actual content before generating a contract-dependent fixture; do not replace an unavailable contract with an invented one.
- **No:** gather the dynamic data requirements through the focused discovery questions below before proposing the response structure.
- **Not yet answered:** wait for the answer while inspecting the project and screen. Do not treat silence as confirmation that no contract exists.

Use a question mechanism that supports the requested input. If a tool accepts only text, ask there for text or a reference; request file attachments through normal conversation instead of claiming the tool supports them.

## Identify the dynamic data

Locate the target application root from the request and project context. Inspect local instructions, the relevant screen, its Services and Entities, existing mocks, and `specification/readme.md` and relevant domain/topic documents when present. Ask for the project or screen only when ambiguous. Write fixtures in the application, not in the installed skill directory or the jails-ai distribution repository.

Use `public/mocks/<domain>/`, following the Starter-Kit's public asset directory; treat `publick/mocks/` as a spelling error unless the developer explicitly requires that literal directory. Create missing directories as needed. If the application configures a different public root, identify it and clarify the destination before writing an unserved fixture.

Resolve `<domain>` from the screen's owning domain in the application, such as `src/domain/home` → `public/mocks/home/`. Reuse the actual domain directory name, not the page title, component name, or a guessed business grouping. If ownership cannot be determined from the request and source, ask which screen domain owns the data before writing files. If the domain is being created, use its agreed name consistently in the source and mock directory.

Keep all fixtures for that screen under its domain directory, including distinct responses and scenario files. For instructions spanning multiple domains, place each screen's fixtures in its respective directory; do not put new JSON files directly in `public/mocks/`.

When no contract exists, ask the developer which screen or section the mock serves and which visible data is dynamic rather than static. Use the actual screen context to make the questions concrete, for example: “Should the order list, summary totals, and filter options all come from this response?” If the initial request already answers these questions, ask only about remaining gaps.

Then ask the relevant follow-up questions needed to shape the JSON:

- Which fields does each item require, and what identifies it?
- Which values are lists, nested objects, or relationships to other records?
- Are counts or totals supplied by the response or computed from the returned items?
- Are filters, ordering, pagination, or separate responses part of the intended data contract?
- What types, allowed statuses, date formats, currencies, or measurement units are expected? Can any values be missing or null?
- Which representative scenarios and approximate record counts are needed, such as populated, empty, or partially available data?

Select and group only questions relevant to this screen; do not present the entire list mechanically. Inspect the code and existing specifications first, reuse answers already available, and ask behavioral questions rather than requiring the developer to design JSON syntax. Wait for answers that materially determine the payload. If the developer explicitly delegates remaining contract decisions, propose reasonable choices and identify them as assumptions in the final explanation.

Map the specified dynamic regions to response fields: repeated items, identifiers, values, relationships, totals, filters, pagination, or status when relevant. Do not turn unrelated static labels or layout structure into API data automatically. Reuse existing field semantics and contracts when they fit the request.

## Respect or propose the contract

When the developer supplies an exact response schema, signature, example contract, or JSON Schema:

- Preserve its root type, field names, nesting, required fields, optionality, nullability, types, enums, and constraints. Do not add an envelope or rename fields for personal preference.
- Generate representative values consistent with that contract. Ask about contradictory requirements rather than silently changing the schema.
- Treat an example as evidence of its visible structure; do not infer constraints it does not establish.

When no exact contract exists, complete the focused discovery above, then propose and write a practical JSON response based on the developer's answers, the screen, and requested behavior. Creating the proposed contract is part of this skill; do not require the developer to supply a schema. Do not skip discovery and silently infer dynamic fields solely from visible UI.

Keep the proposed response data-oriented and usable by a future Service. Follow existing project naming conventions; otherwise use consistent English camelCase field names. Use stable fictional identifiers, correctly typed values, coherent relationships and totals, explicit units or currency when needed, and unambiguous dates. Keep presentation markup, Tailwind classes, SVG bodies, and component configuration out of response data. Avoid unnecessary envelopes, pagination, and metadata when the use case does not need them.

Label inferred field semantics and business assumptions as proposals in the developer-facing explanation, not as confirmed backend guarantees. Do not add invented business rules to the `specification/` documents. Use fictional data and no credentials or personal production records: public fixtures are served to clients.

## Write the fixture

Create the domain directory if missing. Choose a descriptive kebab-case response filename inside it, for example `public/mocks/home/summary.json` or `public/mocks/orders/order-list.json`, unless the developer specifies a filename. Keep the domain directory even when a filename is supplied. Prefer one file per distinct response contract. Add separate scenario files only when requested or needed to demonstrate a specified state; do not create a fixture suite by default.

Inspect a matching existing fixture before changing it. Do not silently move legacy fixtures from the root mock directory or change their consumer URLs; if migration is requested, update affected consumers within scope and report the new paths. Preserve unrelated files and fields required by its contract; if replacement would break existing consumers, identify the conflict and clarify it. Repeated use for the same instruction should update the appropriate fixture rather than create arbitrarily numbered duplicates.

Write UTF-8, consistently indented, strict JSON: no comments, trailing commas, undefined values, NaN, or executable expressions. Use enough representative records to exercise the requested dynamic content without creating an unnecessarily large payload. Do not create schema files, endpoint handlers, dependencies, or application code unless requested.

## Application integration when requested

Read `ui-clean-arch` and its specification through [the upstream catalog](references/standards/upstream-skills.md), and apply [the architecture acceptance criteria](references/standards/ui-clean-architecture.md). Load the relevant `jails` and `jails-stdlib` guidance for changed behavior and inspect the existing Starter-Kit examples.

Read mock responses through the appropriate Service boundary; do not embed fetch or storage access in Components or Stores. Use Entities for necessary semantic adaptation, and the screen Store for cross-component propagation or persistence. A static fixture does not implement filtering, mutations, pagination, latency, or error handling merely by containing fields describing them.

If UI changes are requested, apply [the Tailwind standard](references/standards/tailwind.md) and [the SVG/icon standard](references/standards/icons.md). Keep shared conventions and structural component boundaries intact.

## Validate and show the developer

Parse the saved file with a JSON parser. Check the result against the supplied contract and, when a formal schema and validator are available, validate it with those constraints. For proposed contracts, check consistent types, identifiers, relationships, units, and derived values. Do not claim formal schema validation when only JSON parsing or manual contract review was performed.

In the final response, provide:

1. The fixture file path and expected public URL. For the `home` domain, `public/mocks/home/summary.json` is normally served at `/mocks/home/summary.json`; account for the application's configured base path and do not claim HTTP verification unless performed.
2. A friendly, pretty-printed `json` code block showing the saved payload. Show the complete JSON when reasonably sized. For large payloads, show a clearly labeled representative excerpt retaining the actual nesting and field names, and link to the full file.
3. A short explanation of important fields, collection item shape, units, optional/null values, and assumptions. Distinguish a developer-supplied contract from a proposed one.
4. Validation results and whether application consumption was implemented or the fixture is ready for later Service integration.

The preview must match the saved file; do not show a different illustrative schema or put comments and ellipses inside a block presented as valid JSON.
