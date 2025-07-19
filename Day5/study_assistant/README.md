📘 Learning Companion: PDF Summarizer & Quiz Builder
An easy-to-use Streamlit app that helps you:

Upload and analyze study material (PDF)

Summarize the key content using an LLM

Create a quick quiz based on the summary

Take the quiz in an interactive interface

⚙️ What It Does
Extracts text from PDFs using PyPDF2

Summarizes content using a language model (via LangChain)

Generates multiple-choice questions (MCQs)

Offers a responsive quiz-taking experience with optional score tracking

🧰 Getting Started
Step 1: Clone This Repository
bash
Copy
Edit
git clone <repository-url>
cd Day5
Step 2: Set Up Your Python Environment
Option A: Conda

bash
Copy
Edit
conda create -n study-assistant python=3.10
conda activate study-assistant
Option B: Using venv

bash
Copy
Edit
python -m venv venv

# On macOS/Linux

source venv/bin/activate

# On Windows

venv\Scripts\activate
Step 3: Install Required Libraries
bash
Copy
Edit
pip install -r requirements.txt
Step 4: Configure API Key
Create a .env file in your project root.

Add your Groq API key like this:

ini
Copy
Edit
GROQ_API_KEY=your_groq_api_key_here
▶️ How to Launch
bash
Copy
Edit
streamlit run app.py
🔍 How to Use
Launch the app via the command above.

Upload your study material in PDF format (e.g., Genai.pdf).

Click "Summarize" to get the key points.

Click "Generate Quiz" to build multiple-choice questions.

Take the quiz and get instant feedback.

📦 What's Needed
Ensure your requirements.txt includes:

nginx
Copy
Edit
streamlit
PyPDF2
langchain
langchain-groq
python-dotenv
❓ Common Issues & Fixes
Make sure your Groq API key is present in .env.

Double-check that all dependencies are properly installed.

Ensure the uploaded PDF is readable and not corrupted.

Recommended Python version: 3.10
