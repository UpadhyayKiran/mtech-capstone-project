from langchain_community.vectorstores import FAISS

def create_faiss_index(chunks, embeddings):
    return FAISS.from_documents(chunks, embeddings)
