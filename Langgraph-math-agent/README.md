# LangGraph Mathematical Agent

A conversational agent built with **LangGraph** that handles both general Q&A (via LLM) and math queries (via custom functions).

---

## 🤖 How It Works

1. **Custom Math Tools**:

   - `plus`, `subtract`, `multiply`, `divide` functions implemented with proper edge-case handling.

2. **LLM Integration**:

   - Uses OpenAI's GPT (or swap in Gemini/Groq) for general questions.

3. **LangGraph Setup**:

   - Graph with two nodes:
     - **chat_llm**: performs general Q&A
     - **math_tool**: processes math queries
   - Edge with `is_math_query()` routes math requests.

4. **Execution Flow**:
   - Every input is passed to `chat_llm`.
   - If `is_math_query` detects a math operation, response is forwarded to `math_tool`.
   - Otherwise, the LLM reply is returned directly.

---

## ⚙️ Setup Instructions

```bash

cd langgraph_math_agent
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Example Queries
vbnet
Copy
Edit
You: What is the capital of France?
Agent: Paris.

You: 5 plus 3
Agent: 8

You: 12 divided by 4
Agent: 3.0

You: Tell me about reinforcement learning.
Agent: ...LLM-generated answer...
