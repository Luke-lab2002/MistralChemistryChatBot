from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name=os.getenv("EMBEDDING_MODEL_NAME"),
    model_kwargs={"trust_remote_code": True}
)
