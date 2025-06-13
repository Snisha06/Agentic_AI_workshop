import os
from langchain_community.vectorstores import FAISS
from .preprocess import get_chunked_docs, embeddings

VECTOR_DB_PATH = "vectorstore/index"

def load_vectorstore():
    if os.path.exists(f"{VECTOR_DB_PATH}/index.faiss"):
        return FAISS.load_local(VECTOR_DB_PATH, embeddings, allow_dangerous_deserialization=True)
    docs = get_chunked_docs()
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local(VECTOR_DB_PATH)
    return vectorstore
