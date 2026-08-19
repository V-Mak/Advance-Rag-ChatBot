import streamlit as st

from src.rag import AdvancedRAG
from src.memory import get_history, clear_history


st.set_page_config(
    page_title="Advanced RAG",
    page_icon="📚",
    layout="wide"
)


@st.cache_resource
def load_rag():

    return AdvancedRAG()


rag = load_rag()


st.title("📚 Advanced RAG Chatbot")


if st.button("Clear Conversation"):

    clear_history()

    st.rerun()


question = st.chat_input("Ask a question...")


for message in get_history():

    with st.chat_message("user"):
        st.write(message["question"])

    with st.chat_message("assistant"):
        st.write(message["answer"])


if question:

    with st.chat_message("user"):

        st.write(question)

    with st.chat_message("assistant"):

        with st.spinner("Searching and generating answer..."):

            result = rag.ask(question)

        st.write(result["answer"])

        st.subheader("Sources")

        for source in result["sources"]:

            st.write(
                f"Page: {source['page']} | "
                f"Score: {source['score']:.4f}"
            )