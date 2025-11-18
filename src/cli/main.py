"""
cli main

[what happens here]
runs the command line interface for Graphrag

intercations with folders:
- processed_data
- langgrah_things/workflow.py

note:
- write code for running data processing script
- write the workflow code in workflow python file

"""

from dotenv import load_dotenv

from src.data_processes.data_ingestion import ingest_data
from src.langgraph_things.workflow import workflow

from pprint import pprint

load_dotenv()

from src.langgraph_things.graph_state_init import GraphState, initial_graph_state


def main():
    """
    interface for command line execution
    print statments, user input
    """

    print("Graphrag cli")

    user_input = input("have you added data to data folder and processed it? (y/n): ")
    if user_input.lower() in ['n', 'no']:
        # write code for running data processing script
        ingest_data()
        print("data ingestion complete")

    print("you can interact with Graphrag")
    print("Type 'quit' to quit")

    """
    main loop
    process:
    1. get user input
    2. process input with Workflow
    3. print result
    4. repeat until user quits
    """
    while True:
        try:
            user_input = input("Enter your Question: ")

            if user_input.lower() in ['quit', 'exit', 'q', '']:
                print("Exiting Graphrag cli.")
                break

            print("Processing input...")
            state = initial_graph_state()
            state["question"] = user_input   # update the question

            """
            [explain what happens here]
            """
            for output in workflow.stream(state):
                for key, value in output.items():
                    pprint(f"Finished running: {key}:")
            pprint(value['generated_answer'])
        
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
