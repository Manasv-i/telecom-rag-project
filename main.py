from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import shutil

from app.retrieve import search
from app.generate import generate_answer

app = FastAPI()


class QueryRequest(BaseModel):
    query: str


@app.get("/")
def home():
    return {
        "message": "Telecom RAG Assistant Running"
    }


@app.post("/ask")
def ask_question(request: QueryRequest):

    results = search(request.query)

    context = "\n".join(
        results["documents"][0]
    )

    answer = generate_answer(
        context,
        request.query
    )

    sources = list(
        set(
            meta["source"]
            for meta in results["metadatas"][0]
        )
    )

    return {
        "query": request.query,
        "answer": answer,
        "sources": sources
    }


@app.post("/upload")
def upload_pdf(file: UploadFile = File(...)):

    file_path = file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    from app.ingest import ingest_pdf

    ingest_pdf(file_path)

    return {
        "message": f"{file.filename} uploaded and indexed successfully"
    }