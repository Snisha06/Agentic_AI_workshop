# agents/optimization_strategist.py
from crewai import Agent

optimization_strategist = Agent(
    role="Optimization Strategist Agent",
    goal="Design a data-driven optimization plan based on analyst insights.",
    backstory="I specialize in translating logistical issues into actionable strategies."
)

def plan_optimization(insights: str, products: list) -> str:
    prompt = f"Based on these logistics insights:\n{insights}\n" \
             f"Create targeted optimization strategies for products: {products}."
    return optimization_strategist.run(prompt)
