
from typing import List, TypedDict

### State
class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        question: question
        generation: LLM generation
        documents: list of documents
        graph_context: results from graph search
    """

    question: str
    generated_answer: str
    vector_context: List[str]
    graph_context: str
    enhance_question: bool
    improved_question: list[str]


def initial_graph_state():
    return {
        "question": "",
        "generated_answer": "",
        "vector_context": [],
        "graph_context": "",
        "enhance_question": False,   
        "improved_question": ""
    }