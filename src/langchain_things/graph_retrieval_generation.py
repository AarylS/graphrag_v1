### Graph info retrieval and generation
"""
need to fix this
"""

from langchain_core.prompts import PromptTemplate
from langchain_neo4j import GraphCypherQAChain
from src.database_setups.llamaindex_things import graph_store
from src.database_setups.neo4j import graph

from src.model_setups.ollama_models import get_ollama_llm, get_ollama_graph_llm


cypher_prompt = PromptTemplate(
    template="""You are an expert at generating Cypher queries for Neo4j.
    Use the following schema to generate a Cypher query that answers the given question.
    nodes have one property called id that holds the information and one label called Entity.
    cypher command type(relation) returns the  relationship type.
    remember to check for direction of path.
    Make the query flexible by using case-insensitive matching and partial string matching where appropriate.
    example: MATCH (n:Entity {id: 'info'}) - [r] -> () RETURN type(r) AS relType
    
    Schema:
    {schema}
    
    Question: {question}
    
    Cypher Query:""",
    input_variables=["schema", "question"],
)


qa_prompt = PromptTemplate(
    template="""You are an assistant for question-answering tasks. 
    Use the following Cypher query results to answer the question. If you don't know the answer, just say that you don't know. 
    Use a few sentences maximum and keep the answer concise. 
    
    Question: {question} 
    Cypher Query: {query}
    Query Results: {context} 
    
    Answer:""",
    input_variables=["question", "query", "context"],
)


llm = get_ollama_llm()

graph_llm = get_ollama_llm()

graph_rag_chain = GraphCypherQAChain.from_llm(
    cypher_llm=graph_llm,
    qa_llm=llm,
    validate_cypher=True,
    graph=graph,
    verbose=True,
    return_intermediate_steps=True,
    return_direct=True,
    cypher_prompt=cypher_prompt,
    qa_prompt=qa_prompt,
    allow_dangerous_requests=True
)


if __name__=='__main__':
    question = "What are companies integrating?"
    generation = graph_rag_chain.invoke({"query": question})
    print(generation)
