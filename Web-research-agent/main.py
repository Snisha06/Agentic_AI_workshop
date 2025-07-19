import os
from agents.research_agent import run_web_research_agent
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    user_query = input("Enter your research question: ")
    result = run_web_research_agent(user_query)
    print("\n📄 Final Answer:\n", result)
