# Anticipating use that cannot be enumerated - 2026-11-09

`sea/references/engineering-judgment.md` gained a section, "Anticipate use you cannot enumerate", and the entrypoint's trigger line now also covers features that will face operation orders or environments nobody can list.

## What it asks

- Do not try to imagine "a hundred users". First remove a class of misuse by design: make the illegal state unrepresentable, keep identifiers stable, state the invariant, expose less observable behavior for others to depend on.
- Probe what remains along dimensions taken from the change's lifecycle: interrupted/repeated/reordered operations, several people or devices (including old client with new server), what identifies an entity and whether it can change, every derived copy and when it catches up, environment differences, boundary input, and half-finished results on failure.
- Treat existing practice (failure-mode analysis, state-transition and boundary tests, fault injection, property-based testing) as a source of cases, not a ritual. Spend effort by worst-case cost: lost or misattributed data, then wrong state, then delayed display.

## Limits

The named practices come from common engineering knowledge; no primary source was opened or checked (see the new row in `sea/references/sources.md`). The text is untested: whether it changes an assistant's work for the better has not been measured on held-out tasks.

## Scope

Changed: `sea/SKILL.md`, `sea/references/engineering-judgment.md`, `sea/references/sources.md`, regenerated `SEA.md`. Validator and tests unchanged; `python tests/test_check_skill.py` passes.
