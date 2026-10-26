# Git and hosted collaboration

Apply the repository's existing workflow. Git work is local source control; a hosting service adds collaboration. Neither tool is required for chat-only design work.

## Inspect before changing history

- Resolve the actual repository root, current branch, worktree, staged/unstaged/untracked changes, upstream, and intended remote when relevant. Do not infer the target repository from a parent directory or from a repository name alone.
- Preserve user changes and distinguish task changes from unrelated edits. Avoid broad staging commands unless every included file has been reviewed and belongs to the intended change.
- Reuse a suitable task branch or choose one under the project's convention when necessary. Do not require a branch per file or force Git Flow, trunk-based development, or another model onto every project.
- Inspect remote state before integrating or publishing where needed. Choose merge/rebase according to project policy; preserve both sides' intent when resolving conflicts and rerun affected checks. Do not overwrite remote work or rewrite shared history as a routine fix.

## Build reviewable commits

Inspect the complete staged diff, including generated files, dependency locks, migrations, documentation, and accidental secrets or local artifacts. Keep each commit coherent; avoid unrelated formatting or cleanup. Commit messages explain the concrete change and follow existing conventions; use Conventional Commits only if adopted.

Tie checks to the content being delivered. If relevant files change after verification, run the affected checks again. Report unexecuted checks honestly. Commit only within task scope and existing authorization; do not claim a commit exists until the command succeeds and its identity is known.

## Push and review

When authorized, push the intended branch to the verified remote and check the result. A successful local commit does not prove remote synchronization. Existing authorization to push should be honored without repeated confirmation; creating a public repository, changing visibility, merging, or deploying are separate actions unless already authorized.

Use the host's PR/MR and review workflow where applicable. Describe the problem, final behavior, important trade-offs, verification, and relevant issue links. Honor required checks and protection rules. Identify self-review as self-review; do not invent approvals or bypass failed checks.

Update issue/PR state only when supported by actual evidence. Merge, release, and deployment are distinct states. Handle rejected pushes, conflicts, unavailable authentication, or missing tools explicitly without exposing credentials or falsely claiming synchronization. Avoid force-push, reset, clean, or stash operations that could discard user work without a justified, authorized plan.

Keep adapters optional: GitHub, GitLab, other hosts, APIs, and local CLIs may differ. Verify current capabilities and permissions before relying on host-specific automation. A skill is not a credential or a permission grant.
