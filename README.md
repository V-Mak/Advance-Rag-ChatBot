# Advanced RAG Chatbot

An end-to-end Advanced Retrieval-Augmented Generation (RAG) chatbot built with Python, LangChain, Hugging Face, FAISS, BM25, Cross-Encoder Reranking, and Streamlit.

This chatbot allows users to ask questions about a PDF document and generates answers using information retrieved from the document. It also supports hybrid retrieval, reranking, source information, and conversational memory.

---

## Features

- PDF document loading
- Text splitting and chunking
- Sentence Transformer embeddings
- FAISS vector database
- Semantic search
- BM25 keyword search
- Hybrid search
- MMR-based retrieval
- Cross-Encoder reranking
- Hugging Face LLM
- Conversational memory
- Source/page information
- Streamlit chatbot interface
- Environment variable support using `.env`

---

## Architecture

    PDF Document
          |
          v
    Document Loader
          |
          v
    Text Splitter
          |
          v
    Embeddings
          |
          v
    FAISS Vector Database
          |
          +----------------------+
          |                      |
          v                      v
    FAISS Search            BM25 Search
    Semantic Search         Keyword Search
          |                      |
          +----------+-----------+
                     |
                     v
               Hybrid Search
                     |
                     v
               MMR Retrieval
                     |
                     v
           Cross-Encoder Reranker
                     |
                     v
            Top Relevant Chunks
                     |
                     v
                RAG Prompt
                     |
                     v
             Hugging Face LLM
                     |
                     v
             Answer + Sources
                     |
                     v
           Conversation Memory
                     |
                     v
                Streamlit UI

---

## Project Structure

    RAG-ChatBot-advance/
    │
    ├── data/
    │   └── document.pdf
    │
    ├── src/
    │   ├── embeddings.py
    │   ├── hybrid_search.py
    │   ├── llm.py
    │   ├── loader.py
    │   ├── memory.py
    │   ├── prompts.py
    │   ├── rag.py
    │   ├── reranker.py
    │   ├── retriever.py
    │   ├── sources.py
    │   ├── splitter.py
    │   └── vectorstore.py
    │
    ├── vectorstore/
    │   ├── index.faiss
    │   └── index.pkl
    │
    ├── .env
    ├── .gitignore
    ├── app.py
    ├── requirements.txt
    └── README.md

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| LangChain | RAG application framework |
| Hugging Face Transformers | Language model |
| Sentence Transformers | Embeddings and reranking |
| FAISS | Vector similarity search |
| BM25 | Keyword-based retrieval |
| PyPDF | PDF document loading |
| PyTorch | Deep learning framework |
| Streamlit | Web application |
| python-dotenv | Environment variable management |

---

## How It Works

### 1. Document Loading

The PDF document is loaded and converted into text documents.

The document loader extracts the content from the PDF so that it can be processed by the RAG pipeline.

### 2. Text Splitting

The extracted document is divided into smaller chunks.

Chunking makes it possible to retrieve only the relevant parts of the document instead of sending the complete document to the language model.

### 3. Embeddings

Each text chunk is converted into a numerical vector using a Sentence Transformer embedding model.

These vectors represent the semantic meaning of the text.

### 4. FAISS Vector Store

The generated embeddings are stored in a FAISS vector database.

FAISS is used to perform efficient similarity search between the user's question and the document chunks.

### 5. Semantic Search

When a user asks a question, the question is converted into an embedding.

FAISS compares the question embedding with the stored document embeddings and retrieves semantically similar chunks.

### 6. BM25 Keyword Search

The system also uses BM25 for keyword-based retrieval.

BM25 is useful when exact words, phrases, or technical terms are important.

### 7. Hybrid Search

The system combines FAISS semantic search and BM25 keyword search.

    FAISS Semantic Search
             +
       BM25 Keyword Search
             |
             v
        Hybrid Search

This provides the advantages of both semantic and keyword-based retrieval.

### 8. MMR Retrieval

Maximal Marginal Relevance (MMR) is used to retrieve relevant documents while reducing redundancy.

Instead of retrieving several chunks containing nearly identical information, MMR tries to select chunks that are both relevant and diverse.

### 9. Cross-Encoder Reranking

The retrieved documents are passed through a Cross-Encoder reranker.

The reranker evaluates the relationship between the user's question and each retrieved document.

    Question + Document
            |
            v
      Cross-Encoder
            |
            v
      Relevance Score
            |
            v
      Ranked Documents

The highest-ranked documents are selected as the final context.

### 10. Context Creation

The top-ranked document chunks are combined into a context.

The context is then provided to the language model along with the user's question.

### 11. RAG Prompt

The RAG prompt contains:

- Conversation history
- Retrieved document context
- Current user question

The language model uses these components to generate the answer.

### 12. Hugging Face LLM

The final prompt is passed to a Hugging Face language model.

The model generates an answer using the retrieved information instead of relying only on its pretrained knowledge.

### 13. Conversational Memory

The chatbot stores previous questions and answers during the current application session.

For example:

    User:
    What is BERT?

    Assistant:
    BERT is a Transformer-based encoder model.

    User:
    What is it used for?

    Assistant:
    It is used for tasks such as text classification,
    question answering, and named entity recognition.

The conversation history allows the chatbot to handle follow-up questions more naturally.

### 14. Source Information

The chatbot also displays information about the retrieved sources.

For example:

    Page: 25
    Score: 0.8234

    Page: 31
    Score: 0.7912

This provides information about which parts of the document were retrieved for the answer.

---

## Retrieval Pipeline

The retrieval process is:

    User Question
          |
          v
    +-------------+
    | FAISS Search|
    +-------------+
          |
          +
          |
          v
    +-------------+
    | BM25 Search |
    +-------------+
          |
          v
    Hybrid Results
          |
          v
    MMR Retrieval
          |
          v
    Cross-Encoder
       Reranking
          |
          v
    Top Relevant Chunks

---

## Generation Pipeline

    User Question
          +
    Retrieved Context
          +
    Conversation History
          |
          v
       RAG Prompt
          |
          v
    Hugging Face LLM
          |
          v
      Final Answer

---

## Installation

### 1. Clone the Repository

    git clone https://github.com/V-Mak/RAG-ChatBot-advance.git

### 2. Create a Virtual Environment

    python -m venv venv

### 3. Activate the Virtual Environment

For Windows PowerShell:

    .\venv\Scripts\Activate.ps1

For Windows Command Prompt:

    venv\Scripts\activate

### 4. Install Dependencies

    pip install -r requirements.txt

---

## Hugging Face Configuration

Create a `.env` file in the project root directory.

Add:

    HF_TOKEN=your_huggingface_token

Replace `your_huggingface_token` with your Hugging Face access token.

The token is used by the application to access the configured Hugging Face model.

---

## Add a PDF Document

Place your PDF document inside the `data` directory.

Example:

    data/
    └── document.pdf

If the PDF has a different filename, update the PDF path in the document-loading code.

---

## Create the Vector Store

Before running the chatbot, the PDF needs to be processed.

The process is:

    PDF Document
          |
          v
    Load Document
          |
          v
    Split Text
          |
          v
    Generate Embeddings
          |
          v
    Create FAISS Index
          |
          v
    Save Vector Store

The generated vector store files are stored inside:

    vectorstore/
    ├── index.faiss
    └── index.pkl

---

## Run the Application

Activate the virtual environment:

    .\venv\Scripts\Activate.ps1

Then run:

    streamlit run app.py

The Streamlit application will open in your browser.

---

## Example Conversation

    User:
    What is probability?

    Assistant:
    Probability is a mathematical framework used to measure
    the likelihood of an event occurring.

    User:
    What are its applications?

    Assistant:
    Probability is widely used in statistics, machine learning,
    risk analysis, decision-making, and many other fields.

    User:
    Can you give me an example?

    Assistant:
    A simple example is the probability of getting heads
    when flipping a fair coin.

---

## Why Hybrid Search?

FAISS and BM25 solve different retrieval problems.

### FAISS

FAISS is useful for semantic similarity.

It can retrieve documents that have similar meaning even when the exact words are different.

### BM25

BM25 is useful for keyword-based retrieval.

It is especially useful when exact technical terms or specific words are important.

### Hybrid Search

Combining both approaches provides:

    Semantic Retrieval
           +
    Keyword Retrieval
           |
           v
      Hybrid Retrieval

---

## Why MMR?

Normal similarity search can sometimes return several chunks that contain very similar information.

MMR helps reduce this redundancy by balancing:

- Relevance
- Diversity

This allows the final context to contain more useful information.

---

## Why Reranking?

The initial retrieval stage is designed to retrieve potentially relevant documents.

However, the retrieved documents may not be perfectly ordered.

The Cross-Encoder reranker performs a second relevance check.

    Initial Retrieval
           |
           v
    Retrieved Documents
           |
           v
    Cross-Encoder
           |
           v
    Relevance Scores
           |
           v
    Better Ranked Documents

The highest-ranked documents are then provided to the language model.

---


## Author

**Vivek Makwana**

LinkedIn: https://www.linkedin.com/in/vivek-makwana-2a7796243

---

## License

This project is created for learning, experimentation, and portfolio purposes.
