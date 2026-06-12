from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb


def ingest_pdf(pdf_path):

    # Read PDF
    reader = PdfReader(pdf_path)

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

    # ChromaDB
    client = chromadb.PersistentClient(
        path="./chroma_db"
    )

    # Delete old collection if exists
    try:
        client.delete_collection("telecom_docs")
    except:
        pass

    # Create fresh collection
    collection = client.create_collection(
        name="telecom_docs"
    )

    # Store chunks
    collection.add(
        documents=chunks,
        ids=[f"chunk_{i}" for i in range(len(chunks))]
    )

    print("Stored Successfully")