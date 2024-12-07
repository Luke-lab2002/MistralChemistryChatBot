from .rag import prompt
from models.llm import llm

def generation(chat_history):
    prompt_content = prompt(chat_history)
    result = llm.invoke(prompt_content)

    return result.content