---
identity:
  node_id: "doc:wiki/system/gemma-rag.md"
  node_type: "concept"
edges:
  - {target_id: "doc:wiki/selfDocs/looting_protocol.md", relation_type: "implements"}
compliance:
  status: "implemented"
  failing_standards: []
---

# Gemma-RAG - Looted RAG System

Gemma-RAG is a looted copy of the `rag-with-gemma3` project - a modular Retrieval-Augmented Generation system built with Google DeepMind's Gemma 3 served locally via Ollama.

## Origin

- **Source:** https://github.com/jpcosec/rag-with-gemma3
- **Forked from:** https://github.com/Bbs1412/rag-with-gemma3
- **Location:** `src/looting/gemma-rag/`
- **License:** GPL-3.0

## Purpose

This RAG system provides:
- Document ingestion (PDF, TXT, Markdown)
- Vector embeddings using `mxbai-embed-large`
- FAISS-based vector storage
- Local LLM inference via Ollama (Gemma-3)
- User authentication with SQLite-3
- FastAPI backend + Streamlit UI

Relevant to autopoietic identity for:
- Knowledge base querying
- Document processing pipelines
- Local LLM integration patterns

## Architecture

```
gemma-rag/
├── app.py              # Streamlit frontend
├── server/
│   ├── server.py      # FastAPI backend
│   └── llm_system/   # LangChain LLM orchestration
├── docker/            # Docker configurations
└── requirements.txt  # Python dependencies
```

## Running

### Development

```bash
cd src/looting/gemma-rag
pip install -r requirements.txt
# Start FastAPI
cd server && uvicorn server:app --reload --port 8000
# Start Streamlit (separate terminal)
streamlit run app.py
```

### Docker

```bash
docker build -t gemma-rag:dev --build-arg ENV_TYPE=dev .
docker run -p 8000:8000 -p 8501:8501 gemma-rag:dev
```

## Non-Tracked Assets

The following are NOT part of the topology:
- `node_modules/` - npm dependencies
- `user_data/` - user uploaded documents
- `user_faiss/` - vector store indices
- `storage/` - persistent storage

## Verification

- [ ] Dependencies install without errors
- [ ] FastAPI server starts
- [ ] Streamlit UI loads
- [ ] Ollama connection works (dev mode)

## Related

- `[[looting_protocol]]` - The looting protocol this project follows