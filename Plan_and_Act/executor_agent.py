import pandas as pd 

class ExecutorAgent:
    def __init__(self):
            self.context = {}

    def execute(self, steps):
        for step in steps:
            print(f"Executing step: {step}")

            if step == "Load the CSV file":
                self.context["df"] = pd.read_csv("sales.csv")

            elif step == "Clean missing values":
                self.context["df"].fillna(0, inplace=True)

            elif step == "Compute total sales per product":
                self.context["product_sales"] = (
                        self.context["df"].groupby("product")["sales"].sum()
                    )

            elif step == "Identify top 3 products":
                self.context["top_products"] = (
                        self.context["product_sales"].sort_values(ascending=False).head(3)
                    )
                
            elif step == "Analyze monthly sales trend":
                self.context["monthly_trend"] = (
                        self.context["df"].groupby("month")["sales"].sum()
                    )

            elif step == "Summarize insights":
                return self._summarize()

    def _summarize(self):
        return {
                "top_products": self.context.get("top_products").to_dict(),
                "monthly_trend": self.context.get("monthly_trend").to_dict()
            }



