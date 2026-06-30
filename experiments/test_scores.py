from app.retrieve import search

results = search("What is AMF?")

documents = results["documents"][0]
metadatas = results["metadatas"][0]
distances = results["distances"][0]

for i in range(len(documents)):

    print("=" * 70)

    print(f"Rank      : {i + 1}")

    print(f"Distance  : {distances[i]:.6f}")

    print(f"Source    : {metadatas[i]['source']}")

    print(f"Type      : {metadatas[i]['type']}")

    print("\nPreview:\n")

    print(documents[i][:250])

    print()