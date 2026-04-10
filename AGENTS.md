# AGENTS Guide (Wikipu Ecosystem)

You are operating within **Wikipu**, a Knowledge Graph-driven development ecosystem. 
Your primary directive is to preserve the integrity of the graph and follow the repository's invariant rules.

## 🛑 CRITICAL GUARDRAILS (Read First)
1. **The Hausordnung is Law:** All invariant rules (Identity, Methodology, Navigation, Operations, Code Style) are defined in the **Hausordnung**: `wiki/standards/house_rules.md`. You must adhere to them strictly.
2. **OP-6 (Clean Tree Before Editing):** ALWAYS run `git status` before starting a task. NEVER begin editing files, running refactors, or resolving an issue if the worktree has unstaged/untracked files. Stop and ask the user to commit, or commit the pending atomic unit yourself.
3. **OP-7 (Atomic Commits):** Resolve exactly one issue per commit. NEVER batch multiple distinct tasks into a single edit/commit cycle.
4. **NAV-1 (Graph as Router):** The graph is your primary navigation surface. Do not start with broad directory wandering. Use the `wiki-compiler query` and `context` commands to understand relationships.
5. **Autonomous Issue Execution:** NEVER ask the user to pick an issue. Follow `plan_docs/issues/Index.md` deterministically. Atomize, check contradictions, and execute step-by-step.

## Quick Facts
- **Python:** `>=3.10`
- **Main Code:** `src/wiki_compiler/`
- **Tests:** `tests/` (run via `python -m pytest -q`)
- **CLI:** `wiki-compiler`

## The 4-Zone Rule (ID-4)
| Zone | Purpose | Agents may write? |
|---|---|---|
| `wiki/` | Current truth (The Graph) | Yes (curated, must update `knowledge_graph.json`) |
| `raw/` | Immutable source ore | **NO** |
| `plan_docs/` | Active issues/proposals | Yes (ephemeral, delete when done) |
| `future_docs/` | Deferred backlog | Yes (low-churn) |

## Essential Commands

**State & Context**
- `wiki-compiler status` (Check for git drift/perturbations)
- `wiki-compiler query --type get_node --node-id <id>` (Graph lookup)
- `wiki-compiler context --nodes "<id>"` (Focused context)

**Verification & Build**
- `wiki-compiler build` (Rebuild `knowledge_graph.json` after wiki/code changes)
- `wiki-compiler audit` (Check graph compliance)
- `python -m pytest -q` (Run test suite)
- `wiki-compiler check-workflow` (Validate issue/branch/changelog discipline)

## Issue Workflow (OP-4)
1. Start at `plan_docs/issues/Index.md`.
2. When resolving: update/add tests → run tests → update `changelog.md` → delete issue file → remove from `Index.md`.
3. Run `wiki-compiler check-workflow` before committing.
4. Commit with a message naming the issue.

## Code Contracts
- **Pydantic is Mandatory:** All cross-module boundaries use Pydantic models from `src/wiki_compiler/contracts.py`. No untyped dicts. `Field(description=...)` is required.
