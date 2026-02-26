

# **AI Agents in Clinical Medicine: A Systematic Review** #

## **Problem Statement:** #
Base Large Language Models (LLMs) perform well on medical exams but face safety issues in clinical settings, including hallucinations, misinformation (up to 22% error rate), and inability to perform multi-step reasoning with external data.
This systematic review evaluates whether AI agents—LLMs augmented with tools and/or multi-agent collaboration improve clinical task performance compared to standard LLMs.

## **Algorithms Used:** #
Single-agent tool-calling systems, multi-agent frameworks (3–10 agents), and hybrid architectures were analyzed.
Common frameworks included AutoGen and LangChain using ReAct-style reasoning. Tools included web search (PubMed), Retrieval-Augmented Generation (RAG), medical calculators, and EHR integration.

## **Datasets:** #
    1. Twenty peer-reviewed studies (2024–2025) were included.
    2. Evaluation datasets comprised clinical cases (16–302 cases), 5,120 MCQs, 4,058 exam questions, 10,000 calculation vignettes, 117 patient records, and genomic datasets.
    3. Many relied on synthetic or single-center data.

## **Model Training & Testing:** #
Most studies used comparative designs (80%), testing AI agents against baseline LLMs using accuracy-based metrics.
Risk of bias was assessed using QUADAS-AI criteria.
Results:
    • Median performance improvement was +36% (range 3.5–76%).
    • Single-agent tool systems showed highest median gain (+53%).
    • Optimal multi-agent performance occurred with 4–5 agents.

## **Conclusion & Relevance:** #
AI agents outperform base LLMs when architecture matches task complexity. The findings guide our team in designing structured, tool-augmented agent systems with careful validation.


# **Bio-regulatory Event Extraction using LLMs** #

## **Problem Statement:** ##
Traditional biomedical NLP(BioNLP) methods for extracting bio regulatory events face challenges such as cascading errors in multi-step text mining pipelines and limited topic coverage due to corpus constraints. There is a need for robust semantic understanding and extensive knowledge bases to overcome these issues, especially in low-resource domains like plant biology.

## **Algorithms Used:** ##
    • LLM’s using Kimi from Moonshot AI. 
    • Deep-learning based pipeline that utilizes BioBERT for Named Entity Recognition (NER)
    • Relation Extraction (RE),Conditional Random Field (CRF) and Softmax classification layers.
    • Prompt engineering is a key strategy for LLM application.
      
## **Datasets:** ##
A pre-developed rice-GARE (genetic alteration-caused regulatory events) annotation corpus serves as both prompt samples for the LLM and the golden dataset for evaluation. This corpus includes 4195 GARE records from 32,229 abstracts and 56,368 full-text articles related to rice literature, collected from PubMed and PubMed Central.

## **Model Training and Testing:** ##
The LLM (Kimi) was tested using a prompt engineering strategy, where raw sentences and task instructions were used to query the model. The conventional pipeline models were fine-tuned on the AGAC corpus. Evaluation involved comparing generated GAREs against a manually curated golden dataset of 70 records using precision, recall, and F1-score.

## **Results:** ##
The LLM-based method achieved comparable F1-scores to the AGAC-based pipeline, demonstrating higher precision (+0.14) but lower recall (-0.11). This suggests LLMs have potential to mitigate cascading errors and topic limitations, but may experience reduced loss rates with tightly constrained prompts.

## **Conclusion:** ##
LLMs show promising performance in bio-regulatory event extraction, particularly in semantic comprehension and knowledge base application, potentially surpassing traditional text mining pipelines. However, challenges remain in low-resource domains, computational cost, and the lack of theoretical metrics for prompt design.


## **Relevance to Our Team** ##
This paper is highly relevant as it explores the application of LLMs in a specialised biomedical NLP task, which aligns with our interest in leveraging advanced AI for scientific data extraction. The insights into LLM performance in low-resource domains, prompt engineering, and the comparison with traditional methods provide valuable guidance for developing similar solutions and addressing their inherent challenges.



# **Foundational Architecture for AI Agents in Healthcare** #

## **Problem Statement:** ##
Traditional AI in healthcare often consists of single-function algorithms lacking autonomy and contextual awareness, operating on isolated datasets. The paper addresses the need for a more advanced paradigm: medical AI agents that can manage complex tasks autonomously, adapt to changing scenarios, and integrate diverse data sources to revolutionise healthcare delivery.

## **Algorithms Used:** ##
Large Language Models (LLMs) and Vision Language Models (VLMs) for cognitive processing, reasoning, and decision-making.
Deep learning algorithms are also crucial for tasks like medical imaging analysis.

## **Datasets:** ##
    • Medical AI agents process vast amounts of diverse data, including
    • electronic health records (EHRs),
    • medical imaging (X-rays, MRI, CT scans),
    • laboratory results, genetic information,
    • patient histories and
    • real-time physiological data from wearable devices.

## **Model Training and Testing:** ##
Models can be pre-trained using open-source or proprietary models and then fine-tuned for specific medical contexts. Alternatively, models can be trained from scratch using tailored datasets.
Testing and validation involve in-silico simulations and real-world clinical trials to ensure safety, efficacy, and alignment with medical standards.

## **Results:** ##
Medical AI agents demonstrate significant potential across various clinical applications, including enhancing diagnostic accuracy, personalising treatment, guiding robotic surgery, and real-time patient monitoring.
They can identify subtle patterns, reduce human error, and adapt to evolving medical knowledge, leading to more precise, efficient, and equitable patient care.

## **Conclusion:** ##
Medical AI agents represent a transformative shift in healthcare, offering enhanced efficiency and patient outcomes.Their successful integration requires navigating technical, ethical, and regulatory challenges, emphasising the need for continuous learning, robust validation, and careful consideration of human-agent interaction and data privacy.

## **Relevance to Our Team** ##
This paper is highly relevant as it outlines a foundational architecture for AI agents in healthcare, which aligns with our goals of developing intelligent systems for medical applications.
The emphasis on multimodal data integration, autonomous decision-making, and adaptive learning provides a roadmap for designing robust and context-aware AI solutions.
Understanding the challenges in implementation, such as data privacy, ethical considerations, and regulatory adaptation, is crucial for our team's strategic planning and development efforts.



# **The Levels of Evidence and their role in Evidence-Based Medicine** #

## **Problem Statement:** ##
Evidence-Based Medicine (EBM) uses a hierarchical system, known as levels of evidence, to guide clinical decisions. Physicians are encouraged to seek the highest level of evidence, but plastic surgery has historically shown a lack of higher-level evidence, necessitating an understanding of these levels for improvement.

## **Algorithms Used:** ##
Different organisations have adapted classification systems for levels of evidence based on research questions (e.g., treatment, prognosis) .
Randomised Controlled Trials (RCTs) are generally ranked highest due to their unbiased design, while case series or expert opinions are lowest . Grading systems, like ASPS's Grade Practice Recommendations, provide strength of recommendations based on evidence levels.

## **Datasets:** ##
The article is a conceptual and narrative review. It uses published surgical studies and clinical examples (e.g., silicone breast implants and lymphoma, epinephrine use in fingers) to illustrate levels of evidence.

## **Results and Implications:** ##
While levels of evidence provide a guide, the designated level doesn't always guarantee research quality; even RCTs require scrutiny for proper conduct . Plastic surgery has seen an increase in Level 1 studies but still has room to improve quality . Lower-level evidence, such as case reports, is crucial for hypothesis generation and can lead to more controlled studies, and should not be discarded.

## **Conclusion:** ##
Understanding levels of evidence is vital for EBM, helping prioritise information. However, caution is needed as Level 1 evidence isn't always superior, and lower levels can still be valuable.

## **Relevance to Our Team:** ##
This framework helps us critically appraise research, strategically design studies, and focus on improving research quality by incorporating proper methodologies.








