from google.adk.agents import LoopAgent, Agent
from google.adk.models.lite_llm import LiteLlm
import os

model = LiteLlm(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    api_key=os.getenv("GROQ_API_KEY")
)

improve_agent = Agent(
    name="Improver",
    model=model,
    instruction="Improve the response quality each iteration."
)

root_agent = LoopAgent(
    name="LoopWorkflow",
    sub_agents=[improve_agent],
    max_iterations=3
)
