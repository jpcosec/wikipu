---
identity:
  node_id: "doc:wiki/drafts/step_2_create_folder_structure.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/GUIDES/creating-a-component.md", relation_type: "documents"}
---

```bash

## Details

```bash
cd packages/components

mkdir my-component
cd my-component

mkdir machine logic ui domain tests
touch README.md MyComponent.js

cd machine && touch myMachine.js && cd ..
cd logic && touch createMyComponent.js && cd ..
cd ui && touch MyComponent.html && cd ..
cd domain && touch index.js && cd ..
cd tests && touch README.md MyComponent.test.js && cd ..
```

Result:
```
packages/components/my-component/
├── README.md
├── MyComponent.js
├── machine/myMachine.js
├── logic/createMyComponent.js
├── ui/MyComponent.html
├── domain/index.js
└── tests/
    ├── README.md
    └── MyComponent.test.js
```

---

Generated from `raw/docs_cotizador/docs/GUIDES/creating-a-component.md`.