from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatNVIDIA(
  model=os.getenv("MODEL_NAME"),
  api_key=os.getenv("LLM_API_KEY"),
  temperature=0.5,
  top_p=1,
  max_tokens=1024,
)