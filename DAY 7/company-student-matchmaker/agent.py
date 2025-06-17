import json, os, re
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

def clean_json_response(response_text):
    try:
        if not response_text or not response_text.strip():
            return []
        if response_text.startswith("```"):
            lines = response_text.strip().split("\n")
            response_text = "\n".join([line for line in lines if not line.startswith("```")])
        return json.loads(response_text)
    except json.JSONDecodeError:
        match = re.search(r"(\[.*\]|\{.*\})", response_text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(1))
            except:
                pass
        return []

def analyze_candidate_profiles(students):
    template = PromptTemplate.from_template("""
You are a candidate profile analyzer.
Analyze these students and return this structure:
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
    response = llm.invoke(prompt).content
    return clean_json_response(response)

def compute_fit_scores(analyzed_students, company_prefs):
    template = PromptTemplate.from_template("""
You're a fit scoring agent.
Compare each student to company preferences and give a score (0–100).
Return top matches:
[
  {{
    "name": "Student Name",
    "score": 85,
    "match_reason": "Relevant certifications and interests match FinTech"
  }}
]

CANDIDATES: {students}
PREFERENCES: {prefs}
""")
    prompt = template.format(
        students=json.dumps(analyzed_students, indent=2),
        prefs=json.dumps(company_prefs, indent=2)
    )
    response = llm.invoke(prompt).content
    return clean_json_response(response)
