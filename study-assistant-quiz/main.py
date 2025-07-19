# main.py
import os
from dotenv import load_dotenv
from tools import extract_pdf_text, summarize_text, generate_quiz
from langchain.agents import create_tool_calling_agent, AgentExecutor

load_dotenv()
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not set in .env")

def main():
    print("📚 Study Assistant — Summarize and Quiz Generator\n")

    pdf_path = input("Enter path to your PDF study material: ").strip()
    if not os.path.isfile(pdf_path):
        print("File not found.")
        return

    print("\n📄 Extracting text from PDF...")
    raw = extract_pdf_text(pdf_path)

    executor = AgentExecutor.create_from_tools(
        tools=[summarize_text, generate_quiz]
    )

    print("\n📝 Summarizing content...")
    summary = executor.invoke({"func": "summarize_text", "input": raw}).get("output")
    print("\n✅ Summary:\n", summary)

    print("\n✏️ Generating quiz questions...")
    quiz = executor.invoke({"func": "generate_quiz", "input": summary}).get("output")
    print("\n✅ Quiz Questions:\n", quiz)

if __name__ == "__main__":
    main()
