from langchain_community.retrievers import BM25Retriever


def create_bm25_retriever(documents):

    retriever = BM25Retriever.from_documents(documents)

    retriever.k = 10

    return retriever


def hybrid_search(question,vector_retriever,bm25_retriever):

    vector_results = vector_retriever.invoke(question)

    keyword_results = bm25_retriever.invoke(question)

    results = vector_results + keyword_results

    unique_results = []

    for document in results:

        if document not in unique_results:
            unique_results.append(document)

    return unique_results