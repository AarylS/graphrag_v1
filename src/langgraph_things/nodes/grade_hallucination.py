
from src.langgraph_things.graph_state_init import GraphState
from src.langchain_things.hallucination_grader import hallucination_grader
from src.langchain_things.answer_grader import answer_grader


def grade_hallucination_n_answer(state: GraphState):
    # grade for hallucination and generated answer

    print("---CHECK HALLUCINATIONS---")
    question = state["question"]
    vector_context = state["vector_context"]
    graph_context = state["graph_context"]
    generated_answer = state["generated_answer"]

    context = vector_context.append(graph_context)

    score = hallucination_grader.invoke(
        {"context": context, "generated_answer": generated_answer}
    )
    grade = score["score"]

    # Check hallucination
    if grade == "no":
        print("---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---")
        # Check question-answering
        print("---GRADE GENERATION vs QUESTION---")
        score = answer_grader.invoke({"question": question, "generated_answer": generated_answer})
        grade = score["score"]
        if grade == "yes":
            print("---DECISION: GENERATION ADDRESSES QUESTION---")
            return "useful"
        else:
            print("---DECISION: GENERATION DOES NOT ADDRESS QUESTION---")
            return "not useful"
    else:
        print("---DECISION: GENERATION IS NOT GROUNDED IN DOCUMENTS, RE-TRY---")
        return "not supported"

