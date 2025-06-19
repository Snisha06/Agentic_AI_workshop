import os, json, re
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
            return {}
        if response_text.startswith("```"):
            lines = response_text.strip().split("\n")
            response_text = "\n".join([line for line in lines if not line.startswith("```")])
        return json.loads(response_text)
    except json.JSONDecodeError:
        match = re.search(r"(\{.*\})", response_text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(1))
            except:
                pass
        return {}

def extract_company_preferences(role):
    template = PromptTemplate.from_template("""
You're a RAG-enabled company preference extractor.
Given this role, return:
{
  "required_skills": [...],
  "preferred_skills": [...],
  "diversity_focus": "...",
  "behavioral_traits": [...]
}
ROLE: {role}
""")
    prompt = template.format(role=json.dumps(role, indent=2))
    response = llm.invoke(prompt).content
    return clean_json_response(response)
