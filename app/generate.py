from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_answer(context, query):

    prompt = f"""
Context:
{context}

Question:
{query}

Answer based only on the context.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        print(f"Gemini Error: {e}")

        return (
            "Gemini API unavailable. Returning retrieved context.\n\n"
            + context[:2000]
        )