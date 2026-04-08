---
identity:
  node_id: "doc:wiki/drafts/component_structure.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/component-architecture.md", relation_type: "documents"}
---

```

## Details

```
packages/components/<component-name>/
├── <Component>.js               ← Main component class
├── machine/
│   └── <component>Machine.js   ← XState machine definition
├── logic/
│   └── create<Component>Component.js  ← Factory & mounting logic
├── domain/
│   ├── index.js                ← Export pure functions
│   ├── calculations.js         ← Domain-specific calculations
│   ├── formatting.js           ← Display string generation
│   └── rulesEngine/            ← Rule evaluation (if applicable)
├── ui/
│   └── <Component>.html        ← HTML template with Alpine bindings
└── tests/
    ├── <Component>.test.js     ← Unit + integration tests
    └── README.md               ← Test documentation
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/component-architecture.md`.