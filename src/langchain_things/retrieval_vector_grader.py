# Retrieval Vector Grader

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from src.model_setups.ollama_models import llm


template= """You are a grader assessing whether content retrieved from a vector database
is relevant to a user's question. Your task is to determine if the retrieved
chunks meaningfully support, answer, or relate to the question. 

Give a binary score "yes" or "no" to indicate whether the retrieved content
is relevant. Provide the score as a JSON object with a single key "score"
and do not include any explanation or preamble.

Here is the question:
{question}

Here is the retrieved content:
{context}

"""


# change the prompt to match the new data sources and their descriptions
prompt = PromptTemplate(
    template=template,
    input_variables=["question", "vector_context"],
)

retrieval_vector_grader = prompt | llm | JsonOutputParser()



if __name__ == "__main__":
    from src.data_processes import retriever  # ensure retriever is imported from correct location
    
    question = ""
    print(retrieval_vector_grader.invoke({"question": question}))
