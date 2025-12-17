
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import json
import uvicorn
import asyncio

from src.langgraph_things.workflow import workflow

from pprint import pprint

from src.langgraph_things.graph_state_init import GraphState, initial_graph_state


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, set to ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat/stream")
async def chat_endpoint(request: Request):
    # 1. Parse the incoming JSON body
    data = await request.json()
    user_input = data.get("query")

    print(f"Received Query: {user_input}")

    # 2. Define the generator for Server-Sent Events (SSE)
    async def event_generator():
        try:
            # --- YOUR LANGGRAPH/WORKFLOW LOGIC ---
            state = initial_graph_state()
            state["question"] = user_input
            
            final_answer = ""

            # Iterate through the graph steps
            for output in workflow.stream(state):
                for key, value in output.items():
                    # We log internal steps to the server console
                    print(f"Finished running node: {key}")

                    
                    # Capture the answer if this node produced one
                    if 'generated_answer' in value:
                        final_answer = value['generated_answer']['answer']
                    else:
                        final_answer = "Sorry, I couldn't generate an answer."

            # --- PREPARE RESPONSE FOR FRONTEND ---
            
            # Important: Your frontend calls `append(content)` every time it receives a message.
            # If we stream word-by-word here, your UI will create 100 separate message bubbles.
            # Therefore, we send the FULL answer as one single event at the end.
            
            if final_answer:
                # 1. Wrap content in JSON (as your frontend expects JSON.parse)
                payload = json.dumps({"content": final_answer})
                
                # 2. Format as Server-Sent Event (data: ... \n\n)
                yield f"data: {payload}\n\n"
            else:
                # Fallback if no answer found
                payload = json.dumps({"content": "Sorry, I couldn't generate an answer."})
                yield f"data: {payload}\n\n"

        except Exception as e:
            print(f"Error: {e}")
            payload = json.dumps({"content": f"Error: {str(e)}"})
            yield f"data: {payload}\n\n"

    # 3. Return with the specific SSE media type
    return StreamingResponse(event_generator(), media_type="text/event-stream")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


