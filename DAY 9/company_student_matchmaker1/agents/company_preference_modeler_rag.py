import os, json, re
from dotenv import load_dotenv
load_dotenv()

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

retriever = None

# ✅ Step 1: Load recruiter PDF and create vectorstore
def load_recruiter_preferences(pdf_path="data/recruiter.pdf"):
    global retriever
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)

    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("❌ GOOGLE_API_KEY not found in .env")

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=api_key
    )
    vectorstore = FAISS.from_documents(chunks, embeddings)
    retriever = vectorstore.as_retriever()

# ✅ Step 2: Extract recruiter preferences from vectorstore
def extract_company_preferences(role):
    if not retriever:
        raise ValueError("Retriever not initialized. Call load_recruiter_preferences() first.")

    prompt = PromptTemplate.from_template("""
You are a company preference extractor.
Given a job role and recruiter documents, extract preferences in this JSON format:
{{
  "required_skills": ["..."],
  "preferred_skills": ["..."],
  "diversity_focus": "...",
  "behavioral_traits": ["..."]
}}
ROLE: {role}
""")

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.2,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )

    query = prompt.format(role=role)
    response = chain.run(query)

    # ✅ Clean & parse JSON safely
    def extract_json(text):
        try:
            match = re.search(r"{.*}", text, re.DOTALL)
            if match:
                return json.loads(match.group())
        except json.JSONDecodeError as e:
            print("⚠️ JSON parsing error:", e)
        return {}

    prefs = extract_json(response)
    print("✅ Extracted Preferences:", prefs)
    return prefs
