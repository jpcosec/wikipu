# Context Router Contract

**Explanation:** `wiki-compiler context` already exists, but its interface and output shape are still implicit. The next steps need a stable request/response contract before adding ranking, checklist attachment, or issue intersection.

**Reference:** `src/wiki_compiler/main.py`, `src/wiki_compiler/context.py`, `wiki/reference/context.md`, `wiki/how_to/use_the_cli.md`

**What to fix:** Define and document the context-router CLI contract and bundle schema.

**How to do it:**
1. Decide the stable input flags and output fields.
2. Clarify backward compatibility for existing `context` usage.
3. Add contract-focused tests and doc updates.

**Depends on:** `none`
