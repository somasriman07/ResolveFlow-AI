import os
import sys

from dotenv import load_dotenv
from langchain_ollama import ChatOllama


def create_llm():
    load_dotenv()

    ollama_model = os.getenv("OLLAMA_MODEL")
    ollama_base_url = os.getenv("OLLAMA_BASE_URL")

    if not ollama_model:
        print("Error: OLLAMA_MODEL is not set in .env")
        sys.exit(1)

    if not ollama_base_url:
        print("Error: OLLAMA_BASE_URL is not set in .env")
        sys.exit(1)

    llm = ChatOllama(
        model=ollama_model,
        base_url=ollama_base_url,
        temperature=0
    )

    return llm