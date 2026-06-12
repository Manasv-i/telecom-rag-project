import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="telecom_docs"
)

collection.add(
    documents=[
        "TeleQnA dataset is used",
        "Pizza recipe with cheese",
        "O-RAN dataset improves telecom analysis"
    ],
    ids=[
        "doc1",
        "doc2",
        "doc3"
    ]
)

results = collection.query(
    query_texts=[
        "Which telecom datasets are used?"
    ],
    n_results=2
)

print(results["documents"])