import chromadb

client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_collection(
    "telecom_knowledge"
)

results = collection.get(
    limit=5
)

print("\nDOCUMENT:\n")
print(results["documents"][0][:300])

print("\nMETADATA:\n")
print(results["metadatas"][0])