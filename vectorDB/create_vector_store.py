from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders.csv_loader import CSVLoader
from vectorDB.connection import vector_store
import tqdm
import os

data_dir = "VectorDB/datasets"

def create_vectors(directory):
    print("Creating vectors database:")
    datasets = os.listdir(directory)
    for dataset in tqdm.tqdm(datasets):
        path = os.path.join(data_dir,dataset)
        loader = CSVLoader(path, encoding="utf-8")
        docs = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        all_splits = text_splitter.split_documents(docs)

        # Index chunks
        vector_store.add_documents(documents=all_splits)

    print("Done")
    return vector_store


vector_db = create_vectors(data_dir)
