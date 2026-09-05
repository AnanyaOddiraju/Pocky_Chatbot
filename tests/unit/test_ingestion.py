from pathlib import Path
from src.pipeline.ingestion_pipeline import IngestionPipeline

def test_ingestion_pipeline():
    print("1. starting test")
    pipeline = IngestionPipeline()
    print("2. pipeline created")
    file_path = Path(r"E:\AI Engineer\Pocky\Pocky_Chatbot\tests\test_data\Facts.docx")
    print("Exists:", file_path.exists())
    print("Is file:", file_path.is_file())
    print("Path:", file_path)
    num_chunks = pipeline.ingest(file_path)
    print("3. ingestion completed")
    print(f"Number of chunks ingested: {num_chunks}")