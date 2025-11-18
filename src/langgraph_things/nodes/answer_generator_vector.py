
from src.langgraph_things.graph_state_init import GraphState
from src.langchain_things.answer_generator import answer_generator


def answer_generator_vector(state: GraphState):
    # geneartes answer from vectordb context
    print("---ANSWER GENERATOR VECTOR---")
    question = state["question"]
    context = state.get("vector_context", [])

    # Composite RAG generation
    answer_generated = answer_generator.invoke(
        {"question": question, "context": context}
    )

    return {
        "vector_context": context,
        "question": question,
        "generated_answer": answer_generated,
    }