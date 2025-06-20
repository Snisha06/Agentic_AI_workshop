from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.2, google_api_key=os.getenv("GOOGLE_API_KEY"))

async def plan_transition(roles, skills):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Create a 6-month role transition roadmap."),
        ("user", f"Roles: {roles}\nCurrent Skills: {skills}")
    ])
    res = await llm.ainvoke(prompt.format_messages())
    return res.content
