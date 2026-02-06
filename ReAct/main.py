from agent import ReActDocumentAgent

agent = ReActDocumentAgent()

question = "What are the benefits of microservices?"

result = agent.run(question)

print(result)