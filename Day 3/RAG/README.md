# RAG QA System – AI Research Papers (Gemini)

## 📌 Overview

A Retrieval-Augmented Generation (RAG) QA system that uses **Google Gemini 1.5** to answer questions from AI research papers. It uses **FAISS** for retrieval, **HuggingFace embeddings**, and a **Streamlit UI** for interaction.

## 🚀 Features

- Ask questions about uploaded research PDFs
- Google Gemini + Langchain integration
- FAISS-based vector search
- PDF chunking and embedding
- Streamlit-based web interface

## 🛠️ Setup

1. **Clone & Navigate**
   ```bash
   git clone <repo-url>
   cd Day\ 3/RAG_QA_System_Gemini
   ```

# Install Requirements

pip install -r requirements.txt

# .env File

Added API key

## Add PDFs

Place PDF files in the data/ folder.

## Run App

streamlit run app.py

## STRUCTURE

app.py # Streamlit UI
main.py # (Optional) Check numpy version
requirements.txt # Dependencies
data/ # Place PDFs here
vectorstore/ # FAISS index storage
.env # API key here
src/
├── preprocess.py # PDF loading, chunking, embeddings
├── retriever.py # Loads/creates FAISS vectorstore
└── rag_pipeline.py # QA pipeline using Gemini + retriever

## How It Works

Loads and chunks PDFs → embeds them → stores in FAISS
On question: retrieves top docs → Gemini generates answer
UI displays answer + sources

## DEPENDENCIES

torch
langchain
langchain-community
faiss-cpu
sentence-transformers
streamlit
google-generativeai
langchain-google-genai
python-dotenv
pypdf
numpy==1.26.4
