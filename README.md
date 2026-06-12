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

## Day 1: Backend & Document Processing

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

## Day 2: Document Chunking

### Implemented

* Text chunking using RecursiveCharacterTextSplitter
* Chunk size and overlap configuration
* Generated searchable chunks from telecom documents

### Learned

* Document preprocessing
* Chunking strategies for RAG systems

---

## Day 3: Semantic Retrieval

### Implemented

* Sentence embeddings using all-MiniLM-L6-v2
* Cosine similarity-based semantic search
* Retrieval of relevant document chunks for user queries

### Learned

* Embeddings
* Semantic search
* Retrieval component of RAG

---

## Day 4: Vector Database

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

## Day 5: Project Refactoring

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
