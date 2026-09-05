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
        all_chunks = []
        for document in documents:
            chunks = chunk_document(document, chunk_size=50, chunk_overlap=20)
            all_chunks.extend(chunks)
            for i, chunk in enumerate(chunks, start=1):
                print(f"Chunk {i}:\n{chunk}\n")
        # Embed the chunks
        texts = [chunk["text"] for chunk in all_chunks]
        embeddings = self.embedder.embed_document(texts)

        # Store the embeddings in the vector store
        for chunk_id, (chunk,embedding) in enumerate(zip(all_chunks,embeddings),start=1):
            self.vector_store.add_chunk(chunk_id=chunk_id, vector=embedding, metadata=chunk)
        return len(all_chunks)