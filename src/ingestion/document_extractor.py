from pathlib import Path
from docx import Document
from pypdf import PdfReader

def extract_text_from_txt(file_path: str) -> list[dict]:
    path = Path(file_path)
    text = path.read_text(encoding='utf-8')
    return [{"text": text, "page": None, "source": path.name}]

def extract_text_from_pdf(file_path: str) -> list[dict]:
    path = Path(file_path)
    reader = PdfReader(file_path)
    documents = []
    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""

        if text.strip():  # Only add non-empty pages
            documents.append({"text": text, "page": page_number, "source": path.name})
    return documents

def extract_text_from_docx(file_path: str) -> list[dict]:
    path = Path(file_path)
    doc = Document(file_path)
    text = "\n".join(paragraph.text for paragraph in doc.paragraphs if paragraph.text.strip())
    return [{"text": text, "page": None, "source": path.name}]