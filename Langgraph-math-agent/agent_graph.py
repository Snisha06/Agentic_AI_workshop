
from langgraph import Graph, Node, Edge
from langchain import OpenAI
from math_tools import plus, subtract, multiply, divide
import re

# LLM initialization (adjust to Gemini or Groq if preferred)
llm = OpenAI(temperature=0)

def is_math_query(text: str) -> bool:
    return bool(re.search(r'\b(plus|minus|subtract|times|multiplied|divided|divide)\b', text))

def math_router(text: str):
    pattern = r'(-?\d+\.?\d*)\s*(plus|\+|minus|subtract|\-|times|\*|multiplied|divided|/|divide)\s*(-?\d+\.?\d*)'
    match = re.search(pattern, text)
    if not match:
        return "Error: couldn't parse math expression"

    a, op, b = float(match.group(1)), match.group(2), float(match.group(3))
    if op in ['plus', '+']:
        return plus(a, b)
    if op in ['minus', 'subtract', '-']:
        return subtract(a, b)
    if op in ['times', '*', 'multiplied']:
        return multiply(a, b)
    if op in ['divided', '/', 'divide']:
        return divide(a, b)
    return "Operation not supported"

# Build LangGraph
graph = Graph()

chat_node = Node(
    name="chat_llm",
    func=lambda query, state: llm(query),
    stream=False
)

math_node = Node(
    name="math_tool",
    func=lambda query, state: math_router(query),
    stream=False
)

graph.add_node(chat_node)
graph.add_node(math_node)

# Conditional edge: math queries go to math_node
graph.add_edge(
    Edge(source=chat_node, target=math_node, condition=is_math_query)
)

# Fallback: all queries start at chat_llm, if non-math, return LLM output
