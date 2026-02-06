from retriever import EmbeddingRetriever
from generator import Generator

retriever = EmbeddingRetriever()
generator = Generator()

query = "What are advantages of microservices?"

docs = retriever.retrieve(query)
print("RETRIEVED:")
print(docs)

answer = generator.generate(query, docs)
print("\nANSWER:")
print(answer)