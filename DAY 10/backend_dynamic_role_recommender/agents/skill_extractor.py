from langchain_core.runnables import RunnableLambda
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from utils.resume_parser import parse_resume
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

async def _extract_skills_fn(inputs):
    resume = inputs["resume"]
    github = inputs["github"]
    linkedin = inputs["linkedin"]

    resume_bytes = await resume.read()
    resume.file.seek(0)
    parsed_resume = parse_resume(resume_bytes)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "Extract technical, soft, and domain-specific skills."),
        ("user", f"Resume:\n{parsed_resume}\nGitHub: {github}\nLinkedIn: {linkedin}")
    ])
    response = await llm.ainvoke(prompt.format_messages())

    return {
        "resume": resume,
        "github": github,
        "linkedin": linkedin,
        "quiz": inputs.get("quiz", ""),
        "skills": response.content
    }

extract_skills = RunnableLambda(_extract_skills_fn)
