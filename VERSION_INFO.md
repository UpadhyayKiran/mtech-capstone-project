# Version Information

## Dataset
- Source: PMC Open Access biomedical research articles
- Processed PDFs: 152
- Total chunks: 2267

## Embedding Model
- Model: pritamdeka/S-PubMedBert-MS-MARCO
- Vector Database: FAISS
- Embedding Dimension: 768

## Generation Model
- Base LLM: BioMistral/BioMistral-7B
- Adaptation: QLoRA adapter
- Adapter folder: qlora_biomistral_adapter

## Evaluation
- Retrieval Metrics: Precision@3, NDCG@3, Precision@5, NDCG@5
- Generation Evaluation: backend evaluation script
- UI Metrics: Confidence Score, Validation Score, Retrieved Evidence Count

## Application
- UI Framework: Streamlit
- System Type: Agentic Biomedical RAG Prototype