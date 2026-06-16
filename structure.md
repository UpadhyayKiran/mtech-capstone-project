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