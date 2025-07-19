from crewai import Agent
from models.schemas import ProjectIdea

project_agent = Agent(
    role="Project Idea Agent",
    goal="Recommend practical project ideas by expertise level",
    backstory="Experience mentoring tech learners through hands-on projects",
    tools=[]
)
