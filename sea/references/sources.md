# Official sources and adoption boundaries

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
