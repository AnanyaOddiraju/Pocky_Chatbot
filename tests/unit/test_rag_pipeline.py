from src.pipeline.rag_pipeline import RAGPipeline

def test_rag_pipeline():
    pipeline = RAGPipeline()

    user_query = "Tell me about first domesticated animals"
    response = pipeline.ask(user_query)

    print("\nRAG Pipeline response:")
    print(response)

    assert response