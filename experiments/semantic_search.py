from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Read PDF
reader = PdfReader("RANovate AI.pdf")

text = ""

for page in reader.pages:
    extracted = page.extract_text()

    if extracted:
        text += extracted

# Chunking
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_text(text)

print("Total Chunks:", len(chunks))

# Embedding Model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# Embed Chunks
chunk_embeddings = model.encode(chunks)

# User Question
query = "What datasets are used?"

query_embedding = model.encode(query)

# Similarity Search
scores = cosine_similarity(
    [query_embedding],
    chunk_embeddings
)[0]

# Best Chunk
best_index = scores.argmax()

print("\nBest Chunk Index:", best_index)

print("\nSimilarity Score:", scores[best_index])

print("\nMost Relevant Chunk:\n")

print(chunks[best_index])