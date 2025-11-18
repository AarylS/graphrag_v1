
from src.langgraph_things.graph_state_init import GraphState
from src.langchain_things.answer_generator_graphrag import answer_generator_graphrag


def answer_generator_graph(state: GraphState):
    # geneartes answer from vectordb context
    print("---ANSWER GENERATOR GRAPHRAG---")
    question = state["question"]
    context = state.get("vector_context", [])
    graph_context = state["graph_context"]

    # Composite RAG generation
    answer_generated = answer_generator_graphrag.invoke(
        {"question": question, "context": context, "graph_context":graph_context}
    )

    return {
        "vector_context": context,
        "question": question,
        "generated_answer": answer_generated,
        "graph_context":graph_context
    }