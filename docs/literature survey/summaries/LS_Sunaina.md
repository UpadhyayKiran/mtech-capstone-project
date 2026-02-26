

Title. AI Agents in Clinical Medicine: A Systematic Review

Problem Statement:
Base Large Language Models (LLMs) perform well on medical exams but face safety issues in clinical settings, including hallucinations, misinformation (up to 22% error rate), and inability to perform multi-step reasoning with external data.
This systematic review evaluates whether AI agents—LLMs augmented with tools and/or multi-agent collaboration improve clinical task performance compared to standard LLMs.

Algorithms Used:
Single-agent tool-calling systems, multi-agent frameworks (3–10 agents), and hybrid architectures were analyzed.
Common frameworks included AutoGen and LangChain using ReAct-style reasoning. Tools included web search (PubMed), Retrieval-Augmented Generation (RAG), medical calculators, and EHR integration.

Datasets:
    1. Twenty peer-reviewed studies (2024–2025) were included.
    2. Evaluation datasets comprised clinical cases (16–302 cases), 5,120 MCQs, 4,058 exam questions, 10,000 calculation vignettes, 117 patient records, and genomic datasets.
    3. Many relied on synthetic or single-center data.

Model Training & Testing:
Most studies used comparative designs (80%), testing AI agents against baseline LLMs using accuracy-based metrics.
Risk of bias was assessed using QUADAS-AI criteria.
Results:
    • Median performance improvement was +36% (range 3.5–76%).
    • Single-agent tool systems showed highest median gain (+53%).
    • Optimal multi-agent performance occurred with 4–5 agents.

Conclusion & Relevance:
AI agents outperform base LLMs when architecture matches task complexity. The findings guide our team in designing structured, tool-augmented agent systems with careful validation.
