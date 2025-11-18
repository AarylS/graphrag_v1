### Answer Generator

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from src.model_setups.ollama_models import llm


# template= """You are an assistant for question-answering tasks. 
#     Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. 
#     Question: {question} 
#     Context: {context} 
#     Answer: """

template= """
You are an AI assistant that must answer the user's question only using the information provided in the context.
Do not use your own trained knowledge.
If the answer is not present in the provided context, say:
“The answer is not available in the provided context.”
Do not assume, infer, or guess anything beyond what the context explicitly states.
Cite or reference the parts of the context you used (if needed by the system).
Keep the answer clear, concise, and strictly grounded in the given context.
return a json with single key 'answer' and its value as the generated ansewr.

Context:
{context}

Question:
{question}

Your Answer (using ONLY the context above):

"""


# change the prompt to match the new data sources and their descriptions
prompt = PromptTemplate(
    template=template,
    input_variables=["question", "context"],
)

answer_generator = prompt | llm | JsonOutputParser()


if __name__ == "__main__":
    from src.data_processes import retriever  # ensure retriever is imported from correct location
    
    question = ""
    print(answer_generator.invoke({"question": question}))
