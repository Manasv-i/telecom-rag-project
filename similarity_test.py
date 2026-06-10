from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

text1 = "TeleQnA Dataset"
text2 = "TeleQnA Data Source"
text3 = "Pizza Recipe"

emb1 = model.encode(text1)
emb2 = model.encode(text2)
emb3 = model.encode(text3)

sim1 = cosine_similarity([emb1], [emb2])

sim2 = cosine_similarity([emb1], [emb3])

print(
    f"Dataset vs Knowledge: {sim1[0][0]:.4f}"
)

print(
    f"Dataset vs Pizza Recipe: {sim2[0][0]:.4f}"
)