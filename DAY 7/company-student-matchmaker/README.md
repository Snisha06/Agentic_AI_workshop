# 🎯 AI-Powered Company–Student Matchmaker

This project is an intelligent shortlisting assistant built using **LangChain** and **Gemini (Google Generative AI)** to help recruiters identify best-fit candidates efficiently by analyzing student resumes, job role preferences, and dynamic fit scoring.

---

## 🚀 Goal

> Build an intelligent shortlisting assistant that helps recruiters identify best-fit candidates efficiently.

---

## 🧠 Agents Used

1. **Candidate Profile Analyzer Agent**  
   Extracts skills, certifications, interests, and behavioral signals from student profiles.

2. **Company Preference Modeling Agent (RAG-Enabled)**  
   Uses **Retrieval-Augmented Generation (RAG)** to extract job-specific preferences like required skills, diversity goals, and soft skill expectations.

3. **Fit Scoring & Ranking Agent**  
   Computes fit scores by comparing candidate profiles to role criteria and ranks them accordingly.

4. **Dynamic Shortlist Generator Agent**  
   Continuously updates the top shortlist as students gain new skills or certifications.

---

## 📄 Data Used

- `students.json` — Contains candidate profiles with skills, interests, and certifications.
- `roles.json` — Contains job roles with required skills and preferred industries.
- Resume PDFs (to be connected for deeper RAG-based profile extraction).

---

## 📦 Requirements

langchain
google-generativeai
streamlit
python-dotenv
langchain-community
langchain-google-genai
tqdm
pydantic
PyMuPDF

## 📄 Upload Resume and Match

1. Select a role from dropdown
2. Upload a resume (PDF format)
3. Click **Analyze & Match**
