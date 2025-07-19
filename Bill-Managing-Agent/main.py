
from crewai import Crew
from tasks import task_user, task_processing, task_summary

def main():
    crew = Crew(
        agents=[task_user.agent, task_processing.agent, task_summary.agent],
        tasks=[task_user, task_processing, task_summary],
        process="sequential",
        verbose=True
    )
    final_results = crew.run()
    print("\n=== Final Spending Summary ===\n")
    print(final_results)

if __name__ == "__main__":
    main()
