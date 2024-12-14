from vectorDB.connection import vector_store
from template.chatTemplate import chatTemplate

def retrieve(query):
    retrieve_docs = vector_store.similarity_search(query)
    return retrieve_docs

def prompt(chat_history):
    query = chat_history[-1]["content"]
    docs_content = "\n\n".join(doc.page_content for doc in retrieve(query=query))

    prompt_content = chatTemplate(query=query, chat_history=chat_history, docs_content=docs_content)

    return prompt_content

