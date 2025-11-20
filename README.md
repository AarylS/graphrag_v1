# Graph rag




## pre requisites
this is required to run the project.

    install uv.

    install docker desktop


## installation

1. Clone the repository

   -bash-
   
   git clone https://github.com/AarylS/graphrag_v1.git
   
   cd graphrag_v1

3. create virtual environment

    -bash-
   
    uv venv .venv
   
    source .venv/bin/activate

5. install dependencies

    -bash-
   
    uv pip install -r requirements.txt

7. set docker container

    -bash-
   
    docker compose up -d

9. download ollama model and embedding model, run command

    -bash-
   
    docker ollama ollama pull model_name.

    this model name must be added in the file graphrag_v1/src/config.py.
    add model_name string at ollama_model and ollama_embedding_model variables.

## Usage

1. add the pdfs in the folder named data. 

2. run the command below.

    -bash-
   
    uv run python main.py

4. to run the ingestion
    type n to the question. question is the same as below.
   
    -bash-

    have you added data to data folder and processed it? (y/n):

    the program will run the graphrag after ingestion is completed.

6. to run grahrag on ingested data
    type y to the question. question is the same as below.

    -bash-
   
    have you added data to data folder and processed it? (y/n):

8. type your question when prompted to type the question, 

9. the graphrag runs.


if required:
uv pip install llama-index llama-index-llms-ollama llama-index-embeddings-ollama langchain langgraph langchain-ollama langchain-neo4j langchain-weaviate llama-index-graph-stores-neo4j llama-index-vector-stores-weaviate neo4j weaviate-client ollama