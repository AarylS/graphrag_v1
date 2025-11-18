# Hallucination Grader

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from src.model_setups.ollama_models import llm


template= """
You are an AI system performing a hallucination check.

Your task:
Determine whether the assistant's answer is supported ONLY by the provided context.

Rules:
- Output ONLY a valid JSON object with a single key: "score".
- The value MUST be either "yes" or "no":
    - "yes"  → The answer contains hallucination (not fully supported by the context).
    - "no"   → The answer is fully supported by the context.
- No explanations, no notes, no reasoning outside the JSON.
- DO NOT include anything before or after the JSON.


Context:
{context}

Answer to evaluate:
{generated_answer}

Now respond ONLY with the JSON object:
"""


# change the prompt to match the new data sources and their descriptions
prompt = PromptTemplate(
    template=template,
    input_variables=["context", "generated_answer"],
)

hallucination_grader = prompt | llm | JsonOutputParser()



if __name__ == "__main__":
    from src.data_processes import retriever  # ensure retriever is imported from correct location
    
    question = ""
    print(hallucination_grader.invoke({"question": question}))
