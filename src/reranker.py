from sentence_transformers import CrossEncoder
from src.retriever import get_retriever


model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


def rerank_documents(question, documents, top_k=5):

    pairs = []

    for document in documents:
        pairs.append([
            question,
            document.page_content
        ])

    scores = model.predict(pairs)

    results = list(zip(documents, scores))

    results.sort(key=lambda x: x[1],reverse=True)

    return results[:top_k]


def retrieve_and_rerank(question):

    retriever = get_retriever(k=20, fetch_k=40, lambda_mult=0.5)

    documents = retriever.invoke(question)

    results = rerank_documents(question,documents)

    return results