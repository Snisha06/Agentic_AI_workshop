from crewai import Agent
from tools.code_interpreter_tool import CodeInterpreterTool

code_analyzer_agent = Agent(
    role="Code Analyzer Agent",
    goal="Detect syntax and logical errors in the provided Python code.",
    backstory="Experienced in reading and evaluating Python code.",
    tools=[CodeInterpreterTool()]
)

def analyze_code(code: str) -> str:
    prompt = (
        f"Here is the code:\n{code}\n"
        "1. Use the CodeInterpreter tool to run it.\n"
        "2. Identify errors or issues (syntax/runtime/logical)."
    )
    return code_analyzer_agent.run(prompt)
