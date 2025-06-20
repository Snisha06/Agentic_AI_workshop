import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

async def retrieve_roles(skills, aptitudes):
    """Retrieve matching roles based on skills and aptitudes"""
    try:
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a career counselor who matches skills and aptitudes to suitable job roles."),
            ("user", f"Given skills: {skills} and aptitudes: {aptitudes}, suggest 5 transferable job roles with explanations.")
        ])
        
        response = await llm.ainvoke(prompt.format_messages())
        return response.content
    except Exception as e:
        print(f"Error in retrieve_roles: {e}")
        return {"error": str(e)}

