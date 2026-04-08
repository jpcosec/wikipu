---
identity:
  node_id: "doc:wiki/drafts/scalability_cliff.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/03_critique.md", relation_type: "documents"}
---

Ten mixins and five base classes is manageable. The architecture begins to strain at larger scales because:

## Details

Ten mixins and five base classes is manageable. The architecture begins to strain at larger scales because:

**Discovery cost increases.** A new developer must read every mixin's implementation to understand which fields it initializes, which fields it reads from siblings, and which order constraints exist. There is no manifest or index.

**Role taxonomy growth.** Each new component type either fits an existing base class or requires a new one. With fifteen or more concrete component types, the probability of a component that partially fits an existing role increases — and the temptation to add "just one more mixin" to an existing base class rather than create a new one leads to base classes with capabilities that most of their subclasses never use.

**Cross-cutting concerns cannot be mixins without broad changes.** Adding logging, instrumentation, or caching as a mixin requires modifying every base class definition where it is needed. There is no post-hoc injection point for cross-cutting behavior that applies uniformly to all components.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/03_critique.md`.