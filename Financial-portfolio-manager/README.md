# 💼 Financial Portfolio Manager

A conversational AI system that helps users manage their investments smartly, using multi-agent collaboration and dynamic workflows via StateFlow.

## 🎯 What It Does

This system enables:

- Portfolio analysis
- Personalized growth/value investment recommendations
- A detailed investment report

## 🧠 Key Agents

1. **User Proxy Agent**  
   Initiates the conversation and forwards user intent.

2. **Group Chat Manager**  
   Coordinates other agents and routes workflow dynamically.

3. **Portfolio Analysis Agent**  
   Analyzes the user's financial data and classifies investment needs.

4. **Growth Investment Agent**  
   Suggests aggressive high-growth options.

5. **Value Investment Agent**  
   Suggests stable, long-term assets.

6. **Investment Advisor Agent**  
   Generates the final investment recommendation report.

## ⚙️ How to Run

### 1. Clone the Repo

2. Create a Virtual Environment
   bash
   Copy
   Edit
   python -m venv venv
   source venv/bin/activate # Linux/Mac
   venv\Scripts\activate # Windows
3. Install Requirements
   bash
   Copy
   Edit
   pip install -r requirements.txt
4. Run the Main Script
   bash
   Copy
   Edit
   python main.py
