FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Install CPU-only torch first (sentence-transformers needs it).
# This avoids pulling the much larger CUDA build, which we don't need
# since this runs on a CPU-only EC2 instance.
COPY requirements.txt .
RUN pip install --extra-index-url https://download.pytorch.org/whl/cpu torch==2.12.0 \
    && pip install -r requirements.txt

# Copy application code and the curated telecom dataset.
COPY app/ ./app/
COPY static/ ./static/
COPY data/ ./data/
COPY experiments/bulk_ingest.py ./experiments/bulk_ingest.py
COPY main.py .

# Build the ChromaDB vector index INTO the image at build time, so the
# container starts up ready-to-query with no manual ingestion step on
# the server. (This is the same data your bulk_ingest.py uses locally.)
RUN python -m experiments.bulk_ingest

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
