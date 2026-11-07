# Judgment update for work that outlives the conversation — 2026-11-07

SEA's entrypoint gained one paragraph about work whose result depends on something staying alive: a run that takes hours, a connection that can lapse, an outcome stored only in a fragile place. It extends the same thought-led approach as the 2026-10-27 update and adds no procedure, tool name, time limit or checklist.

## What the paragraph asks the agent to consider

- Treat attention and the environment as finite resources, and reason about what survives their loss.
- State what evidence would change the decision before the evidence arrives, so the result cannot quietly reshape the question.
- Keep the outcome where its own failure cannot reach it.
- Let a mechanism carry the waiting instead of relying on a person to remember to ask.
- Separate waiting for evidence from waiting for a human, and say which one is blocking.

The means are chosen from what the situation offers; the paragraph is a way of thinking about time and loss, not a procedure.

## Origin and limits

It came from a long evaluation workflow in which a remote session was recycled after a run finished and the only copy of the results was lost. That is a single observed case; the paragraph is a judgment aid, not a validated improvement, and it does not claim to change outcomes on every task.

## Scope

Changed: `sea/SKILL.md` and the single-file edition `SEA.md` (same paragraph). `python tests/test_check_skill.py` passes. No change to the validator, references or permissions: the skill still adds no permission to publish, deploy, delete, contact others or replace the user's goal.
