from google.adk.agents import SequentialAgent, Agent
from google.adk.models.lite_llm import LiteLlm
import os

model = LiteLlm(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    api_key=os.getenv("GROQ_API_KEY")
)

analyze_agent = Agent(
    name="Analyzer",
    model=model,
    instruction="Analyze the user request and extract key tasks."
)

plan_agent = Agent(
    name="Planner",
    model=model,
    instruction="Create a step-by-step execution plan."
)

execute_agent = Agent(
    name="Executor",
    model=model,
    instruction="Execute the plan and generate final output."
)

workflow = SequentialAgent(
    name="SequentialWorkflow",
    sub_agents=[analyze_agent, plan_agent, execute_agent]
)
