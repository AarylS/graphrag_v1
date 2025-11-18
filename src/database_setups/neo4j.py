
from langchain_community.graphs import Neo4jGraph

graph = Neo4jGraph(
    username="neo4j",
    password="test1234",
    url="bolt://localhost:7687",
)


if __name__=='__main__':
    pass