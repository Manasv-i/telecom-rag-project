from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

text = "TeleQnA Dataset"

embedding = model.encode(text)

print("Length:", len(embedding))

print("\nFirst 10 values:")

print(embedding[:10])