from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

class VectorStore:
    def __init__(self, collection_name: str = "documents"):
        self.client = QdrantClient(path="./qdrant_data")
        self.collection_name = collection_name
        self._create_collection()

    def _create_collection(self):
        if not self.client.collection_exists(self.collection_name):
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(size=384, distance=Distance.COSINE),
            )