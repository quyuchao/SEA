# Operations and maintenance

Load for running services, desktop/runtime lifecycle changes, incidents, upgrades, or long-lived systems. Scale operational work to user impact and deployment context.

## Operability by design

Identify startup/shutdown, configuration validation, dependency availability, health/readiness, background-worker lifecycle, cancellation, and recovery behavior. Define useful logs, metrics, correlation, and alerts according to real failure modes. Avoid logging credentials or sensitive payloads.

Derive availability, performance, durability, recovery-time, and recovery-point needs from requirements and actual context. Record unknowns instead of inventing service-level targets. Verify backup restoration before asserting recoverability. Provide a short runbook when someone must operate or recover the system.

## Incidents and corrective work

Establish symptoms, affected users/components, timestamps, running versions/configuration, and available evidence. Mitigate under existing authorization, preserve relevant diagnostic evidence, and separate mitigation from root-cause repair. Do not experiment on live state when an isolated reproduction is possible.

Reproduce the issue where practical, analyze causal contributors, implement a scoped correction, and verify recovery and affected regressions. Record unresolved hypotheses, customer-visible effects, and follow-up actions. Do not claim a root cause from correlation alone.

## Evolution and retirement

Track corrective, adaptive, preventive, and improvement work. Prioritize technical debt by current cost, risk, and expected value, with revisit conditions. Plan supported dependency/runtime upgrades, deprecations, API/schema migration windows, documentation, and compatibility checks.

Integrate security through development and maintenance: assess relevant trust boundaries and permissions, protect secrets and artifacts, inspect dependency and licensing implications when changing them, and handle reported vulnerabilities proportionately. Security or privacy-sensitive work may require focused expertise; do not turn every small change into a full audit.

When retiring a component, identify consumers, replacement or migration, state retention/deletion, operational shutdown, and records that must remain traceable. Stop obsolete jobs and integrations only within authorized scope.
