from app.document_loader import load_all_documents
from app.chunker import chunk_text
from app.glossary import extract_glossary_entries, glossary_entries_to_chunks

import chromadb
from sentence_transformers import SentenceTransformer


print("Loading documents...")

documents = load_all_documents()

print(f"Loaded {len(documents)} documents.")


all_chunks = []
all_metadata = []


print("Chunking documents...")

for document in documents:

    chunks = chunk_text(document["text"])

    all_chunks.extend(chunks)

    for _ in chunks:

        all_metadata.append(
            {
                "source": document["source"],
                "type": document["type"]
            }
        )

    # Glossary/abbreviation entries (e.g. "UPF\tUser Plane Function") get
    # diluted when they're swept into generic 500-char chunks alongside
    # many unrelated entries. Pulling them out as standalone chunks makes
    # direct "What is X?" questions far more retrievable.
    glossary_entries = extract_glossary_entries(document["text"])
    glossary_chunks = glossary_entries_to_chunks(glossary_entries)

    all_chunks.extend(glossary_chunks)

    for _ in glossary_chunks:

        all_metadata.append(
            {
                "source": document["source"],
                "type": "glossary"
            }
        )

print(f"Total Chunks: {len(all_chunks)}")


print("Loading embedding model...")

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


print("Generating embeddings...")

embeddings = model.encode(
    all_chunks,
    show_progress_bar=True
)


print("Connecting to ChromaDB...")

client = chromadb.PersistentClient(
    path="chroma_db"
)


try:
    client.delete_collection(
        "telecom_knowledge"
    )
except:
    pass


collection = client.create_collection(
    name="telecom_knowledge"
)


print("Uploading to ChromaDB...")

batch_size = 500

for i in range(0, len(all_chunks), batch_size):

    batch_chunks = all_chunks[i:i + batch_size]

    batch_embeddings = embeddings[i:i + batch_size]

    batch_metadata = all_metadata[i:i + batch_size]

    collection.add(
        documents=batch_chunks,
        embeddings=batch_embeddings.tolist(),
        metadatas=batch_metadata,
        ids=[
            f"doc_{j}"
            for j in range(
                i,
                i + len(batch_chunks)
            )
        ]
    )

    print(
        f"Uploaded {i + len(batch_chunks)} / {len(all_chunks)} chunks"
    )


print("\nKnowledge Base Created Successfully!")