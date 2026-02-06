from planner_agent import PlannerAgent 
from executor_agent import ExecutorAgent

goal = "Analyze sales.csv and generate insights"

planner = PlannerAgent()
executor = ExecutorAgent()

plan = planner.create_plan(goal)
result = executor.execute(plan)

print(result)