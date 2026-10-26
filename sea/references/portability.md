# Cross-AI use

The core is plain Markdown for assistants able to read instructions. Discovery mechanisms, context limits, and permissions vary. Do not promise automatic installation or identical behavior across platforms.

## Loading and evaluation preflight

Before attributing an output to SEA, confirm that the assistant actually received the core, either through a successful file read or by providing the core inline. Record the delivery method and the evaluated content version in the test harness. An assistant's ordinary answer after a failed read is not SEA behavior evidence.

When file access is unavailable, stop repeating the same failing reads and use the documented inline mode if appropriate. Otherwise mark the evaluation blocked. Keep structural checks, behavioral observations, host integration, and comparative improvement claims separate. A blocked load is an environment result, not evidence that the engineering rules passed or failed.

Without a skill loader, provide SKILL.md or ask the assistant to read it, then state the task:

> Read SEA's SKILL.md and apply its risk-based workflow to this software task. Inspect the current implementation, perform requirements and technology/design work as needed, then implement and report actual verification. Do not change application code for planning-only requests.

The standalone core contains the complete workflow. Do not pretend to read absent references. For full use, preserve the sea directory and relative paths.

With a loader, consult the target platform's current official installation instructions and use its permitted location. Codex, Claude, and IDE assistants may need different adapters; do not assume shared discovery directories. The optional agents/openai.yaml supplies host-specific display metadata. Referencing SEA must not override existing project instructions or authorization.

| Capability limit | Adaptation |
|---|---|
| Chat only | Provide designs/suggestions and pending checks; do not claim edits or execution |
| Read/write only | Edit authorized files and mark execution as unperformed |
| Command execution | Use actual project build/tests and report results |
| No network | Mark changing facts unverified; prefer confirmed local versions |
| No renderer | Provide diagram source/tables without claiming visual checks |
| No independent reviewer | Perform self-review without inventing reviewers |

Scripts are optional structural aids, not semantic review. The core does not require a particular shell, OS, connector, or cloud. Communicate in the user's preferred language even though skill instructions are English.
