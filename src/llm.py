import os
import torch

from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace


load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"


def get_llm():

    endpoint = HuggingFaceEndpoint(
        repo_id=MODEL_NAME,
        huggingfacehub_api_token=HF_TOKEN,
        max_new_tokens=300,
        temperature=0.2,
        repetition_penalty=1.1,
        timeout=100
    )

    llm = ChatHuggingFace(llm=endpoint)

    return llm