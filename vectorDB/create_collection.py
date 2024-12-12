import os

from qdrant_client import models, QdrantClient
from connection import client

collection_name="chemistry"

client.create_collection(
    collection_name=collection_name,
    vectors_config=models.VectorParams(size=1024, distance=models.Distance.COSINE),
)