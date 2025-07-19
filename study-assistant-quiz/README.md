# Study Assistant for Quiz Question Generation

A lightweight study assistant built with **LangChain** that:

1. 📄 Extracts text from a PDF
2. 🔹 Summarizes the content into concise bullet points
3. 📝 Generates 3 multiple-choice quiz questions based on the summary

---

## 🧩 Project Structure

study_assistant_quiz/
├── main.py # CLI interface
├── tools.py # Summarizer and quiz generator tools
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## ⚙️ Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/study_assistant_quiz.git
   cd study_assistant_quiz
   Install dependencies:
   ```
   python3 -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   pip install -r requirements.txt

Add your OpenAI API key:
OPENAI_API_KEY=your_key_here
