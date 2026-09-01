from src.chunking.text_chunker import chunk_text, chunk_document

text = """This is a sample text that will be chunked into smaller pieces. The purpose of this test is to ensure that the chunking function works correctly and handles various edge cases, such as empty strings, strings with only whitespace, and strings that are shorter than the specified chunk size."""
source = "test_source"
def test_chunk_text():
    txt_text = text
    document = {
        "text": text, 
        "source": source+".docx",
        "page": None,
    }

    #chunks = chunk_text(text, chunk_size=50, chunk_overlap=10)
    chunks = chunk_document(document, chunk_size=50, chunk_overlap=10)
    for i, chunk in enumerate(chunks, start=1):
        print(f"Chunk {i}:\n{chunk}\n")
    #assert isinstance(chunks, str)
    assert len(chunks) > 0
    #assert all(isinstance(c, str) and c.strip() for c in chunks)

    #combined = " ".join(c.strip() for c in chunks)
    #assert "sample text" in combined
