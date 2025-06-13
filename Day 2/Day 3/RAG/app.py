import streamlit as st
from src.rag_pipeline import answer_question

st.title("🔍 AI Research Paper QA with RAG")

query = st.text_input("Ask a question about the research papers")

if query:
    with st.spinner("Retrieving answer..."):
        answer, sources = answer_question(query)
        st.write("### 📌 Answer")
        st.write(answer)
        # st.write("### 📖 Sources")
        # for src in set(sources):
        #     st.write(f"- {src}")
