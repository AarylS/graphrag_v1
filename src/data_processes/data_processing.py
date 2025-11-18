"""
data processing
here will be the function to processes data from folder "./data"

here all data is processed
- chunking


"""
from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
import re
from llama_index.core import Document

def clean_text(text):
    # Remove newlines between words
    text = re.sub(r'\n\s*\n', ' ', text)
    text = re.sub(r'\n', ' ', text)
    # Collapse multiple spaces
    text = re.sub(r'\s+', ' ', text)
    return text.strip()



def chunk_data(doc_path):
    # load documents
    raw_docs = SimpleDirectoryReader(doc_path).load_data()
    print(f"Successfully loaded {len(raw_docs)} pages.")

    cleaned_docs = []
    for doc in raw_docs:
        cleaned_docs.append(
            Document(
                text=clean_text(doc.text),
                extra_info=doc.extra_info    
            )
        )

    splitter = SentenceSplitter(
        chunk_size=200,
        chunk_overlap=40,
    )

    chunks = splitter.get_nodes_from_documents(cleaned_docs)
    print(f"data chunked into {len(chunks)} chunks")

    return chunks, cleaned_docs



""" this is data chunking using pymupdf library

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader

def chunk_data(doc_path):
    loader = PyMuPDFLoader(doc_path)

    docs = loader.load()


    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,  # chunk size (characters)
        chunk_overlap=200,  # chunk overlap (characters)
        add_start_index=True,  # track index in original document
    )
    all_splits = text_splitter.split_documents(docs)

    print(f"Split data into {len(all_splits)} sub-documents.")

    return all_splits
"""
