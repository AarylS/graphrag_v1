"""
graphrag
- by aaryl


"""

# from src.cli.main import main
from src.streamlit.app import run

if __name__ == "__main__":
    # main()
    run()


# # testing ingestion
# from src.data_processes.data_ingestion import ingest_data
# from src.database_setups.llamaindex_things import get_retrievers
# from src.langchain_things.graph_retrieval_generation import graph_rag_chain

# if __name__ == "__main__":
#     # ingest_data()


#     # v,g = get_retrievers()
#     # question = "how ai helps in customer service?"
#     # documents = v.retrieve(question)
#     # docs = [doc.node.get_content() for doc in documents]
#     # print(len(docs))
#     # print("vetor retrieve")
#     # print(docs)


#     # nodes = g.retrieve(question)
#     # for node in nodes:
#     #     print(node)

#     # kgs = [doc.node.get_content() for doc in nodes]
#     # print("graph retrieve")
#     # print(len(kgs))
#     # for kg in kgs:
#     #     print(f"\n {kg}")
#     # print("\n\nend")


#     question = "What are companies integrating?"
#     generation = graph_rag_chain.invoke({"query": question})
#     print(generation)