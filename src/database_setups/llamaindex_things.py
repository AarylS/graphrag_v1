"""
everythin needed by llamaindex

"""
from src.database_setups.weaviatedb import weaviate_client
from llama_index.vector_stores.weaviate import WeaviateVectorStore
from llama_index.graph_stores.neo4j import Neo4jGraphStore
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import Settings
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.llms.ollama import Ollama
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.core import VectorStoreIndex, PropertyGraphIndex, KnowledgeGraphIndex

def set_ollama_embedding_model():
    ollama_embedding = OllamaEmbedding(
        model_name="nomic-embed-text",
        # model_name="llama3.2:1b",
        base_url="http://localhost:11434",
    )

    Settings.embed_model = ollama_embedding

def set_ollama_llm():
    llm = Ollama(
        # model="llama3.2:latest",
        model="llama3.2:1b",
        # request_timeout=120.0,
        base_url="http://localhost:11434",
        context_window=512,
    )
    Settings.llm = llm



def set_gemini_llm():

    llm = GoogleGenAI(
        model="models/gemini-2.0-flash-lite",
        api_key="",  # uses GOOGLE_API_KEY env var by default
    )
    Settings.llm = llm


vector_store = WeaviateVectorStore(
    weaviate_client=weaviate_client, 
    index_name="Weaviate_vectordb"
)

def clear_vectordb():
    weaviate_client.collections.delete("Weaviate_vectordb")  # or your index name


graph_store = Neo4jGraphStore(
    username="neo4j",
    password="test1234",
    url="bolt://localhost:7687",
    # database="neo4j_graphdb",
)

from llama_index.graph_stores.neo4j import Neo4jPropertyGraphStore

# graph_store = Neo4jPropertyGraphStore(
#     username="neo4j",
#     password="test1234",
#     url="bolt://localhost:7687",
# )

def get_retrievers():
    set_ollama_embedding_model()  
    set_ollama_llm()

    storage_context = StorageContext.from_defaults(
        # vector_store=vector_store,
        # graph_store=graph_store,
        persist_dir="./storage_1"
    )

    # vector_index = load_index_from_storage(
    #     storage_context,
    #     index_id="vector_store"
    # )

    # graph_index = load_index_from_storage(
    #     storage_context,
    #     index_id="knowledge_graph"
    # )

    vector_index = VectorStoreIndex.from_vector_store(vector_store)

    ollama_embedding = OllamaEmbedding(
        model_name="nomic-embed-text",
        # model_name="llama3.2:1b",
        base_url="http://localhost:11434",
    )

    ollama_llm=Ollama(
        # model="llama3.2:latest",
        model="llama3.2:1b",
        # request_timeout=120.0,
        base_url="http://localhost:11434",
        context_window=512,
        temperature=0
    )

    # graph_index = PropertyGraphIndex.from_existing(
    #     property_graph_store=graph_store,
    #     llm=ollama_llm,
    #     embed_model=ollama_embedding,
    # )

    # graph_index = KnowledgeGraphIndex.from_existing(
    #     property_graph_store=graph_store,
    #     llm=ollama_llm,
    #     embed_model=ollama_embedding,
    # )

    

    # Create retrievers
    vector_retriever = vector_index.as_retriever(similarity_top_k=3)

    # graph_retriever = graph_index.as_retriever(
    #     # include_embeddings=True,
    #     max_path=2
    # )

    return vector_retriever#, graph_retriever


