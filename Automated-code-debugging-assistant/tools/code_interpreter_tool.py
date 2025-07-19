from crewai_tools import BaseTool
import subprocess, tempfile, os

class CodeInterpreterTool(BaseTool):
    name = "CodeInterpreter"
    description = "Runs Python code and returns syntax or runtime outputs/errors."

    def _run(self, code: str) -> str:
        try:
            with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
                f.write(code)
                temp_path = f.name
            result = subprocess.run(
                ["python", temp_path],
                capture_output=True,
                text=True,
                timeout=5
            )
            os.remove(temp_path)
            if result.stderr:
                return "ERROR:\n" + result.stderr
            return result.stdout or "Ran successfully with no output."
        except Exception as e:
            return f"Tool exception: {e}"
