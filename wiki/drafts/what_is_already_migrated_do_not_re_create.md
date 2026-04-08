---
identity:
  node_id: "doc:wiki/drafts/what_is_already_migrated_do_not_re_create.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/I-1-database/objectives.md", relation_type: "documents"}
---

| Artifact | Status | Location |

## Details

| Artifact | Status | Location |
|---|---|---|
| `Config_Schema.js` (11-table schema) | ✅ Migrated | `packages/database/src/Config_Schema.js` |
| `IStore.js` + `ModelFactory.js` + `InMemoryStore.js` | ✅ Migrated | `packages/database/src/` |
| `createDatabase({ adapter, schema, seed })` | ✅ Migrated | `packages/database/src/createDatabase.js` |
| `seed.js` minimal fixture (SEED_DATA format) | ✅ Exists | `packages/database/src/seed.js` |
| `csvSeed.js` — Node.js CSV loader | ✅ Created | `packages/database/src/csvSeed.js` |
| Real production CSV data (188 items, 63 rules) | ✅ Migrated | `data/init/*.csv` |

Generated from `raw/docs_cotizador/plan/legacy/I-1-database/objectives.md`.