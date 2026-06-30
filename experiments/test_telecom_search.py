import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_collection(
    "telecom_knowledge"
)

query = "What is the role of AMF in 5G?"

query_embedding = model.encode(query)

results = collection.query(
    query_embeddings=[query_embedding.tolist()],
    n_results=3
)

print("\nQUERY:")
print(query)

print("\nTOP RESULTS:\n")

for i, doc in enumerate(results["documents"][0], start=1):
    print(f"Result {i}")
    print(doc[:500])
    print("\n" + "-"*50 + "\n")