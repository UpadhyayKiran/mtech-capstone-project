def semantic_search(vectorstore, query, k=5):
    return vectorstore.similarity_search(query, k=k)
