### Answer Grader

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from src.model_setups.ollama_models import llm


template= """You are a grader assessing whether an 
    answer is useful to resolve a question. Give a binary score 'yes' or 'no' to indicate whether the answer is 
    useful to resolve a question. Provide the binary score as a JSON with a single key 'score' and no preamble or explanation.
     
    Here is the answer:
    {generated_answer} 

    Here is the question: {question}

"""


# change the prompt to match the new data sources and their descriptions
prompt = PromptTemplate(
    template=template,
    input_variables=["generated_answer", "question"],
)

answer_grader = prompt | llm | JsonOutputParser()



if __name__ == "__main__":
    from src.data_processes import retriever  # ensure retriever is imported from correct location
    
    question = ""
    print(answer_grader.invoke({"question": question}))
