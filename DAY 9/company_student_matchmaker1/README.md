# 🎯 AI-Powered Company–Student Matchmaker

This intelligent shortlisting assistant matches student resumes to recruiter expectations using **RAG (Retrieval-Augmented Generation)**, **Gemini (Google Generative AI)**, and **LangGraph**.

---

## 🚀 Project Goal

Help recruiters identify the **best-fit candidates** efficiently by analyzing uploaded resumes and dynamically extracting company hiring criteria from recruiter documents (PDFs).

---

## 🧠 Core Agents

| Agent                                           | Description                                                                                                        |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| 🧾 **Candidate Profile Analyzer**               | Extracts skills, certifications, interests, and soft signals from uploaded student resumes.                        |
| 🏢 **Company Preference Modeler (RAG-Enabled)** | Uses Gemini + vector DB (FAISS) to retrieve and extract hiring expectations directly from recruiter PDF documents. |
| 📊 **Fit Scoring Agent**                        | Compares each candidate’s profile against company expectations and computes a personalized fit score (0–100).      |
| ♻️ **LangGraph Workflow**                       | Modular, reactive state flow that connects each agent (Analyze → Retrieve → Score) in order.                       |

---

## 📄 Input Data

- ✅ **Resume Upload:** Accepts **PDF resumes** from students.
- ✅ **Recruiter Preferences:** A **PDF file** containing job role expectations like required skills, diversity goals, etc.

---

## 📂 File Structure

.
├── agents/
│ ├── candidate_profile_analyzer.py
│ ├── company_preference_modeler_rag.py
│ └── fit_scoring_agent.py
├── data/
│ └── recruiter.pdf ← RAG input for hiring expectations
├── streamlit_app.py ← UI to upload resume and get match
└── README.md

---

## 🧠 Key Technologies Used

- **LangChain** — Core LLM orchestration
- **Gemini 1.5 Flash (Google Generative AI)** — Used for all LLM tasks
- **FAISS Vector DB** — Stores recruiter PDF chunks for semantic RAG retrieval
- **LangGraph** — Used for structuring the multi-agent workflow
- **PyMuPDF** — Extracts text from uploaded student PDF resumes
- **Streamlit** — Interactive user interface for matching

---

## 💡 How It Works

1. **Upload Resume (PDF)** via Streamlit interface.
2. **Select Job Role** for which matching is needed.
3. **Company Preferences** are extracted using RAG from `recruiter.pdf`.
4. **Fit Score** is calculated using Gemini.
5. **Match Results** are shown instantly with score and reasons.

---

## ✅ Requirements

langchain
langchain-google-genai
google-generativeai
streamlit
python-dotenv
PyMuPDF
langgraph
tqdm
pydantic
