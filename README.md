# Agentic Evidence-Based Clinical Research Assistant

## Overview
This project is an agentic biomedical Retrieval-Augmented Generation (RAG) system designed for evidence-based clinical research support using biomedical literature from PMC Open Access articles.

## Features
- PMC biomedical document processing
- Section-aware preprocessing
- Metadata-preserving chunking
- PubMedBERT-based embeddings
- FAISS semantic retrieval
- QLoRA-adapted BioMistral generation
- PICO extraction
- Biomedical entity extraction
- Query reformulation
- Retrieval planning
- Response validation
- Confidence score
- Study comparison table
- Precision@K and NDCG@K evaluation
- CSV export support
- Streamlit-based interactive clinical research assistant UI
- PDF upload and extractive summarization

## Pipeline
1. PDF parsing
2. Text cleaning
3. Section extraction
4. Chunking
5. Embedding generation
6. FAISS index creation
7. Retrieval evaluation
8. QLoRA dataset preparation
9. QLoRA fine-tuning
10. Streamlit app execution
11. PDF text extraction
12. Extractive PDF summarization

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Models Used

* Embedding model: `pritamdeka/S-PubMedBert-MS-MARCO`
* Generator: `BioMistral/BioMistral-7B`
* Vector DB: `FAISS`

## Agentic Workflow

The implemented workflow includes:

1. Query Understanding Agent
2. PICO + Biomedical Entity Extraction
3. Query Reformulation Agent
4. Retrieval Planning Agent
5. Evidence Retrieval Agent
6. Evidence Reasoning Agent
7. Validation Agent
8. Final Evidence Output Agent

## Evaluation

The system supports:

* Precision@3
* NDCG@3
* Precision@5
* NDCG@5

through the Retrieval Evaluation UI.

Additional runtime validation includes:

* confidence score
* validation score
* evidence count
* reasoning trace
* Retrieval benchmarking using representative biomedical queries

## Project Structure

```text
Capstone_Final/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
├── VERSION_INFO.md
│
├── prompts/
├── vectorstore/
├── chunks/
├── json/
├── qlora_dataset/
```

## Future Work

* Cross-encoder reranking
* Hybrid BM25 + dense retrieval
* Advanced biomedical NER
* True autonomous multi-hop reasoning
* MLflow tracking
* Cloud deployment

## System Characterization

The final system behaves as:

> “An Agentic Evidence-Based Clinical Research Assistant for biomedical literature retrieval, evidence-grounded reasoning, and explainable clinical research support.”

instead of a simple biomedical semantic-search chatbot.