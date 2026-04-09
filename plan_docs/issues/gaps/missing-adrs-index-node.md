# Missing wiki/adrs/Index.md

**Explanation:** The graph references `doc:wiki/adrs/Index.md` but the file does not exist on disk. Every wiki domain is required by NAV-4 to have exactly one canonical `Index.md` entry point. Its absence means the ADR domain has no navigational node, and any tool that reads graph-referenced paths (e.g. `validate-wiki`, `context`) will fail or silently degrade when it encounters this node.

**Reference:** `wiki/adrs/` (contains `001_feature_methodology_superseded.md`, `002_documentation_consolidation.md`), `wiki/standards/00_house_rules.md` (NAV-4), `knowledge_graph.json`

**What to fix:** Create `wiki/adrs/Index.md` as a proper `index` node that lists the two existing ADR files and their relationships.

**How to do it:**
1. Create `wiki/adrs/Index.md` using the `index` node template from `wiki/standards/artifacts/`.
2. Add frontmatter edges pointing to `doc:wiki/adrs/001_feature_methodology_superseded.md` and `doc:wiki/adrs/002_documentation_consolidation.md`.
3. Run `wiki-compiler build` and `wiki-compiler validate-wiki --path wiki/adrs/Index.md` to confirm the node is valid.
4. No new tests needed — this is a docs-only structural change.

**Depends on:** `none`
