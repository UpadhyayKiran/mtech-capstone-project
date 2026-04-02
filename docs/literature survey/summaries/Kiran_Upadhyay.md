# **Title: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks**

## **Problem Statement**

The paper addresses the limitation of parametric language models that store knowledge only within fixed model parameters, making them difficult to update and prone to hallucinations. The study proposes a retrieval-based approach to improve factual accuracy and performance on knowledge-intensive NLP tasks by accessing external knowledge sources dynamically.

## **Algorithms Used**

The study introduces the **Retrieval-Augmented Generation (RAG)** framework, which combines dense passage retrieval (DPR) with sequence-to-sequence transformer models such as BART. The model retrieves relevant documents from external knowledge sources and integrates them during response generation.

## **Datasets**

The model is evaluated on knowledge-intensive tasks including open-domain question answering datasets such as Natural Questions, WebQuestions, CuratedTREC, and FEVER fact verification datasets. Wikipedia is used as the external knowledge source.

## **Model Training and Testing**

The retriever and generator components are jointly trained. The retriever selects relevant passages using dense vector similarity, and the generator produces responses conditioned on retrieved documents. Performance is evaluated using answer accuracy and factual correctness.

## **Results**

The RAG model significantly improves performance on knowledge-intensive tasks compared to parametric-only models. It produces more factual and interpretable outputs while allowing knowledge updates without retraining the entire model.

## **Conclusions**

The authors conclude that combining retrieval with generation improves factual accuracy, interpretability, and scalability of language models.

## **Open Questions**

Future work includes improving retrieval efficiency, handling noisy retrieved documents, and improving integration between retrieved knowledge and generation.

## **Relevance to Our Team**

This paper directly supports our project’s RAG pipeline for clinical document analysis. The retrieval-based framework aligns with our approach of retrieving relevant medical text chunks and generating evidence-based responses from external knowledge sources.

## **Reference:**

Patrick Lewis et al.,	2020,	NeurIPS Proceedings,	https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html

---

# **Title: REALM: Retrieval-Augmented Language Model Pre-Training**

## **Problem Statement**

The paper addresses the challenge of storing and accessing factual knowledge in language models. Traditional models require retraining to update knowledge and struggle with knowledge-intensive tasks.

## **Algorithms Used**

The study introduces **REALM (Retrieval-Augmented Language Model)**, which integrates neural retrieval with masked language model pretraining. It jointly trains a retriever and language model to access external documents during training.

## **Datasets**

The model uses large text corpora including Wikipedia as the knowledge base and evaluates performance on open-domain question answering benchmarks.

## **Model Training and Testing**

The model retrieves relevant documents using dense embeddings and incorporates retrieved text into masked language modeling objectives. Training jointly optimizes retrieval and prediction performance.

## **Results**

REALM significantly improves performance on knowledge-intensive tasks and reduces dependency on large parameter sizes by leveraging external knowledge.

## **Conclusions**

The authors conclude that retrieval during pretraining enables language models to learn knowledge access mechanisms and improves factual reasoning.

## **Open Questions**

Future work includes scaling retrieval databases and improving retrieval quality for complex reasoning tasks.

## **Relevance to Our Team**

REALM provides foundational support for our system’s embedding-based retrieval and knowledge access mechanisms. It justifies using external medical knowledge sources rather than storing all knowledge in model parameters.

## **Reference:**

Kelvin Guu et al.,	2020,	ICML (PMLR Proceedings),	https://proceedings.mlr.press/v119/guu20a.html

---

# **Title: Leveraging Passage Retrieval with Generative Models for Open Domain Question Answering**

## **Problem Statement**

The paper addresses limitations of generative models in open-domain question answering, where models struggle to produce accurate responses without access to external knowledge.

## **Algorithms Used**

The study combines passage retrieval methods with generative transformer models. It uses dense retrieval methods to fetch relevant passages and conditions answer generation on retrieved text.

## **Datasets**

The model is evaluated on open-domain question answering datasets including Natural Questions and TriviaQA.

## **Model Training and Testing**

The system retrieves relevant passages using embedding similarity and feeds them into a generative model. Training optimizes answer generation conditioned on retrieved context.

## **Results**

The approach improves answer accuracy and factual consistency compared to models without retrieval.

## **Conclusions**

The authors conclude that integrating retrieval with generation improves knowledge access and enhances performance on question answering tasks.

## **Open Questions**

Future work includes improving passage ranking and handling irrelevant retrieval results.

## **Relevance to Our Team**

This paper supports our design of retrieving relevant medical document chunks before generating responses. It validates the importance of retrieval-based question answering for evidence-based systems.

## **Reference:**

Gautier Izacard & Edouard Grave,	2021,	ACL Anthology (EACL 2021 Proceedings),	https://aclanthology.org/2021.eacl-main.74/

---

# **Title: Atlas: Few-shot Learning with Retrieval Augmented Language Models**

## **Problem Statement**

The paper addresses the challenge of few-shot learning in language models, where models require large training data and struggle to generalize with limited examples.

## **Algorithms Used**

The study introduces the **Atlas framework**, which integrates retrieval-based memory with language models to support few-shot learning. It combines dense retrieval with transformer-based generation.

## **Datasets**

The model is evaluated on multiple NLP benchmarks including question answering, reasoning, and knowledge-intensive tasks using large-scale text corpora.

## **Model Training and Testing**

The model retrieves relevant examples from external databases and conditions predictions on retrieved information. Training involves optimizing retrieval and generation jointly.

## **Results**

Atlas achieves strong few-shot performance and improves knowledge access without requiring extensive training data.

## **Conclusions**

The authors conclude that retrieval-based augmentation improves generalization and reduces dependence on large training datasets.

## **Open Questions**

Future work includes improving retrieval quality and scaling retrieval systems for large knowledge bases.

## **Relevance to Our Team**

Atlas supports our system design where limited labeled clinical data can be supplemented using retrieval from external medical documents. It helps improve evidence-based response generation with minimal training data.

## **Reference:**

Izacard et al.,	2023,	Journal of Machine Learning Research (JMLR),	https://www.jmlr.org/papers/v24/23-0037.html

---

# **Title: Improving Language Models by Retrieving from Trillions of Tokens**

## **Problem Statement**

The paper addresses the limitations of large language models that store knowledge only in their parameters. Scaling model size improves performance but requires high computational resources and large training data. The study investigates whether language models can be enhanced by retrieving relevant information from large external text databases instead of increasing model parameters, thereby improving knowledge access and prediction quality.

## **Algorithms Used**

The study introduces the **Retrieval-Enhanced Transformer (RETRO)** architecture. It combines a frozen BERT-based retriever with a transformer language model and uses chunk-based retrieval with cross-attention mechanisms. The model retrieves relevant text segments from a large corpus using approximate nearest neighbor search and incorporates the retrieved information during token prediction.

## **Datasets**

The model is trained and evaluated using large-scale text corpora including MassiveText (containing trillions of tokens from web pages, books, Wikipedia, and news articles). Performance is evaluated on multiple benchmarks such as C4, Wikitext103, The Pile, and question answering datasets. The retrieval database contains up to two trillion tokens.

## **Model Training and Testing**

The input text is divided into chunks, and relevant chunks are retrieved using BERT-based embeddings. The retrieved information is integrated into the transformer model through cross-attention layers. The model is trained using standard language modeling objectives and evaluated using perplexity and knowledge-intensive task performance.

## **Results**

The RETRO model achieves performance comparable to very large transformer models while using significantly fewer parameters. It improves results on knowledge-intensive tasks and demonstrates that retrieval from large external databases enhances factual accuracy and language modeling performance. The study shows that increasing retrieval database size improves model effectiveness without increasing model complexity.

## **Conclusion**

The authors conclude that retrieval-based language modeling is an effective alternative to scaling model size. External memory through retrieval enables efficient knowledge storage and improves performance on knowledge-intensive tasks. The approach reduces computational requirements while maintaining strong performance.

## **Open Questions**

The study suggests future work on further improving retrieval efficiency, handling potential data leakage from retrieval databases, and improving integration of retrieved knowledge for complex reasoning tasks.

## **Relevance to Our Project**

This paper is highly relevant to our project on building an AI agent for clinical research using a Retrieval-Augmented Generation (RAG) pipeline. The proposed RETRO architecture demonstrates how retrieving relevant document chunks from large external knowledge sources improves factual accuracy and model performance. Our project similarly uses vector embeddings, document retrieval, and generation to provide evidence-based responses from medical documents. The chunk-based retrieval mechanism and external knowledge integration proposed in this paper support the design of our system for processing unstructured medical documents and generating reliable answers. The study provides strong theoretical justification for using retrieval-based methods to reduce hallucination and improve decision support in clinical applications.

## **Reference:**

Borgeaud et al.,	2022,	ICML 2022 (PMLR Proceedings), https://proceedings.mlr.press/v162/borgeaud22a.html

---

# **Title: BioBERT: a Pre-trained Biomedical Language Representation Model for Biomedical Text Mining**

## **Problem Statement**

The paper addresses the challenge of applying general NLP models (like BERT) to biomedical text mining tasks. Standard language models are trained on general-domain text such as Wikipedia and books, which differ significantly from biomedical literature in vocabulary and structure. This domain mismatch leads to poor performance in extracting biomedical entities, relations, and answers from medical documents. The study aims to adapt BERT specifically for biomedical text understanding.

## **Algorithms Used**

* BERT (Bidirectional Encoder Representations from Transformers)
* BioBERT (domain-specific extension of BERT)
* Transformer-based contextual embeddings
* WordPiece tokenization
* Fine-tuning tasks:

  * Named Entity Recognition (NER)
  * Relation Extraction (RE)
  * Question Answering (QA)

BioBERT initializes from BERT weights and is further pre-trained on biomedical corpora.

## **Datasets**

### Pre-training datasets:

* PubMed abstracts
* PubMed Central (PMC) full-text articles
* Wikipedia + BooksCorpus (initial BERT training)

### Evaluation datasets:

* NER datasets (disease, gene, chemical entities)
* Relation extraction datasets (gene–disease, protein–chemical)
* BioASQ biomedical QA dataset

These datasets represent large-scale biomedical literature and clinical data.

## **Model Training and Testing**

BioBERT follows two stages:

### **Pre-training**

* Initialized with BERT weights
* Further trained on biomedical corpora
* Trained for weeks using multiple GPUs
* Learns domain-specific biomedical vocabulary

### **Fine-tuning**

* Applied to NER, RE, and QA tasks
* Uses standard evaluation metrics:

  * Precision, Recall, F1 (NER, RE)
  * Accuracy and MRR (QA)

## **Results**

BioBERT significantly outperforms BERT and previous state-of-the-art models:

* Improved biomedical entity recognition accuracy
* Better relation extraction performance
* Large improvements in biomedical question answering
* Better understanding of domain-specific terms

The study shows domain-specific pre-training greatly improves biomedical NLP performance.

## **Conclusions**

The authors conclude that domain-specific pre-training is essential for biomedical NLP tasks. BioBERT successfully adapts general language models for specialized domains and achieves state-of-the-art results with minimal architectural changes.

## **Open Questions**

Although BioBERT achieves state-of-the-art performance across multiple biomedical NLP tasks, the study leaves several research directions open. The authors experiment with different combinations of general-domain and biomedical corpora, suggesting that further investigation into optimal corpus composition and scale may yield additional improvements. While BioBERT retains the original BERT WordPiece vocabulary for compatibility, the impact of constructing a domain-specific biomedical vocabulary remains unexplored. Additionally, the paper highlights the substantial computational cost required for large-scale pre-training, indicating that more efficient domain adaptation strategies could be investigated. Finally, although BioBERT demonstrates strong results on NER, relation extraction, and question answering, its performance across other biomedical text mining tasks and broader clinical settings warrants further study.

## **Relevance to Our Team**

This paper is highly relevant to our project because it demonstrates how domain-specific language models improve biomedical text understanding. Our proposed system processes clinical documents and medical reports using NLP and embeddings. BioBERT provides a strong foundation for biomedical entity extraction, document understanding, and retrieval in our RAG pipeline, improving evidence-based answer generation.

## **Reference:**

Jinhyuk Lee et al.,	2019,	Bioinformatics (Oxford University Press), https://doi.org/10.1093/bioinformatics/btz682

---

# **Title: SciBERT: A Pretrained Language Model for Scientific Text**

### **Problem Statement**

The paper addresses the challenge of applying general NLP models (like BERT) to scientific documents. Scientific text contains domain-specific vocabulary and structure, making general pretrained models less effective. The study proposes a specialized language model trained on scientific literature to improve performance on scientific NLP tasks such as entity recognition, classification, and relation extraction.

### **Algorithms Used**

* Transformer-based architecture (BERT framework)
* Domain-specific pretraining on scientific corpus
* WordPiece tokenization with new scientific vocabulary (SciVocab)
* Fine-tuning strategies for NLP tasks
* Task-specific neural models for classification and tagging

### **Datasets**

* 1.14 million scientific papers from Semantic Scholar
* 3.17 billion tokens
* Domains:

  * 82% biomedical
  * 18% computer science
* Evaluation tasks:

  * Named Entity Recognition (NER)
  * Text Classification
  * Relation Extraction
  * Dependency Parsing
  * PICO extraction from clinical trials

### **Model Training and Testing**

* Model pretrained using masked language modeling and sentence prediction.
* Scientific vocabulary constructed using SentencePiece.
* Training performed using TPU hardware.
* Performance evaluated on multiple scientific NLP benchmarks.
* Compared against BERT-Base and BioBERT.

### **Results**

* SciBERT significantly outperforms BERT-Base on scientific tasks.
* Achieved state-of-the-art results on multiple datasets.
* Improved performance in:

  * Biomedical text processing
  * Computer science literature tasks
  * Scientific entity extraction and classification
* Domain-specific vocabulary improves model accuracy.

### **Conclusions**

The authors conclude that domain-specific pretraining significantly improves NLP performance for scientific documents. SciBERT provides better contextual understanding of technical terminology and can serve as a general resource for scientific NLP applications. Future work includes scaling the model and improving domain coverage.

### **Open Questions**

* Training domain-specific models requires high computational cost.
* More domain coverage and larger models could improve performance further.
* Impact of domain mixture and vocabulary design needs further study.

### **Relevance to Our Team**

This paper is highly relevant to our project on AI for clinical research and RAG pipelines. It shows how domain-specific language models improve information extraction from scientific and medical documents. The approach can help our system better process clinical papers, extract entities, and generate evidence-based answers from medical literature.

## **Reference:**

Iz Beltagy et al.,	2019,	EMNLP 2019 (ACL),	https://arxiv.org/abs/1903.10676

---

# **Title: ClinicalBERT: Modeling Clinical Notes and Predicting Hospital Readmission**

### **Problem Statement**

The paper addresses the challenge of utilizing **unstructured clinical notes** from electronic health records (EHRs) for medical prediction tasks. Traditional machine learning models mainly use structured data (lab values, medications), while clinical notes contain rich but complex information. The study aims to develop a model that effectively learns representations from clinical notes to predict **30-day hospital readmission risk** and support clinical decision-making.

### **Algorithms Used**

The study proposes **ClinicalBERT**, a transformer-based language model built on BERT architecture and specialized for clinical text.

Key techniques include:

* Transformer encoder with self-attention mechanism
* Masked Language Modeling (MLM)
* Next Sentence Prediction (NSP)
* Domain-specific pretraining on clinical notes
* Fine-tuning for readmission prediction
* Attention-based interpretability

The model learns contextual embeddings from clinical text and predicts readmission probability using a classification layer.

### **Datasets**

The model is trained and evaluated using:

* **MIMIC-III Dataset**

  * ~58,000 hospital admissions
  * ~2 million clinical notes
  * ICU patient records
  * Data from Beth Israel Deaconess Medical Center

The dataset includes physician notes, nursing reports, discharge summaries, and patient history.

### **Model Training and Testing**

* Pretrained using masked language modeling and next sentence prediction.
* Fine-tuned for predicting 30-day hospital readmission.
* Evaluation metrics:

  * AUROC (Area Under ROC Curve)
  * AUPRC (Area Under Precision-Recall Curve)
  * Recall at 80% precision
* Compared against baseline models:

  * Bag-of-words
  * Word2Vec
  * FastText
  * Bi-LSTM
  * Standard BERT

### **Results**

* ClinicalBERT significantly outperforms traditional models and standard BERT.
* Achieves better prediction accuracy and recall for hospital readmission.
* Captures semantic relationships between medical concepts.
* Provides interpretable predictions using attention weights.
* Demonstrates improved clinical language modeling performance.

### **Conclusions**

The authors conclude that domain-specific language models trained on clinical text improve medical prediction performance. ClinicalBERT provides accurate clinical representations, improves hospital readmission prediction, and can support various healthcare applications such as mortality prediction and diagnosis estimation.

### **Open Questions**

* Performance depends on hospital-specific data; models may need retraining for different institutions.
* Handling extremely long clinical notes remains challenging.
* More research needed on large-scale clinical deployment.

### **Relevance to Our Team**

This paper is highly relevant to our project on **AI agents for clinical research using RAG and medical document processing**. It demonstrates how domain-specific language models extract meaningful knowledge from unstructured medical documents. The methodology supports clinical information extraction, entity understanding, and predictive modeling, which aligns with our system for evidence-based medical question answering using NLP, embeddings, and retrieval pipelines.

## **Reference:**

Kexin Huang et al.,	2019,	CHIL 2020 Workshop (ACM) / arXiv,	https://arxiv.org/abs/1904.05342

---

# **Title: ReAct: Synergizing Reasoning and Acting in Language Models**

### **Problem Statement**

The paper addresses limitations of large language models (LLMs) where reasoning and action generation are treated separately. Traditional reasoning approaches such as Chain-of-Thought perform internal reasoning but cannot interact with external environments, leading to hallucinations and outdated knowledge. Conversely, action-based models interact with environments but lack structured reasoning. The study proposes a unified framework that combines reasoning and action to improve task-solving performance, factual grounding, and decision-making.

### **Algorithms Used**

The study introduces **ReAct (Reasoning + Acting)**, a prompting-based framework where language models generate both reasoning traces and actions in an interleaved manner. The model produces reasoning steps (thoughts) to guide decision-making and performs actions such as retrieving information from external sources. The process follows an iterative sequence:

```
Thought → Action → Observation → Thought → Action
```

The framework uses few-shot prompting with large language models such as PaLM and GPT to integrate reasoning with environment interaction.

### **Datasets**

The framework is evaluated on multiple reasoning and decision-making benchmarks including:

* **HotpotQA** — multi-hop question answering
* **FEVER** — fact verification
* **ALFWorld** — interactive decision-making environment
* **WebShop** — web-based task completion environment

These tasks require reasoning, planning, and information retrieval.

### **Model Training and Testing**

The model uses few-shot prompting with human-annotated reasoning and action trajectories. It interacts with external tools such as Wikipedia search APIs and environment simulators. Performance is evaluated based on accuracy, success rate, and interpretability across different tasks. 

### **Results**

The framework demonstrates improved performance compared to reasoning-only and action-only methods. It reduces hallucinations, improves factual grounding, increases success rates in decision-making tasks, and provides interpretable reasoning traces. The model dynamically retrieves relevant information during reasoning, leading to more reliable outputs.

### **Conclusions**

The authors conclude that integrating reasoning and action improves the reliability, interpretability, and performance of language models. ReAct enables models to dynamically retrieve information and update reasoning during task execution, making them more effective for complex real-world tasks.

### **Open Questions**

Future work includes scaling the framework with larger datasets, combining ReAct with reinforcement learning, improving reasoning and action generation through fine-tuning, and extending the framework to more complex environments.

### **Relevance to Our Team**

This work is highly relevant to our RAG-based clinical research agent. ReAct provides a framework for iterative reasoning and retrieval, which can improve evidence-based answer generation, reduce hallucination, and support reliable decision-making in medical document processing.

## **Reference:**

Shunyu Yao et al.,	2023,	ICLR (OpenReview),	https://openreview.net/forum?id=WE_vluYUL-X

---

# **Title: Toolformer: Language Models Can Teach Themselves to Use Tools (NeurIPS 2023)**

### **Problem Statement**

The paper addresses limitations of large language models in performing tasks requiring factual retrieval, numerical computation, and access to external knowledge. LLMs often generate hallucinated or outdated information and struggle with precise calculations. Existing tool-augmented approaches require extensive human supervision or task-specific design. The study proposes a self-supervised framework that enables language models to autonomously learn when and how to use external tools to improve reasoning and factual accuracy.

### **Algorithms Used**

The study introduces **Toolformer**, a self-supervised framework that enables language models to use external tools through API calls. The model learns to decide when to call a tool, which tool to use, what input to provide, and how to integrate the output into predictions.

The training pipeline consists of:

```
Sample API Calls → Execute Tools → Filter Useful Calls → Fine-tune Model
```

The model retains only tool calls that improve prediction performance. Tools used include a calculator, question answering system, Wikipedia search engine, machine translation system, and calendar API.

### **Datasets**

The model is evaluated on multiple tasks requiring reasoning and external knowledge, including:

* **LAMA benchmark** — factual knowledge completion
* **Mathematical reasoning benchmarks** — ASDiv, SVAMP, MAWPS
* **Question answering datasets** — WebQuestions, TriviaQA
* **Multilingual question answering** — MLQA
* **Temporal reasoning datasets**

These datasets evaluate factual accuracy, reasoning ability, and decision-making performance.

### **Model Training and Testing**

The approach uses a pretrained language model (GPT-J) and augments training data with API calls that improve prediction accuracy. The model is fine-tuned on this augmented dataset and evaluated in zero-shot settings across multiple downstream tasks.

### **Results**

Toolformer improves mathematical reasoning, factual accuracy, and zero-shot performance by leveraging external tools. It reduces hallucination and achieves performance competitive with larger models while maintaining core language modeling capabilities.

### **Conclusions**

The authors conclude that language models can autonomously learn to use external tools through self-supervision. Toolformer enhances reasoning, factual grounding, and decision-making by integrating tool usage into language model predictions without requiring task-specific supervision.

### **Open Questions**

Future work includes enabling multi-step tool chaining, supporting interactive tool usage, improving sample efficiency of tool learning, integrating domain-specific tools, and considering computational costs of tool usage.

### **Relevance to Our Team**

This work is highly relevant to our RAG-based clinical research agent. Toolformer provides a framework for autonomous tool usage and external knowledge integration, which can improve factual grounding, reduce hallucination, and enhance reliability in medical document analysis and clinical decision support.

## **Reference:**

Timo Schick et al.,	2023,	NeurIPS,	https://proceedings.neurips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html

---

# **Title: OpenBioLink: A Benchmarking Framework for Large-Scale Biomedical Link Prediction**

### **Problem Statement**

The paper addresses the lack of standardized, high-quality benchmarks for evaluating link prediction algorithms in large-scale biomedical knowledge graphs. While many machine learning and embedding-based methods have been proposed for predicting missing links in knowledge networks, existing benchmarks either suffer from information leakage, lack biomedical specificity, or do not reflect the heterogeneous and multi-relational nature of biomedical data. The study aims to introduce a robust, transparent, and reproducible benchmarking framework tailored specifically for biomedical link prediction tasks. 

### **Algorithms Used**

The paper does not propose a new prediction algorithm. Instead, it introduces **OpenBioLink**, a modular benchmarking framework consisting of three main components:

1. **Graph creation module** — constructs biomedical knowledge graphs from multiple public data sources.
2. **Train–test split module** — creates robust splits while preventing trivial inference and information leakage.
3. **Training and evaluation module** — evaluates link prediction models using standardized metrics.

The framework supports evaluation using graph embedding models such as:

* TransE
* TransR

and integrates with external libraries like PyKEEN for training and evaluation.

Evaluation metrics include:

* Hits@k
* Mean Reciprocal Rank (MRR)
* ROC AUC
* Precision-Recall AUC

### **Datasets**

The OpenBioLink benchmark dataset includes:

* **7 node types**
* **30 edge types**
* Multiple biomedical entities (genes, diseases, proteins, anatomy, etc.)
* Both directed and undirected graph versions
* Quality-filtered subsets (high, medium, low confidence)

The dataset ensures:

* No trivial inference between train and test sets
* No inverse relation leakage
* Typed negative sampling for robust evaluation

This creates a challenging and realistic biomedical link prediction environment. 

### **Model Training and Testing**

Baseline experiments were conducted using graph embedding models (TransE and TransR). Hyperparameter optimization was performed, and models were evaluated using standardized link prediction metrics. The framework ensures that the test set does not include trivially inferable relations and that negative samples are properly constructed.

### **Results**

Baseline models achieved relatively modest performance (e.g., Hits@10 around 7.5%), indicating that the benchmark is challenging and leaves significant room for algorithmic improvement. The results highlight the difficulty of large-scale biomedical link prediction and the need for more advanced methods.

### **Conclusions**

The authors conclude that OpenBioLink provides a standardized, transparent, and reproducible framework for evaluating biomedical link prediction methods. It addresses flaws in previous benchmarks and creates a realistic large-scale environment for algorithm development. The benchmark can support future advances in biomedical knowledge graph learning and hypothesis generation.

### **Open Questions**

Future work includes:

* Hosting annual benchmarking events
* Extending the dataset with additional biomedical resources
* Evaluating more advanced embedding and rule-learning models
* Supporting experimental validation of predicted biomedical links

### **Relevance to Our Team**

This paper is highly relevant to our RAG-based clinical research agent and biomedical AI system. While our project focuses on document retrieval and reasoning, biomedical link prediction can enhance knowledge discovery, drug–disease association prediction, and hypothesis generation. Integrating structured knowledge graph reasoning with our retrieval pipeline can improve clinical evidence linking and decision support capabilities.

## **Reference:**

A. Breit et al.,	2020,	Oxford Academic (Bioinformatics Journal),	https://doi.org/10.1093/bioinformatics/btaa274

---

# **Title: KGen: A Knowledge Graph Generator from Biomedical Scientific Literature**

### **Problem Statement**

The paper addresses the challenge of extracting structured knowledge from large volumes of unstructured biomedical scientific literature. Scientific texts contain complex sentences, implicit relations, abbreviations, and domain-specific terminology, making automatic knowledge extraction difficult. The study aims to develop a method for generating knowledge graphs from biomedical texts by identifying entities and relationships and linking them to biomedical ontologies for knowledge representation and discovery.

### **Algorithms Used**

The study introduces **KGen**, a semi-automatic framework that generates ontology-linked knowledge graphs from biomedical texts using Natural Language Processing techniques.

The pipeline consists of four main steps:

* **Preprocessing** — sentence splitting, co-reference resolution, abbreviation handling, and sentence simplification
* **Triples extraction** — extracting subject–predicate–object relations using semantic role labeling and dependency parsing
* **Ontology linking** — mapping entities and relations to biomedical ontologies using UMLS and SPARQL queries
* **Graph generation** — constructing ontology-linked knowledge graphs using RDF triples

The method combines rule-based extraction and NLP techniques for information extraction and semantic representation.

### **Datasets**

The method is evaluated using biomedical scientific literature abstracts related to Alzheimer’s disease. Physicians manually extracted knowledge from the same texts to compare with automatically generated knowledge graphs.

### **Model Training and Testing**

The system uses NLP tools such as named entity recognition, semantic role labeling, and dependency parsing for extracting relations. Extracted entities are mapped to biomedical ontologies such as the Unified Medical Language System (UMLS) and National Cancer Institute Thesaurus. The quality of generated knowledge graphs is evaluated through comparison with expert manual extraction and qualitative analysis.

### **Results**

The proposed method successfully extracts a large number of meaningful triples from biomedical texts and effectively links them to biomedical ontologies. The generated knowledge graphs demonstrate high quality and support knowledge discovery by representing relationships between biomedical entities.

### **Conclusions**

The authors conclude that semi-automatic knowledge graph generation from biomedical literature is effective for representing scientific knowledge and supporting research discovery. Ontology-linked knowledge graphs enable better analysis of biomedical concepts and relationships across studies.

### **Open Questions**

Future work includes improving automatic relation extraction, handling more complex biomedical texts, enhancing ontology linking methods, and extending the approach to other biomedical domains.

### **Relevance to Our Team**

This work is highly relevant to our RAG-based clinical research agent. The method provides a framework for extracting structured knowledge from medical research papers and representing relationships between biomedical entities. Such knowledge graphs can enhance retrieval accuracy, improve evidence linking, and support clinical reasoning in our system.

## **Reference:**

Rossanez et al.,	2020,	Springer,	https://doi.org/10.1186/s12911-020-01341-5

---

# **Title: PubMedQA: A Dataset for Biomedical Research Question Answering**

### **Problem Statement**

The paper addresses the challenge of building intelligent systems that can understand and reason over biomedical research literature. Existing biomedical question answering datasets are small, simple, or require limited reasoning. The authors propose a new dataset that requires models to perform complex reasoning over scientific texts, particularly involving quantitative analysis and medical evidence.

### **Algorithms Used**

The study proposes a biomedical question answering framework and provides baseline models including:

* **BioBERT fine-tuning**
* **Multi-phase training strategy**
* **Pseudo-labeling and bootstrapping methods**
* **Bag-of-Words auxiliary supervision**
* Neural models such as:

  * BiLSTM
  * ESIM with BioELMo
  * Shallow feature models

The best performance is achieved using multi-phase fine-tuning of BioBERT.

### **Datasets**

The authors introduce **PubMedQA**, a biomedical QA dataset derived from PubMed articles. Each instance contains:

* A research question
* Context (abstract without conclusion)
* Long answer (conclusion)
* Yes/No/Maybe label

Dataset composition:

* **1k expert-annotated samples**
* **61.2k unlabeled samples**
* **211.3k automatically generated samples**

The dataset focuses on reasoning over biomedical research texts.

### **Model Training and Testing**

Models are trained using a multi-phase approach:

* Pre-training on automatically generated data
* Bootstrapping unlabeled data using pseudo-labeling
* Final fine-tuning on labeled dataset

Performance is evaluated using accuracy and macro-F1 score. Models must reason over scientific context rather than directly extract answers.

### **Results**

The multi-phase BioBERT model achieves the best performance (≈68% accuracy), outperforming baseline methods. However, results remain significantly below human performance (≈78%), indicating the difficulty of biomedical reasoning tasks.

### **Conclusions**

The study introduces a large-scale biomedical QA dataset that requires complex reasoning over scientific texts. The dataset enables evaluation of machine reasoning ability in biomedical research and supports evidence-based decision systems. The authors conclude that more advanced reasoning methods are required to match human performance.

### **Open Questions**

Future work includes:

* Better handling of numerical and statistical reasoning
* Improved reasoning over scientific evidence
* More advanced supervision techniques
* Generation-based answer prediction

### **Relevance to Our Team**

This paper is highly relevant to our project on **AI-based clinical research assistants using RAG pipelines**. It provides a benchmark dataset and evaluation framework for biomedical question answering, which supports retrieval-based evidence extraction and reasoning over medical literature.

## **Reference:**

Qiao Jin et al.,	2019,	EMNLP-IJCNLP 2019 (ACL Anthology),	https://aclanthology.org/D19-1259/

---

# **Title: On Faithfulness and Factuality in Abstractive Summarization (2020)**

## **Problem Statement**

The paper addresses the challenge of ensuring **faithfulness and factual correctness** in abstractive text summarization models. While modern neural summarization models generate fluent and coherent summaries, they often produce **hallucinated content** — information that is not supported by the source document or is factually incorrect. The study aims to understand why hallucinations occur, how frequently they appear, and how to measure and reduce them.

## **Algorithms Used**

The study evaluates multiple neural summarization architectures:

* **Pointer-Generator Networks (PTGEN)** — RNN-based sequence-to-sequence model with copy mechanism.
* **Topic-aware Convolutional Sequence-to-Sequence (TCONVS2S)** — CNN-based summarization using topic representations.
* **Transformer-based Models**

  * GPT-TUNED (pretrained GPT fine-tuned for summarization)
  * TRANS2S (Transformer encoder-decoder)
  * BERTS2S (BERT-based encoder-decoder with pretraining)

The paper also uses:

* **Textual Entailment models** to measure factual consistency.
* **Question Answering (QA) evaluation** to check information validity.
* **Human evaluation framework** for hallucination analysis.

## **Datasets**

* **XSUM Dataset**

  * 226,711 BBC news articles.
  * Each article paired with a single-sentence summary.
  * Requires highly abstractive summarization.

* Human annotations for:

  * Hallucination detection
  * Faithfulness evaluation
  * Factual correctness assessment

## **Model Training and Testing**

* Models trained using maximum likelihood estimation.
* Beam search used for decoding summaries.
* Human annotators evaluated:

  * Intrinsic hallucinations (misinterpreting source content)
  * Extrinsic hallucinations (adding unsupported information)
  * Factual correctness of generated summaries.
* Evaluation metrics:

  * ROUGE
  * BERTScore
  * Textual entailment
  * QA-based evaluation
  * Human judgment.

## **Results**

* More than **70% of generated summaries contained hallucinations**.
* Most hallucinations were **extrinsic and factually incorrect**.
* Pretrained models (BERTS2S) produced more faithful summaries than non-pretrained models.
* ROUGE and BERTScore showed weak correlation with factual correctness.
* Textual entailment showed better correlation with faithfulness.
* Pretraining improves factuality but does not eliminate hallucination.

## **Conclusions**

* Hallucination is a major challenge in abstractive summarization.
* Neural text generation models prioritize fluency over factual accuracy.
* Pretrained language models improve faithfulness but still produce errors.
* Traditional evaluation metrics (ROUGE) are insufficient for measuring summary correctness.
* Semantic inference-based metrics such as textual entailment are more reliable.

## **Open Questions**

* How to design training objectives that explicitly enforce factual correctness?
* How to integrate external knowledge safely into summaries?
* How to develop better automatic evaluation metrics for faithfulness?
* How to reduce hallucinations in large language models?

## **Relevance to Our Team**

This paper is highly relevant to our project on **RAG-based medical document retrieval and evidence-based answering**. It highlights:

* Risks of hallucination in LLM-generated responses.
* Importance of evidence grounding from source documents.
* Need for factual consistency verification.
* Importance of retrieval-based methods for reliable outputs.

The findings support our project design that combines document retrieval with generation to produce trustworthy medical responses.

## **Reference:**

Joshua Maynez et al.,	2020,	ACL,	https://arxiv.org/abs/2005.00661

---

# **Title: Survey of Hallucination in Natural Language Generation**

### **Problem Statement**

The paper addresses the problem of hallucination in Natural Language Generation (NLG), where language models generate factually incorrect or unsupported information not grounded in input data. This issue significantly affects reliability in applications such as summarization, dialogue systems, question answering, and data-to-text generation. The study aims to systematically review existing research, evaluation metrics, and mitigation methods for hallucinations in NLG systems.

### **Algorithms Used**

The study provides a survey of existing techniques rather than proposing a new model. It categorizes hallucinations into intrinsic hallucination (contradicting source input) and extrinsic hallucination (adding unsupported information). The paper reviews detection methods, training strategies, evaluation metrics, and mitigation techniques such as constrained decoding, knowledge grounding, and post-generation verification.

### **Datasets**

The paper reviews multiple datasets used across NLG tasks, including summarization datasets, machine translation benchmarks, and dialogue datasets. It discusses commonly used datasets for hallucination evaluation rather than focusing on a single dataset.

### **Model Training and Testing**

The survey analyzes training approaches used in literature such as reinforcement learning, factual consistency training, knowledge-grounded generation, and alignment-based evaluation. Performance is evaluated using metrics measuring factual correctness, faithfulness, and semantic consistency rather than traditional metrics like BLEU or ROUGE alone.

### **Results**

The study highlights that modern language models often produce fluent but factually incorrect outputs. It shows that existing evaluation metrics poorly capture hallucination and emphasizes the need for better automatic evaluation methods. The survey identifies trends in hallucination mitigation strategies and compares their effectiveness across tasks.

### **Conclusions**

The authors conclude that hallucination remains a major challenge in NLG systems. They emphasize the need for improved evaluation metrics, better grounding methods, and robust training strategies to enhance factual consistency and reliability of generated text.

### **Open Questions**

The paper suggests future work in developing standardized benchmarks, improving automatic hallucination detection methods, designing stronger factuality metrics, and improving model interpretability to understand hallucination causes.

### **Relevance to Our Team**

This paper provides important insights into ensuring factual correctness in language models, which is critical for our RAG-based clinical research agent. Understanding hallucination detection and mitigation techniques can help improve evidence-based answer generation, enhance model trustworthiness, and support reliable medical document analysis in our project.

## **Reference:**

Ziwei Ji et al.,	2023,	ACM Computing Surveys,	https://doi.org/10.1145/3571730

---

# **Title: Attention Is All You Need**

### **Problem Statement**

Traditional sequence models like RNNs and CNNs process data sequentially, making training slow and limiting their ability to capture long-range dependencies. The paper addresses this limitation by proposing a fully attention-based architecture that removes recurrence and convolution.

---

### **Algorithms Used**

The paper introduces the **Transformer architecture**, which relies entirely on:

* Self-Attention mechanism
* Multi-Head Attention
* Positional Encoding
* Encoder-Decoder architecture

The key idea is computing dependencies using attention instead of sequential processing .

---

### **Datasets**

* WMT 2014 English-German dataset (~4.5M sentence pairs)
* WMT 2014 English-French dataset (~36M sentence pairs)

---

### **Model Training and Testing**

* Trained using Adam optimizer with learning rate scheduling
* Uses positional encoding since no recurrence exists
* Fully parallelizable → significantly faster training
* Evaluated using BLEU score

---

### **Results**

* Achieved **28.4 BLEU (EN-DE)** and **41.0 BLEU (EN-FR)**
* Outperformed previous state-of-the-art models
* Reduced training cost significantly

---

### **Conclusions**

The Transformer demonstrates that attention alone is sufficient for sequence modeling, enabling better performance, scalability, and parallelization compared to RNN/CNN-based models.

---

### **Open Questions**

* Handling very long sequences efficiently
* Reducing quadratic complexity of attention
* Improving memory efficiency

---

### **Relevance to Our Team**

This paper forms the **core foundation of our project**:

* Our AI agent uses Transformer-based models (BioBERT / BioMistral)
* RAG pipeline relies on embeddings derived from Transformer architectures
* Attention mechanism enables semantic understanding of clinical queries

---

## **Reference:**

Ashish Vaswani et al.,2017,NeurIPS,https://arxiv.org/abs/1706.03762

---

# **Title: BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding**

---

### **Problem Statement**

Previous language models (like GPT) are unidirectional and cannot fully capture context from both left and right simultaneously. This limits performance on tasks requiring deep contextual understanding.

---

### **Algorithms Used**

BERT introduces:

* **Bidirectional Transformer Encoder**
* **Masked Language Modeling (MLM)**
* **Next Sentence Prediction (NSP)**

These enable learning deep contextual representations .

---

### **Datasets**

* BooksCorpus (800M words)
* English Wikipedia (2.5B words)

---

### **Model Training and Testing**

* Pre-training on large unlabeled text
* Fine-tuning on downstream tasks (QA, NLI, etc.)
* Uses WordPiece embeddings and special tokens ([CLS], [SEP])

---

### **Results**

* State-of-the-art on **11 NLP tasks**
* GLUE score: **80.5%**
* SQuAD F1: **93.2**

---

### **Conclusions**

BERT shows that bidirectional context significantly improves NLP performance and reduces the need for task-specific architectures.

---

### **Open Questions**

* High computational cost
* Domain adaptation challenges
* Handling long documents

---

### **Relevance to Our Team**

* Used in **BioBERT / SciBERT embeddings**
* Helps in **clinical entity extraction (NER)**
* Improves query understanding in our AI agent pipeline

---

## **Reference:**

Jacob Devlin et al.,2019,NAACL-HLT 2019 (ACL),https://aclanthology.org/N19-1423/

---

# **Title: Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks**

## **Problem Statement**

The paper addresses a major limitation of BERT-based models: while BERT produces powerful contextual embeddings, it is not efficient for computing sentence similarity. Comparing two sentences using vanilla BERT requires passing both sentences together through the model, which is computationally expensive and not scalable for large datasets.

The study aims to develop a method for generating fixed-size sentence embeddings that can be efficiently compared using similarity measures such as cosine similarity.

---

## **Algorithms Used**

The paper introduces **Sentence-BERT (SBERT)**, which modifies the BERT architecture using a **Siamese and triplet network structure**.

Key components include:

* Shared BERT encoder for sentence pairs
* Pooling operations (mean pooling, max pooling) to generate sentence embeddings
* Training using similarity objectives such as:

  * Cosine similarity loss
  * Triplet loss

This design allows sentences to be encoded independently and compared efficiently.

---

## **Datasets**

The model is trained and evaluated on several benchmark datasets, including:

* STS (Semantic Textual Similarity) benchmark datasets
* SNLI (Stanford Natural Language Inference)
* MultiNLI

These datasets provide labeled sentence pairs for measuring semantic similarity and entailment.

---

## **Model Training and Testing**

The SBERT model is trained using sentence pairs with similarity labels. During training:

* Each sentence is passed independently through the same BERT encoder
* Embeddings are compared using cosine similarity
* The model is optimized to minimize the difference between predicted and actual similarity scores

Evaluation is performed using correlation metrics such as Pearson and Spearman correlation with human-annotated similarity scores.

---

## **Results**

Sentence-BERT achieves:

* Significant speed improvements (up to 10,000x faster for similarity search compared to vanilla BERT)
* Comparable or better performance on semantic similarity tasks
* Efficient scalability for large-scale retrieval systems

The model enables real-time semantic search and clustering tasks.

---

## **Conclusions**

The authors conclude that SBERT successfully addresses the computational limitations of BERT for sentence similarity tasks by producing meaningful and reusable sentence embeddings.

This makes it highly suitable for applications such as:

* Semantic search
* Information retrieval
* Clustering and ranking

---

## **Open Questions**

* How to further improve embedding quality for domain-specific tasks (e.g., biomedical text)
* Integration with retrieval-augmented systems for better contextual grounding
* Handling very long documents efficiently

---

## **Relevance to Our Team**

This paper is highly relevant to our project, particularly for the **retrieval and embedding stages**.

In our system:

* Sentence embeddings are used to convert queries and documents into vector representations
* These embeddings enable **semantic similarity search** in vector databases
* SBERT provides a strong foundation for efficient and scalable retrieval in our RAG-based pipeline

---

## **Reference**

Reimers, N., & Gurevych, I., 2019, EMNLP Proceedings
[https://aclanthology.org/D19-1410/](https://aclanthology.org/D19-1410/)

---
