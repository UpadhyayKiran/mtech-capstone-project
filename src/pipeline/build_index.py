from utils import load_json_documents
from chunker import chunk_documents
from embedder import get_embeddings
from faiss_index import create_faiss_index
from store import semantic_search

# Path
input_dir = "your_json_folder"
index_path = "faiss_index"

# 1. Load documents
print("Loading documents...")
documents = load_json_documents(input_dir)
print(f"Loaded {len(documents)} documents")

# 2. Chunk
print("Chunking...")
chunks = chunk_documents(documents)
print(f"Created {len(chunks)} chunks")

# 3. Embeddings
print("Loading embeddings...")
embeddings = get_embeddings()

# 4. Create FAISS index
print("Building FAISS index...")
vectorstore = create_faiss_index(chunks, embeddings)

# 5. Save index
print("Saving index...")
vectorstore.save_local(index_path)

print("Index built successfully!")

query = """which kinetic parameters and experimentally measurable cytokine levels and T-cell populations were most important for segregating response phe- notypes?"""

print("Testing semantic search...")
results = semantic_search(vectorstore, query, k=5)
for doc in results:
    print("QUERY:", query)
    print("MATCH:", doc.page_content[:300])
    print("SOURCE:", doc.metadata["source"])
