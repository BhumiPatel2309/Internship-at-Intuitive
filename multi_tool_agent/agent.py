import datetime
import os
from zoneinfo import ZoneInfo
from google.adk.models.lite_llm import LiteLlm
from google.adk.agents.llm_agent import Agent

os.environ["OLLAMA_API_BASE"] = "http://localhost:11434"

def get_time(city: str) -> str:
    """Get current time for a given city."""
    zones = {
        "india": "Asia/Kolkata",
        "new york": "America/New_York",
        "london": "Europe/London",
    }
    city = city.lower()
    if city not in zones:
        return f"I don't know the timezone for {city}"
    now = datetime.datetime.now(ZoneInfo(zones[city]))
    return f"Current time in {city.title()} is {now.strftime('%H:%M:%S')}"

def calculator(expression: str) -> str:
    """Evaluate a math expression."""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Calculation error: {e}"

my_ollama_model = LiteLlm(model="ollama_chat/llama3.1")

root_agent = Agent(
    name="multi_tool_agent",
    model=my_ollama_model,  
    description="A multi-tool agent that can calculate and tell time.",
    instruction="""
You are a helpful assistant.

Rules:
- If the user asks for time in a city → use get_time
- If the user asks to calculate → use calculator
- Otherwise answer normally
""",
    tools=[get_time, calculator],
)
