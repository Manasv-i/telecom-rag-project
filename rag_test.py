from app.retrieve import search
from app.generate import generate_answer

query = "What telecom datasets are used?"

results = search(query)

chunks = results["documents"][0]

context = "\n".join(chunks)

answer = generate_answer(
    context,
    query
)

print("\nAnswer:\n")
print(answer)