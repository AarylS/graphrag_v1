### Answer Generator

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from src.model_setups.ollama_models import llm


template= """
You are an AI system that must answer the user's question ONLY using the provided context.
You MUST NOT use any trained knowledge.
If the answer is not present in the context, reply with:
"The answer is not available in the provided context."

You must follow these rules:
- Do NOT assume or infer anything outside the context.
- Do NOT generate explanations outside the context.
- Respond ONLY with a valid JSON object containing a single key: "answer".
- The JSON must contain ONLY the final answer string.
- DO NOT output anything outside the JSON object (no notes, no explanations, no text before/after).


Context:
{context}

graph context:
{graph_context}

Question:
{question}


Now respond ONLY with the JSON object:
"""


# change the prompt to match the new data sources and their descriptions
prompt = PromptTemplate(
    template=template,
    input_variables=["question", "context", "graph_context"],
)

answer_generator_graphrag = prompt | llm | JsonOutputParser()


if __name__ == "__main__":
    from src.data_processes import retriever  # ensure retriever is imported from correct location
    
    question = ""
    print(answer_generator_graphrag.invoke({"question": question}))
