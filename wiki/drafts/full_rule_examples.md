---
identity:
  node_id: "doc:wiki/drafts/full_rule_examples.md"
  node_type: "doc_standard"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/GUIDES/writing-rules.md", relation_type: "documents"}
---

### Block oversized groups

## Details

### Block oversized groups

```javascript
{
  ID_Regla:       'R_SALON_MAX_PAX',
  Nombre:         'Salón: aforo máximo',
  Scope:          'ITEM',
  Tipo_Accion:    'ERROR',
  Condicion_JSON: { ">": [{ "var": "pax" }, 320] },
  Payload_JSON:   { message: 'Capacidad máxima del salón: 320 personas' },
  Prioridad:      10,
  Activo:         true,
}
```

### Warn about after-hours events

```javascript
{
  ID_Regla:       'R_OVERTIME_WARNING',
  Nombre:         'Evento fuera de horario estándar',
  Scope:          'ITEM',
  Tipo_Accion:    'WARNING',
  Condicion_JSON: { ">": [{ "var": "horaMin" }, 1260] },
  Payload_JSON:   { message: 'El evento comienza después de las 21:00. Se aplica cargo por extensión.' },
  Prioridad:      20,
  Activo:         true,
}
```

### Block events that end past midnight

```javascript
{
  ID_Regla:       'R_NO_PAST_MIDNIGHT',
  Nombre:         'No se puede continuar después de medianoche',
  Scope:          'ITEM',
  Tipo_Accion:    'ERROR',
  Condicion_JSON: { ">": [{ "var": "horaFinMin" }, 1440] },
  Payload_JSON:   { message: 'El ítem excede la medianoche. Ajusta la hora o la duración.' },
  Prioridad:      15,
  Activo:         true,
}
```

### Warn about very short durations

```javascript
{
  ID_Regla:       'R_MIN_DURATION',
  Nombre:         'Duración mínima recomendada',
  Scope:          'ITEM',
  Tipo_Accion:    'WARNING',
  Condicion_JSON: { "and": [
    { ">": [{ "var": "duracionMin" }, 0] },
    { "<": [{ "var": "duracionMin" }, 30] }
  ] },
  Payload_JSON:   { message: 'La duración mínima recomendada es 30 minutos.' },
  Prioridad:      25,
  Activo:         true,
}
```

---

Generated from `raw/docs_cotizador/docs/GUIDES/writing-rules.md`.