# 🔎 Web Research Agent using ReAct Pattern

This project implements a ReAct-based AI agent capable of answering research questions using real-time web search.

## ✨ Features

- Built using LangChain and OpenAI
- Uses ReAct (Reason + Act) loop for intelligent reasoning
- Integrates Tavily API for real-time search

## 📂 Project Structure

- `agents/research_agent.py` – Runs the ReAct agent
- `tools/tavily_tool.py` – Tavily web search tool
- `main.py` – Input interface for queries
- `.env` – API key configuration

## 🧪 Example Usage

```bash
$ python main.py
Enter your research question: What are the latest trends in generative AI?
```
