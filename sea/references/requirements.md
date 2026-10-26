# Requirements and traceability

Establish the user, scenario, current behavior, expected outcome, and evidence. Distinguish functional requirements, quality requirements, environmental constraints, and assumptions. Turn "fast," "stable," and "easy" into observable conditions. Establish a baseline when measurements are missing; do not invent thresholds.

Record scope/exclusions, inputs/outputs, failure/cancellation, permissions, compatibility, and dependencies. Ask about unknowns affecting requirements or consequential choices; state ordinary reversible assumptions and continue.

Assign stable IDs to important requirements without renumbering them when reordered. Reuse project records and track:

| ID | Scenario and requirement | Acceptance method | Design/implementation | Evidence | Status |
|---|---|---|---|---|---|
| R-01 | Duplicate events must not apply a business effect twice | Applying the same event twice produces the same state as once | Actual module/symbol | Actual check or pending | Not started / Implementing / Verified / Blocked |

Replace this example with real requirements. Describe acceptance through initial conditions, action/event, expected result, and forbidden side effects. Implementing a function does not establish scenario acceptance. Synchronize design, implementation, and verification when requirements change; distinguish this increment from later work.

Use phases for stable dependencies, short iterations for exploration, and time-boxed prototypes with success and exit criteria for technical unknowns. A prototype answers its specific question; integration still requires verification.
