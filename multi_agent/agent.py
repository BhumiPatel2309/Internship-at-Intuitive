from google.adk.agents.llm_agent import Agent
from dotenv import load_dotenv
import os

load_dotenv()

tech_agent = Agent(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    name="tech_agent",
    description="Handles technical questions",
    instruction="""
You answer programming, AI, ML, and software-related questions.
Be accurate, structured, and concise.
"""
)

general_agent = Agent(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    name="general_agent",
    description="Handles general questions",
    instruction="""
You answer general knowledge, daily life, and casual questions.
Keep the tone simple and friendly.
"""
)

router_agent = Agent(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    name="router_agent",
    description="Decides which agent should answer",
    instruction="""
You are a router.

Rules:
- Programming, AI, ML, coding → tech_agent
- Everything else → general_agent

Respond with ONLY one word:
tech_agent OR general_agent
"""
)

root_agent = Agent(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    name="root_agent",
    description="Main orchestrator agent",
    instruction="""
You are the main assistant.
You DO NOT answer questions directly.

Your job:
1. Ask the router_agent which agent should handle the question
2. Send the user question to that agent
3. Return the agent's response as the final answer
"""
)

class MultiAgentSystem:
    def handle(self, query: str) -> str:
        decision = router_agent.run(query).strip().lower()

        if "tech_agent" in decision:
            return tech_agent.run(query)

        if "general_agent" in decision:
            return general_agent.run(query)

        return general_agent.run(query)

if __name__ == "__main__":
    system = MultiAgentSystem()
    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        response = system.handle(user_input)
        print("\nAgent:", response, "\n")
