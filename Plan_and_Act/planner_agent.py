class PlannerAgent:
    def create_plan(self, goal: str) -> list:
        return [
            "Load the CSV file",
            "Clean missing values",
            "Compute total sales per product",
            "Identify top 3 products",
            "Analyze monthly sales trend",
            "Summarize insights"
        ]
