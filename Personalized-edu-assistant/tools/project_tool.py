from crewai_tools import BaseTool

class ProjectSuggestionTool(BaseTool):
    name = "project_suggester"
    description = "Generate tailored project ideas."

    def _run(self, topic: str, level: str):
        if level == "beginner":
            return [f"{topic} Intro App"]
        if level == "intermediate":
            return [f"{topic} Dashboard"]
        if level == "advanced":
            return [f"{topic} End-to-end Platform"]
        return [f"{topic} Project Idea"]
