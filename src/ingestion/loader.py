#Decides which loader to use based on the file type
from pathlib import Path
from .document_extractor import (extract_text_from_docx, extract_text_from_pdf, extract_text_from_txt)

#file_path is expected to be a string dtype and function must return list data type (which has json ex: [{page :1 }, {page:2},{page:3}])
def load_document(file_path : str) -> list[dict]:
    path = Path(file_path)
    extension = path.suffix.lower()

    if extension ==".pdf":
        return extract_text_from_pdf(file_path)
    elif extension in [".docx", ".doc"]:
        return extract_text_from_docx(file_path)    
    elif extension in [".txt", ".md"]:
        return extract_text_from_txt(file_path) 
    raise ValueError(f"Unsupported file type: {extension}. Supported types are: .pdf, .docx, .doc, .txt, .md")
    