---
# ==========================================
# 🤖 BLOQUE DETERMINISTA (Machine-Readable)
# Mapea 1:1 con el modelo KnowledgeNode
# ==========================================
identity:
  node_id: "file:src/scraper/job_parser.py"
  node_type: "code_construct"

edges:
  - target_id: "file:src/scraper/models.py"
    relation_type: "depends_on"
  - target_id: "dir:data/raw/jobs"
    relation_type: "reads_from"
  - target_id: "dir:data/persistent/jobs"
    relation_type: "writes_to"
  - target_id: "doc:docs/standards/ingestion_layer.md"
    relation_type: "documents"
  - target_id: "file:src/wiki/concepts/job_posting.md"
    relation_type: "transcludes"

io_ports:
  - medium: "disk"
    path_template: "data/raw/jobs/{site_id}/*.html"
  - medium: "memory"
    schema_ref: "JobPosting"

compliance:
  status: "implemented"
  failing_standards: []
---

# 🧠 Job Parser (Scraper Module)

**Intent:** Este componente es el motor principal de extracción usando Crawl4AI.

## 🏗️ Modelo de Datos (Atómico)
El resultado de este parser es el siguiente contrato:
![[job_posting]] 

## 📜 Historial y Decisiones (ADRs)
Migramos de LiteLLM a Crawl4AI para mayor estabilidad en DOMs variables.
*Ver contexto en: `[[adr_004_crawl4ai_migration]]`*

## ⚠️ Fallbacks
Si el CSS falla, recurrimos al patrón:
![[concept_llm_rescue_pattern]]