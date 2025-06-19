import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import fitz
from agents.candidate_profile_analyzer import analyze_candidate_profiles
from agents.company_preference_modeler_rag import extract_company_preferences, load_recruiter_preferences
from agents.fit_scoring_agent import compute_fit_scores

st.set_page_config(page_title="AI Resume Matchmaker", layout="wide")
st.title("📄 AI-Powered Company–Student Matchmaker")

st.subheader("Match Student Resume to Company Preferences")
st.caption("Upload a student's resume and specify a job role to see how well they fit.")
st.divider()

job_role = st.text_input("Enter Job Role Title", "Data Analyst")
pdf_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

load_recruiter_preferences()  # ✅ Load once

def extract_text_from_pdf(uploaded_file):
    try:
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        return "".join(page.get_text() for page in doc)
    except Exception as e:
        st.error(f"Failed to extract text: {e}")
        return None

if st.button("🔍 Analyze & Match"):
    if not pdf_file:
        st.warning("Please upload a resume PDF.")
    else:
        with st.spinner("Processing resume..."):
            resume_text = extract_text_from_pdf(pdf_file)
            student_data = [{"name": "Candidate", "resume": resume_text}]
            analyzed = analyze_candidate_profiles(student_data)

            st.write("📑 Analyzed Student Data", analyzed)

            preferences = extract_company_preferences(job_role)
            st.write("🏢 Recruiter Preferences", preferences)

            ranked = compute_fit_scores(analyzed, preferences)

            st.success("✅ Match Results")
            if ranked:
                st.write(f"**Name:** {ranked[0]['name']}")
                st.metric("Score", f"{ranked[0]['score']}/100")
                st.markdown(f"**Reason:** {ranked[0]['match_reason']}")
            else:
                st.warning("❌ No suitable match found.")
