# Telecom RAG Assistant

## Overview

A Retrieval-Augmented Generation (RAG) system for telecom documents that enables semantic search and context-aware information retrieval using AI.

## Tech Stack

* Python
* FastAPI
* PyPDF
* LangChain
* Sentence Transformers
* Scikit-learn
* Git & GitHub

---

# Day 1: Backend & Document Processing

### Implemented

* FastAPI backend setup
* PDF upload API
* PDF text extraction using PyPDF
* API testing with Swagger UI

### Learned

* FastAPI fundamentals
* REST APIs
* File handling in backend systems

---

# Day 2: Document Chunking

### Implemented

* Text chunking using RecursiveCharacterTextSplitter
* Chunk size and overlap configuration
* Generated searchable chunks from telecom documents

### Learned

* Document preprocessing
* Chunking strategies for RAG systems

---

# Day 3: Semantic Retrieval

### Implemented

* Sentence embeddings using all-MiniLM-L6-v2
* Cosine similarity-based semantic search
* Retrieval of relevant document chunks for user queries

### Learned

* Embeddings
* Semantic search
* Retrieval component of RAG

---

# Day 4: Vector Database

### Implemented
* Integrated ChromaDB for vector storage
* Stored document chunks persistently
* Implemented semantic retrieval using ChromaDB
* Retrieved relevant chunks without reprocessing PDFs

### Learned
* Vector databases
* Persistent embedding storage
* Efficient semantic retrieval
* Difference between in-memory search and vector databases

  ---

# Day 5: Project Refactoring

### Implemented
* Modular project structure
* Separated ingestion and retrieval logic
* Organized experimental scripts
* Added `.gitignore`
* Added `requirements.txt`

### Project Structure

```text
telecom-rag-project/
│
├── app/
│   ├── ingest.py
│   └── retrieve.py
│
├── experiments/
│   ├── chroma_test.py
│   ├── embeddings_test.py
│   ├── pdf_chunking.py
│   ├── semantic_search.py
│   ├── similarity_test.py
│   └── test_chunking.py
│
├── requirements.txt
├── test_app.py
├── main.py
└── README.md
```

# Day 6 – Gemini Integration & Complete RAG Pipeline

### What I Learned

* Integrated Google Gemini API into the Telecom RAG Assistant.
* Connected retrieval and generation components to create a complete Retrieval-Augmented Generation (RAG) workflow.
* Learned prompt engineering using retrieved context.
* Understood how LLMs use retrieved documents to generate grounded responses.

### What I Built

* Created `generate.py` for Gemini-based answer generation.
* Connected ChromaDB retrieval with Gemini generation.
* Built an end-to-end pipeline:

  * Query → Retrieval → Context → Gemini → Answer
* Tested the pipeline using telecom-related questions.

### Results

Successfully generated answers from retrieved telecom documents instead of directly querying the LLM.

Example:
Question: "What telecom datasets are used?"

Answer:

* TeleQnA Dataset
* O-RAN Dataset
* Simu5G Data
* 3GPP Release 16 & 18 Docs

### Key Takeaway

Today I completed the core RAG architecture by combining document retrieval with LLM-based answer generation, creating a functional Telecom RAG Assistant prototype.

# Day 7 – Dockerization

### What I Learned
* Docker basics
* Dockerfile creation
* Containerizing FastAPI applications
* Environment variable handling in Docker
* Building and running Docker images

### What I Implemented
- Created a Dockerfile for the Telecom RAG Assistant
- Added `.dockerignore` to reduce image size
- Built Docker image using:

```bash
docker build -t telecom-rag .
```
### Outcome
* Successfully containerized the entire RAG application
* FastAPI server running inside Docker
* Gemini API accessible from container
* ChromaDB retrieval working inside container

---


# Day 8 – End-to-End RAG API Deployment

### What I Learned
- FastAPI endpoint integration
- Connecting Retrieval + Generation pipeline
- Handling Docker runtime issues
- Managing ChromaDB collections in containers

### What I Implemented

#### Query Endpoint
Created `/ask` endpoint:

```http
POST /ask
```

### Workflow:

User Query
→ ChromaDB Retrieval
→ Context Generation
→ Gemini API
→ Final Answer

### Outcome
* Complete end-to-end Telecom RAG pipeline operational
* Retrieval-Augmented Generation working successfully
* API tested through FastAPI Swagger UI
* Fully functional inside Docker container

# Day 9: Continuous Integration (CI) with GitHub Actions

### Objective
Automate project validation and Docker image building whenever new code is pushed to GitHub.

### What I Learned
- Basics of Continuous Integration (CI)
- GitHub Actions workflows
- Automating dependency installation
- Running validation checks in CI
- Automated Docker image building

## Tasks Completed

### Created GitHub Actions Workflow

Created:

.github/workflows/ci.yml

### Configured CI Pipeline

Workflow automatically triggers on:

- Push to main branch
- Pull requests to main branch

### Automated Steps

The pipeline performs:

1. Repository Checkout
2. Python Environment Setup
3. Dependency Installation
4. FastAPI Import Verification
5. ChromaDB Import Verification
6. Application Import Verification
7. Docker Image Build

### CI Validation

Successfully verified:

- FastAPI imports
- ChromaDB imports
- Application modules
- Docker image creation

### GitHub Actions Result

Pipeline completed successfully with all jobs passing.

## Outcome

Implemented a fully automated CI pipeline that validates the project and builds a Docker image on every code change.

## Technologies Used

- GitHub Actions
- Docker
- Python
- FastAPI
