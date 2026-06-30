import os

from app.loaders import (
    load_docx,
    load_pdf,
    load_csv
)


def load_all_documents():

    documents = []

    # -----------------------------
    # 3GPP Documents
    # -----------------------------
    folder = "data/3gpp"

    for filename in os.listdir(folder):

        if filename.endswith(".docx"):

            text = load_docx(
                os.path.join(folder, filename)
            )

            documents.append(
                {
                    "text": text,
                    "source": filename,
                    "type": "3gpp"
                }
            )

    # -----------------------------
    # O-RAN Documents
    # -----------------------------
    folder = "data/oran"

    for filename in os.listdir(folder):

        if filename.endswith(".pdf"):

            text = load_pdf(
                os.path.join(folder, filename)
            )

            documents.append(
                {
                    "text": text,
                    "source": filename,
                    "type": "oran"
                }
            )

    # -----------------------------
    # TeleQnA
    # -----------------------------
    folder = "data/teleqna"

    for filename in os.listdir(folder):

        if filename.endswith(".csv"):

            text = load_csv(
                os.path.join(folder, filename)
            )

            documents.append(
                {
                    "text": text,
                    "source": filename,
                    "type": "teleqna"
                }
            )

    return documents