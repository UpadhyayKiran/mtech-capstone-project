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













