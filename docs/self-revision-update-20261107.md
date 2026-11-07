# Self-revision as a principle — 2026-11-07

SEA's entrypoint gained one paragraph saying that its own guidance is a hypothesis about how to work and can be wrong. It states an attitude, not a mechanism: no automatic rewriting, scoring loop, tool or schedule is added.

## What it asks

- Let experience, not preference, revise the guidance; a principle that misleads, adds weight without changing a decision, or fails on a case it should have handled is evidence about the principle itself.
- Prefer sharpening or removing a principle to stacking another beside it.
- Keep negative results; test a proposed change on cases it was not written for, so the guidance does not only learn its own history.
- Aim for judgment that improves with use and stays small. Changes remain the owner's decision.

## Limits

This is an intention, not evidence that the skill improves a model. Whether guidance of this kind raises the quality of an assistant's work has to be measured on held-out tasks with and without the skill; that measurement has not been done. A static text does not evolve on its own: revision happens when someone applies this paragraph to real failures.

## Scope

Changed: `sea/SKILL.md` and `SEA.md` (same paragraph). Validator and tests unchanged; run `python tests/test_check_skill.py`.
