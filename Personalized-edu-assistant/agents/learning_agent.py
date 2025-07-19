from crewai import Agent
import requests
import os
from models.schemas import LearningMaterial

OPENAI = os.getenv("OPENAI_API_KEY")
SERPER = os.getenv("SERPER_API_KEY")

learning_agent = Agent(
    role="Learning Material Agent",
    goal="Curate learning materials based on user topics",
    backstory="Deep knowledge of educational content curation",
)

def run_learning_agent(topic: str) -> LearningMaterial:
    # Use Serper search for articles
    sr = requests.get(
        "https://google.serper.dev/search",
        headers={"X-API-KEY": SERPER},
        params={"q": topic + " tutorial", "num": 3}
    ).json()
    articles = [item["link"] for item in sr.get("organic", [])][:3]

    response = learning_agent.run(f"Provide 3 video links about {topic}")
    videos = response.split("\n")[:3]
    exercises = [f"{topic} exercise {i+1}" for i in range(3)]

    return LearningMaterial(
        topic=topic,
        videos=videos,
        articles=articles,
        exercises=exercises
    )
