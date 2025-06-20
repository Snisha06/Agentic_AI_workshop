import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.2, google_api_key=os.getenv("GOOGLE_API_KEY"))

async def map_aptitudes(quiz, github):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Score aptitudes from quiz text and GitHub projects on a scale of 1-100."),
        ("user", f"Quiz: {quiz}\nGitHub: {github}")
    ])
    res = await llm.ainvoke(prompt.format_messages())
    return res.content
