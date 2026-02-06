import os 
import sys
from dotenv import load_dotenv 
sys.path.append(os.path.dirname(os.path.abspath(__file__))) 
load_dotenv() 

from google.adk.agents import SequentialAgent
from .sequential_agent import workflow as seq_workflow
from .parallel_agent import parallel_workflow
from .loop_agent import loop_workflow

root_agent = SequentialAgent(
    name="MainWorkflowAgent",
    sub_agents=[
        seq_workflow,      
        parallel_workflow, 
        loop_workflow      
    ]
)
