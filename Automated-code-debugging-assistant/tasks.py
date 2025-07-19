from crewai import Task
from agents.code_analyzer_agent import analyze_code, code_analyzer_agent
from agents.code_corrector_agent import correct_code, code_corrector_agent

analysis_task = Task(
    description="Analyze the Python code for syntax and logical errors.",
    expected_output="List of errors or issues found in the code.",
    agent=code_analyzer_agent
)

correction_task = Task(
    description="Produce corrected version of the Python code.",
    expected_output="Corrected full Python code.",
    agent=code_corrector_agent
)
