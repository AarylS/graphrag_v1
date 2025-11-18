### question enhancer

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from src.model_setups.ollama_models import llm

"""
Provide the output as a JSON object with a single key "subquestions", where
the value is a list of short, precise questions.
"""

template= """You are an assistant that rewrites a user's question by breaking it into
simpler, focused sub-questions. Your goal is to help the user think more
clearly by decomposing the original question into its essential parts.
With these essential parts, form a single question that improves upon the original question.
Provide the output as a JSON object with a single key "improved_question", where
the value is a single improved questions.
Do not include any explanation or preamble.

Here is the original question:
{question}


"""


# change the prompt to match the new data sources and their descriptions
prompt = PromptTemplate(
    template=template,
    input_variables=["question"],
)

question_enhancer = prompt | llm | JsonOutputParser()



if __name__ == "__main__":
    from src.data_processes import retriever  # ensure retriever is imported from correct location
    
    question = ""
    print(question_enhancer.invoke({"question": question}))
