---
identity:
  node_id: "doc:wiki/drafts/concrete_example.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/III-1-resolver/field_contracts.md", relation_type: "documents"}
---

`resolveItemDefinition('ITEM_CENA', db)` returns:

## Details

`resolveItemDefinition('ITEM_CENA', db)` returns:

```js
{
  ID_Item:                    'ITEM_CENA',
  Nombre:                     'Cena de Gala',
  Default_Glosa:              'Menú de tres tiempos',
  ID_Categoria:               'CAT_GASTRO',
  ID_Perfil_Precio_Override:  null,
  Def_Unidades_Por_Pax_Override: null,
  Activo:                     true,

  categoria: {
    ID_Categoria:             'CAT_GASTRO',
    Nombre:                   'Gastronomía',
    ID_Perfil_Precio_Default: 'PERF_PAX',
    Def_Requiere_Pax:         true,
    Def_Requiere_Cant:        false,
    Def_Requiere_Tiempo:      false,
    Def_Requiere_Hora:        false,
    Def_Duracion_Min:         0,
    Def_Unidades_Por_Pax:     1,
    Icono_UI:                 'utensils',
    Activo:                   true,
  },

  perfil: {
    ID_Perfil_Precio:         'PERF_PAX',
    Nombre:                   'Por Persona',
    Costo_Base_Fijo:          0,
    Costo_Unitario_Pax:       50000,
    Costo_Unitario_Tiempo:    0,
    Costo_Unitario_Item:      0,
    Activo:                   true,
  },

  reglas: [
    {
      ID_Regla:       'REGLA_MIN_PAX',
      Nombre:         'Mínimo 20 personas',
      Etapa:          'RESTRICCION_UI',
      Scope:          'ITEM',
      ID_Componente:  'ITEM_CENA',
      Tipo_Accion:    'ERROR',
      Hook:           null,
      Condicion_JSON: { '<': [{ 'var': 'item.pax' }, 20] },
      Payload_JSON:   { message: 'Se requieren al menos 20 personas' },
      Prioridad:      1,
      Acumulable:     false,
      Activo:         true,
    }
  ]
}
```

---

Generated from `raw/docs_cotizador/plan/legacy/III-1-resolver/field_contracts.md`.