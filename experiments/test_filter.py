from app.retrieve import search


print("=" * 50)
print("WITHOUT FILTER")
print("=" * 50)

results = search("Near RT RIC")

for i, meta in enumerate(results["metadatas"][0], start=1):
    print(f"\nResult {i}")
    print(meta)


print("\n" + "=" * 50)
print("ONLY O-RAN")
print("=" * 50)

results = search(
    "Near RT RIC",
    source_type="oran"
)

for i, meta in enumerate(results["metadatas"][0], start=1):
    print(f"\nResult {i}")
    print(meta)