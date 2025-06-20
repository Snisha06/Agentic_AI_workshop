# AI Career Profile Analyzer - Backend

This is the backend service of the **AI Career Profile Analyzer**. It accepts resume files and public profile URLs to generate AI-driven insights such as extracted skills, mapped aptitudes, recommended roles, career transition roadmaps, and mentor connections.

---

## 🔧 Technologies Used

- **FastAPI** – Modern Python web framework for building APIs
- **Uvicorn** – ASGI server for FastAPI
- **LangChain & LangGraph** – Agentic AI framework for orchestrating skill extraction and recommendation workflows
- **FAISS** – Vector similarity search for semantic retrieval
- **OpenAI API** – For embedding generation and reasoning
- **pdfminer.six** – PDF text extraction
- **GitPython** – GitHub repository scraping
- **BeautifulSoup4** – HTML parsing from LinkedIn or other sources
- **Tavily** – Web-enhanced search integration (optional)
- **Dotenv** – Secure management of API keys and configurations

---

## 📁 Folder Structure

BACKEND_DYNAMIC_ROLE_RECOMMENDER
├── agents/
│ ├── init.py
│ ├── aptitude_mapper.py
│ ├── mentor_connector.py
│ ├── role_retreiver.py
│ ├── skill_extractor.py
│ └── transition_planner.py
│
├── crud/
│ └── student_crud.py
│
├── database/
│ └── session.py
│
├── models/
│ └── student.py
│
├── utils/
│ ├── init.py
│ ├── rag_faiss.py
│ └── resume_parser.py
│
├── .env
├── main.py
├── requirements.txt
└── student_profiles.db

---

## 📦 Requirements

Install all dependencies listed below using `pip install -r requirements.txt`:

```txt
fastapi
uvicorn
python-multipart
pydantic
openai
langchain
langgraph
faiss-cpu
pdfminer.six
gitpython
beautifulsoup4
httpx
tavily-python
python-dotenv
langchain-community

```

How to run
git clone https://github.com/your-org/backend-career-analyzer.git
cd backend-career-analyzer

Set up environment variables

Create a .env file:
GOOGLE_API_KEY = key

INstall dependencies
python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate
pip install -r requirements.txt

RUN THE SERVER
uvicorn main:app --reload --host 0.0.0.0 --port 8000

🔌 API Endpoint
POST /process-profile
Request
Content-Type: multipart/form-data

Form Fields

resume: File (.pdf, .docx)

github: String (GitHub profile URL)

linkedin: String (LinkedIn profile URL)

quiz: String (optional aptitude quiz results)

DATABASE:

SQLite database: student_profiles.db

ORM Models in: models/student.py

Insertion logic in: crud/student_crud.py

Connection via: database/session.py

Health Check:

GET /health
→ { "status": "healthy", "service": "AI Career Profile Analyzer" }
