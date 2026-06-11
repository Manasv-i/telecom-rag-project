from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb

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

print("Chunks:", len(chunks))

# Chroma Client
client = chromadb.PersistentClient(
    path="./chroma_db"
)

# Delete old collection if it exists
try:
    client.delete_collection("telecom_docs")
except:
    pass

# Create fresh collection
collection = client.create_collection(
    name="telecom_docs"
)

# Add chunks
collection.add(
    documents=chunks,
    ids=[f"chunk_{i}" for i in range(len(chunks))]
)

print("Stored Successfully")