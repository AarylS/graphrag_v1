
from src.langgraph_things.graph_state_init import GraphState
from src.langchain_things.question_enhancer import question_enhancer


def enhance_question(state: GraphState):
    # enhances the question
    print("---ENHANCE QUESTION---")
    question = state["question"]

    enhance_question = True

    improved_question = question_enhancer.invoke(
        {"question": question}
    )

    return {
        "question": question,
        "improved_question": improved_question['improved_question'],
        "enhance_question": enhance_question
    }