from utils import load_json_documents
from chunker import chunk_documents
from embedder import get_embeddings
from faiss_index import create_faiss_index

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

print("✅ Index built successfully!")
