from app.document_loader import load_all_documents

documents = load_all_documents()

print(f"\nTotal Documents Loaded: {len(documents)}\n")

for i, doc in enumerate(documents, start=1):

    print("=" * 60)
    print(f"Document {i}")
    print("=" * 60)

    print("Source :", doc["source"])
    print("Type   :", doc["type"])
    print("Length :", len(doc["text"]))

    print("\nPreview:\n")
    print(doc["text"][:300])

    print("\n")