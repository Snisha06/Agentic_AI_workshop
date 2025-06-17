import streamlit as st
import fitz  # PyMuPDF
from agent import analyze_candidate_profiles, compute_fit_scores
from rag_agent import extract_company_preferences
from utils import load_data
import json

st.set_page_config(layout="wide", page_title="📄 AI Resume Matchmaker")
st.title("🎯 Upload Resume – Company–Student Matchmaker")

roles = load_data("data/roles.json")

selected_role = st.selectbox("Select a Role", [r["role"] for r in roles])
pdf_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

def extract_text_from_pdf(uploaded_file):
    try:
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        st.error(f"❌ Failed to extract PDF: {e}")
        return None

if st.button("🔍 Analyze & Match"):
    if not pdf_file:
        st.warning("Please upload a PDF resume.")
    else:
        with st.spinner("Processing resume..."):
            resume_text = extract_text_from_pdf(pdf_file)
            if not resume_text:
                st.error("Resume text extraction failed.")
                st.stop()

            # Simulate as one-student input
            dummy_student = {"name": "Uploaded Candidate", "resume": resume_text}
            analyzed = analyze_candidate_profiles([dummy_student])
            role_data = next(r for r in roles if r["role"] == selected_role)
            prefs = extract_company_preferences(role_data)
            ranked = compute_fit_scores(analyzed, prefs)

            st.success("🎯 Match Results")
            if ranked:
                st.markdown(f"**Name:** {ranked[0]['name']}")
                st.metric("Score", f"{ranked[0]['score']}/100")
                st.markdown(f"**Reason:** {ranked[0]['match_reason']}")
            else:
                st.warning("No match found.")
