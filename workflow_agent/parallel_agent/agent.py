from google.adk.agents import ParallelAgent, Agent
from google.adk.models.lite_llm import LiteLlm
import os

model = LiteLlm(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    api_key=os.getenv("GROQ_API_KEY")
)
research_agent = Agent(
    name="Researcher",
    model=model,
    instruction="Research the topic and gather facts."
)

summary_agent = Agent(
    name="Summarizer",
    model=model,
    instruction="Summarize the topic concisely."
)

examples_agent = Agent(
    name="ExampleGenerator",
    model=model,
    instruction="Generate practical examples."
)

parallel_workflow = ParallelAgent(
    name="ParallelWorkflow",
    sub_agents=[research_agent, summary_agent, examples_agent]
)
