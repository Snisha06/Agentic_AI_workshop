# agents/logistics_analyst.py
from crewai import Agent

logistics_analyst = Agent(
    role="Logistics Analyst Agent",
    goal="Investigate current logistics operations and identify inefficiencies.",
    backstory="I've worked with delivery fleets and inventory systems to spot bottlenecks and waste."
)

def analyze_operations(products: list) -> str:
    prompt = f"Analyze logistics operations for these products: {products}. " \
             "Focus on route efficiency, inventory turnover, and typical pain points."
    return logistics_analyst.run(prompt)
