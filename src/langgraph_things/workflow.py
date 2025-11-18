"""
main part where workflow is created and initialized

contains:
- state
- build graph,flow of the workflow 
- complied workflow

intercations with folders:
- processed_data
- langgrah_things/workflow.py

note:
- write code for running data processing script
- write the workflow code in workflow python file

"""

from langgraph.graph import END, StateGraph

from src.langgraph_things.nodes.question_router import route_question
from src.langgraph_things.nodes.retrieve_vector import retrieve_vector
from src.langgraph_things.nodes.retrieve_graph import graphrag
from src.langgraph_things.nodes.grade_vector_context import grade_vector_context
from src.langgraph_things.nodes.decide_enhance_question import decide_enhance_question
from src.langgraph_things.nodes.answer_generator_graphrag import answer_generator_graph
from src.langgraph_things.nodes.answer_generator_vector import answer_generator_vector
from src.langgraph_things.nodes.enhance_question import enhance_question
from src.langgraph_things.nodes.grade_hallucination import grade_hallucination_n_answer

from src.langgraph_things.graph_state_init import GraphState, initial_graph_state

workflow_structure = StateGraph(GraphState)




"""
write all nodes and control flow functions here.


"""

# Define the nodes
workflow_structure.add_node("retrieve", retrieve_vector)  
workflow_structure.add_node("graphrag", graphrag)  
workflow_structure.add_node("grade_vector_context", grade_vector_context)  
workflow_structure.add_node("answer_generator_graph", answer_generator_graph)
workflow_structure.add_node("answer_generator_vector", answer_generator_vector)
workflow_structure.add_node("enhance_question", enhance_question)

# Set conditional entry point
workflow_structure.set_conditional_entry_point(
    route_question,
    {
        "retrieve": "retrieve",
        "graphrag": "graphrag",
    },
)


# Add edges
workflow_structure.add_edge("retrieve", "grade_vector_context")

workflow_structure.add_edge("graphrag", "answer_generator_graph")

workflow_structure.add_conditional_edges(
    "grade_vector_context",
    decide_enhance_question,
    {
        "enhance_question": "enhance_question",
        "generate_answer": "answer_generator_vector",
    },
)

workflow_structure.add_edge("enhance_question", "graphrag")

workflow_structure.add_conditional_edges(
    "answer_generator_graph",
    grade_hallucination_n_answer,
    {
        "not supported": "enhance_question",
        "useful": END,
        "not useful": "enhance_question",
    },
)

workflow_structure.add_conditional_edges(
    "answer_generator_vector",
    grade_hallucination_n_answer,
    {
        "not supported": "enhance_question",
        "useful": END,
        "not useful": "enhance_question",
    },
)

# Compile
workflow = workflow_structure.compile()