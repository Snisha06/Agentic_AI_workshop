from crewai import Agent

manager_agent = Agent(
    role="Manager Agent",
    goal="Coordinate analysis and correction of Python code automatically.",
    backstory="Oversees process and ensures smooth handoff between agents.",
    planning=True
)
