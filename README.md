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

   [add the line that prints asking did you ingest data.]

    the program will run the graphrag after ingestion is completed.

6. to run grahrag on ingested data
    type n to the question. question is the same as below.

    -bash-
   
    [add the line that prints asking did you ingest data.]

8. type your question when prompted to type the question, 

9. the graphrag runs.


