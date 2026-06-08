import fitz


def extract_text(pdf_file):

    # Always reset to beginning
    pdf_file.seek(0)

    pdf_bytes = pdf_file.read()

    if not pdf_bytes:
        return ""

    pdf = fitz.open(
        stream=pdf_bytes,
        filetype="pdf"
    )

    text = ""

    for page in pdf:
        page_text = page.get_text()

        if page_text:
            text += page_text + "\n"

    pdf.close()

    return text.strip()