from app.loaders import load_docx
from app.loaders import load_pdf
from app.loaders import load_csv
from app.chunker import chunk_text


docx_text = load_docx("data/3gpp/TS23501.docx")
pdf_text = load_pdf("data/oran/architecture.pdf")
csv_text = load_csv("data/teleqna/teleqna.csv")


all_text = docx_text + "\n" + pdf_text + "\n" + csv_text


chunks = chunk_text(all_text)

print("Total Chunks:", len(chunks))

print("\nFirst Chunk:\n")
print(chunks[0])