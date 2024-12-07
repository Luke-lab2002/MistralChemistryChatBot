from qdrant_client import QdrantClient, models
from langchain_qdrant import QdrantVectorStore
from models.embedding import embeddings
from dotenv import load_dotenv
import os
load_dotenv()

client = QdrantClient(url=os.getenv("VECTORDB_URL"))

collection_name="chemistry"

client.create_collection(
    collection_name=collection_name,
    vectors_config=models.VectorParams(size=1024, distance=models.Distance.COSINE),
)

vector_store = QdrantVectorStore(
    client=client,
    collection_name=collection_name,
    embedding=embeddings,
)