from langchain_community.vectorstores import FAISS
import os
from src.loader import load_pdf
from src.splitter import split_documents
from src.embeddings import get_embedding_model


VECTORSTORE_PATH = "vectorstore"


def create_vectorstore():

    documents = load_pdf("data/Python for Probability, Statistics, and Machine Learning.pdf")

    chunks = split_documents(documents)

    embeddings = get_embedding_model()

    vectorstore = FAISS.from_documents(documents=chunks, embedding=embeddings)

    vectorstore.save_local(VECTORSTORE_PATH)


def load_vectorstore():

    if not os.path.exists(VECTORSTORE_PATH):
        print(f"{VECTORSTORE_PATH}' folder not fount. Creating it now from raw documents....")
        create_vectorstore()

    embeddings = get_embedding_model()

    vectorstore = FAISS.load_local(
        VECTORSTORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vectorstore


def get_all_documents():

    documents = load_pdf("data/Python for Probability, Statistics, and Machine Learning.pdf")

    chunks = split_documents(documents)

    return chunks