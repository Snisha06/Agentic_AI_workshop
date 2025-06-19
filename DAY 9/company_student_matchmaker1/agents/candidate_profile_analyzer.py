import os, json, re
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

def clean_json_response(text):
    try:
        return json.loads(re.sub(r"```json|```", "", text.strip()))
    except:
        return []

def analyze_candidate_profiles(students):
    template = PromptTemplate.from_template("""
You are a candidate profile analyzer.
Analyze these students and return:
[
  {{
    "name": "Student Name",
    "skills": [...],
    "certifications": [...],
    "interests": [...],
    "signals": ["Team player", "Open source contributor"]
  }}
]
STUDENTS: {students}
""")
    prompt = template.format(students=json.dumps(students, indent=2))
    return clean_json_response(llm.invoke(prompt).content)
