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

## Evidence and completion

For an affected user journey, inspect actual display and exercise the important interaction in an appropriate environment when tools permit. A screenshot supports appearance at that state/viewport; interaction supports that journey; build and type checks support other claims. Mocks or isolated previews do not prove production integration. Record what was actually checked, remaining limitations and necessary documentation/design-token updates.
