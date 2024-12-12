from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders.csv_loader import CSVLoader
from vectorDB.connection import vector_store
from qdrant_client import models
import tqdm
import os
from connection import client

collection_name="chemistry"
data_dir = "./datasets"


def add_dataset(directory):
    print("add dataset:")
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

if __name__ == "__main__":

    vector_store = add_dataset(data_dir)