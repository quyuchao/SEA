# Aesthetic and motion judgment — 2026-11-07

`readability-and-product-design.md` (and the matching appendix of `SEA.md`) gained a section on aesthetic and motion judgment. It is written as principles, not a style guide, a timing table or a library recommendation.

## What it says

- Aesthetics are plural. Each style is coherent under its own rules; name the intent first, then judge fit to purpose and internal consistency, not fashion or the agent's preference. Learn the owner's taste; otherwise use a restrained default and state the assumption.
- Motion is information before decoration: it should tell the user something, weigh less when frequent, follow distance and importance, stay consistent within a product, never block the task, and degrade for reduced-motion preferences and slow devices.
- Taste is tested by repeated use in context, not a first glance; the agent's sense of beauty is a hypothesis, and the intent is recorded so later changes can be checked against it.

## Limits

The wording is the author's synthesis. A community motion-design skill (LottieFiles/motion-design-skill) was consulted only at repository-description level; its detailed timing and easing tables were not read, and nothing is copied from it. No claim is made that this improves visual quality; that would need comparison on held-out design tasks.

## Scope

Changed: the reference, the matching `SEA.md` appendix, and one line of the entrypoint's reference list in `sea/SKILL.md` and `SEA.md`. `python tests/test_check_skill.py` passes.
