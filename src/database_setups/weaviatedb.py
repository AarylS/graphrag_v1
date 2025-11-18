
import weaviate
from langchain_weaviate.vectorstores import WeaviateVectorStore
from src.model_setups.ollama_embedding_model import get_ollama_embedding_model

weaviate_client = weaviate.connect_to_local()


def create_weaviatedb_index( all_splits):
    embedding_model = get_ollama_embedding_model()

    vectorstore = WeaviateVectorStore.from_documents(
        client=weaviate_client,
        documents=all_splits,
        embedding=embedding_model,
        index_name="graphrag_v2_test1",  
    )


def get_retriever():
    embedding_model = get_ollama_embedding_model()

    vectorstore = WeaviateVectorStore(
        client=weaviate_client,
        index_name="graphrag_v2_test1",  
        text_key="text",                
        embedding=embedding_model,
    )

    retriever = vectorstore.as_retriever(search_type="mmr")
    return retriever