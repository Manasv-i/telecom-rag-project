from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.retrieve import search
from app.generate import generate_answer

app = FastAPI(title="Telecom RAG Assistant")

# Allow the frontend (served from the same origin, but kept open for now
# in case you host frontend/backend separately later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    query: str


@app.get("/api/health")
def health():
    return {"status": "ok", "message": "Telecom RAG Assistant Running"}


@app.post("/api/ask")
def ask_question(request: QueryRequest):

    query = request.query.strip()

    if not query:
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    results = search(query)

    documents = results.get("documents", [[]])[0]

    if not documents:
        return {
            "query": query,
            "answer": "I couldn't find anything relevant in the telecom knowledge base for that question.",
            "sources": []
        }

    context = "\n".join(documents)

    answer = generate_answer(context, query)

    sources = sorted(set(
        meta["source"]
        for meta in results["metadatas"][0]
    ))

    return {
        "query": query,
        "answer": answer,
        "sources": sources
    }


# Serve the frontend (static/index.html) at the root.
# Mounted last so it doesn't shadow the /api routes above.
app.mount("/", StaticFiles(directory="static", html=True), name="static")
