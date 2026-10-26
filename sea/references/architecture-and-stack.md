# Architecture, technology, and data

## Technology decisions

List constraints and the existing system first. Compare the current approach with reasonable alternatives for important decisions. Record evidence, uncertainty, consequences, and reconsideration triggers. Do not portray subjective scoring as objective measurement.

| Dimension | Evidence |
|---|---|
| Workload | Data volume, peaks, CPU/I/O characteristics, measured bottlenecks |
| Quality | Latency/throughput, precision, reliability, failure impact |
| Ecosystem | Required libraries, protocols, hardware, platforms, versions |
| Operations | Build, deployment, monitoring, upgrades, recovery |
| Maintenance | Team skills, debugging, support, migration cost |
| Resources | CPU/memory, delivery time, licensing, operating cost |

As relevant, inspect ownership, lifetime, undefined behavior, ABI, and builds for C++; runtime, framework compatibility, threads/transactions, and memory for Java; type boundaries, environments, numeric dependencies, and CPU/I/O concurrency constraints for Python; and goroutine lifetime, cancellation, errors, races, and builds for Go. These are evaluation prompts, not a language ranking. Evaluate other languages against the same project constraints.

Measure before optimizing. Across language boundaries, define protocols, serialization, errors, time units, versions, build/deployment, and contract testing costs. Verify changing support, versions, and licensing against current primary sources; retain explicit unknowns when verification is unavailable.

## Modules and contracts

Partition around business capabilities and state ownership, not merely folders. Record responsibilities, interfaces, owned data, dependencies, and failure policies. Distinguish static dependencies from runtime calls.

Separate business rules from UI/framework details. Use functions, protocols, or interfaces at real boundaries. Apply single responsibility, open/closed, substitution, interface segregation, and dependency inversion where they provide value; avoid mechanical layering.

Define validation, identity/authorization, errors, versions, timeouts, cancellation, retries, and idempotency for external interfaces. Do not blindly retry payments, orders, or other effects; query or reconcile uncertain outcomes.

## Data and databases

- Evaluate relational, document/key-value, columnar-file, and object storage against access patterns and consistency. Volume alone does not justify a distributed database.
- Define entities, keys, uniqueness/referential constraints, null semantics, monetary precision, time zones, and intervals. Protect important constraints at appropriate layers.
- Define transactions, isolation, locking or version checks, races, and deadlock handling. Coordinate idempotency keys and state updates within a consistency-preserving boundary.
- Validate indexes against queries and execution plans. Define cache invalidation, staleness tolerance, and origin failures. Require evidence for partitioning/sharding.
- Identify authoritative data and derived views. Evaluate outbox or compensation patterns for cross-resource effects; do not assume distributed atomicity.
- Define schema evolution, old/new version compatibility, migration validation, backup/recovery, permissions, and retention. Untested restoration does not establish backup recoverability.

Use the project's ADR convention for consequential choices: context/constraints, alternatives, decision, negative consequences, verification, and reconsideration triggers. Do not add ADRs for routine local decisions.
