# Project management

Load for multi-step development, roadmap/backlog work, or changes spanning components. Keep a small local task lightweight.

## Establish the working agreement

Inspect existing tasks, milestones, repository instructions, and delivery conventions. Identify the authoritative tracker and reuse it; do not create a parallel backlog. If none exists, use a small project record rather than requiring a hosted service. Define scope, outcomes, stakeholders or decision roles when relevant, constraints, and completion evidence.

For an unfamiliar project, record only useful facts: architecture and entry points, stack/lockfiles, component ownership, build/test commands, deployment units, source repositories, and known limitations. Use the project profile template only when a durable record helps.

## Plan and execute

- Break outcomes into independently verifiable increments. Include necessary design, integration, migration, testing, documentation, and recovery work in estimates and task scope.
- Record an ID, acceptance conditions, priority/rationale, dependencies, status, and next action for substantial tasks. Record owners or decision roles when known; do not invent people or assignments.
- Adapt statuses to the existing process. A minimal model is planned, ready, in progress, review/verification, done, or blocked. A blocked task needs a reason and an unblocking action. Tests or publishing not performed cannot be represented as done.
- Order work by value, dependency, risk, and information gained. Identify schedule-critical dependencies when needed, without imposing a formal critical-path analysis on small tasks.
- Give numerical effort/schedule estimates only when useful and supported by a task breakdown or comparable evidence. Otherwise describe drivers and missing inputs; hypothetical examples are not project estimates. Use assumptions, ranges, and confidence where justified. Include maintenance and operational cost in consequential decisions. Do not fabricate dates, staffing, budgets, or percentage completion.
- Track scope changes and their impact on acceptance, architecture, cost, schedule, and risk. Adjust the plan when evidence changes instead of silently adding work or preserving an obsolete promise.

## Review and close

Update the authoritative tracker as work changes. Link important requirements to implementation, verification, and relevant commits/PRs when available. A proposed patch, a passing build, and a deployed feature are different milestones.

Record unresolved defects, technical debt, and accepted limitations with consequences, priority, and a revisit condition. Do not present debt as completed functionality or require a new issue for every cosmetic detail. Close the increment using actual acceptance evidence; report remaining work and a concrete next step.

Use GitHub Issues, Projects, or another tracker when available and authorized. Existing authorization persists; a plan or skill invocation alone does not authorize external mutations. Missing hosting tools must not block local planning or implementation.
