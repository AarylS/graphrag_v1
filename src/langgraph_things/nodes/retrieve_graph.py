
from src.langchain_things.graph_retrieval_generation import graph_rag_chain # need to change
from src.database_setups.llamaindex_things import get_retrievers
from src.langgraph_things.graph_state_init import GraphState

def graphrag(state: GraphState):
    """
    Perform GraphRAG search using Neo4j
    """

    print("---GRAPH SEARCH---")
    if state["enhance_question"]:
        question = state["improved_question"]
        print("retrieve context enhanced question")
    else:
        question = state["question"]
        print("retrieve context original question")

    vector_retriever = get_retrievers()

    # vector retriever
    documents = vector_retriever.retrieve(question)
    docs = [doc.node.get_content() for doc in documents]

    # Use the graph_rag_chain to perform the search
    result_dict = graph_rag_chain.invoke({"query": question})
    
    result = result_dict['result']
    graph_context = result
    # if returns nodes and edges then call a context generator
    # this should be graph sentaence.



    return {"graph_context": graph_context, "vector_context": docs}
