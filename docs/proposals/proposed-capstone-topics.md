## Proposed Capstone Project Ideas

---

## **Option 1: AI-based Defect De-deduplication**
**Proposed by:** Priyanka Jain

A Defect De-Duplication AI System automatically identifies whether a newly reported defect (bug) is already reported earlier, even if the wording is different.

**Example:**
- “Upper bar is missing”
- “Top border not visible”
- “No header line displayed”

Though text is different, AI detects them as the same defect.

**Benefits:**

• Reduces duplicate bug reports by 40–70%  
• Saves QA & developer time  
• Faster bug triage  
• Clean defect tracking system  

This system will proposedly use NLP, Semantic Embedding, Smiliarity Matching, etc.

**Dataset sources:** Kaggle, Github

---

## **Option 2: Selection, Optimization, and Performance Analysis of Transformer-Based Language Models for Text Classification**
**Proposed by:** Kiran Upadhyay

### **Problem Statement**
Text classification is a core task in Natural Language Processing and is widely used in applications such as customer support ticket categorization, sentiment analysis, and document classification. Multiple transformer-based language models are available, but selecting the most suitable model and optimization strategy under accuracy and computational constraints remains challenging.

### **Proposed Solution**
A research-driven evaluation and comparison of transformer-based language models to identify the most suitable model and optimization strategy for text classification tasks.

### **Key Techniques**
- Transformer-based language models (DistilBERT, BERT, RoBERTa)
- Fine-tuning and layer-freezing strategies
- Optimizer and learning rate scheduling
- Performance and efficiency benchmarking

### **Datasets**
- AG News (news classification)
- IMDb Movie Reviews (sentiment analysis)
- Optional: Amazon Reviews (subset)

### **Evaluation Metrics**
- Accuracy, Precision, Recall, F1-score
- Training time and GPU memory usage
- Inference latency

### **Expected Outcomes**
- Guidelines for selecting the right language model for a given text classification use case
- Optimized model configurations balancing performance and computational cost
- Reusable benchmarking and evaluation framework
- Proof-of-concept implementation

---

## **Option 3:Machine Learning–Based Parking Occupancy Detection and Availability Prediction**
**Proposed by:** Sunaina K S

This project investigates machine learning models for parking occupancy classification and short-term availability prediction using public datasets, with a focus on comparative evaluation and predictive performance.

**Objectives**

* Analyze public parking datasets
* Build ML models for parking occupancy classification
* Develop time-series models for availability prediction
* Compare model performance using standard metrics
* Identify limitations and future improvements

**ML Models for Comparison**
* CNN – Deep learning baseline
* ResNet / MobileNet – Transfer learning
* SVM + HOG – Classical ML baseline
  
**Time-Series Prediction Models**
* ARIMA – Statistical baseline
* Random Forest – Nonlinear pattern learning
* LSTM – Deep temporal modeling

**Dataset Source**
1. CNRPark / CNRPark+EXT Dataset
Source: Institute of Information Science and Technologies (ISTI-CNR), Italy

Access Link:
https://cnrpark.it

3. Kaggle Smart Parking / Parking Occupancy Dataset
Source: Kaggle (Public Open Dataset Platform)

Access Link:
https://www.kaggle.com

**Core Research Gap (ML-focused)**

Existing studies focus either on parking space detection or simple statistical analysis, while limited work integrates occupancy classification with short-term availability prediction using comparative machine learning models on real-world datasets

- Lack of predictive capability: Most software-based smart parking systems focus only on real-time occupancy classification and do not predict short-term future parking availability.
- No integrated ML pipeline: Existing works often treat parking occupancy detection and availability prediction as separate problems, with limited integration into a unified machine learning framework.
- Insufficient comparative evaluation: There is a lack of systematic comparison between classical machine learning, deep learning, and statistical models on the same parking datasets using standard evaluation metrics.
  
**What’s Novel ?**
* Clear data-driven ML pipeline
*  Separate classification vs prediction models
*  Strong research gap from ML perspective
*  Explicit model comparison (classical ML vs deep learning)
*  Clean evaluation metrics (Accuracy, F1, MAE, RMSE)
  
---

## **Option 4:Personalized AI Tutor with Long-Term Memory (Agentic EdTech)**
**Proposed by:** Sunaina K S

**Problem Statement**
Most existing e-learning platforms provide static or shallow personalization. They adapt content only based on recent quizzes or session-level performance, 

**Ignoring:**

- Long-term learning behavior
- Forgetting patterns
- Learning speed differences
- Concept dependencies
  
This results in one-size-fits-all learning, poor retention, and disengagement.

**Proposed Solution**

This project proposes an Agentic AI-based Personalized Tutor that:

- Acts as an autonomous tutor agent
- Observes student interactions continuously
- Maintains long-term memory of:
  * Strengths & weaknesses
  * Learning pace
  * Mistake patterns
  * Concept mastery over time
- Plans personalized learning paths
- Adapts content difficulty in real time
- Learns from feedback (student success/failure)
  
The tutor is not just a recommender — it is an autonomous decision-making agent.

**Software & Programming Used:**
The project is implemented primarily in Python. PyTorch and Stable-Baselines3 are used to build the reinforcement-learning tutor agent, while Gymnasium defines the student–tutor interaction environment. Pandas/NumPy handle student datasets and long-term memory storage, with optional Flask/Streamlit for a demo interface.

**Dataset Source**

We can combine Real+synthetic datasets.

- Publicly Available Datasets : ASSISTments Dataset
- EdNet Dataset : Large-scale real student data
- KDD Cup Educational Datasets : ·Student problem-solving sequences
- Synthetic Data (Recommended)

**What's Novel?**

* Long-Term Memory (Most systems lack this)
* Agentic Decision-Making (Not rule-based)
* Teaching Strategy Adaptation
* Continuous Feedback Loop

**Research Gap**

🔴 Gap 1: Lack of Long-Term Personalization : Most tutoring systems Reset or weakly retain student history and Ignore forgetting and concept decay.

🔴 Gap 2: Limited Agent Autonomy : Use static policies and Do not self-improve teaching strategies

🔴 Gap 3: Poor Adaptation to Learning Pace : Treat all students similarly and Struggle with slow or irregular learners

🔴 Gap 5: Limited Explainability : Black-box tutors reduce trust.

---

## **Option 5:An AI agent that helps clinical researchers quickly navigate unstructured medical literature and case studies, delivering evidence-based insights and reducing review time from weeks to days**
**Proposed by:** Divya Narasimha Prasanna
**Problem**

Clinical researchers spend weeks manually reviewing:
Unstructured medical literature
Case studies
Clinical trial reports
PDFs, guidelines, EMRs, and white papers

**This leads to:**
Slow evidence synthesis
Information overload
Missed insights
High human effort & cost

 **Core Capabilities**
**Intelligent Literature Understanding**

NLP-based parsing of:
Research papers
Clinical notes
Case reports
Trial data
Guidelines
Converts unstructured text → structured knowledge

**🔍 Semantic Search (Not Keyword Search)**
Context-aware search
Concept matching (e.g., "cardiac failure" ≈ "heart failure")
Disease–symptom–drug–outcome linking

**📊 Evidence-Based Insight Engine**
Auto-summarization of findings
Risk–benefit analysis
Outcome comparison
Confidence scoring based on source credibility

**🧬 Clinical Knowledge Graph**
Relationships between:
Diseases
Drugs
Genes
Symptoms
Treatments
Outcomes

**🧪 Use Cases**
Clinical trial design
Systematic reviews
Meta-analysis support
Drug discovery research
Rare disease research
Personalized treatment planning
Evidence-based medicine (EBM)

**🧩 Tech Stack Suggestion**
NLP: BioBERT, ClinicalBERT, SciSpacy
LLMs: GPT-based agents, Med-PaLM style models
Vector DB: FAISS / Pinecone
Knowledge Graph: Neo4j
Search: Semantic + hybrid search
ML: Topic modeling, clustering, classification
UI: Evidence dashboard + chat-based interface

---

## **Option 6: Explainable AI (XAI) for Credit Scoring and Loan Approval**

While the provided XAI survey focuses on biomedicine, the methods (SHAP, LIME, Counterfactuals) are heavily researched in finance for regulatory compliance (GDPR / EU AI Act). There is a massive volume of IEEE papers on "Fairness" and "Explainability" in banking.

### **Problem Statement**
"Black box" deep learning models (like XGBoost or Neural Nets) offer high accuracy for credit scoring but lack transparency. This project implements and evaluates post-hoc explainability methods to ensure loan approval decisions are fair and understandable.

### **Literature Search Keywords (for IEEE Xplore)**
- Explainable AI (XAI) in Credit Risk  
- Fairness-aware Machine Learning  
- SHAP / LIME for Tabular Financial Data  
- Counterfactual Explanations in Banking  

### **Implementation Steps (Based on Source)**
1. **Model Training**  
   Train a complex model (Gradient Boosting or Deep Learning) on a dataset like the German Credit Data.

2. **Bias Detection**  
   Use metrics like Disparate Impact or Demographic Parity to measure if the model discriminates against a protected group (e.g., age or gender).

3. **Explainability Layer**  
   Implement SHAP (Shapley Additive Explanations) to generate global and local feature importance plots.

4. **Fairness Mitigation**  
   Apply a pre-processing technique (like Reweighting) or in-processing technique (like Adversarial Debiasing) to reduce bias.

5. **Dashboard**  
   Build a dashboard (using Streamlit or Dash) that visualizes the "Why" behind a rejection  
   (e.g., "Loan rejected because credit history < 2 years").

---










