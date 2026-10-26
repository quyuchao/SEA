# Configuration and change management

Configuration management identifies, controls, traces, and audits the work products that define a software system. Git is one mechanism, not the entire discipline.

## Identify controlled items and baselines

Select relevant requirements, decisions, API/schema definitions, code, dependency locks, build/deployment configuration, tests, documentation, and data/model manifests. Assign each item a known source, owner or responsibility boundary where known, and version or content identity.

Do not commit secrets, unrestricted production data, or large generated artifacts merely to make them versioned. Use appropriate secret stores, artifact storage, data/model registries, or protected systems with traceable references. A redacted configuration template can be tracked without its secret values.

A baseline is an identified, agreed reference set suitable for comparison or reproduction. Record it for consequential migrations and releases, not every edit. Explain which source revisions, dependencies, schemas, data/model versions, and build settings it includes. Do not label an untested snapshot as known-good.

## Control a change

1. Establish the current baseline and requested outcome. Preserve unrelated work and identify the actual repository boundary, especially in nested or multi-repository projects.
2. Analyze affected requirements, components, callers, contracts, data, configuration, documentation, verification, deployment, and recovery. Assess cost and schedule changes when material.
3. Apply the project's decision and authorization rules, reusing existing authorization. Use proportionate review; do not automatically invent a change-control board or approval gate.
4. Implement a coherent change, update related records, and verify the affected configuration. Recheck assumptions when requirements or dependencies change.
5. Record the resulting identities and actual state: proposed, implemented, verified, committed, published, or deployed as applicable.

## Account for and audit state

Maintain enough traceability to answer: what changed, why, in which version, against which requirements, with which verification, and where it is running. Audit a release by comparing intended contents, source/configuration, and delivered artifacts. A successful push is not a deployment audit.

For data/model-driven systems, distinguish source-code revisions from data/model identity. Check that environments and reproducibility manifests do not silently drift. Record exceptions and residual uncertainty rather than claiming exact reproducibility without evidence.
