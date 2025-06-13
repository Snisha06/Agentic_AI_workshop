import os
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain_google_genai import GoogleGenerativeAI
from .retriever import load_vectorstore

load_dotenv()

llm = GoogleGenerativeAI(
    model="gemini-1.5-flash",  # or "gemini-1.5-pro"
    api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.2
)

vectorstore = load_vectorstore()
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

def answer_question(query: str):
    result = qa_chain({"query": query})
    answer = result["result"]
    sources = [doc.metadata['source'] for doc in result["source_documents"]]
    return answer, sources
