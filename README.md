# RANovate AI

A domain-specific Retrieval-Augmented Generation (RAG) system for telecom knowledge, built to answer questions grounded in 3GPP specification documents — including notoriously tricky definitional queries like *"What is UPF?"*.

RANovate AI pairs an AI retrieval pipeline with a proper DevOps setup: containerized deployment, a curated dependency footprint, and a purpose-built glossary extractor that solves a real failure mode in generic chunking strategies.

---

## Why this exists

Generic fixed-size chunking works fine for prose but falls apart on structured, abbreviation-heavy telecom specs. Standard RAG pipelines routinely fail on simple definitional questions because the abbreviation table gets diluted across chunk boundaries. RANovate AI fixes this with a dedicated glossary extraction stage, alongside a clean, minimal, deployable stack.

---

## Features

- **Conversational Q&A over 3GPP specs** — ask telecom questions in plain English, get grounded answers with retrieved context
- **Domain-aware chunking** — a dedicated glossary extractor (`app/glossary.py`) pulls abbreviation-format entries out of raw spec text using regex and indexes them as standalone `type: "glossary"` chunks, dramatically improving retrieval for "What is X?" style queries
- **Gemini-powered generation** — uses `gemini-2.5-flash` for response generation
- **ChromaDB vector store** — persistent local vector index, baked into the Docker image at build time
- **Telecom NOC-console styled UI** — a chat-style frontend built from scratch to feel like an operator console
- **Lightweight, production-minded Docker setup** — CPU-only PyTorch, `python:3.13-slim` base, and a trimmed dependency list (~13 packages, down from a bloated ~140-package `pip freeze` dump)

---

## Architecture

```
┌─────────────────┐      ┌──────────────┐      ┌────────────────┐
│  Frontend (UI)   │ ───► │  FastAPI     │ ───► │  Gemini API     │
│  static/index.html│     │  main.py     │      │ (gemini-2.5-flash)│
└─────────────────┘      └──────┬───────┘      └────────────────┘
                                  │
                                  ▼
                          ┌──────────────┐
                          │  ChromaDB     │
                          │  (retrieve.py)│
                          └──────┬───────┘
                                  │
                          ┌──────▼───────┐
                          │  Ingestion    │
                          │  ingest.py    │
                          │  glossary.py  │
                          │  bulk_ingest.py│
                          └──────────────┘
```

**Retrieval flow:** query → embed → ChromaDB top-6 similarity search (glossary chunks + regular spec chunks) → context assembly → Gemini generation → response.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, FastAPI |
| Vector store | ChromaDB |
| LLM | Google Gemini API (`gemini-2.5-flash`) |
| Frontend | Static HTML/CSS (NOC-console aesthetic) |
| Containerization | Docker (`python:3.13-slim`, CPU-only PyTorch) |
| CI/CD | GitHub Actions *(in progress)* |
| Deployment | AWS EC2, free tier *(in progress)*, GHCR for image hosting |
| Data source | 3GPP specification documents |

---

## Project Structure

```
.
├── main.py                  # FastAPI app entrypoint, static file mount
├── app/
│   ├── generate.py          # Gemini API call + generation logic
│   ├── retrieve.py          # ChromaDB query/retrieval logic
│   └── glossary.py          # Regex-based abbreviation extractor for glossary chunks
├── experiments/
│   ├── ingest.py            # Core ingestion pipeline
│   └── bulk_ingest.py       # Bulk ingestion entrypoint (wires in glossary.py)
├── static/
│   └── index.html           # Chat-style frontend UI
├── Dockerfile
├── requirements.txt         # Curated, minimal dependency list
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.13+
- Docker (recommended for consistent builds)
- A Google Gemini API key

### Local setup

```bash
# Clone the repo
git clone https://github.com/Manasv-i/telecom-rag-project
cd ranovate-ai

# Install dependencies
pip install -r requirements.txt

# Set your Gemini API key
export GEMINI_API_KEY=your_key_here

# Ingest documents (builds the ChromaDB index, including glossary extraction)
python -m experiments.bulk_ingest

# Run the app
uvicorn main:app --reload
```

Visit `http://localhost:8000` to use the chat UI.

### Docker

```bash
docker build -t ranovate-ai .
docker run -p 8000:8000 -e GEMINI_API_KEY=your_key_here ranovate-ai
```

The ChromaDB index is baked into the image at build time, so the container is ready to serve queries immediately on startup — no cold-start ingestion delay.

---

## Roadmap

- [x] Fix ChromaDB collection name mismatch between ingest and retrieve
- [x] Migrate to `gemini-2.5-flash` with proper error logging
- [x] Trim requirements from ~140 to ~13 packages
- [x] Build glossary extraction module for definitional query support
- [x] Build chat-style NOC-console frontend
- [x] Slim, CPU-only Docker build
- [ ] AWS EC2 deployment with live URL
- [ ] GitHub Actions CI/CD pipeline
- [ ] Push images to GHCR
- [ ] Multi-agent orchestration (v2)
- [ ] Auth (v2)
- [ ] Prometheus/Grafana monitoring (v2)
- [ ] Advanced retrieval strategies (v2)

---

## Design Decisions

**Why a dedicated glossary extractor instead of smarter general-purpose chunking?**
3GPP specs pack abbreviation tables densely, and generic fixed-size or sentence-based chunking splits or dilutes them, so retrieval for "What is X?" queries returned poor or irrelevant context. A regex-based extractor pulls these entries out as standalone chunks tagged `type: "glossary"`, so they're retrieved cleanly and independently of surrounding spec prose.

**Why CPU-only PyTorch in Docker?**
GPU-enabled PyTorch builds pull in multi-gigabyte CUDA dependencies that aren't needed for this workload and would make the image needlessly large and slow to build/deploy on free-tier infrastructure.

**Why manually curate `requirements.txt` instead of using `pip freeze`?**
`pip freeze` output tends to be bloated and fragile, pinning transitive dependencies unnecessarily and complicating Docker builds. A minimal, manually maintained list keeps builds fast and reproducible.

---
