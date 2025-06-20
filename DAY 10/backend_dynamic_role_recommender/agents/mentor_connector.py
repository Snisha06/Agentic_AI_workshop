from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.2, google_api_key=os.getenv("GOOGLE_API_KEY"))

async def connect_mentor(roles):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Connect users to mentors or simulated advisors based on roles."),
        ("user", f"Roles: {roles}")
    ])
    res = await llm.ainvoke(prompt.format_messages())
    return res.content
