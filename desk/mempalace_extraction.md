# Multi-Paradigm Extraction: MemPalace & Graphify

This document distills the architectural methodologies from the MemPalace and Graphify repositories. 

## 1. How do they extract data?
**Multi-Modal Heuristics (No LLM required):**
*   **Graphify (Structural):** Uses deterministic AST parsing via `tree-sitter`. It loads language-specific configurations (for Python, JS, C++, etc.) to precisely identify classes, functions, properties, and boundaries without relying on error-prone regex.
*   **MemPalace (Semantic):** Uses a pure heuristic approach (`general_extractor.py`) to parse unstructured plain text. It searches for predefined keyword arrays to classify text into five memory types: `decision`, `preference`, `milestone`, `problem`, and `emotional`. It uses basic sentiment analysis (counting positive vs negative words) to disambiguate overlaps (e.g., distinguishing a "resolved problem" from an "active problem").

## 2. How do they extract relations?
**Deterministic vs. Temporal Triggers:**
*   **Graphify (Code-driven):** The AST walker explicitly hunts for relationship signatures based on language rules: `import` statements create `imports` edges; method invocations create `calls` edges; class inheritance creates `inherits` edges.
*   **MemPalace (Time-bound Explicit):** Uses a temporal Entity-Relationship graph (`knowledge_graph.py`) built on local SQLite. Relations are explicitly added as Triples (Subject → Predicate → Object) but with a critical feature: **Temporal Validity** (`valid_from`, `valid_to`). Facts can be "invalidated" by setting an end date, meaning the system knows *when* a relation was true, enabling queries like `as_of="2026-01-15"`.

## 3. How do they organize data?
**The "Palace" Architecture (Spatial Memory):**
Instead of flat vector indices, MemPalace organizes knowledge spatially to improve retrieval accuracy by 34%:
*   **Wings:** Major domains (e.g., a specific person or project).
*   **Rooms:** Specific topics within a wing (e.g., the "auth-migration" room inside the "Orion Project" wing).
*   **Halls:** Connective tissue between rooms in the same wing representing memory types (facts, events, advice).
*   **Tunnels:** Cross-wing connections linking identical rooms (e.g., the "auth" room in Project A connects to the "auth" room in Project B).
*   **Closets & Drawers:** Closets hold high-density summaries (pointers), while Drawers hold the raw, verbatim text (ChromaDB) so nothing is ever lost to LLM summarization drift.

## 4. How do they "compress"?
**The AAAK Dialect (Lossy Symbolic Abbreviation):**
MemPalace does not use standard compression algorithms; it uses a custom, lossy shorthand dialect called AAAK designed specifically for LLM context windows.
*   **Entity Coding:** Names are reduced to 3-letter codes (Alice = ALC).
*   **Emotion/Flag Coding:** Sentences are tagged with standardized shortcodes (`vul` = vulnerability, `joy` = joy) and structural flags (`ORIGIN`, `CORE`, `PIVOT`, `DECISION`).
*   **Structure:** `ZID:ENTITIES|topic_keywords|"key_quote"|WEIGHT|EMOTIONS|FLAGS`
*   **Purpose:** It packs repeated entities and relationships into drastically fewer tokens at scale, serving as a dense "Layer 1" wake-up context that any text-reading LLM can natively parse without needing a decoder script.
