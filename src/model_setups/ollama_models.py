from langchain_ollama import ChatOllama


def get_ollama_llm():
    llm = ChatOllama(
        model="llama3.2:latest",
        temperature=0,
    )

    return llm

llm = ChatOllama(
        model="llama3.2:latest",
        temperature=0,
    )

def get_ollama_graph_llm():
    llm = ChatOllama(
        model="codellama:7b",
        temperature=0,
    )

    return llm
   
