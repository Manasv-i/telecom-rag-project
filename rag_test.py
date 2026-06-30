from app.retrieve import search

query = "What is AMF?"

results = search(query)

print(results["documents"][0][0][:1000])