from app.retrieve import search

results = search(
    "What is AMF?"
)

print("\nDOCUMENTS:\n")

for doc in results["documents"][0]:
    print(doc[:300])
    print("\n" + "-"*50)

print("\nMETADATA:\n")

for meta in results["metadatas"][0]:
    print(meta)