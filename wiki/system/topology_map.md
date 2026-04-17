---
identity:
  node_id: "doc:wiki/system/topology_map.md"
  node_type: "system"
edges:
  - {target_id: "doc:wiki/selfDocs/WhereAmI.md", relation_type: "documents"}
  - {target_id: "doc:wiki/selfDocs/WhatAmI.md", relation_type: "documents"}
compliance:
  status: "implemented"
  failing_standards: []
---

# Wikipu Topology Map

```mermaid
flowchart TB
    subgraph "raw/ ✱ Inviolable"
        R["📥 Seed<br/>Raw content"]
    end
    
    subgraph "exclusion/ ✱ Inviolable"
        E["🚫 Hidden<br/>.git, .*, configs"]
    end
    
    subgraph "wiki/ ★ Knowledge"
        W["📚 Curated<br/>Current truths"]
    end
    
    subgraph "desk/ ⚡ Operations"
        D["⚡ Active<br/>In-progress"]
    end
    
    subgraph "drawers/ ⏳ Deferred"
        DR["⏳ Queued<br/>Future potential"]
    end
    
    subgraph "src/ ⚙ Motor"
        S["⚙ CLI<br/>Tools"]
    end
    
    R --> W
    W --> D
    D --> DR
    D --> S
    S -.->|executes| R
    E -.->|bounds| R
    E -.->|bounds| W
    E -.->|bounds| D
    E -.->|bounds| DR
    E -.->|bounds| S

    style R fill:#f9f,stroke:#333,stroke-width:2px
    style E fill:#fcc,stroke:#333,stroke-width:2px
    style W fill:#9f9,stroke:#333,stroke-width:2px
    style D fill:#ff9,stroke:#333,stroke-width:2px
    style DR fill:#9ff,stroke:#333,stroke-width:2px
    style S fill:#cff,stroke:#333,stroke-width:2px
```

## Zone Relationships

| Zone | Role | Boundary | Flow |
|------|------|----------|------|
| `raw/` | Seed ore | ✱ inviolable | Read → `wiki` |
| `exclusion/` | Hidden | ✱ inviolable | Bounds all |
| `wiki/` | Current truth | Modifiable | → `desk` |
| `desk/` | In-progress | Modifiable | → `drawers` |
| `drawers/` | Future potential | Modifiable | → `desk` |
| `src/` | Motor organs | Modifiable | Executes → `raw` |

## Key Invariants

1. **raw/ is read-only** — never modify raw content
2. **exclusion/ is invisible** — .git, .*, configs never enter wiki
3. **desk/ is active surface** — current work lives here
4. **Every edit → immediate commit** — prevents energy debt

## Related

- [[wiki/selfDocs/WhereAmI.md]]
- [[wiki/selfDocs/WhatAmI.md]]
- [[wiki/selfDocs/HowAmI.md]]