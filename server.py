from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import time # For simulation
import uvicorn

from src.langgraph_things.workflow import workflow

from pprint import pprint

from src.langgraph_things.graph_state_init import GraphState, initial_graph_state

app = FastAPI()

# Define the request body structure
class ChatRequest(BaseModel):
    messages: list

# 1. Your RAG Logic function
def run_rag_system(query: str):

    try:
        print("Processing input...")
        state = initial_graph_state()
        state["question"] = query   # update the question

        """
        run graphrag workflow
        """
        for output in workflow.stream(state):
            for key, value in output.items():
                pprint(f"Finished running: {key}:")
        pprint(value['generated_answer'])
        response = value['generated_answer']
        
    except Exception as e:
        print(f"Error: {str(e)}")
    
    # Simulate streaming words
    for word in response.split():
        yield f"{word} "
        time.sleep(0.1)

# 2. The API Endpoint
@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    # Get the last message from the user
    last_message = request.messages[-1]['content']
    
    # Create a generator for streaming
    def event_stream():
        for chunk in run_rag_system(last_message):
            # We just send raw text chunks
            yield chunk

    return StreamingResponse(event_stream(), media_type="text/plain")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)