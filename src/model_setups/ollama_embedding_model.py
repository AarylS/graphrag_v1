
from langchain_ollama import OllamaEmbeddings


def get_ollama_embedding_model():
    embedding_model = OllamaEmbeddings(model="nomic-embed-text")
    return embedding_model

