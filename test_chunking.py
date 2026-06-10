from langchain_text_splitters import RecursiveCharacterTextSplitter

sample_text = """
Telecom Radio Access Networks are rapidly evolving.

The system provides:
- Conversational Telecom Q&A
- Root Cause Analysis
- Anomaly Detection
- Network Optimization

RAG combines retrieval with language models.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=10
)

chunks = splitter.split_text(sample_text)

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print(chunk)