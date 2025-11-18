
from src.langgraph_things.graph_state_init import GraphState
from src.langchain_things.router import router


def route_question(state: GraphState):
    print("---ROUTE QUESTION---")

    if state["enhance_question"]:
        question = state["improved_questions"]
        print("routing enhanced question")
    else:
        question = state["question"]
        print("routing original question")

    source = router.invoke({"question": question})
    print(source)
    print("source extracting from ", source["datasource"])

    if source["datasource"] == "graphrag":
        return "graphrag"
    else:
        return "retrieve"








