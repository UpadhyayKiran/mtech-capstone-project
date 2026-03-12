**1.RAG-Enhanced Open SLMs for Hypertension Management Chatbots**
https://pmc.ncbi.nlm.nih.gov/articles/PMC12615560/#:~:text=Finally%2C%20deploying%20healthcare%20chatbots%20requires,for%20patient%20interactions%20%5B8%5D
Gianluca Aguzzi , Matteo Magnini
•	Problem Statement: Chronic disease management, specifically hypertension, requires continuous monitoring and high adherence to therapy. While Large Language Models (LLMs) can power supportive chatbots, they present privacy risks by storing sensitive data on third-party servers and require high computational power.
•	Algorithms Used: The researchers implemented Retrieval-Augmented Generation (RAG) to enhance Small Language Models (SLMs). Retrieval methods included Vector Search (using cosine similarity), BM25 (keyword-based), Hybrid Search, and LLM-based Reranking.
•	Datasets: The study used an initial set of 315 human-to-physician conversations about hypertension. This was augmented using GPT-4 to create a final dataset of 1,473 QA records.
•	Model Training & Testing: Eight open-source SLMs (e.g., Gemma 3, Qwen 3, Llama 3.2) were tested in three configurations: Role-playing, Full-context, and RAG-based. Testing utilized the RAGAS framework to generate 21 complex evaluation samples.
•	Results: RAG generally improved response quality over SLM-only baselines, with significant performance gains for models like Gemma 3. However, newer models like Qwen 3 performed strongly even without retrieval.
•	Conclusion & Relevance: RAG-enhanced SLMs provide a privacy-preserving, computationally efficient solution for local deployment on patient devices. While RAG is effective, rapidly advancing SLM architectures may eventually reduce the need for complex retrieval mechanisms.

2.Benchmarking Retrieval-Augmented Generation for Medicine
https://aclanthology.org/2024.findings-acl.372.pdf
Authors: Guangzhi Xiong, Qiao Jin, Zhiyong Lu, Aidong Zhang Univeristy of Virginia
Problem Statement
Large Language Models (LLMs) often suffer from hallucinations and outdated knowledge in high-stakes medical fields. While Retrieval-Augmented Generation (RAG) is a promising solution, the lack of best practices for its modular components—corpora, retrievers, and LLMs—hinders its optimal medical adoption.
Algorithms Used
The study introduces MEDRAG, a toolkit featuring:
•	Retrievers: Lexical (BM25) and semantic models (Contriever, SPECTER, MedCPT).
•	Fusion: Reciprocal Rank Fusion (RRF) to combine multiple retrievers.
•	Generation: Chain-of-Thought (CoT) prompting to leverage LLM reasoning.
Datasets
The authors proposed MIRAGE, a benchmark of 7,663 questions from five medical datasets:
•	Examination: MMLU-Med, MedQA-US, and MedMCQA.
•	Research/Literature: PubMedQA* and BioASQ-Y/N.
•	Corpora: PubMed, StatPearls, Textbooks, Wikipedia, and a combined "MedCorp".

Model Training & Testing
Testing focused on zero-shot, multi-choice, and question-only retrieval (where options are withheld during retrieval) . Six LLMs were evaluated, including general (GPT-4, Mixtral) and domain-specific models (MEDITRON, PMC-LLaMA).

Results
•	MEDRAG improved accuracy by up to 18% over baseline CoT prompting.
•	GPT-3.5 and Mixtral with RAG achieved performance comparable to GPT-4.
•	PubMed was the most robust single corpus, while combined corpora (MedCorp) yielded the best overall results.
Conclusion & Relevance
The research provides the first systematic benchmark for medical RAG, demonstrating that RAG is a flexible, cost-efficient alternative to large-scale pre-training. It identifies a log-linear scaling property and "lost-in-the-middle" effects, offering practical guidelines for future medical AI deployments.

3.Medical LLMs: Fine-Tuning vs. Retrieval-Augmented Generation
https://pmc.ncbi.nlm.nih.gov/articles/PMC12292519/#:~:text=To%20enable%20efficient%20inference%2C%20we,in%20medical%20question%2Danswering%20applications
Bhagyajit Pingua , Adyakanta Sahoo 
Problem Statement
Large language models (LLMs) trained on general datasets often lack the specialized knowledge required for niche domains like healthcare. For medical applications, ensuring answers are accurate, reliable, and contextually relevant is critical to prevent dangerous misinformation. This study aims to evaluate the most effective methods—fine-tuning (FT) versus Retrieval-Augmented Generation (RAG)—to tailor LLMs for medical question-answering.

Algorithms Used
The researchers employed three primary methodological approaches:
•	Fine-Tuning (FT): Updating internal model parameters using domain-specific data.
•	Retrieval-Augmented Generation (RAG): Leveraging external knowledge at inference time without modifying model weights.
•	Hybrid (FT+RAG): Applying RAG on top of a previously fine-tuned model.
•	Optimization: Models were 4-bit quantized using the Unsloth library to reduce memory usage.

Datasets
The study utilized MedQuAD (Medical Question Answering Dataset), which contains 47,457 expert-checked question-answer pairs. The data spans 5,126 medical focus areas, including oncology, cardiology, and infectious diseases.

Model Training & Testing
Five LLMs were evaluated: Llama-3.1-8B, Gemma-2-9B, Mistral-7B-Instruct, Qwen2.5-7B, and Phi-3.5-Mini-Instruct. Fine-tuning was performed for one epoch using the SFTTrainer with a learning rate of $2 \times 10^{-4}$. RAG was implemented using ChromaDB as a vector database and a recursive text splitter with a 500-token window.

Results
•	Top Performer: LLAMA-3.1-8B emerged as the best overall model, showing superior consistency across lexical and semantic metrics.
•	Method Efficacy: RAG alone and the hybrid FT+RAG approach consistently outperformed standalone FT across most models.
•	Metric Gains: LLAMA's accuracy improved by up to 18% over baseline methods, achieving a BERTScore F1 of 0.891.
•	Model Specifics: PHI demonstrated the lowest perplexity when fine-tuned, while QWEN showed minimal progress regardless of the method.
Conclusion & Relevance
The research concludes that RAG is the most effective and computationally efficient adaptation strategy for medical LLMs. While the hybrid FT+RAG method offers synergistic advantages for models like PHI, RAG's simplicity makes it ideal for dynamic healthcare settings where accuracy and up-to-date knowledge are paramount

4.Evaluating Retrieval-Augmented Generation vs Long-Context Input for Clinical Reasoning over EHRs
https://arxiv.org/pdf/2508.14817
Skatje Myers1;Dmitriy Dligach;
•  Problem Statement: Clinicians face "note bloat" in Electronic Health Records (EHRs), which are often noisy, redundant, and can exceed 200,000 words. While Large Language Models (LLMs) can assist, the volume of documentation often exceeds their context windows, and simply providing recent notes risks omitting critical historical information.
•  Algorithms Used: The study implemented a RAG pipeline using BGE-en-large-v1.5 for embedding 128-token chunks. It utilized cosine similarity to retrieve the top-N (20, 40, 60) relevant passages. LLMs tested included o4-mini, GPT-4o-mini, and DeepSeek-R1.
•  Datasets: The researchers constructed datasets from 200 inpatient hospitalizations at a US hospital for three tasks: extracting imaging procedures, generating antibiotic timelines, and identifying key diagnoses.
•  Model Training & Testing: Performance was evaluated using F1 scores or Jaccard index across varying token budgets (3K to 128K). RAG was compared against baselines of "recent notes" and full-context processing.
•  Results: RAG achieved near-parity with full-context models (up to 128K tokens) while using only a fraction of the input tokens. Performance was highest in extractive tasks like imaging but plateaued in complex reasoning tasks like antibiotic timelines.
•  Conclusion & Relevance: RAG remains a competitive and efficient solution for longitudinal EHR reasoning, even as LLM context windows expand, by significantly reducing computational costs without sacrificing accuracy.

5.Federated knowledge retrieval elevates large language model performance on biomedical benchmarks
Federated knowledge retrieval elevates large language model performance on biomedical benchmarks | GigaScience | Oxford Academic
Janet Joy, Andrew I. Su
•  Problem Statement: While large language models (LLMs) have advanced biomedical natural language processing, they rely on implicit statistical patterns, leading to "hallucinations"—factually incorrect but syntactically fluent outputs. Such inaccuracies pose significant risks in high-stakes biomedical contexts by misdirecting research or compromising patient safety.
•  Algorithms Used: The researchers developed BioThings Explorer-Retrieval-Augmented Generation (BTE-RAG). This framework uses zero-shot entity recognition, executes query-focused graph traversals via the BTE API federation, and employs S-PubMedBert-MS-MARCO for similarity-based context pruning.
•  Datasets: Three specialized mechanistic benchmarks were created from DrugMechDB, a curated knowledge base of 5,666 expert-annotated pathways. These targeted gene-centric (798 questions), metabolite-centric (201), and drug-centric (842) mechanisms. The GeneTuring gene-disease association benchmark was also used.
•  Model Training & Testing: BTE-RAG was tested using GPT-4o and GPT-4o-mini. Performance was compared against "LLM-only" baselines and established frameworks like GeneGPT.
•  Results: BTE-RAG significantly improved accuracy. On the gene-centric task, it increased accuracy from 51% to 75.8% for GPT-4o-mini. In metabolite-focused questions, high-similarity response proportions rose by over 77% for both models.
•  Conclusion & Relevance: Federated knowledge retrieval provides transparent accuracy gains, establishing BTE-RAG as a practical tool for reducing hallucinations and enhancing mechanistic clarity in translational biomedical research.
6.Retrieval-Augmented Generation in Medicine: A Scoping Review of Technical Implementations, Clinical Applications, and Ethical Considerations 
https://arxiv.org/pdf/2511.05901
Rui Yang, Matthew Yu Heng
•  Problem Statement: Large language models (LLMs) face significant clinical hurdles, including static training data that cannot keep pace with rapidly evolving medical knowledge, a tendency for hallucinations (content without factual grounding), and a lack of explainability. Furthermore, they cannot access private patient data, which is essential for personalized treatment.
•  Algorithms Used: Research primarily utilizes "Naive RAG" (index-retrieve-generate pipeline). Retrieval is dominated by dense retrieval (84.38%), often using general embedding models like OpenAI’s text-embedding series or medical-specific ones like BioBERT and MedCPT. Sparse (BM25) and hybrid retrieval methods are used less frequently.
•  Datasets: Studies rely heavily on public data (80.35%), primarily biomedical scientific corpora (e.g., PubMed) and clinical guidelines. Other sources include online info, electronic health records (EHRs), and medical textbooks.
•  Model Training & Testing: Evaluations are split between automated metrics—assessing linguistic quality (ROUGE, BLEU) and task performance (accuracy, F1 score)—and human evaluations focusing on factual accuracy, relevance, and clinical utility.
•  Results: RAG is mostly applied to question answering, report generation, and text summarization. While technical reliability is improving, there is an imbalance in evaluation, with very few studies addressing bias (2.79%) or safety (9.56%).
•  Conclusion & Relevance: Medical RAG is in its early stages. To achieve trustworthy clinical implementation, advances are needed in rigorous clinical validation, cross-linguistic adaptation for non-English settings, and robust ethical oversight.
7.EHRNoteQA: AnLLMBenchmarkfor Real-World Clinical Practice Using Discharge Summaries
https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf
Sunjun Kweon, Jiyoun Kim
•  Problem Statement: Extracting vital information from Electronic Health Records (EHR) discharge summaries is challenging for clinicians due to the extreme length and complexity of notes, especially when they accumulate across multiple patient admissions. Existing benchmarks fail to reflect real-world clinical inquiries because they typically focus on single notes or narrow, predefined topics.
•  Algorithms Used: Researchers utilized GPT-4 for initial data generation and as an automated evaluator. They evaluated 27 Large Language Models (LLMs), including the GPT series (GPT-3.5, GPT-4) and 24 open-source models like Llama2, Llama3, and Mistral.
•  Datasets: The benchmark is built on the MIMIC-IV database, comprising 962 QA pairs linked to distinct patients. It covers ten diverse clinical topics, such as etiology, treatment, and test results.
•  Model Training & Testing: Models were tested on two levels: Level 1 (under 3,000 tokens) and Level 2 (3,000–7,000 tokens) to assess performance across varying context lengths. Evaluation involved both multi-choice and open-ended formats.
•  Results: Performance generally declined as note length and the number of admissions increased. Llama3-70b-Instruct performed close to GPT-4, which achieved the highest scores.
•  Conclusion & Relevance: EHRNoteQA is a superior proxy for expert evaluation compared to other benchmarks, showing high correlation with manual clinician assessments. It is publicly available to help develop more reliable clinical QA agents
8.Extracting PICO Sentences from Clinical Trial Reports using Supervised Distant Supervision
https://jmlr.org/papers/volume17/15-404/15-404.pdf
Byron C. Wallace, Jo¨el Kuiper, Benjamin M. Marlin;C. David Page;Suchi Saria
Problem Statement: Systematic reviews are essential for Evidence-Based Medicine, but the "data deluge" of clinical trials makes them onerous to produce. Identifying Population, Intervention, Comparator, and Outcome (PICO) elements in full-text reports is a critical, time-consuming task currently performed by highly-trained individuals.
Algorithms Used: The researchers proposed a novel Supervised Distant Supervision (SDS) model. This approach uses regularized logistic regression to learn a mapping that filters noisy distant supervision using a small amount of manual direct supervision.
Datasets: The model exploits the Cochrane Database of Systematic Reviews (CDSR), which contains summaries for over 50,000 clinical trials. The study utilized 12,808 linked full-text articles.
Model Training & Testing: The researchers derived distant supervision by soft-labeling sentences most similar to CDSR summaries. They manually labeled 2,821 candidate sentences from 133 articles to provide direct supervision and enable proxy evaluation.
Results: The SDS approach consistently outperformed baselines that relied only on distant supervision or small sets of direct supervision. It also matched or exceeded the performance of existing models for jointly learning from both supervision types.
Conclusion & Relevance: SDS effectively capitalizes on large, "free" distantly labeled datasets while using minimal manual effort to reduce noise. This technology can semi-automate data extraction, helping Evidence-Based Medicine keep pace with newly published evidence
9.NimbleLabs: Accelerating Healthcare AI Development Through Agentic AI
https://www.preprints.org/frontend/manuscript/4a73196aabc7b1e4eb49749b4bfd4453/download_pub
Soorya Ram Shimgekar , Abhay Goya
Problem Statement: Extracting insights from unstructured healthcare data is a major bottleneck, often consuming up to 80% of a data scientist's time. Current solutions are typically clinician-facing and do not produce machine-ready datasets, forcing manual data-wrangling and increasing costs.
Algorithms Used: The system utilizes a multi-agent architecture featuring six specialized agents. Key technologies include the Magika library for file classification, Google's MedGemma (a vision language model) for medical image interpretation, and Gemini-2.0-Flash for semantic enrichment and summarization.
Datasets: Evaluation was conducted on two distinct datasets: Hospice and Palliative Care Evaluation (HOPE) tabular data for anxiety level classification and an annotated compilation of colonoscopy video sequences (CVC-ColonDB, GLRC, and KUMC) for polyp detection.
Model Training & Testing: The framework automates the machine learning pipeline by identifying features, enriching them with external documentation, and optimizing input-output sets based on user intent. It recommends model architectures, hyperparameters, and preprocessing protocols through a Modeling Advisory Agent.
Results: Preliminary benchmarking indicates that workflows once requiring hours of expert labor can now be completed in minutes. This system potentially reduces operational costs by up to 22% and accelerates project initiation by ten times.
Conclusion & Relevance: NimbleLabs democratizes medical AI development by lowering technical barriers for institutions without specialized engineering teams. It provides a scalable, domain-specific solution for transforming heterogeneous healthcare data into actionable research insights.
Automated Clinical Trial Data Analysis and Report Generation by Integrating Retrieval-Augmented Generation (RAG) and Large Language Model (LLM) Technologies
https://www.researchgate.net/publication/394896953_Automated_Clinical_Trial_Data_Analysis_and_Report_Generation_by_Integrating_Retrieval-Augmented_Generation_RAG_and_Large_Language_Model_LLM_Technologies
Sheng-Ming Kuo, Shao-Kuo Tai
Problem Statement: Following clinical trials, manual statistical analysis and report drafting create major bottlenecks, typically requiring three months to complete. Traditional workflows struggle with the massive scale of heterogeneous data (millions of records) and the high reliability required for medical decision-making. Large Language Models (LLMs) alone often suffer from hallucinations and limited real-world grounding.
Algorithms Used: The study employs a hierarchical Retrieval-Augmented Generation (RAG) pipeline integrated with a Llama-3 8B-Instruct backbone. Optimization includes LoRA/QLoRA parameter-efficient fine-tuning and GRPO (Guided Reinforcement with Policy Optimization) for clinical alignment.
Datasets: The system uses historical data from a Taiwanese healthcare system, including tens of thousands of EHR encounters, one million National Health Insurance (NHI) claims, and over ten thousand DICOM imaging sets.
Model Training & Testing: The model was trained using FastLanguageModel with a de-identified corpus of 100k segments. Testing utilized a 50% corpus split, evaluating retrieval recall, factual consistency, and end-to-end latency.
Results: The system achieved a Composite Quality Index (CQI) of 78.3, outperforming Med-PaLM 2 (72.6). It reduced report drafting time by over 75% ($p<0.01$).
Conclusion & Relevance: The integrated RAG-LLM framework is a feasible solution for fully automated clinical reporting. It significantly reduces human workload and errors while ensuring high factual traceability in multi-site healthcare environments.




















