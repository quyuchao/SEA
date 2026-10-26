# Engineering judgment and design philosophy

Use for consequential decisions or explicit discussion of engineering philosophy. These are decision aids, not mandatory ceremonies. Sources and adoption boundaries are maintained in sources.md. No source establishes a universally best architecture, algorithm or working method.

## Turn principles into decisions

| Perspective | Practical question | Consequence and limit |
|---|---|---|
| Purpose and evidence | What observable outcome is needed, and what evidence could refute our proposed solution? | Separate requirements, observations and hypotheses. An elegant model of the wrong problem remains wrong. |
| Information hiding | Which design decision is likely to change, and who currently has to know it? | Localize volatility behind a useful contract. More files or wrappers do not by themselves reduce coupling. |
| Cognitive complexity | How much context must a maintainer hold to make one safe change? | Improve names, interfaces, ownership and locality. A short function can still conceal a distributed state machine. |
| Invariants and state | Which conditions must survive every reachable transition and failure? | Define valid states, identity, units and commit boundaries. Encapsulation alone does not prove atomicity or thread safety. |
| Workload and whole-system cost | Which operations dominate, at what scale and distribution? | Compare runtime, memory, I/O, mutation cost and human/operational cost. An index that speeds reads adds write and consistency work. |
| Reversibility and uncertainty | What would make us change this decision, and what would reversal cost? | Keep cheap-to-change choices simple; reduce risk early for costly state/protocol boundaries. Deferring a feature does not excuse neglecting known recovery needs. |
| End-to-end reasoning | Where can the required business result actually be established? | An acknowledgement or queue guarantee may not establish a committed application effect. Place validation, identity and reconciliation where enough context exists. |
| Feedback and evolution | What is the smallest complete change that tests this assumption? | Use observations, incremental delivery and explicit revisit conditions. A prototype, mock, benchmark or passing test supports only its measured scope. |

## Reconcile competing advice

- Simplicity and performance: retain a clear baseline until workload evidence or a stated constraint justifies complexity. A necessary index or batching scheme can simplify the overall system; the fewest lines are not automatically simplest.
- Abstraction and locality: extract a boundary when it hides a real decision, owns an invariant or removes meaningful duplication. Keep closely related logic together when splitting it would force readers to reconstruct the same operation across files.
- Future flexibility and delivery: separate established variation from imagined possibilities. Prefer a reversible local decision for uncertainty; address known high-impact migrations before they become irreversible.
- Immutability and cost: immutable snapshots can simplify reasoning; large copies may consume memory or latency budgets. Explain ownership and synchronization for either design.
- Reliability and responsiveness: choose timeout, retry and backpressure behavior around the operation's semantics. Dropping disposable observations differs from losing durable commands. Do not claim universal exactly-once effects without a defined identity, consistency boundary and recovery protocol.
- Formal reasoning and experiments: specifications reveal ambiguity and reachable states; implementation checks expose assumptions about arithmetic, runtimes, storage and users. Choose the useful strength of each rather than claiming one replaces the others.

## Minimal decision record

For a consequential choice, record in the existing project record: problem and constraints; current evidence; plausible alternatives; decision and negative consequences; invariants and verification; conditions for reconsideration. Mark uncertainty explicitly. For a routine local edit, a direct implementation and appropriate inspection may be enough.

Avoid authority-based choices, pattern catalogs presented as architecture, invented benchmark results, automatic language/database replacements, and numerical quality scores with no defensible measurement. The goal is better software and clearer decisions, not more documentation.
