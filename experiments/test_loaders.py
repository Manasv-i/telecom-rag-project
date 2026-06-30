from app.loaders import load_docx
from app.loaders import load_pdf
from app.loaders import load_csv

print("DOCX")
print(
    load_docx("data/3gpp/TS23501.docx")[:500]
)

print("\nPDF")
print(
    load_pdf("data/oran/architecture.pdf")[:500]
)

print("\nCSV")
print(
    load_csv("data/teleqna/teleqna.csv")[:500]
)