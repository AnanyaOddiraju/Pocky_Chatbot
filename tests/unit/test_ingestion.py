from src.pipeline.ingestion_pipeline import IngestionPipeline

def test_ingestion_pipeline():
    pipeline = IngestionPipeline()
    file_path = "E:\\AI Engineer\\Pocky\\Pocky_Chatbot\\tests\\test_data\\sample_document.doc"  # Replace with the path to your test document
    num_chunks = pipeline.ingest(file_path) 
    print(f"Number of chunks ingested: {num_chunks}")