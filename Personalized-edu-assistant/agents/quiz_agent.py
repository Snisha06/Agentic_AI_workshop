from crewai import Agent
from models.schemas import QuizQuestion
import os

OPENAI = os.getenv("OPENAI_API_KEY")

quiz_agent = Agent(
    role="Quiz Creator Agent",
    goal="Generate a 5-question quiz for users on the topic",
    backstory="Skilled in creating assessments that test comprehension."
)

def run_quiz_agent(topic: str) -> QuizQuestion:
    prompt = (
        f"Generate a quiz with 5 multiple-choice questions about {topic}. "
        "Return JSON list with question, options, and correct answer."
    )
    resp = quiz_agent.run(prompt)
    # Expect JSON list; parse safely
    import json
    data = json.loads(resp)
    questions = [QuizQuestion(**q) for q in data]
    return questions
