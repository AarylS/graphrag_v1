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

2. create virtual environment

    -bash-
    uv venv .venv
    source .venv/bin/activate

3. install dependencies

    -bash-
    uv pip install -r requirements.txt

4. set docker container

    -bash-
    docker compose up -d

5. download ollama model and embedding model, run command

    -bash-
    docker ollama ollama pull model_name.

    this model name must be added in the file graphrag_v1/src/config.py.
    add model_name string at ollama_model and ollama_embedding_model variables.


## Usage

1. add the pdfs in the folder named data. 

2. run the command below.

    -bash-
    uv run python main.py

3. to run the ingestion
    type n to the question. question is the same as below.
    -bash-
    [add the line that prints asking did you ingest data.]

    the program will run the graphrag after ingestion is completed.

4. to run grahrag on ingested data
    type n to the question. question is the same as below.

    -bash-
    [add the line that prints asking did you ingest data.]

5. type your question when prompted to type the question, 

6. the graphrag runs.


