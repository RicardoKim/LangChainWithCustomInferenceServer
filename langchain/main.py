from langchain.chains import GraphCypherQAChain
from langchain.chat_models import ChatOpenAI
from langchain.graphs import Neo4jGraph
from llm.FakeLLM import FakeLLM

graph = Neo4jGraph(
    url="bolt://localhost:7687", username="neo4j", password="password"
)

customLLM = FakeLLM()

chain = GraphCypherQAChain.from_llm(
    customLLM, graph=graph, verbose=True
)

while True:
    query = input("Ask about graph : ")
    chain.run(query)