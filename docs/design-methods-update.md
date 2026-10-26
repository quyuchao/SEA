# Design-methods update — 2026-10-26

This update makes engineering judgment, workload-driven data structure/algorithm selection, code readability and product interaction explicit in SEA. Detailed guidance remains in three on-demand references; small edits keep the lightweight path. The sources and adoption limits are recorded in [sources.md](../sea/references/sources.md). No universal best-method ranking, author endorsement or OpenAI affiliation is claimed.

The package adds guidance on dominant operations, active versus historical growth, average/amortized/worst-case costs, memory/I/O, index maintenance, authoritative state, numeric semantics, retention, failure/recovery, independent correctness checks and comparable measurements. Readability and user experience have separate inspection criteria. Existing permission and delivery boundaries remain in force.

## Limited forward validation

The installed candidate was structurally checked and independently exercised by another agent in a fresh context with raw synthetic inputs. It received the skill, task and permitted workspace without the intended solution. A primary-agent review examined the actual outputs and file effects.

| Request | Actual result | Boundary |
|---|---|---|
| Change a small static button caption while preserving its behavior | Only the target visible text changed; inverse replacement restored the original file hash | No browser or runtime interaction was claimed |
| Design the scheduler scenario now recorded as B7 | Compared list/hash/heap/index alternatives; selected a transactional indexed baseline conditionally; specified claim/cancel ordering, recovery and validation; execution file hash was unchanged | Design only; no target implementation, concurrency experiment or performance benchmark was executed; 10ms remains a target |

These two cases provide limited behavior evidence, not a cross-model benchmark, baseline-comparison proof, all-task correctness claim or host automatic-loading test. Keyword or heading presence is not evidence of a correct algorithm. The complete private workspace logs are not part of this repository; the scenario and result scope are stated here so the claim is inspectable without publishing machine paths or unrelated project/account artifacts.

## Maintainer checks

Run the existing checks on the repository package:

```sh
python sea/scripts/check_skill.py sea
python -m unittest discover -s tests -v
python sea/scripts/check_skill.py sea --portable SEA.md
```

The regression suite checks the validator and deterministic inclusion of all 17 referenced resources in the generated edition. It does not prove engineering behavior, performance, browser usability or installation on every host. CI remains the existing Linux/Python 3.10 package workflow; a local passing result is distinct from a hosted CI result.
