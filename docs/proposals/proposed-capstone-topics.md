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
