
from src.langgraph_things.graph_state_init import GraphState
from src.langchain_things.retrieval_vector_grader import retrieval_vector_grader


def grade_vector_context(state: GraphState):
    """ goes through all retrieved context and grades them as yes or no, 
    the context docs that are deemed no are removed
    """

    print("---GRADE VECTOR CONTEXT---")

    question = state["question"]
    vector_context = state.get("vector_context", [])

    # eval each doc of context
    filtered_context = []
    for d in vector_context:
        score = retrieval_vector_grader.invoke(
            {"question": question, "context": d}
        )
        grade = score["score"]
        # Document relevant
        if grade.lower() == "yes":
            print("---GRADE: DOCUMENT RELEVANT---")
            filtered_context.append(d)
        else:
            print("---GRADE: DOCUMENT NOT RELEVANT---")
            continue

    enhance_question = False
    if len(filtered_context) == 0:
        """ if true then filtered_context is an empty list
        this means there are no vector context documents
        so we need to attempt enhancing the question
        """
        enhance_question = True


    return {
        "vector_context": filtered_context, 
        "question": question, 
        "enhance_question":enhance_question
        }