from qdrant_client import QdrantClient
from openai import OpenAI
from pydantic import BaseModel

class RAG(BaseModel):
    client: QdrantClient = QdrantClient(host="localhost", port=6333)
    openai: OpenAI = OpenAI(api_key="your_openai_key")

    def ingest(self, text: str):
        embedding = self.openai.embeddings.create(model="text-embedding-3", input=text).data[0].embedding
        self.client.upsert("knowledge", [embedding])

    def query(self, text: str) -> str:
        embedding = self.openai.embeddings.create(model="text-embedding-3", input=text).data[0].embedding
        results = self.client.search("knowledge", embedding, top=5)
        return " ".join([r.payload['text'] for r in results if r.payload])
