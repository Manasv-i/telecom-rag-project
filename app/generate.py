import os
import logging

from google import genai
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

_api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=_api_key) if _api_key else None

# gemini-2.0-flash was shut down by Google on June 1, 2026.
# gemini-2.5-flash is the current recommended low-cost replacement.
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")


def generate_answer(context: str, query: str) -> str:

    if client is None:
        logger.error("GEMINI_API_KEY is not set; cannot call Gemini.")
        return (
            "Gemini API key is not configured on the server. "
            "Here is the most relevant retrieved context instead:\n\n"
            + context[:2000]
        )

    prompt = f"""You are a telecom domain assistant. Answer the question using ONLY the context below.
If the context does not contain the answer, say so clearly instead of guessing.

Context:
{context}

Question:
{query}

Answer:"""

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
        logger.info("Gemini (%s) responded successfully.", MODEL_NAME)
        return response.text

    except Exception as e:
        # Log the *real* error server-side so it's debuggable,
        # instead of silently swallowing it.
        logger.exception("Gemini generation failed: %s", e)
        return (
            "The answer generation service is temporarily unavailable. "
            "Here is the most relevant retrieved context instead:\n\n"
            + context[:2000]
        )
