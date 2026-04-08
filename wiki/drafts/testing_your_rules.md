---
identity:
  node_id: "doc:wiki/drafts/testing_your_rules.md"
  node_type: "doc_standard"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/GUIDES/writing-rules.md", relation_type: "documents"}
---

Use the Item sandbox to test rules interactively before storing them in the database:

## Details

Use the Item sandbox to test rules interactively before storing them in the database:

```
http://localhost:8090/step-03-item/
```

Or write a unit test:

```javascript
import { Item } from '../../Item.js';

const item = await Item.fromDefinition({
  id: 'SALON_01',
  name: 'Salón Principal',
  pricingProfile: { tipo: 'porPersona', tarifa: 5000 },
  rules: [
    {
      ID_Regla: 'R_TEST',
      Nombre: 'Test overtime',
      Scope: 'ITEM',
      Tipo_Accion: 'WARNING',
      Condicion_JSON: { ">": [{ "var": "horaMin" }, 1260] },
      Payload_JSON: { message: 'Overtime applies' },
      Prioridad: 10,
      Activo: true,
    }
  ]
}).initialize();

item.setOverride('hora', '22:00');
const { ruleWarnings } = item.toDisplayObject();
console.log(ruleWarnings); // → [{ message: 'Overtime applies', ... }]
```

---

Generated from `raw/docs_cotizador/docs/GUIDES/writing-rules.md`.