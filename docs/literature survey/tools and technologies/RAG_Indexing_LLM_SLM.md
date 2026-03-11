# Notes for RAG, Indexing, and LLM/SLM Strategy

## 1. Role of RAG in Our System

Retrieval-Augmented Generation (RAG) is an architecture that combines **information retrieval with language model generation**.

Instead of relying only on the internal knowledge of a language model, the system retrieves relevant documents from an external knowledge base and uses them as context for generation.

This approach is particularly important for biomedical applications because:

* medical answers must be **evidence-based**
* LLMs may **hallucinate unsupported claims**
* research outputs must include **citations and traceability**

Therefore, RAG ensures that responses are **grounded in retrieved biomedical literature**.

---

## 2. Agentic RAG Pipeline

The system follows an **agent-driven RAG workflow**.

### Pipeline

```
User Research Query
        ↓
Query Understanding
        ↓
Hybrid Retrieval
        ↓
Evidence Selection (Top-K)
        ↓
Evidence Processing
        ↓
Agent Reasoning (RAG)
        ↓
Validation
        ↓
Structured Evidence Output
```

Each stage contributes to a different part of the reasoning process.

---

## 3. Indexing Strategy

Indexing converts biomedical documents into a searchable format.

### Steps involved

1. Convert document chunks into embeddings
2. Store embeddings in a vector index
3. Retrieve similar vectors during queries

Indexing allows the system to quickly locate relevant evidence passages.

---

## 4. Vector Database

The recommended vector database is:

**FAISS (Facebook AI Similarity Search)**

FAISS is widely used in retrieval systems because it enables efficient similarity search over dense vectors.

### Advantages

* open source
* fast similarity search
* supports large datasets
* can run locally
* GPU acceleration available

### Disadvantages

* metadata management must be implemented separately
* requires additional logic for document storage

---

## 5. Retrieval Strategies

Three retrieval strategies can be used in RAG systems.

### 5.1 Semantic Retrieval

Semantic retrieval uses **vector embeddings** to capture meaning.

**Steps**

1. Convert query into embedding
2. Compute similarity with stored embeddings
3. Retrieve most similar chunks

**Pros**

* understands contextual meaning
* handles paraphrased questions
* effective for conceptual queries

**Cons**

* may miss exact biomedical terminology

---

### 5.2 Lexical Retrieval

Lexical retrieval uses **keyword matching techniques**.

Examples:

* BM25
* TF-IDF
* keyword search

**Pros**

* captures exact biomedical terms
* useful for drug names and gene symbols

**Cons**

* cannot capture semantic similarity

---

### 5.3 Hybrid Retrieval

Hybrid retrieval combines both methods.

```
Hybrid Retrieval = Semantic Search + Lexical Search
```

**Advantages**

* improves recall and precision
* captures both meaning and exact terminology
* commonly used in modern retrieval systems

Hybrid retrieval is an important component of our architecture.

---

## 6. Top-K Evidence Retrieval

After retrieving candidate passages, the system selects the most relevant ones.

### Recommended configuration

```
Top-K = 5 to 8 evidence passages
```

### Why this works

* enough evidence for synthesis
* prevents excessive context length
* improves LLM reasoning quality

---

## 7. Reranking

Reranking improves the relevance of retrieved evidence.

A reranker evaluates retrieved passages again and reorders them based on relevance.

### Recommended model

```
cross-encoder/ms-marco-MiniLM-L6-v2
```

### Advantages

* improves retrieval accuracy
* removes noisy passages
* provides higher-quality evidence to the LLM

### Disadvantages

* adds additional computational cost
* increases latency

---

## 8. Evidence Processing

Before generation, retrieved evidence must be processed.

### Tasks may include

* biomedical entity extraction
* filtering irrelevant passages
* extracting study information
* structuring evidence

### Example transformation

Raw text

```
Drug A reduced HbA1c by 1.2% in type-2 diabetes patients
```

Structured extraction

```
Intervention: Drug A
Population: Type-2 Diabetes
Outcome: HbA1c reduction
Result: 1.2%
```

### Benefits

* enables comparison across studies
* improves reasoning quality
* reduces noise for the LLM

---

## 9. LLM / SLM Architecture

We propose a **hybrid architecture combining SLMs and LLMs**.

```
SLM → structured extraction tasks
LLM → reasoning and synthesis
```

---

### 9.1 Role of SLMs

Small language models can perform:

* entity recognition
* PICO extraction
* evidence filtering
* structured data extraction

Examples:

* BioBERT
* SciBERT

**Advantages**

* domain-specific knowledge
* efficient inference
* suitable for structured tasks

---

### 9.2 Role of LLMs

Large language models perform:

* reasoning across multiple papers
* summarization
* insight generation
* explanation synthesis

### Recommended model

```
BioMistral
```

BioMistral is trained on biomedical literature and performs well in medical reasoning tasks.

**Advantages**

* strong biomedical knowledge
* open-source
* supports local inference

---

## 10. Prompt Templates

Prompt templates guide the LLM to produce structured outputs.

### Example Prompt

```
You are a biomedical research assistant.

Using only the retrieved evidence:

1. Summarize key findings
2. Compare results across studies
3. Provide citations
4. Present structured output
```

### Benefits

* reduces hallucinations
* ensures consistent formatting
* encourages evidence-based responses

---

## 11. Validation Layer

Generated answers must be verified before being returned.

### Possible validation techniques

* claim–evidence similarity scoring
* citation verification
* confidence estimation

### Benefits

* improves reliability
* prevents unsupported claims
* enhances transparency

---

## 12. Structured Output

Instead of plain text responses, the system generates structured research summaries.

### Example

| Study      | Population   | Outcome | Result |
| ---------- | ------------ | ------- | ------ |
| Smith 2022 | 200 patients | HbA1c   | −1.2%  |
| Lee 2023   | 150 patients | HbA1c   | −0.9%  |

Structured output improves readability and usability for researchers.

---

## 13. Evidence-to-Claim Traceability

Each claim in the generated answer should be supported by evidence.

### Example

Claim

```
Drug A significantly improves glycemic control
```

Evidence

```
Smith et al., 2022
Lee et al., 2023
```

### Benefits

* improves explainability
* reduces hallucination
* ensures research reliability

---

## 14. Implementation Frameworks

Several frameworks can help implement the system.

### LangChain

LangChain helps build RAG pipelines by connecting:

* document loaders
* chunking
* embeddings
* vector stores
* retrievers
* prompt templates
* language models

---

### LlamaIndex

LlamaIndex focuses on:

* document indexing
* retrieval pipelines
* query engines

---

### FAISS

Used for **vector similarity search**.

---

### Sentence Transformers

Used for:

* embedding generation
* reranking models

---

## 15. Implementation Steps

### Step 1 — Index Construction

* generate embeddings
* store embeddings in FAISS
* store metadata for citations

---

### Step 2 — Retrieval System

* implement semantic retrieval
* implement lexical retrieval
* combine into hybrid retrieval

---

### Step 3 — Evidence Selection

* retrieve candidate passages
* select Top-K evidence
* apply reranking if required

---

### Step 4 — Agent Reasoning

* feed retrieved evidence to LLM
* apply prompt templates
* generate evidence-based insights

---

### Step 5 — Validation

* verify evidence alignment
* compute confidence score
* confirm citation support

---

## 16. Pros and Cons of the Approach

### FAISS Index

**Pros**

* fast
* open source
* scalable

**Cons**

* manual metadata handling

---

### Hybrid Retrieval

**Pros**

* high retrieval accuracy
* robust to query variations

**Cons**

* more complex system

---

### SLM + LLM Architecture

**Pros**

* efficient task specialization
* improved reasoning accuracy

**Cons**

* increased architectural complexity

---

## 17. Innovation of the System

Our architecture introduces several improvements beyond standard RAG systems.

### Key innovations

1. Agentic multi-step reasoning pipeline
2. Hybrid retrieval (semantic + lexical search)
3. Evidence extraction before generation
4. Citation-grounded structured outputs
5. Evidence-to-claim traceability

These improvements make the system suitable for biomedical research applications.

---

## 18. Recommendation

The best approach for our project is to build an **Agentic Biomedical RAG System** with:

* FAISS vector indexing
* hybrid retrieval
* evidence processing
* LLM reasoning
* prompt-guided synthesis
* validation mechanisms
* citation-grounded outputs

This design:

* demonstrates **Agentic AI**
* runs locally with **zero cost**
* provides strong **research novelty**
* supports **evidence-based clinical research**.

---

# 19. RAG System Evaluation

## 19.1 Purpose of Evaluation

Evaluation measures how effectively the RAG system retrieves relevant biomedical evidence and generates accurate responses.

Evaluation helps determine:

* whether retrieval returns relevant documents
* whether generated answers are evidence-supported
* whether responses are useful for research

A proper evaluation ensures that the system is **scientifically validated rather than purely conceptual**.

---

## 19.2 Evaluation Components

The RAG system will be evaluated across three dimensions:

1. Retrieval Performance
2. Generation Quality
3. Human Evaluation

---

## 19.3 Retrieval Evaluation

Retrieval evaluation measures how well the system retrieves relevant biomedical evidence.

### Precision@K

Precision@K measures the proportion of retrieved documents that are relevant.

Example

```
Precision@5 = 3 / 5
```

**Advantages**

* simple to compute
* widely used in information retrieval

**Limitations**

* does not measure completeness

---

### Recall@K

Recall measures how many relevant documents were retrieved.

Example

```
Recall = 3 / 5
```

**Advantages**

* measures completeness of retrieval

**Limitations**

* requires knowledge of all relevant documents

---

### Mean Reciprocal Rank (MRR)

MRR evaluates how early the first relevant document appears.

Example

```
MRR = 1 / 2
```

**Advantages**

* measures ranking quality

**Limitations**

* considers only the first relevant result

---

## 19.4 Generation Evaluation

Generation evaluation measures the quality of responses produced by the LLM.

### Faithfulness

Faithfulness measures whether generated answers are supported by retrieved evidence.

Example

```
Drug A significantly reduces HbA1c levels in diabetic patients
```

If supported by retrieved literature, the answer is considered **faithful**.

---

### Answer Relevance

Measures whether the generated response directly addresses the query.

Example query

```
Effectiveness of statins in cardiovascular disease prevention
```

A relevant answer should discuss clinical outcomes and research evidence.

---

### Citation Accuracy

Citation accuracy measures whether cited papers support generated claims.

Example

```
Drug A reduced HbA1c by 1.2% (Smith 2022)
```

The cited paper should actually support the claim.

---

## 19.5 Hallucination Rate

Hallucination rate measures unsupported claims generated by the model.

Example

```
Hallucination Rate = Unsupported Claims / Total Claims
```

Reducing hallucination is critical for biomedical systems.

---

## 19.6 Human Evaluation

Human evaluation assesses system outputs manually.

### Evaluation criteria

* Relevance
* Evidence support
* Clarity and usefulness

Rating scale

1 - poor

5 - excellent

---

### Human Evaluation Procedure

1. Prepare **10–15 biomedical research queries**
2. Run queries through the RAG system
3. Collect generated responses
4. Ask **3–5 evaluators** to rate outputs
5. Compute average scores

Example evaluation table

| Query | Relevance | Evidence Support | Clarity |
| ----- | --------- | ---------------- | ------- |
| Q1    | 5         | 4                | 5       |
| Q2    | 4         | 4                | 3       |
| Q3    | 5         | 5                | 4       |

---

## 19.7 Baseline Comparison (Optional)

To demonstrate improvement, compare with a baseline system.

Baseline

```
LLM without retrieval
```

Proposed system

```
Hybrid Retrieval + RAG
```

Example results

| System     | Relevance | Evidence Support |
| ---------- | --------- | ---------------- |
| LLM Only   | 3.0       | 2.5              |
| RAG System | 4.3       | 4.1              |

---

## 19.8 Expected Outcome

The proposed system is expected to achieve:

* higher retrieval accuracy
* lower hallucination rate
* stronger evidence-grounded responses
* higher relevance scores

These results validate the effectiveness of the **agentic biomedical RAG architecture**.

---
