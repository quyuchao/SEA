# Architecture review

Self-review using SEA's proportional design and evidence rules. Reviewed published core, portability rules, validator and README at 76b32dd. No new behavioral or installation success is claimed.

| Priority | Finding | Action / acceptance |
|---|---|---|
| P1 | No direct installation entry | Add skills CLI commands; actual fresh installation, update and removal still need isolated tests |
| P1 | Local checks do not protect subsequent changes | Add CI for structure, regressions and generated-edition freshness; configured CI is not a passing result |
| P1 | Structure is not behavior or loading evidence | Record OS, host/installer version, source SHA, installation scope, actual core delivery and task output separately |
| P2 | Loading architecture was not visible | Add matching diagrams to bilingual README |
| P2 | Broad core may consume unnecessary context | Measure context and omission rates before moving rules; preserve standalone usability |
| P2 | Host metadata checks only invocation strings | Add schema-aware malformed-field cases in a future increment |
| P2 | Behavior fixtures lack comparative protocol | Use fresh contexts, raw versioned inputs/outputs and explicit acceptance; add a baseline before claiming improvement |

Keep the existing core plus on-demand references. Keep trading guidance optional. Reuse the established installer rather than building a custom npm installer or an MCP service solely for Markdown. Keep generated SEA.md separate from authoritative sources.

References: [SEA core](../sea/SKILL.md), [portability](../sea/references/portability.md), [skills CLI](https://github.com/vercel-labs/skills), [REA README](https://github.com/morluto/rea). REA informed clear setup and invocation presentation; no artwork or implementation copied.
