from pypdf import PdfReader
from docx import Document
import pandas as pd


def load_pdf(file_path):

    pdf = PdfReader(file_path)

    text = ""

    for page in pdf.pages:
        text += page.extract_text()

    return text


def load_docx(file_path):

    doc = Document(file_path)

    text = "\n".join(
        para.text
        for para in doc.paragraphs
    )

    return text


def load_csv(file_path):

    df = pd.read_csv(file_path)

    rows = []

    for _, row in df.iterrows():

        rows.append(
            " | ".join(
                str(value)
                for value in row.values
            )
        )

    return "\n".join(rows)