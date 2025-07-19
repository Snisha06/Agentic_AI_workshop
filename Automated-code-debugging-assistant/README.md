# 🤖 Automated Code Debugging Assistant

A CrewAI-powered assistant to analyze and correct Python code using a two-agent workflow.

## 🧠 Agents

- **Manager Agent**: Coordinates the workflow (planning mode enabled).
- **Code Analyzer Agent**: Runs the code using `CodeInterpreterTool` and reports syntax/runtime issues.
- **Code Corrector Agent**: Fixes the code and provides the corrected version.
