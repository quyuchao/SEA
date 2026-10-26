# Verification and delivery

Unit/integration/system are test levels; black-box/white-box are complementary methods. Choose verification by risk rather than by template.

| Change | Priority checks |
|---|---|
| Presentation | Actual display and affected interaction; build if relevant |
| Rules | Independent examples, boundaries, errors, invariants |
| Interfaces | Caller contracts, compatibility, error semantics |
| State | Isolated storage, concurrency, duplicates, partial failure, recovery |
| User workflows | Critical journeys and useful end-to-end checks |
| Performance | Reproducible workload, baseline, resources, comparison |

A regression check should fail under the old defect and pass after the fix; demonstrate this when feasible. Avoid asserting only function calls or copying implementation logic into the oracle, except where interaction itself is the contract.

Use a sufficiently realistic, isolated environment. Test doubles do not establish real integration; record versions, data, and relevant time/randomness assumptions. Do not use real accounts as fixtures.

Record commands, environment, results, failures, and limits. Distinguish product, test, environment, and existing problems. Do not hide failure through skipping, changed expectations, or reruns. Justify test changes from requirements. Expand regressions by impact and stop repeating checks without new concerns.

Persistent migrations require before/after invariants, backup/recovery, compatibility windows, idempotency/checkpoints, data validation, and stop conditions. Prefer compatible expansion followed by cutover; handle destructive contraction separately. Code rollback is not data recovery.

Choose shadow comparison, flags, or progressive cutover according to impact, with observation, stop, and recovery conditions. Actual release and side effects require authorization. Keep sensitive information out of logs/metrics; derive recovery objectives from requirements.

Before completion, inspect design, behavior, errors, dependencies, compatibility, verification, and documentation. Distinguish self-review from independent review. Report implemented/verified/released/blocked separately. For effectiveness work, define application-level baselines, windows, and sources; consider speed, failures, rework, and recovery together rather than gaming metrics.
