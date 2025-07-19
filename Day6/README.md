🎓 Placement Readiness Scorer
This project is an AI-powered student evaluation tool that assesses academic and communication readiness for placement using structured inputs, a PDF resume, and a custom LangChain agent backed by Gemini 2.0 Flash.

🚀 Features
Upload student resume (PDF) and extract text.

Input academic & soft skill metrics via sliders.

Use two custom LangChain tools:

📘 Academic Scorer

💬 Soft Skills Scorer

AI-generated professional readiness report using Gemini.

Flag students for support if needed.

📁 Project Structure
bash
Copy
Edit
placement-readiness-scorer/
├── scorer_tools.py # Academic & soft skills scoring functions
├── agent.py # LangChain Agent definition
├── app.py # Streamlit frontend
├── requirements.txt # Dependencies
├── README.md # Project overview and usage
📦 Installation
Clone the repo:

bash
Copy
Edit
git clone https://github.com/your-username/placement-readiness-scorer.git
cd placement-readiness-scorer
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
requirements.txt

txt
Copy
Edit
streamlit
langchain
langchain-google-genai
pymupdf
Set your Gemini API key in agent.py:

python
Copy
Edit
llm = ChatGoogleGenerativeAI(
model="gemini-2.0-flash",
temperature=0,
google_api_key="YOUR_GOOGLE_API_KEY"
)
▶️ Run the App
bash
Copy
Edit
streamlit run app.py
🧠 How it Works
Frontend: Built using Streamlit for user-friendly input and PDF upload.

Backend: Uses LangChain AgentExecutor with Gemini 2.0 to:

Call academic_score_tool and soft_skills_tool.

Analyze resume for skill signals.

Output a final structured placement report.

📝 Example Output
markdown
Copy
Edit
Academic readiness: 78.5%. Analysis: Good attendance; Adequate assignment performance; Good test performance

Communication readiness: 73.0% (+3% resume bonus). Analysis: Adequate interview skills; Bio needs minor improvements; Good faculty feedback; Strong technical skills evident; Relevant work experience

Recommendations:

- Attend resume building workshops
- Improve communication via mock interviews
- Consider certification in industry tools

Status: Needs Improvement
📌 TODO
Add student database backend (e.g., Firebase or Supabase)

Add option to export reports as PDF

Enable batch uploads for multiple students
