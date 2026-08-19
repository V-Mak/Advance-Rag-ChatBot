from src.vectorstore import load_vectorstore


def get_retriever(k=20, fetch_k=40, lambda_mult=0.5):

    vectorstore = load_vectorstore()

    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": k,
            "fetch_k": fetch_k,
            "lambda_mult": lambda_mult
        })
    return retriever


def retrieve_documents(query):

    retriever = get_retriever()

    documents = retriever.invoke(query)

    return documents