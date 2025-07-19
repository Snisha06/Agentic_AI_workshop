# tasks.py
from crewai import Task
from agents.logistics_analyst import analyze_operations, logistics_analyst
from agents.optimization_strategist import plan_optimization, optimization_strategist

analyze_task = Task(
    description="Investigate logistics operations for product list.",
    expected_output="Insights into inefficiencies, routes, inventory.",
    agent=logistics_analyst
)

optimize_task = Task(
    description="Generate optimization strategy based on analysis.",
    expected_output="Detailed plan with steps and metrics.",
    agent=optimization_strategist
)
