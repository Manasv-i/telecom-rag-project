import chromadb
from sentence_transformers import SentenceTransformer


model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


def search(query, source_type=None):

    client = chromadb.PersistentClient(
        path="./chroma_db"
    )

    collection = client.get_collection(
        name="telecom_knowledge"
    )

    query_embedding = model.encode(query)

    if source_type is None:

        results = collection.query(
            query_embeddings=[
                query_embedding.tolist()
            ],
            n_results=3
        )

    else:

        results = collection.query(
            query_embeddings=[
                query_embedding.tolist()
            ],
            n_results=3,
            where={
                "type": source_type
            }
        )

    return results