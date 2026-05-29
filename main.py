from fastapi import FastAPI, UploadFile, File
from pypdf import PdfReader
import io

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Telecom RAG Assistant Running"
    }


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    pdf_bytes = await file.read()

    pdf_reader = PdfReader(io.BytesIO(pdf_bytes))

    text = ""

    for page in pdf_reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted

    return {
        "filename": file.filename,
        "pages": len(pdf_reader.pages),
        "characters": len(text),
        "preview": text[:500]
    }