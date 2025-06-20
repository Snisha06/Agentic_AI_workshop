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


# role_recommender_cross_training_planner

# AI Career Profile Analyzer - Frontend

This is the frontend of the AI Career Profile Analyzer application, built with Flutter. It provides an intuitive user interface that allows users to upload their resume, submit GitHub and LinkedIn URLs, and view AI-driven analysis on skills, aptitudes, and career recommendations.

---

## Features

- Upload `.pdf`, `.doc`, or `.docx` resumes
- Input GitHub and LinkedIn profile URLs
- (Optional) Provide aptitude quiz results
- Send data to backend via HTTP Multipart Request
- Display AI-processed insights including:
  - Skills Extracted
  - Aptitudes Mapped
  - Recommended Roles
  - Transition Roadmap
  - Mentor Connections

---

## Technologies Used

- **Flutter**: UI development framework
- **Dart**: Programming language
- **http**: For making multipart API requests
- **file_selector**: For cross-platform file picking
- **ExpansionTile, Cards, Material UI**: UI rendering
- **SelectableText & JSON encoder**: Result presentation

---

## Folder Structure

lib/
├── main.dart
├── screens/
home_screen.dart
│ └── upload_screen.dart
├── widgets/
│ └── result_scaffold.dart
│ └── skills_extracted_screen.dart
│ └── aptitudes_mapped_screen.dart
│ └── roadmap_screen.dart
│ └── mentors_screen.dart

---

## How to Run

1. Ensure Flutter SDK is installed: [Flutter installation guide](https://flutter.dev/docs/get-started/install)
2. Clone the repository:

   ```bash
   git clone https://github.com/your-username/frontend-ai-analyzer.git
   cd frontend-ai-analyzer
   ```

   Got Dependencies:
   flutter pub get
   Run:
   flutter run

   Configuration:
   static const String baseUrl = 'http://<my-backend-ip>:8000';


   Demo Video Link:- https://drive.google.com/file/d/1_PfGlfBMvP-6xMjwXuWPRE7tJkOcQHHz/view?usp=sharing
   Project Architecture :- https://drive.google.com/file/d/1m4dakUm8rf0eNgN0aDqWLlf51RaRJwdq/view?usp=sharing
