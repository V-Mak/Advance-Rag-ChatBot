from src.retriever import get_retriever
from src.reranker import rerank_documents
from src.prompts import get_rag_prompt
from src.llm import get_llm
from src.hybrid_search import (create_bm25_retriever, hybrid_search)
from src.vectorstore import get_all_documents
from src.sources import get_sources
from src.memory import add_message, get_history


class AdvancedRAG:

    def __init__(self):

        self.retriever = get_retriever(k=20,fetch_k=40,lambda_mult=0.5)

        documents = get_all_documents()

        self.bm25 = create_bm25_retriever(documents)

        self.prompt = get_rag_prompt()

        self.llm = get_llm()


    def ask(self, question):

        # Get previous conversation
        history = get_history()

        # Search documents
        documents = hybrid_search(
            question,
            self.retriever,
            self.bm25
        )

        # Rerank documents
        results = rerank_documents(
            question,
            documents,
            top_k=5
        )

        # Make context
        context = ""

        for document, score in results:
            context += document.page_content
            context += "\n\n"

        # Create prompt
        prompt = self.prompt.invoke({
            "context": context,
            "question": question
        })

        # Generate answer
        answer = self.llm.invoke(prompt)

        # Get sources
        sources = get_sources(results)

        return {
            "answer": answer,
            "documents": results,
            "sources": sources
        }