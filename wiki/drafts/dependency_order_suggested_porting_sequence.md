---
identity:
  node_id: "doc:wiki/drafts/dependency_order_suggested_porting_sequence.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/looting/README.md", relation_type: "documents"}
---

```

## Details

```
10 (shadcn install)  ← do this first, no deps

01 (stores + sync discipline from 17)
  ├─ 02 (floating edges)
  ├─ 03 (edge inheritance)  →  05 (GroupShell)  →  16 (recursive collapse)
  ├─ 08 (layout hook)
  └─ 11 (DomainGraph contract)  →  15 (InternalNodeRouter + L3 registry)

07 (type registry)  →  06 (NodeShell + zoom tiers + 12 FallbackNode inline)
                    └─  09 (Inspector Sheet)
                    └─  14 (GraphEditor shell)

04 (keyboard)       →  mounts inside 14
13 (focus layout)   →  after stores + layout stable
18 (smart handles)  →  after L3 registry + NodeShell stable
19 (ghost drag)     →  last, only if performance is an actual problem
```

Generated from `raw/docs_postulador_ui/plan/looting/README.md`.