import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    name="telecom_docs"
)

results = collection.query(
    query_texts=[
        "What datasets are used?"
    ],
    n_results=2
)

print("\nRetrieved Chunks:\n")

for doc in results["documents"][0]:
    print("-" * 50)
    print(doc)