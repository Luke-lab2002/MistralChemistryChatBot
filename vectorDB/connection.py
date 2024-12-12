from qdrant_client import QdrantClient, models
from langchain_qdrant import QdrantVectorStore
from models.embedding import embeddings
from dotenv import load_dotenv
import os
load_dotenv()

client = QdrantClient(url=os.getenv("VECTORDB_URL"))

vector_store = QdrantVectorStore(
    client=client,
    collection_name="chemistry",
    embedding=embeddings,
)