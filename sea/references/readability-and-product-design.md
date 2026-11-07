# Readability and product design

Use the relevant part for substantive code/design changes or UI work. Internal maintainability and user-facing usability are different quality dimensions; neither is established solely by passing backend tests. A small copy edit usually needs direct inspection, not a design-system project.

## Readable and changeable code

- Use domain names that distinguish identities, units, timestamps and lifecycle states. Make meaningful boundary contracts explicit with the project's type/schema conventions. Dictionaries are useful for flexible metadata; critical records need discoverable fields and validation, not implicit assumptions spread among callers.
- Organize around responsibilities, ownership and reasons to change. Hide representation/algorithm details behind a useful interface while keeping important state transitions and failure outcomes visible. A collection of forwarding layers or getters is not evidence of effective modularity.
- Read the operation from a caller's perspective: what can be assumed, what changes, what can fail, and what may be retried? Keep validation and side effects in a comprehensible order. Separate pure calculations when doing so improves reasoning and testing; do not fragment an inseparable critical section to meet a line-count rule.
- Comments explain domain rules, invariants, non-obvious choices or constraints. Avoid narrating syntax, speculative TODOs and stale architecture claims. Document performance-motivated complexity and how to validate its benefit.
- Review dependency direction, shared mutation, error handling and concurrency. Ask whether a maintainer can locate the owner of a rule and identify the affected tests without traversing unrelated modules. Prefer consistent local idioms; keep broad formatting/refactoring out of an unrelated fix.

Readability review can use a concrete change scenario: if one rule changes, where is it represented and how many contracts must be understood? Explain known problems rather than declaring the code clean from its naming, file count or test count.

## Product and visual design

Understand the user's primary tasks, information priority and costly mistakes. Reuse the existing design system where suitable. For a new surface, establish a restrained visual language appropriate to the domain: hierarchy, spacing, typography, component behavior, units, numeric/date formatting and status semantics. A particular color palette or aesthetic is not universally correct.

Make important actions discoverable in the layouts where users need them. Distinguish submitting, pending, committed, failed, uncertain, stale and empty states; show feedback supported by authoritative state. Preserve useful form data and stable operation identity across uncertain responses when the operation requires it. Frontend disabling does not replace server-side correctness or authorization.

Use labels, focus order, keyboard operation, visible focus, suitable contrast, scalable text and status cues beyond color as relevant. Respect reduced-motion preferences when animation is involved. Verify applicable requirements instead of claiming blanket WCAG conformance from a visual check.

Use realistic long text, large/small numbers, empty/loading/error data and the affected screen widths. Check overflow, table scrolling, fixed actions, responsive hierarchy and useful failure recovery. Keep implementation details out of product language unless they help a user make a meaningful decision.

## Aesthetic and motion judgment

Aesthetics are plural. A trading terminal, a children's app, an editorial page and a developer tool ask for different things, and each minimal, ornate, playful or austere style is coherent under its own rules. Name the intent first (calm, precise, urgent, playful, trustworthy), then choose means that serve it, and judge a design by fit to purpose and internal consistency rather than fashion or the agent's own preference. Learn the owner's taste when it is visible; when it is not, choose a restrained default and say what was assumed. Distrust the generic look that appears everywhere by default; distinctiveness should express the product's identity, not novelty for its own sake.

Motion is information before it is decoration. Ask what it tells the user: that an action had an effect, where something went, that the system is working, what changed. If removing it loses nothing, remove it. Match its weight to frequency: an action repeated all day needs less than a rare moment. Let duration follow distance and importance, let elements that move together share an order the eye can follow, and keep one product's motion consistent, since consistency usually matters more than any single curve. Motion also spends attention, battery and frame time, so it must never block the task, and it must degrade for reduced-motion preferences and slow devices.

Taste is tested by use, not by a first glance. Watch the result at real speed, repeated many times, in the real context; a flourish that delights once and grates on the tenth viewing is a defect. Treat the agent's own sense of beauty as a hypothesis, keep options open for the owner's judgment, and record the intent so a later change can be checked against it.

## Evidence and completion

For an affected user journey, inspect actual display and exercise the important interaction in an appropriate environment when tools permit. A screenshot supports appearance at that state/viewport; interaction supports that journey; build and type checks support other claims. Mocks or isolated previews do not prove production integration. Record what was actually checked, remaining limitations and necessary documentation/design-token updates.
