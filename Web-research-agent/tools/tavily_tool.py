from langchain.tools import TavilySearchResults
from langchain.agents import Tool
import os

tavily_tool_instance = TavilySearchResults(api_key=os.getenv("TAVILY_API_KEY"))

tavily_search_tool = Tool(
    name="Tavily Web Search",
    func=tavily_tool_instance.run,
    description="Useful for answering research questions with current, real-time information from the web."
)
