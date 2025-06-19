import os, json, re
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

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

def compute_fit_scores(analyzed_students, company_prefs):
    if not company_prefs or not analyzed_students:
        return [{"name": analyzed_students[0]["name"], "score": 0, "match_reason": "Missing preferences or student data"}]

    template = PromptTemplate.from_template("""You're a fit scoring agent.
Compare each student to the company preferences and assign a score (0–100).
Return top matches:
[
  {{
    "name": "Student Name",
    "score": 85,
    "match_reason": "Relevant certifications and interests match FinTech"
  }}
]

CANDIDATES: {students}
PREFERENCES: {prefs}""")

    prompt = template.format(
        students=json.dumps(analyzed_students, indent=2),
        prefs=json.dumps(company_prefs, indent=2)
    )
    return clean_json_response(llm.invoke(prompt).content)
