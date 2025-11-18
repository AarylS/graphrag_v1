### Router

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from src.model_setups.ollama_models import llm


# template= """You are an expert at routing a user question to the most appropriate data source. 
#     You have two options:
#     1. 'vectorstore': Use for questions about LLM agents, prompt engineering, and adversarial attacks.
#     2. 'graphrag': Use for questions that involve relationships between entities, such as authors, papers, and topics, or when the question requires understanding connections between concepts.

#     You do not need to be stringent with the keywords in the question related to these topics. 
#     Choose the most appropriate option based on the nature of the question.

#     Return a JSON with a single key 'datasource' and no preamble or explanation. 
#     The value should be one of: 'vectorstore' or 'graphrag'.
    
#     Question to route: 
#     {question}"""

template = """You are a router that decides whether a user's request should be handled by
VectorStore RAG or by GraphRAG. Your task is to analyze the question and
select the most appropriate system based on the reasoning structure implied
by the query.

Choose "vectorstore" when the request is best served by semantic retrieval
over chunks of text, such as direct fact lookup, summarization, or
document-based Q&A.

Choose "graphrag" when the request benefits from relational understanding,
entity linking, multi-hop reasoning, graph traversal, or structural
knowledge that depends on connections between concepts.

Return a JSON object with a single key "datasource" whose value is either
"vectorstore" or "graphrag". Do not include any explanations or preamble.

Here is the user question:
{question}
"""


# change the prompt to match the new data sources and their descriptions
prompt = PromptTemplate(
    template=template,
    input_variables=["question"],
)

router = prompt | llm | JsonOutputParser()

