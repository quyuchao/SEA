# Reason about execution, resources and guarantees

Use when performance, concurrency, persistence or communication makes the hidden execution mechanism consequential. Follow only the relevant path; these lenses are not a curriculum, a required questionnaire or a reason to redesign a small edit. The checked primary sources and their limits are in sources.md.

## Connect meaning to mechanism

Follow the operation from its domain meaning through representation, scheduling, storage or transport to the result a consumer can observe. Trace deep enough to explain the symptom or test a consequential assumption. An abstraction remains useful when its contract is sufficient; inspect below it when behavior depends on what it hides. Establish the actual runtime, engine, version and configuration before relying on implementation details.

Distinguish accepted, executing, visible, durable and reconciled states where the contract requires them. A successful socket write does not establish a committed business effect; a value visible in memory does not establish recovery after power loss. Locate the boundary that provides the required guarantee and verify at its consumer. CPU cache coherence, language memory ordering, database isolation and distributed consistency solve different problems; analogy does not transfer their guarantees.

## Account for work, movement and waiting

An algorithm runs through a representation on finite hardware. Include bytes moved, copies, allocations and access locality alongside operation counts. Repeated reads or object conversion can dominate inexpensive arithmetic. Contiguous or batched work may improve locality, but bigger batches can increase memory and response latency. Numerical representation also constrains units, range and error; an optimization must preserve the required meaning.

Locate the end-to-end bottleneck with a representative workload before selecting threads, vectorization, caching or hardware. Separate useful execution from I/O, lock, pool and queue waits. Improving a minor component has limited total benefit, and relieving one bottleneck can expose another. Compare equivalent completed work, resource consumption and relevant latency distributions, not just a faster inner loop or average response. Cache warmness, skew and bursts matter when they change the decision; microbenchmarks do not establish application benefit.

## Treat concurrency as ownership and scheduling

Operating systems multiplex finite processors, memory and I/O; application concurrency also consumes handles, connections and retained request state. More runnable work need not mean more progress. Async I/O can release waiting threads while connections, memory and downstream capacity remain occupied.

Model who owns shared state and resources, when they are acquired/released, and which operations depend on others. Choose synchronization around an invariant; a lock in one process does not coordinate another process. Consider deadlock, starvation or cancellation only where the relevant ownership and wait relationships permit them. Separate the mechanism from policy: a worker pool does not decide which work may be delayed or discarded.

When a dependency slows, bounded admission, backpressure or isolation may preserve unrelated work. Limits and priorities must follow actual capacity and product importance; increasing priority can starve supporting work. Rejecting a request, retaining a durable command and dropping a replaceable observation have different semantics. Releasing local resources on timeout does not prove remote work stopped. Check resource release and remaining work on the affected failure path.

## Reason from partial knowledge across a network

The caller and receiver can disagree about completion when a response is delayed or lost. Treat timeout as an uncertain outcome unless the protocol proves otherwise. Establish operation identity, effect boundaries and a way to reconcile before retrying consequential writes. A deduplication token is useful only if its scope, retention, payload binding and effect recording support the required guarantee.

Fit connection/request deadlines and retry budgets to the whole operation. Retries at multiple layers can multiply load; backoff and jitter reduce synchronized pressure but do not make duplicate effects safe. Choose a responsible retry layer where appropriate and verify existing client behavior. Cancellation and failover need defined handling of late completions. Do not infer a global order from unsynchronized wall clocks or delivery order across separate connections.

Use traces or controlled delayed/lost-response experiments to distinguish transport success, application acceptance and committed effects. Never convert transport reliability into an unqualified exactly-once claim. Additional replicas, speculative requests or services require evidence that their coordination and load costs fit the task.

## Derive storage choices from workload and guarantees

Treat storage as an execution, concurrency and recovery system. Start with data meaning and access patterns: the operations that dominate, their consistency/atomicity boundary, freshness, growth, retention and recovery needs. Determine whether a store owns authoritative state or a rebuildable projection. Preserve the existing store when it satisfies those needs; a familiar brand, a fashionable category or company scale is not a migration argument. Embedded/server, relational/document and row/column layouts describe different, overlapping dimensions, not a single ranking.

Follow the relevant read/write path through planning or lookup, indexes/layout, concurrency control, buffering, logging and replication where present. Trace actual engine, version, deployment and configuration. An index has read, write and maintenance costs; a snapshot need not protect a read-check-write invariant; a replica need not be fresh enough for the operation. Establish whether the required atomicity covers a key, document, row, transaction, partition or several services. Select constraints, conditional writes or coordination from the real contract, not from SQL/NoSQL labels.

Examples below illustrate mechanisms that change decisions. Load only the actual engine's primary documentation when needed; the examples are neither an exhaustive catalogue nor a required technology stack.

| Observed mechanism | Consequence for judgment |
|---|---|
| PostgreSQL and InnoDB both support MVCC but have distinct concurrency implementations. InnoDB uses undo for older row versions and rollback. | Check the actual isolation level, read/update semantics and competing sessions; neither the shared acronym nor a snapshot proves the business invariant. |
| SQLite WAL supports concurrent readers and a writer, but only one writer at a time; a long read can hold back checkpoint progress. | Investigate transaction lifetime, writer contention and checkpoint behavior before adding writers or replacing the embedded database. |
| MongoDB writes are atomic at the single-document level; multi-document operations need their own transaction boundary when all-or-nothing behavior is required. | Fit schema and update predicates to the invariant; neither assume all NoSQL stores lack transactions nor assume a bulk call is one atomic effect. |
| Redis offers snapshots, append-only logging or no persistence. | Establish whether data is authoritative and what loss is acceptable; low response time does not establish durable recovery. |
| ClickHouse MergeTree creates data parts and merges them in the background; its key/layout support selective analytical reads. | Examine filters, layout, insert batching and background work. Familiar SQL does not establish the same update, uniqueness or transaction guarantees as another engine. |
| RocksDB compaction policies trade read, write and space amplification. | Include deferred maintenance and steady-state resource demand when comparing ingestion performance, rather than judging only a short write burst. |

For other stores, including time-series, graph, search/vector systems or file/object-backed tables, establish the same relevant contracts from their actual implementation. Check exactness versus approximation, update visibility, deletion and recovery when they affect the task. Avoid forcing an unfamiliar system into the nearest example. A file format or storage engine alone does not supply every guarantee of a database service; multiple stores also introduce synchronization and operational costs.

Verify the suspected mechanism with the supported plan/trace or an isolated workload. Estimated query cost is not measured latency. Execution-based diagnostics such as MySQL EXPLAIN ANALYZE run supported statements, so account for effects and load. Database, OS and device buffers are separate layers; recovery logs, replication and backups serve different purposes. Preserve the agreed failure model instead of weakening durability to report a speedup. Process restart testing alone does not establish power-loss safety.

## Challenge the causal model

Select evidence that can distinguish competing explanations: a wait profile rather than CPU percentage alone, two controlled sessions rather than one successful transaction, a lost acknowledgement after commit rather than a server that never received the request. Preserve a simple baseline and check that the intervention improves the intended result without moving failure or cost elsewhere. Sources suggest hypotheses; the project's observed behavior decides applicability. Stop descending through layers when the important uncertainty is resolved.
