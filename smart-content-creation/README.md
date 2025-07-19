# 📘 Smart Content Creation – Agentic Simulation

## 🎯 Objective

This project simulates a two-agent system:

- A **Content Creator Agent** drafts content on _Generative AI_.
- A **Content Critic Agent** reviews and provides feedback for improvements.

It uses a **reflection-based agentic pattern** with iterative revisions to improve the content and present a polished final draft in **markdown format**.

---

## 🧠 Agents Used

1. **Content Creator Agent**

   - Role: Drafts educational content on Generative AI.
   - Behavior: Revises the draft based on critic's feedback.

2. **Content Critic Agent**
   - Role: Evaluates drafts.
   - Feedback: Focuses on clarity, technical accuracy, and structure.

---

## 🗂️ Project Structure

smart_content_creation/
├── agents/
│ ├── content_creator.py
│ └── content_critic.py
├── main.py
├── conversation_flow.py
├── README.md
├── requirements.txt
└── .env
