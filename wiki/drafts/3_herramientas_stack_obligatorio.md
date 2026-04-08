---
identity:
  node_id: "doc:wiki/drafts/3_herramientas_stack_obligatorio.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/proposals/migration_agent_prompt.md", relation_type: "documents"}
---

Estás OBLIGADO a usar el siguiente stack. NO inventes soluciones custom si la librería ya lo resuelve:

## Details

Estás OBLIGADO a usar el siguiente stack. NO inventes soluciones custom si la librería ya lo resuelve:

- Estilos: Tailwind CSS (utility classes ÚNICAMENTE). Usa utils/cn.ts para mezclar clases.
- Componentes base: átomos de src/components/atoms/ (Button, Badge, Tag, Spinner, Kbd).
- Data fetching: @tanstack/react-query. Prohibido useEffect + fetch manual para datos del servidor.
- Layouts divisibles: react-resizable-panels (si el spec pide SplitPane).
- Librerías específicas para esta vista: [INSERTAR LIBRERÍAS, ej. @uiw/react-codemirror, @xyflow/react].

Referencia de lógica legacy (NO de UI):
Puedes leer [INSERTAR RUTA LEGACY] ÚNICAMENTE para entender el shape del JSON de entrada/salida.
IGNORA sus estilos y su HTML.

Generated from `raw/docs_postulador_ui/plan/01_ui/proposals/migration_agent_prompt.md`.