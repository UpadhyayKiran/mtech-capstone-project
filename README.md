# Agentic Evidence-Based Clinical Research Assistant

## Overview

This project presents an **Agentic Evidence-Based Clinical Research Assistant**, a biomedical Retrieval-Augmented Generation (RAG) system designed to support evidence-based clinical research using biomedical literature from PubMed Central (PMC) Open Access articles.

The system combines biomedical document processing, metadata-aware retrieval, agentic query understanding, evidence-grounded reasoning, QLoRA-adapted BioMistral generation, and response validation to provide explainable clinical research support.

---

## Model Weights

The trained BioMistral QLoRA adapter is available on Hugging Face:

**Hugging Face Model Repository**

https://huggingface.co/KiranUpadhyay/biomistral-qlora-clinical-research-assistant

The adapter was trained using a retrieval-grounded biomedical dataset generated from PMC Open Access literature and can be loaded using PEFT.

---

## Key Features

### Data Collection & Processing

* PMC Open Access article collection
* Metadata extraction and enrichment
* Balanced biomedical dataset creation
* PDF text extraction
* Section-aware preprocessing
* Noise removal and content cleaning

### Retrieval Pipeline

* Metadata-preserving chunking
* PubMedBERT biomedical embeddings
* FAISS vector database
* Metadata-aware retrieval filtering
* Duplicate chunk removal
* PMCID diversity enforcement
* Evidence ranking and selection

### Agentic Workflow

* Query Understanding Agent
* PICO Extraction Agent
* Biomedical Entity Extraction Agent
* Query Reformulation Agent
* Retrieval Planning Agent
* Evidence Retrieval Agent
* Evidence Reasoning Agent
* Validation Agent

### Generation

* BioMistral-7B
* QLoRA Fine-Tuning
* Evidence-grounded answer generation
* Structured clinical research summaries
* Source traceability with PMCID references

### Explainability & Validation

* Confidence score calculation
* Validation score calculation
* Evidence count tracking
* Reasoning trace visualization
* Study comparison tables
* Hallucination pattern detection

### Evaluation

* Precision@3
* Precision@5
* NDCG@3
* NDCG@5
* Automated generation evaluation
* Retrieval benchmarking

### User Interface

* Streamlit-based application
* Clinical research query interface
* Evidence visualization
* Retrieval evaluation dashboard
* CSV export support

---

## System Architecture

```text
PMC Open Access Articles
          ↓
Metadata Collection
          ↓
Balanced Dataset Selection
          ↓
PDF Preprocessing
          ↓
Section Extraction
          ↓
Metadata-Aware Chunking
          ↓
PubMedBERT Embeddings
          ↓
FAISS Vector Store
          ↓
Query Understanding Agent
          ↓
PICO Extraction Agent
          ↓
Biomedical Entity Extraction Agent
          ↓
Query Reformulation Agent
          ↓
Retrieval Planning Agent
          ↓
Metadata-Aware Evidence Retrieval
          ↓
QLoRA Adapted BioMistral
          ↓
Response Validation Agent
          ↓
Confidence Scoring
          ↓
Evidence-Based Clinical Research Answer
```

---

## Models Used

### Embedding Model

* Model: `pritamdeka/S-PubMedBert-MS-MARCO`
* Domain: Biomedical Retrieval
* Embedding Dimension: 768

### Generation Model

* Base Model: `BioMistral/BioMistral-7B`
* Adaptation: QLoRA Fine-Tuning

### Vector Database

* FAISS

---

## Dataset Information

### Source

* PubMed Central (PMC) Open Access Articles

### Statistics

* Processed PDFs: 152
* Total Chunks: 2267
* Average Chunks per Document: 14.91

### Dataset Preparation

* Metadata extraction
* Quality filtering
* Balanced year-wise selection
* Noise reduction
* Section-aware preprocessing

---

## Repository Structure

```text
mtech-capstone-project
│
├── README.md
├── requirements.txt
├── Dockerfile
├── VERSION_INFO.md
├── GENERATION_EVALUATION.md
│
├── docs/
│   ├── architecture/
│   ├── literature_survey/
│   ├── presentations/
│   └── proposals/
│
├── app.py
│
├── prompts/
│
├── scripts/
│   ├── pmc_search_and_collect.py
│   ├── data_collection_pdf.py
│   ├── data_collection_dir.py
│   ├── generate_metadata_new.py
│   ├── metadata_balanced_pdf_filter.py
│   ├── preprocessing_final.py
│   ├── create_chunks.py
│   ├── create_faiss_index.py
│   ├── prepare_qlora_dataset.py
│   ├── qlora_train.py
│   ├── evaluate_retrieval.py
│   ├── evaluate_generation_auto.py
│   └── logger_utils.py
│
├── tests/
│   ├── test_retrieval.py
│   └── test_finetuned_model.py
│
├── vectorstore/
│   ├── faiss_index.index
│   └── chunk_metadata.json
│
├── qlora_dataset/
│   └── biomistral_qlora_train.jsonl
│
├── qlora_biomistral_adapter/
│
├── screenshots/
│
└── sample_outputs/
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/UpadhyayKiran/mtech-capstone-project.git
cd mtech-capstone-project
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
streamlit run app.py
```

---

## Retrieval Evaluation

Metrics:

* Precision@3
* Precision@5
* NDCG@3
* NDCG@5

Run:

```bash
python scripts/evaluate_retrieval.py
```

---

## Generation Evaluation

Generation quality is evaluated using:

* Response structure
* Grounding overlap
* Source traceability
* PMCID references
* Answer completeness
* Length validation

Run:

```bash
python scripts/evaluate_generation_auto.py
```

---

## QLoRA Fine-Tuning

Dataset generation:

```bash
python scripts/prepare_qlora_dataset.py
```

Fine-tuning:

```bash
python scripts/qlora_train.py
```

Configuration:

* Base Model: BioMistral-7B
* Quantization: 4-bit NF4
* LoRA Rank: 8
* LoRA Alpha: 16
* LoRA Dropout: 0.05
* Epochs: 2

---

## Explainability Features

The system provides:

* Evidence traceability
* PMCID source references
* Confidence scoring
* Validation scoring
* Reasoning trace visualization
* Study comparison support

This enables transparent and interpretable biomedical question answering.

---

## Future Work

* Cross-Encoder Re-Ranking
* Hybrid BM25 + Dense Retrieval
* Advanced Biomedical NER
* True Multi-Hop Autonomous Reasoning
* MLflow Integration
* Cloud Deployment
* Automated Continuous Evaluation

---

## System Characterization

> An Agentic Evidence-Based Clinical Research Assistant that combines metadata-aware biomedical retrieval, QLoRA-adapted BioMistral generation, response validation, and explainable evidence-grounded reasoning for clinical research support.

---
