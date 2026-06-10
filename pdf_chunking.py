from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Read PDF
reader = PdfReader("RANovate AI.pdf")

text = ""

for page in reader.pages:
    extracted = page.extract_text()

    if extracted:
        text += extracted


print("\nTotal Characters:", len(text))


# Chunking
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_text(text)

print("\nTotal Chunks:", len(chunks))


for i, chunk in enumerate(chunks[:3]):
    print(f"\n========== CHUNK {i+1} ==========")
    print(chunk)