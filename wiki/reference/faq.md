---
identity:
  node_id: "doc:wiki/reference/faq.md"
  node_type: "faq"
compliance:
  status: "implemented"
  failing_standards: []
---

This FAQ answers the recurring questions that agents and developers hit when they first work with Wikipu. Use it for quick clarification, then follow the `see_also` pointers to the canonical standards, concepts, or how-to pages.

**Q:** Why a knowledge graph instead of just a file tree?
**A:** A file tree encodes location but not meaning. The graph gives every node typed relationships, so both humans and agents can ask structural questions like what depends on a node or whether a proposed module duplicates existing intent before touching code. `see_also:` `wiki/concepts/how_wikipu_works.md`

**Q:** What is the difference between `wiki/` and `raw/`?
**A:** `raw/` is immutable seed material. `wiki/` is curated truth with frontmatter, typed edges, and compliance status, and it is the durable documentation surface that gets compiled into the graph. `see_also:` `wiki/standards/00_house_rules.md`

**Q:** Why was `00_INDEX_MOC.md` renamed to `Index.md`?
**A:** `Index.md` is a semantic entrypoint name, while `00_INDEX_MOC.md` depended on tool-specific jargon and sort-order hacks. Wikipu now uses `Index.md` for navigational entrypoints in `wiki/` domains and `Board.md` for operational entrypoints in work surfaces. `see_also:` `wiki/standards/00_house_rules.md`

**Q:** When should I commit?
**A:** Commit once per resolved atomic unit of work or one coherent structural change. A commit is a claim that the system is valid at that granularity, not a snapshot of half-finished edits. `see_also:` `wiki/standards/00_house_rules.md`

**Q:** How do I know whether a node is current truth or only planned?
**A:** Check `compliance.status`. `implemented` means the code and docs match current reality; `planned` or `scaffolding` means the node describes future or partial state. `see_also:` `wiki/reference/knowledge_node_facets.md`

**Q:** What should I do if a rule causes friction during a session?
**A:** Encode the friction rather than silently working around it. If a rule is wrong, unclear, or contradictory, update the canonical rule or add a durable decision record before the session closes. `see_also:` `wiki/standards/00_house_rules.md`
