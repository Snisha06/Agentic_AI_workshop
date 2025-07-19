class CriticAgent:
    def review(self, report: str) -> str:
        feedback = ""
        if "###" not in report:
            feedback += "Use headers to structure report.\n"
        if "Visualization" not in report:
            feedback += "Include at least one plot.\n"
        # More review checks...
        return feedback or "Report looks well-structured."
