# Perception Gates and Perturbation Classification

**Explanation:** The perception foundation now tracks file drift and untracked raw files, but it does not yet classify perturbations into response actions or inspect gate staleness. Those higher-level responses still need a dedicated layer on top of the GitFacet/status runtime.

**Reference:** `src/wiki_compiler/perception.py`, `wiki/reference/cli/status.md`, `raw/autopoiesis_system.md`

**What to fix:** Add perturbation classification and gate-age/status reporting on top of the existing perception foundation.

**How to do it:**
1. Add response-classification rules for raw, source, and graph drift events.
2. Add `desk/Gates.md` staleness detection once the desk surface exists.
3. Extend tests and status output with those categories.

**Depends on:** `none`
