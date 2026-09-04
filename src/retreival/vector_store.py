from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

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
    def add_chunk(self, chunk_id: int, vector: list[float], metadata: dict):
        point = PointStruct(id=chunk_id, vector=vector, payload=metadata)
        self.client.upsert(collection_name=self.collection_name, points=[point])
    def search(self,query_embedding:list[float],limit: int =3):
        results = self.client.query_points(collection_name=self.collection_name, query=query_embedding, limit=limit, with_payload=True)
        return results.points
    