---
identity:
  node_id: "doc:wiki/drafts/machine_additions_extends_i_1.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/III-1-resolver/objectives.md", relation_type: "documents"}
---

Two new context fields on the existing browsing state:

## Details

Two new context fields on the existing browsing state:

```
resolverItemId   string | null   — item currently selected in resolver dropdown
resolvedItem     object | null   — output of resolveItemDefinition(resolverItemId)
```

One new transition:

| From | Event | Guard | To |
|------|-------|-------|----|
| browsing | SELECT_RESOLVER_ITEM | — | browsing (updates resolverItem context) |

Alpine connection:

```
Resolver dropdown  → actor.send({ type: 'SELECT_RESOLVER_ITEM', itemId })
Panel visible      ← resolvedItem !== null
```

Generated from `raw/docs_cotizador/plan/legacy/III-1-resolver/objectives.md`.