# Versions, integration, and releases

## Choose version boundaries

Inspect existing version files, tags, artifact naming, release history, and deployment units. Decide whether the product ships together or components are independently released; repository layout alone does not decide this. Preserve the established scheme unless a justified change is part of the task.

When adopting Semantic Versioning, define the public contract and apply major/minor/patch according to compatibility, with its special rules for initial development and prereleases. Do not increment a product version for every edited file or equate commit count with a compatibility guarantee. Check current policy before bumping manifests or creating tags.

## Coordinate frontend, backend, and storage

For a cross-component change, trace the user flow through UI/client types, API requests/responses/errors, backend behavior, database schema, configuration, tests, and documentation. Identify old clients, cached assets, background jobs, and other consumers where relevant.

Define a compatibility window and rollout order for independently deployed components. Prefer compatible expansion, consumer migration, and later contraction when appropriate. Consider feature flags or capability negotiation only when needed. Update generated clients and contract checks with their actual source schema.

A single product release can use a shared version; independently shipped components need identities and compatibility information. State the intended pairing explicitly. Database migrations, API contracts, model/data identities, and source commits have different meanings and must not be collapsed into one arbitrary number.

## Assemble and verify a release

Use a minimal manifest suited to risk. Record product/component versions, source revision(s), artifact identity/digest, build environment or dependency locks, API/schema compatibility, migrations, relevant configuration, data/model references, verification, and remaining limitations. Protect secret values.

Verify that artifacts came from the intended source and configuration. Distinguish reproducible builds from merely repeatable commands; do not promise byte-identical output without evidence. For consequential releases, retain traceable artifact storage and appropriate provenance rather than rebuilding an unknown replacement later.

Update release notes with user-visible changes, compatibility, migrations, and known issues. Tags and release entries identify a release but do not prove it was deployed. Tag/release creation, publication, repository visibility changes, and deployment must remain within existing authorization and project policy.

## Deploy, observe, recover

Define readiness, rollout order, observation, stopping, and recovery criteria. Check post-deployment health and critical behavior before calling deployment verified. Record what version actually runs in each relevant environment and its verification state.

Explain whether recovery uses rollback, roll-forward, restore, or compensation. Code rollback cannot undo incompatible schema changes, lost data, or external side effects. Validate recovery against the relevant invariants and keep release/deployment failures visible in task status.
