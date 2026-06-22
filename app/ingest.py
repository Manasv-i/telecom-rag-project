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

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    print("Chunks:", len(chunks))

    client = chromadb.PersistentClient(
        path="./chroma_db"
    )

    try:
        client.delete_collection("telecom_docs")
    except:
        pass

    collection = client.create_collection(
        name="telecom_docs"
    )

    collection.add(
        documents=chunks,
        ids=[f"chunk_{i}" for i in range(len(chunks))]
    )

    print("Stored Successfully")


# OUTSIDE THE FUNCTION
if __name__ == "__main__":
    ingest_pdf("RANovate AI.pdf")