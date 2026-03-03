Offline pipeline(Data Ingestion Module)
Input -> Unstructured medical documents(PubMed abstracts, review articles, case studies, guidelines, clinical trial reports, pdfs, xml/html docs(optional))
Step1: Parsing and Cleaning(parsing, stripping, section extraction, noise removal, reference removal(optional))
Output -> Structured Text Documents
Step2: Chunking(Fixed-length chunking, semantic chunking, sliding window with overlap)
Output -> Document chunks + metadata
Step3: Embedding(domain specific transformer encoder, embeddings, vector normalization)
Output -> Dense vector representations
Step4: Vector DB and Semantic Indexing(Vector DB(FAISS, Milvus, Pinecone), ANN indexing, metadata storage)
Output -> ANN indexed Vector DB
Step5: Lexical Indexing(BM 25 index, store term frequencies, maintain document IDs)
Output -> BM25 Index

Online pipeline
Input -> User Query
Step1:  Query Processing(NLP preprocessing, NER, entity linking, query expansion)
Output -> Processed Query
Step2: Query Embedding(Embedding Model)
Output -> Query Vector
Step3: Hybrid Retrieval(Query vector with vector DB, query text with BM25)
Output -> top k semantic and lexical matches
Step4: Hybrid Fusion + Re-ranking -> Innovation(weighted scoring)
Output -> Final top k evidence chunks
Step5: Context Assembly(Deduplication, NLI, evidence level filtering, prompt construction)
Output -> Optimized context block
Step6: RAG(Fine tuned biomedical LLM evidence synthesis)
Output -> Draft output
Step7: Verification & Groundedness(Confidence score, Attribution alignment, detect hallucinations)
Output -> Validated response
Step8: Structured Output(evidence summary, citations, score, insights)
Output -> Evidence based Insights in structured format

