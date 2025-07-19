# main.py
import os
from dotenv import load_dotenv
from langchain import OpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import get_weather, get_attractions

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
if not openai_key:
    raise ValueError("OPENAI_API_KEY not set in .env")

llm = OpenAI(model="gpt-3.5-turbo", temperature=0)
tools = [get_weather, get_attractions]

agent = create_tool_calling_agent(llm=llm, tools=tools)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

def main():
    print("🧭 Travel Assistant AI — get weather + attractions!\nType 'exit' to quit.")
    while True:
        city = input("Enter destination city: ")
        if city.lower() in ("exit", "quit"):
            break

        prompt = (
            f"Tell me the current weather in {city}, "
            f"and list the top tourist attractions there."
        )
        result = executor.invoke({"input": prompt})
        print("\n" + result.get("output", "No response.") + "\n")

if __name__ == "__main__":
    main()
