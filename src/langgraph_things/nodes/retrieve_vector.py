
from src.langgraph_things.graph_state_init import GraphState
from src.database_setups.llamaindex_things import get_retrievers


def retrieve_vector(state: GraphState):
    """Retrieve documents from vector store."""
    print("---RETRIEVE VECTOR---")
    vector_retriever = get_retrievers()

    if state["enhance_question"]:
        question = state["improved_questions"]
        print("retrieve enhanced question")
    else:
        question = state["question"]
        print("retrieve original question")

    documents = vector_retriever.retrieve(question)
    docs = [doc.node.get_content() for doc in documents]


    return {"vector_context": docs}
