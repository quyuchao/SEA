# Data structures and algorithms

Use when algorithmic behavior, workload or persistent representation materially affects correctness, growth or performance. For small bounded work, apply the reasoning directly without a report. This is a selection guide, not a requirement to replace lists, dictionaries or an existing database.

## 1. Model the operation and workload

Establish inputs, outputs, identity/equality, ordering/tie rules, mutation, units and precision. Distinguish unknown, absent and zero. Identify authoritative state and derived structures.

Define relevant scale variables: active records, historical records, groups, window size, result count, payload bytes, concurrent writers or dependency edges. Inspect observed or expected distributions: skew, bursts, duplicates, out-of-order arrival and query/update ratios. Mark unmeasured values and targets as unknown. Do not invent an SLA.

List dominant operations and their frequency: lookup, append, cancellation/deletion, min/max, range search, sorting, aggregation, joins, graph traversal or incremental updates. Count costs over the whole operation: a linear scan inside a per-group loop can dominate a constant-time individual lookup. Consider serialization, copies, allocations, locks, network/disk trips and index maintenance.

## 2. Compare plausible representations

These costs assume standard implementations and bounded-cost comparisons/hashing; inspect runtime-specific behavior when it matters.

| Need | Candidate | Trade-off to verify |
|---|---|---|
| Small bounded or sequential collection | Array/list | Simple contiguous iteration; arbitrary search/deletion can be linear. Repeated full copies may dominate. |
| Exact identity lookup or membership | Hash map/set | Typically average constant-time lookup with additional memory; collision, resizing and key-cost assumptions matter. It does not supply chronological/range order. |
| FIFO or recent window | Deque/ring buffer | Efficient end operations and explicit capacity; arbitrary ID removal or indexing may still be linear. Define overflow and eviction behavior. |
| Next priority/deadline | Heap, optionally with ID index | Typical peek O(1), insertion/pop O(log n); arbitrary cancellation needs an indexed structure or lazy deletion. Bound tombstones and account for compaction latency. |
| Ordered/range queries or durable history | Sorted structure/database index | Evaluate insertion, deletion, ranges and matching predicates/order. Use execution plans and result cardinality; extra indexes have write/storage costs. |
| Batch numerical or analytical work | Contiguous/columnar arrays and vectorized kernels | Can reduce interpreter/allocation cost; intermediate copies, sparse data, memory pressure and numeric behavior may negate the benefit. |
| Dependency relations | Adjacency representation | Traversal/topological ordering can be O(V+E); define cycles, disconnected components and deterministic tie-breaking. |

For top-k selection, compare a bounded heap (often O(n log k), O(k) working storage) with sorting when the full order is needed or inputs are small. For rolling statistics, compare recomputation with incremental state; verify deletion/expiry, rounding drift and recovery. For pagination, distinguish simple offset pagination from cursor/keyset pagination for deep history; define a stable unique ordering and behavior under concurrent inserts/updates. Do not promise snapshot pagination without a snapshot contract.

Prefer existing library/database primitives. Introduce custom trees, indexes or schedulers only for a demonstrated requirement, with tests of update, deletion and failure paths.

## 3. Preserve semantics and consistency

- Define invariants, preconditions/postconditions and termination or cancellation. Check empty/singleton inputs, duplicate identities, ties, bounds, overflow, NaN/infinity, precision, time zones and out-of-order data where relevant.
- Distinguish average, amortized and worst-case bounds; include working memory and retained memory. Amortized throughput can conceal a pause that violates a latency requirement.
- Specify who owns and mutates each representation. Define synchronization or version checks and how authoritative data, lookup indexes, group indexes and aggregates change together. Identify the commit/linearization boundary; test interrupted or competing changes.
- Separate persistent history from the active working set. Bound caches, queues and deferred deletion; define backpressure, eviction and rebuild/reconciliation behavior. Retain required audit and deduplication evidence or provide a durable equivalent before dropping it.
- For approximate/probabilistic algorithms, state the error/failure model and whether the domain permits it. Do not replace exact money, authorization or required event membership with an approximation merely for speed.

## 4. Verify and record the decision

Use independent examples, invariants, a simple trusted baseline, differential/property tests, or bounded state exploration as appropriate. Useful checks include conservation, stable tie order, query equivalence after indexing, and replay/restart equivalence. Test adversarial distributions and sustained resource growth, not just happy-path averages.

For a performance claim, keep inputs and semantic work comparable; record data size/distribution, versions/environment, warmup, repetitions, statistics and what was mocked. Profile the actual hot path; compare CPU, I/O, peak/retained memory or lock waiting as relevant. State when measurement overhead, background load or small samples limit the conclusion. Big-O analysis is not a latency measurement, and a faster result with missing required work is not an equivalent optimization.

Record only the consequential decision: workload and invariants; baseline/candidates; operation and memory costs with assumptions; chosen trade-off; correctness and measurement evidence; remaining limits/revisit trigger. Reuse the existing engineering record. A representation decision must not silently change the user's business algorithm or risk policy.
