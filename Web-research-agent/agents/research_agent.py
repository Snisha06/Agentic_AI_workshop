from langchain.agents import initialize_agent, AgentType, Tool
from langchain.chat_models import ChatOpenAI
from tools.tavily_tool import tavily_search_tool

def run_web_research_agent(query: str):
    tools = [tavily_search_tool]
    llm = ChatOpenAI(model_name="gpt-4", temperature=0)
    agent_executor = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )
    return agent_executor.run(query)
