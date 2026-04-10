# Bootstrap + Upgrade Lifecycle

**Explanation:** The external LLM-wiki has a bootstrap script (`scripts/bootstrap_knowledge_system.py`) that generates 30 files in one command, plus an upgrade path (`scripts/upgrade.sh`) that updates scripts without touching wiki content. We have AGENTS.md and CLAUDE.md but no bootstrap script that scaffolds a new project from scratch, and no upgrade path for existing projects.

**Reference:** LLM-wiki `scripts/bootstrap_knowledge_system.py`, `scripts/upgrade.sh`, `docs/release-notes-v1.1.0.md`

**What to fix:** Implement bootstrap and upgrade:
1. Bootstrap: `wiki-compiler bootstrap --project <path> --name <name>` that creates the full directory structure (wiki/, manifests/, desk/ if needed)
2. Upgrade: `wiki-compiler upgrade` that pulls latest scripts without touching wiki content
3. Version markers in generated scripts for upgrade detection

**Depends on:** none

**Priority:** low — useful for onboarding new projects