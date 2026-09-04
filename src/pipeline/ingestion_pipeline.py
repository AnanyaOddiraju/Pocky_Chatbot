from src.ingestion.loader import load_document
from src.chunking.text_chunker import chunk_document
from src.embeddings.text_embedder import TextEmbedder
from src.retreival.vector_store import VectorStore

class IngestionPipeline:
    def __init__(self):
        self.embedder = TextEmbedder()
        self.vector_store = VectorStore()

    def ingest(self, file_path: str):
        # Load the document
        documents = load_document(file_path)

        # Chunk the document
        chunks=[]
        document_text= chunk_document(documents)
        for document in documents:
            chunks.extend(document_text)

        # Embed the chunks
        texts = [chunk["text"] for chunk in chunks]
        embeddings = self.embedder.embed_document(texts)

        # Store the embeddings in the vector store
        for chunk_id, (chunk,embedding) in enumerate(zip(chunks,embeddings),start=1):
            self.vector_store.add_chunk(chunk_id=chunk_id, vector=embedding, metadata=chunk)
        return len(chunks)