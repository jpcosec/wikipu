---
# ==========================================
# 🤖 DETERMINISTIC BLOCK (Machine-Readable)
# Maps 1:1 with KnowledgeNode model
# ==========================================
identity:
  node_id: "file:src/scraper/job_parser.py"
  node_type: "code_construct"

edges:
  - target_id: "dir:data/raw/jobs"
    relation_type: "reads_from"
  - target_id: "dir:data/persistent/jobs"
    relation_type: "writes_to"
  - target_id: "file:src/wiki/concepts/job_posting.md"
    relation_type: "transcludes"

io_ports:
  - medium: "disk"
    path_template: "data/raw/jobs/{site_id}/*.html"
  - medium: "memory"
    schema_ref: "JobPosting"

compliance:
  status: "implemented"
---

# 🧠 Job Parser (Scraper Module)

**Intent:** This component is the primary extraction engine using Crawl4AI.

## 🏗️ Data Model (Atomic)
The result of this parser is the following contract:
![[job_posting]] 

## 📜 History and Decisions (ADRs)
Migrated from LiteLLM to Crawl4AI for better stability on variable DOMs.
*See context in: ![[adr_004_crawl4ai_migration]]*
