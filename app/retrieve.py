import chromadb


def search(query):

    client = chromadb.PersistentClient(
        path="./chroma_db"
    )

    collection = client.get_collection(
        name="telecom_docs"
    )

    results = collection.query(
        query_texts=[query],
        n_results=2
    )

    return results