# Official sources and adoption boundaries

## Selected recent agent research, checked 2026-10-27

This is a focused sample, not an exhaustive frontier survey or a ranking of companies. Read portions are stated below; a paper's reported gains are not SEA results. Several studies depend on model training, synthetic environments or specialized auditing tools that a Markdown skill does not provide. The rows support conditional reasoning and evaluation choices, not a fixed workflow.

| Research and version | Primary material actually checked | Implication for SEA and boundary |
|---|---|---|
| Google Research-led collaborators, Towards a Science of Scaling Agent Systems; first submitted 2025-12-09, v3 revised 2026-04-08 | https://arxiv.org/html/2512.08296v3 ; abstract, evaluation design and limitations; official 2026-01-28 explanation at https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/ | Coordination effectiveness depends on task structure and overhead. Choose complexity based on task evidence, not a default that more agents means better reasoning. Do not copy thresholds across workloads or assume permission to delegate. The January article describes an earlier experimental version; do not mix its counts with v3. |
| Anthropic, AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors; official article 2026-03-10 | https://alignment.anthropic.com/2026/auditbench/ ; benchmark, investigator, results and Tool-to-Agent Gap sections; linked paper https://arxiv.org/abs/2602.22755v3 | Distinguish evidence surfaced by a tool, evidence understood by an agent and a correct final diagnosis. Useful observations can still become wrong hypotheses. The study concerns intentionally implanted behaviors, not general software engineering or demonstrated SEA improvements. |
| Anthropic and UC Berkeley collaborators, Automated Researchers Can Reliably Mitigate Alignment Failures; released 2026-08-28 | Official article https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures ; linked paper https://www-cdn.anthropic.com/7b1c44894e980876479947dcdd40716278aeeffd/automated-alignment-researchers-august-2026.pdf , abstract, introduction and evaluation setup | Test improvements on withheld evaluations and preserve general capability; guard against optimizing the score rather than the intended outcome. The research uses post-training and controlled benchmarks. It does not establish that adding self-reflection instructions transfers its gains into SEA or makes an agent a reliable universal researcher. |
| Snowflake and UNC Chapel Hill, Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning; v1 2026-02-10 | https://arxiv.org/html/2602.10090v1 ; affiliations, abstract, introduction and section 6.2 Verification Design; author repository https://github.com/Snowflake-Labs/agent-world-model | Ground state claims in executable transitions and inspected state. Code-augmented evaluation helped in the studied synthetic training setting, while rigid checks could reject valid work when the environment was imperfect. Do not equate code execution with a correct domain oracle or require a world-model training system for ordinary tasks. |

Provenance note: a Microsoft Research catalogue page also links the Agent World Model paper, but the checked paper affiliations are Snowflake and UNC; catalogue hosting is not authorship. The same distinction applies to attributing engineering principles to a company. These observations strengthen SEA's existing evidence, proportionality and invariant lenses rather than adding an instruction for each paper.

## Judgment refinement and skill evaluation, checked 2026-10-27

The provenance, contextual meaning, invariant and evolution lenses in engineering-judgment.md are SEA's synthesis informed by user-reported failures. The reports motivated the change; they are not independently reproduced incidents or proof that these lenses improve an AI model. Their examples do not establish universal product semantics or a fixed sequence of actions.

[OpenAI, Testing Agent Skills Systematically with Evals](https://developers.openai.com/blog/eval-skills), especially the success-definition, captured-run and grader sections, supports evaluating actual actions and resulting artifacts with focused checks. [OpenAI, Build skills](https://developers.openai.com/plugins/build/skills), especially workflow boundaries and testing, supports concise instructions, conditional supporting material and representative/edge/non-trigger cases. These sources guide how to test the revision; no before/after model evaluation or improvement estimate is claimed from reading them. Existing sources and their original check dates below remain unchanged.

Research checked: 2026-10-25. Public material does not represent every internal team or establish a "most efficient" ranking. SEA's risk levels, package layout, and agent execution rules are a synthesis.

| Official source | URL | Adopted scope |
|---|---|---|
| Microsoft ISE Design Reviews | https://microsoft.github.io/code-with-engineering-playbook/design/design-reviews/ | Early review, alternatives, and decision records; no copied approval ceremonies |
| Microsoft Architectural principles | https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/architectural-principles | Separation, encapsulation, dependency inversion; no .NET/Azure requirement |
| Microsoft ISE Class Diagrams | https://microsoft.github.io/code-with-engineering-playbook/design/diagram-types/class-diagrams/ | Attributes, operations, visibility, relationships; no diagram for every change |
| Microsoft ISE Definition of Done | https://microsoft.github.io/code-with-engineering-playbook/agile-development/team-agreements/definition-of-done/ | Acceptance, checks, documentation; tailored to risk |
| Google Code Review | https://google.github.io/eng-practices/review/reviewer/looking-for.html | Design, behavior, complexity, tests, naming |
| Google Small CLs | https://google.github.io/eng-practices/review/developer/small-cls.html | Small complete increments, without fixed line limits |
| Apple WWDC19 Testing | https://developer.apple.com/videos/play/wwdc2019/413/ | Test levels and configurations; no XCTest requirement |
| Apple WWDC23 Test Reports | https://developer.apple.com/videos/play/wwdc2023/10175/ | Failure reports and UI evidence; no inference about all internal processes |
| Tencent CODING DevOps | https://cloud.tencent.com/product/coding | Requirement-to-delivery links; product capabilities are not company-wide policy |
| DORA Metrics | https://dora.dev/guides/dora-metrics/ | Contextual delivery, instability, and recovery; avoid metric gaming |
| Google SRE Embracing Risk | https://sre.google/sre-book/embracing-risk/ | Reliability investment by business risk; no arbitrary relaxation of data correctness |

Return to primary sources when updating. Recheck versions, support, capabilities, and installation paths when relevant. Old example versions are not current selection advice. Avoid extensive quotation or attributing SEA's synthesized rules as company originals.

## Local engineering-judgment extension: 2026-10-26

This user-requested extension adds explicit workload/algorithm selection, engineering judgment, readability and product-design guidance to the installed local SEA. It is a local adaptation, not an OpenAI official skill, a new verified upstream release, or an endorsement by the authors below. The previous sections retain their original research dates. Only the sources and portions listed here were checked for this addition; no claim is made to have read every cited book/course in full.

| Primary source or academic reproduction | Checked URL | Adopted idea and boundary |
|---|---|---|
| E. W. Dijkstra, Notes on Structured Programming, EWD249, author archive | https://www.cs.utexas.edu/~EWD/transcriptions/EWD02xx/EWD249/EWD249.html | Structured reasoning, refinement, scale and assumptions about correctness; not a demand for a formal proof of every edit. |
| D. L. Parnas, On the Criteria To Be Used in Decomposing Systems into Modules, academic transcription of the 1972 paper | https://www.cs.lafayette.edu/~gexia/cs301/resources/parnas.html | Responsibilities and information hiding around design decisions; the reproduction warns it is not guaranteed to match the original. The alternative UMD PDF was inaccessible during this check. |
| MIT OCW 6.006, Introduction to Algorithms, Spring 2020, course overview | https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/ | Explicit computation models, representations and performance analysis; practical choices still require the actual runtime and workload. The SEA selection table is an engineering synthesis, not a copied course specification. |
| John Ousterhout, Stanford CS190 Software Design Studio, Winter 2024, course overview | https://web.stanford.edu/~ouster/cs190-winter24/ | Complexity management, useful interfaces, information hiding, error handling, documentation and iterative review; no universal class/layer/line-count rule. |
| Leslie Lamport, Specifying Systems, author's book overview and contents | https://lamport.azurewebsites.net/tla/book.html | Explicit state/specification thinking; model checking is an optional risk-driven verification technique. The full book was not reviewed for this addition. |
| J. H. Saltzer, D. P. Reed and D. D. Clark, End-to-End Arguments in System Design, author-hosted paper | https://web.mit.edu/saltzer/www/publications/endtoend/endtoend.pdf | Place a guarantee where enough application context exists; lower-layer acknowledgements alone do not establish a committed business effect. SEA's transaction/idempotency rules are adaptations, not quotations. |
| Martin Fowler, Yagni | https://martinfowler.com/bliki/Yagni.html | Avoid speculative features while retaining maintainable, evolvable design; no excuse to omit a known correctness or recovery requirement. |
| Google Engineering Practices, What to look for in a code review | https://google.github.io/eng-practices/review/reviewer/looking-for.html | Review design, behavior, complexity, tests, names and actual UI impact; no claim that passing tests establishes readability. |
| W3C WAI, WCAG 2.2 Quick Reference | https://www.w3.org/WAI/WCAG22/quickref/ | Relevant labels, keyboard/focus, contrast, reflow and interaction criteria; a visual inspection is not WCAG conformance certification. |

The word "best" needs a context: goals, constraints, scale, failure costs and available evidence. SEA does not rank schools, authors or companies, force a named design methodology, or guarantee optimal output from an agent. Its added decision rules are original concise syntheses for this workflow, with assumptions and proportionality made explicit.

## Management and lifecycle additions

Checked against the public resources discussed on 2026-10-25. IEEE public descriptions and indexed topic outlines were available; direct full-guide retrieval was unavailable, so this is not a claim to have read the complete guide. Apply these references proportionately, not as mandatory organizational ceremonies.

| Official source | URL | Adopted scope |
|---|---|---|
| IEEE Computer Society SWEBOK public overview and topics | https://www.computer.org/education/bodies-of-knowledge/software-engineering/topics | Lifecycle knowledge map, configuration and engineering management; not a claim of full SWEBOK compliance |
| NASA Software Engineering Handbook - Configuration Management | https://swehb.nasa.gov/spaces/SWEHBVD/pages/133235384/A.08+Software+Configuration+Management | Controlled items, baselines, change impact, status accounting and audits; no automatic formal change board |
| Microsoft ISE Backlog Management | https://microsoft.github.io/code-with-engineering-playbook/agile-development/backlog-management/ | Acceptance, ready/done, design work and debt in planning |
| Microsoft ISE Component Versioning | https://microsoft.github.io/code-with-engineering-playbook/source-control/component-versioning/ | Component identities and compatibility; no required tool or independent version per file |
| GitHub flow | https://docs.github.com/en/get-started/using-github/github-flow | Branch-based collaboration as one option; follow existing repository policy |
| GitHub Projects | https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects | Optional issue/PR-linked planning, not a dependency of SEA |
| GitHub Releases | https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases | Tags, release notes and artifacts, distinct from runtime deployment |
| Semantic Versioning | https://semver.org/ | Public-contract-based version rules when adopted; respect initial-development/prerelease rules |
| NIST SSDF | https://csrc.nist.gov/Projects/ssdf | Security across the lifecycle, adapted to risk and context |
| SLSA Provenance | https://slsa.dev/spec/v1.2/provenance | Trace artifact origin to source/build, without claiming an attained assurance level |


## Goal-directed initiative: company practice, philosophy and psychology

Checked: 2026-10-26. This addition is a user-requested synthesis. The dates below are publication/text dates, not claims of frontier novelty. These public materials do not establish a company's current universal internal policy. Only the stated portions were reviewed; no exhaustive literature review, replication review, clinical assessment or independent empirical validation of these practices in AI agents was performed. Existing source dates above remain unchanged. The engineering adaptations appear in engineering-judgment.md; the recommendations must still be tested against the actual task.

| Source and original date | Material actually checked | Adopted scope and limitation |
|---|---|---|
| Amazon, Jeff Bezos, 2016 Letter to Shareholders (published 2017) | https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders ; customer outcomes, proxies and decision-making sections | Outcome over process proxies; reversibility and constructive dissent. Not a verified optimal management system or a rule to proceed with a fixed percentage of information. |
| Google, SRE Book, Chapter 15, Postmortem Culture (2016) | https://sre.google/sre-book/postmortem-culture/ ; philosophy, contributing causes, triggers and follow-up | System-level learning and preventive actions after significant failures. Not absence of responsibility, a formal report for every bug or proof that all Google teams follow identical practices. |
| Microsoft Research ExP, Patterns of Trustworthy Experimentation: During-Experiment Stage (2021-01-25) | https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-during-experiment-stage/ ; metric taxonomy, early checks, repeated testing and intervention | Measurement quality, outcome/diagnostic/guardrail distinctions and analysis discipline. No mandatory experiment length, significance threshold or automatic transfer from online product experiments to other domains. |
| Karl Marx, Theses on Feuerbach (1845), Cyril Smith's 2002 translation based on work with Don Cuckson | https://www.marxists.org/archive/marx/works/1845/theses/ ; short text, especially theses II and III and its translation/version note | Practice and self-correction as a limited engineering analogy. Archive-hosted primary-text translation, not a new empirical study, a software prescription, or a full account of Marx's philosophy; distinguish the original text from Engels' later edited version. |
| Charles G. Lord, Mark R. Lepper and Elizabeth Preston, Considering the Opposite (1984), Journal of Personality and Social Psychology 47(6), 1231-1243 | https://www.researchgate.net/profile/Mark-Lepper-2/publication/16669522_Considering_the_Opposite_A_Corrective_Strategy_for_Social_Judgment/links/56107d7508ae48337519fedb/Considering-the-Opposite-A-Corrective-Strategy-for-Social-Judgment.pdf ; author-profile-hosted original-paper copy, abstract and general discussion | Contrary explanations as a review aid. Two social-judgment experiments are not proof of universal debiasing or effects in language models; replication literature was not surveyed. |
| Daniel Kahneman and Gary Klein, Conditions for Intuitive Expertise: A Failure to Disagree (2009), American Psychologist 64(6), 515-526, DOI 10.1037/a0016755 | https://bear.warrington.ufl.edu/brenner/mar7588/Papers/kahneman-klein-2009.pdf ; university-hosted original-paper copy, abstract, conclusions and discussion of prospective failure review | Feedback/regularity conditions and limits of subjective confidence; optional failure anticipation for consequential decisions. Human expertise research is not an AI capability evaluation or a guarantee of improved engineering/business results. |
