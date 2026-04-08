---
identity:
  node_id: "doc:wiki/drafts/output_shape_resolveditemdefinition.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/III-1-resolver/field_contracts.md", relation_type: "documents"}
---

```js

## Details

```js
{
  // ── From ITEM_CATALOGO ──────────────────────────────────────────
  ID_Item:                    string,        // PK — e.g. 'ITEM_CENA'
  Nombre:                     string,        // e.g. 'Cena de Gala'
  Default_Glosa:              string | null, // description / default comment
  ID_Categoria:               string,        // FK (informational — categoria is joined below)
  ID_Perfil_Precio_Override:  string | null, // FK (informational — perfil is resolved below)
  Def_Unidades_Por_Pax_Override: number | null, // null = inherit from categoria
  Activo:                     boolean,

  // ── From CATEGORIAS (full row, joined on ID_Categoria) ──────────
  categoria: {
    ID_Categoria:             string,
    Nombre:                   string,        // e.g. 'Gastronomía'
    ID_Perfil_Precio_Default: string,        // FK used for profile resolution
    Def_Requiere_Pax:         boolean,       // pricing uses pax (P)
    Def_Requiere_Cant:        boolean,       // pricing uses quantity (Q)
    Def_Requiere_Tiempo:      boolean,       // pricing uses time (T)
    Def_Requiere_Hora:        boolean,       // UI: show time-of-day selector
    Def_Duracion_Min:         number,        // default duration in minutes
    Def_Unidades_Por_Pax:     number,        // default units per pax (can be fractional)
    Icono_UI:                 string | null, // icon name for UI badge
    Activo:                   boolean,
  },

  // ── From PERFILES_PRECIO (resolved profile) ─────────────────────
  // Resolution order: item.ID_Perfil_Precio_Override ?? categoria.ID_Perfil_Precio_Default
  perfil: {
    ID_Perfil_Precio:         string,
    Nombre:                   string,        // e.g. 'Por Persona'
    Costo_Base_Fijo:          number,        // flat base fee (CLP)
    Costo_Unitario_Pax:       number,        // cost per person (CLP)
    Costo_Unitario_Tiempo:    number,        // cost per minute (CLP)
    Costo_Unitario_Item:      number,        // cost per unit/quantity (CLP)
    Activo:                   boolean,
  },

  // ── From REGLAS_NEGOCIO (filtered subset) ───────────────────────
  // Filter: Activo=true AND Scope='ITEM' AND Etapa='RESTRICCION_UI'
  //         AND (ID_Componente IS NULL OR ID_Componente = itemId)
  // Sorted: by Prioridad ASC
  reglas: [
    {
      ID_Regla:        string,
      Nombre:          string,
      Etapa:           'RESTRICCION_UI',
      Scope:           'ITEM',
      ID_Componente:   string | null,   // null = global; value = only this item
      Tipo_Accion:     'ERROR' | 'WARNING',  // only these two affect UI availability
      Hook:            string | null,
      Condicion_JSON:  object | null,   // JSON-Logic expression
      Payload_JSON:    object | null,   // { message: string, ... }
      Prioridad:       number,
      Acumulable:      boolean,
      Activo:          true,            // always true (filtered out otherwise)
    }
  ]
}
```

> `Updated_At` is intentionally stripped from all nested objects — it is metadata, not needed by components.

---

Generated from `raw/docs_cotizador/plan/legacy/III-1-resolver/field_contracts.md`.