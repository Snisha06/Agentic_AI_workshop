# tools.py
import os
import PyPDF2
from langchain import OpenAI
from langchain.tools import tool

# Initialize LLM
llm = OpenAI(temperature=0)

@tool
def summarize_text(text: str) -> str:
    """
    Summarize the provided text into concise bullet points.
    """
    prompt = (
        "Summarize the following text into 3-5 concise bullet points:\n\n" + text
    )
    result = llm(prompt)
    return result

@tool
def generate_quiz(summary: str) -> str:
    """
    Generate 3 multiple-choice questions (with 4 options each) based on the summary.
    """
    prompt = (
        "Based on the following summary, create 3 multiple-choice questions.\n"
        "Each question should have options a), b), c), d) and indicate the correct answer.\n\n"
        + summary
    )
    result = llm(prompt)
    return result

def extract_pdf_text(pdf_path: str) -> str:
    """
    Extract all text from a PDF file.
    """
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text
