import os
from dotenv import load_dotenv
from crewai import Crew
from tasks import analysis_task, correction_task
from managers.code_input import TEST_CODE

load_dotenv()

def main():
    print("=== Automated Code Debugging Assistant ===")
    code = """
def fibonacci_iterative(n):

    if n < 0:

        return []

    elif n == 1:

        return [0]

    elif n == 2:

        return [0, 1]

    fib_sequence = [0, 1]

    for i in range(2, n):

    next_fib = fib_sequence[-1] + fib_sequence[-2]

    fib_sequence.append(next_fib)

    return fib_sequence
"""
    print("\n📥 Input Code:\n", code)
    tasks = [analysis_task, correction_task]
    crew = Crew(agents=[analysis_task.agent, correction_task.agent], tasks=tasks, planning=True, verbose=True)
    result = crew.run(inputs={"analysis_task": {"code": code}, "correction_task": {"code": code}})
    # The outputs are in chronological responses; adjust based on implementation
    analysis = result["analysis_task"]
    correction = result["correction_task"]
    print("\n🧩 Analysis Result:\n", analysis)
    print("\n✅ Corrected Code:\n", correction)

if __name__ == "__main__":
    main()
