from src.embeddings.text_embedder import TextEmbedder
from src.retreival.vector_store import VectorStore
from src.generation.llm import LLM


class RAGPipeline:
    def __init__(self):
        self.embedder = TextEmbedder()
        self.vector_store = VectorStore()
        self.llm = LLM()

    def ask(self, question: str, limit: int = 3) -> str:

        # 1. Convert user's question into an embedding
        query_embedding = self.embedder.embed_text(question)

        # 2. Search Qdrant for relevant chunks
        results = self.vector_store.search(
            query_embedding=query_embedding,
            limit=limit
        )

        # 3. Extract text from retrieved chunks
        context = "\n\n".join(
            result.payload["text"]
            for result in results
        )

        # 4. Create prompt containing retrieved context
        prompt = f"""
You are Pocky, a helpful Multimodal RAG chatbot.

Answer the user's question using ONLY the information
provided in the context below.

If the answer cannot be found in the context, say:
"I don't have enough information in the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""

        # 5. Send context + question to Gemini
        response = self.llm.generate(prompt)

        return response