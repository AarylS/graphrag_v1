"""
data ingestion
here the processed data is stored into vector and graph dataabase


"""
from src.config import file_path
from src.data_processes.data_processing import chunk_data
from src.database_setups.llamaindex_things import set_ollama_embedding_model, set_ollama_llm
from src.database_setups.llamaindex_things import vector_store, graph_store, clear_vectordb
from llama_index.core.indices.property_graph import SchemaLLMPathExtractor
from llama_index.core import VectorStoreIndex, PropertyGraphIndex, KnowledgeGraphIndex
from llama_index.core import StorageContext
from llama_index.llms.ollama import Ollama

from llama_index.embeddings.ollama import OllamaEmbedding

def ingest_data():
    clear_vectordb()
    chunks, docs = chunk_data(file_path)

    # setting model
    set_ollama_embedding_model()
    set_ollama_llm()
    # set_gemini_llm()
    # ollama_embedding = OllamaEmbedding(
    #     model_name="nomic-embed-text",
    #     # model_name="llama3.2:1b",
    #     base_url="http://localhost:11434",
    # )

    # ollama_llm=Ollama(
    #     # model="llama3.2:latest",
    #     model="llama3.2:1b",
    #     # request_timeout=120.0,
    #     base_url="http://localhost:11434",
    #     context_window=512,
    #     temperature=0
    # )

    storage_context = StorageContext.from_defaults(
        vector_store=vector_store,
        graph_store=graph_store
    )

    VectorStoreIndex.from_documents(
        chunks, 
        storage_context=storage_context,
        index_id="vector_store"
    )

    print("\n end of vector store index")

    # PropertyGraphIndex.from_documents(
    #     chunks,
    #     storage_context=storage_context,
    #     embed_model=ollama_embedding,
    #     max_triplets_per_chunk=3,
    #     num_workers=1, 
    #     show_progress=True,
    #     index_id="knowledge_graph",
    # )


    # PropertyGraphIndex.from_documents(
    #     chunks,
    #     embed_model=ollama_embedding,
    #     storage_context=storage_context,
    #     kg_extractors=[
    #         SchemaLLMPathExtractor(
    #             llm=ollama_llm
    #         )
    #     ],
    #     # property_graph_store=graph_store,
    #     max_triplets_per_chunk=3,
    #     show_progress=True,
    #     index_id="knowledge_graph",
    # )

    graph_index = KnowledgeGraphIndex.from_documents(
        docs,
        max_triplets_per_chunk=10,
        storage_context=storage_context,
        index_id="knowledge_graph"
    )

    # PropertyGraphIndex.from_documents(
    #     chunks,
    #     embed_model=ollama_embedding,
    #     kg_extractors=[
    #         SchemaLLMPathExtractor(
    #             llm=ollama_llm
    #         )
    #     ],
    #     property_graph_store=graph_store,
    #     show_progress=True,
    # )

    print("Created graph index:", graph_index.index_id)


    print("\n end of graph store index")

    storage_context.persist("./storage")

    print("\n end ingestion")
    
    

















""" old implementation
from src.model_setups.ollama_embedding_model import get_ollama_embedding_model
from src.data_processes.data_processing import chunk_data
from src.database_setups.weaviatedb import create_weaviatedb_index, get_retriever

def ingest_data():
    # 1. Chunk the data
    splits = chunk_data(file_path)

    # 2. create and populate vector store and get retriever
    embed_model = get_ollama_embedding_model()
    create_weaviatedb_index(embed_model, splits)
    # retriver = get_retriever(embed_model)

    # return retriver
"""
