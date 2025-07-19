from crewai import Agent, ToolResponse
from tools.code_interpreter_tool import CodeInterpreterTool

code_corrector_agent = Agent(
    role="Code Corrector Agent",
    goal="Correct the identified issues and produce runnable code.",
    backstory="Polishes code to correct logic and style issues.",
    tools=[CodeInterpreterTool()]
)

def correct_code(code: str, analysis: str) -> str:
    prompt = (
        f"Original code:\n{code}\n"
        f"Analysis:\n{analysis}\n"
        "Please fix errors and output the full corrected code block."
    )
    return code_corrector_agent.run(prompt)
