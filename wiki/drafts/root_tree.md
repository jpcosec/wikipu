---
identity:
  node_id: "doc:wiki/drafts/root_tree.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/index/conceptual_tree.md", relation_type: "documents"}
---

```text

## Details

```text
PhD 2.0
├── README.md                        # repo entrypoint
├── docs/                            # current truth only
│   ├── index/                       # navigation only
│   ├── runtime/                     # current runnable backend/runtime behavior
│   ├── policy/                      # current enforceable policy/rules only
│   ├── reference/                   # stable current reference
│   ├── ui/                          # current UI/workbench/sandbox behavior
│   └── operations/                  # current operator playbooks
├── plan/                            # planning only
│   ├── adr/                         # architecture decisions
│   ├── runtime/                     # backend/runtime plans
│   ├── ui/                          # UI/workbench plans
│   ├── template/                    # plan templates and planning rules
│   └── archive/                     # archived plan snapshots worth keeping
└── code-local docs                  # heavy implementation docs near code
    ├── src/core/*/README.md
    ├── src/nodes/*/README.md
    └── apps/review-workbench/.../README.md
```

Generated from `raw/docs_postulador_langgraph/docs/index/conceptual_tree.md`.