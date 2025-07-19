# main.py
import os
from dotenv import load_dotenv
from crewai import Crew
from tasks import analyze_task, optimize_task

load_dotenv()

def main():
    print("📦 Logistics Optimization CrewAI\n")
    products = input("Enter product names separated by commas: ").split(',')

    crew = Crew(
        agents=[analyze_task.agent, optimize_task.agent],
        tasks=[analyze_task, optimize_task],
        process="sequential",
        verbose=True
    )

    result = crew.run(inputs={
        "analyze_task": {"products": products},
        "optimize_task": {"products": products}
    })

    print("\n🎯 Final Optimization Strategy:")
    print(result["optimize_task"])

if __name__ == "__main__":
    main()
