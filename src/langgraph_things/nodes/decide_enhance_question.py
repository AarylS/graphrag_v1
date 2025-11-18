
from src.langgraph_things.graph_state_init import GraphState



def decide_enhance_question(state: GraphState):
    """
    checks if enhancing the question is to be done.
    """

    print("---DECIDE TO ENHANCE QUESTION---")

    if state["enhance_question"]:
        # All documents have been filtered check_relevance
        # We will re-generate a new query
        print(
            "---DECISION: ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, question enhancer required---"
        )

        return "enhance_question"
    else:
        # We have relevant documents, so generate answer
        print("---DECISION: GENERATE ANSWER---")
        return "generate_answer"