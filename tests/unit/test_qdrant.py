from src.embeddings.text_embedder import TextEmbedder
from src.retreival.vector_store import VectorStore

def add_chunk_to_vector_store():
    embedder = TextEmbedder()
    store = VectorStore()

    chunk = {
        "text": "This is a sample chunk of text.",
        "source": "test.txt",
    "page": None,
    }
    embedding = embedder.embed_text(chunk["text"])
    store.add_chunk(chunk_id=1, vector=embedding, metadata=chunk)
    print("Chunk added to vector store with ID 1 ")

    result = store.client.retrieve(collection_name="documents", ids=[1]) 
    print(result)

def test_search_vector_store():
    embedder = TextEmbedder()
    store = VectorStore()

    user_query = "What's the example sentence?"
    query_embedding = embedder.embed_text(user_query)
    result_text= store.search(query_embedding=query_embedding, limit=3)
    for result in result_text:
        print("Id:", result.id)
        print("Score:", result.score)
        print("Retrieved chunk:", result.payload["text"])
        print()


