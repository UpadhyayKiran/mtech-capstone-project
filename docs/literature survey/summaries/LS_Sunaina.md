

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

Reference Link - https://pmc.ncbi.nlm.nih.gov/articles/PMC12407621/ ,
Year - 2025 ,
Author - Alon Gorenshtein,Mahmud Omar, et al.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

Reference Link - https://pmc.ncbi.nlm.nih.gov/articles/PMC11529424/,
Year - 2024,
Author - Xinzhi Yao , Zhihan He , Jingbo Xia 

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

Reference Link - https://www.sciencedirect.com/science/article/pii/S2666379125004471 ,
Year - 2025 ,
Fei Liu ,Yue Niu, et al.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

Reference Link - https://pmc.ncbi.nlm.nih.gov/articles/PMC3124652/,
Year - 2011,
Author - Patricia B Burns,Rod J Rohrich,Kevin C Chung

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# **Evidence-Based Medicine: Navigating Uncertainty** #
Problem Statement
Modern medicine faces significant challenges due to an overload of information and the critical need for well-founded clinical decision-making. This environment necessitates a structured approach to manage vast amounts of data and ensure that clinical practices are based on reliable evidence, rather than unfounded beliefs or unscientific practices .The paper aims to provide a systematic method to address uncertainties in daily clinical practice.

## **Algorithms Used** ##
This paper focuses on the methodological framework of Evidence-Based Medicine (EBM), which is a human-driven process for clinical decision-making. It does not describe specific computational algorithms in the context of data processing or machine learning. Instead, it outlines a five-step systematic method for clinicians to follow:
    • Formulating clinical questions,
    • Conducting efficient literature searches,
    • Critically appraising evidence,
    • Evaluating its applicability, and
    • Integrating knowledge into clinical practice.

## **Datasets** ##
The paper does not utilise or refer to specific datasets in the conventional sense of computational analysis. Instead, it refers to 'scientific sources' and 'literature' as the body of information that clinicians must navigate and critically appraise. The process involves searching databases like PubMed and considering tertiary and secondary sources.

## **Model Training and Testing** ##
This paper does not involve model training or testing, as it describes a methodological framework for clinical practice rather than a computational model. The 'training' aspect in this context refers to clinicians learning and applying the EBM steps, and 'testing' involves evaluating the appropriateness of clinical practices based on scientific evidence.

## **Results** ##
The paper presents the EBM framework as a structured and practical approach to improve health care by balancing care quality, efficiency, and resource management. It emphasises that EBM helps professionals make optimal, evidence-based decisions and avoid accepting conclusions without critical questioning. The framework aims to integrate evidence with clinical expertise and patient preferences.

## **Conclusion** ##
Evidence-based medicine offers a robust, five-step framework to navigate the uncertainties of modern medicine, ensuring clinical decisions are well-founded and patient-centered. It combines scientific rigour with practical application, emphasising critical appraisal and integration of evidence into practice. The paper also acknowledges the emerging role of artificial intelligence as a tool to enhance, but not replace, EBM processes, particularly in information retrieval and synthesis.

## **Relevance to Our Team** ##
This paper is highly relevant for our team involved in healthcare, research, or evidence synthesis, as it outlines a foundational approach to decision-making in a complex information environment. It provides a clear, systematic methodology for evaluating and applying scientific evidence, which is crucial for developing guidelines, conducting research, or informing clinical practice. The emphasis on critical appraisal and structured questioning can enhance the rigour and effectiveness of our work.

Reference Link - https://www.sciencedirect.com/science/article/pii/S2341287925002649,
Year - 2025,
Author - Rafael Martín-Masot a, Carlos Ochoa Sangrador,et al.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

# **Clinical Entity Augmented Retrieval (CLEAR) for Information Extraction** #

## **Problem Statement** #
Traditional large language models (LLMs) often struggle with inefficient retrieval and high token usage when extracting information from extensive clinical notes, leading to increased inference times and potential performance degradation due to long input lengths.
Existing retrieval-augmented generation (RAG) methods, while an improvement, still rely on embeddings that can be inefficient.

## **Algorithms Used** ##
The paper introduces Clinical Entity Augmented Retrieval (CLEAR), a RAG pipeline that utilises clinical entities for information retrieval. It involves
    • Named Entity Recognition (NER) utilised Flan-T5-XXL to identify clinical entities,
    • Bio+Clinical BERT for cosine similarity for filtering relevance to the input query, 
    • Ontologies (UMLS) to augmenting the list and
    • LLMs (GPT-4) to enhance sensitivity .

## **Datasets** ##
The study used two real-world EHR-derived datasets:
    • The Stanford Medication for Opioid Use Disorder (MOUD) dataset and t
    • The CheXpert dataset.
The MOUD dataset included 13 clinical variables related to substance use, mental health, and social determinants of health.
The CheXpert dataset focused on 5 variables from chest X-ray reports, such as cardiomegaly and pneumonia.

## **Model Training and Testing** ##
CLEAR's performance was compared against embedding RAG and full-note approaches across six LLMs. For fine-tuning, BERT-sized models were used, with the output of CLEAR serving as labels.The models were evaluated on information extraction tasks for 18 variables, and inter-rater reliability was assessed using Cohen's Kappa.

## **Results** ##
CLEAR achieved average F1 scores of 0.90, outperforming embedding RAG (0.86) and full-note approaches (0.79). It demonstrated a >70% reduction in token usage and inference time, with average inference times of 4.95 seconds per note compared to 17.41 seconds for embedding RAG and 20.08 seconds for full-note methods.

## **Conclusion** ##
CLEAR significantly improves clinical information extraction efficiency and performance by leveraging clinical entities for retrieval, leading to substantial reductions in token usage and inference time while maintaining or improving accuracy compared to modern RAG and full-note methods.

## **Relevance to Our Team** ##
This research offers a highly efficient and accurate method for clinical information extraction, which could be invaluable for teams working with large volumes of EHR data.The reduced token usage and inference time make it a practical solution for real-world clinical applications, potentially streamlining research, quality improvement, and predictive modelling efforts by providing a more affordable and scalable approach to processing clinical text.

Reference Link - https://www.nature.com/articles/s41746-024-01377-1#Sec8,
Year - 2025,
Author - Ivan Lopez,Akshay Swaminathan,Karthik Vedula, et al.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# **AI with Agency in a vision for adaptive, efficient, and ethical Healthcare** #

## **Problem Statement** ##
The healthcare industry faces significant operational challenges, including high administrative burdens, inefficiencies in patient care, resource allocation, and administrative processes, leading to increased costs and suboptimal patient outcomes. Current AI systems often rely on fixed rules, lacking the adaptability and autonomy needed to navigate the complexity of real-time healthcare environments. The core problem is the need for an intelligent system that can learn, evolve, and operate with autonomy to ease administrative burdens, support clinical decision-making, and streamline operations.

## **Algorithms Used** ##
The paper primarily discusses the application of agentic AI, which utilises machine learning (ML) algorithms to adapt to real-time healthcare environments. These systems are goal-driven and continuously update their behaviour based on new information.
Specific mention is made of AI-powered natural language processing and voice recognition technologies for medical transcription ,predictive models for patient risk identification, and AI-based monitoring systems for vital signs.
For surgical operations, robotic-assisted procedures are mentioned, with agentic robotic systems learning from sensor feedback to adjust actions dynamically.
The YOLOv5s model is noted for its effectiveness in clinical imaging tasks.

## **Datasets** ##
The paper implies the use of various healthcare datasets, including
routine data for continuous learning,
large datasets for training AI models in areas like sepsis detection ,claims data for identifying inconsistencies and fraud, historical admission rates, seasonal illness patterns, and external factors for predicting resource needs, patient history and genetic information for medication management, and imaging data for diagnostic purposes .
Real-time patient data and streaming patient data are crucial for agentic AI systems to refine treatment strategies and make dynamic adjustments.

## **Model Training and Testing** ##
Agentic AI systems are trained to continuously learn from routine data and adjust responses to evolving healthcare demands. They adapt their behaviour as new information comes in. This involves recalibrating detection thresholds over time based on behavioural data for mental health applications and autonomously learning from each new imaging dataset to improve interpretive accuracy. The systems are designed to continuously update their diagnostic models based on real-world clinical data.

## **Results** ##
Agentic AI offers significant benefits, including reducing human error, enhancing efficiency, streamlining workflows, and lowering administrative workload. It can lower cognitive workload by up to 52% and identify patients at risk, leading to fewer hospitalisations and better outcomes. In administrative tasks, AI-driven automation significantly reduces manual workloads and frees up time for direct patient care.
AI-powered CDSS has enhanced diagnostic accuracy, reduced medical errors, and improved patient outcomes, with systems leading to a 5% change in treatment decisions]. AI in diagnostic imaging has surpassed human radiologists in detecting certain diseases and improved tuberculosis screening. Economically, agentic AI has the potential to contribute significantly to the US healthcare system annually by optimising cost structures, reducing hospital readmissions, and automating administrative tasks.

## **Conclusion** ##
Agentic AI represents a transformative approach in healthcare, moving beyond static rules to create adaptive, autonomous systems that continuously learn and evolve. This shift is crucial for addressing the industry's complex challenges, improving efficiency, enhancing clinical decision-making, and reducing costs. By integrating autonomy and adaptability, agentic AI can optimise patient care, streamline operations, and foster a more patient-centered and financially sustainable healthcare system.

## **Relevance to Our Team** ##
For our team, the paper highlights the importance of developing AI systems that are not just automated but are agentic, capable of continuous learning and adaptation. This means focusing on models that can dynamically adjust to real-time data, personalize interventions, and proactively refine workflows. The emphasis on ethical considerations, explainability, and interoperability is also crucial for successful implementation and user trust.

Reference Link - https://pmc.ncbi.nlm.nih.gov/articles/PMC12092461/,
Year - 2025,
Author - Vasco Gerardo Hinostroza Fuentes, et al.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# **Biomedical Relation Extraction with GPT Models** #
## **Problem Statement** ##
Relation Extraction (RE) in the biomedical domain is a crucial Natural Language Processing (NLP) task focused on identifying semantic relationships between biomedical entities from large data collections like PubMed articles. The complexity of RE increases with the number of entities involved in a relation.
Traditional methods, including co-occurrence, rule-based, and early machine learning approaches, faced limitations such as false positives, low recall, and the need for extensive annotated data .This paper investigates the effectiveness of recent large language models (LLMs), specifically GPT-3.5-turbo and GPT-4, for this task.

## **Algorithms Used** ##
The study primarily utilised GPT-3.5-turbo and GPT-4, which are generative pre-trained transformer models, for relation extraction.
These models are pre-trained on large Web corpora using auto-regressive language modelling . The researchers developed various prompts for zero-shot and one-shot experiments to guide these models in classifying relations.

## **Datasets** ##
Three standard biomedical datasets were used: EU-ADR, Gene Associations Database (GAD), and ChemProt . For each dataset, three versions were created: masked entities, original unmasked entities, and expanded entities where abbreviations were replaced with full terms.

## **Model Training and Testing** ##
    • The models were tested using zero-shot and one-shot learning approaches with different prompts and temperature settings (0 and 1).
    • The chat completion model from the GPT API was used for the experimental setup.
    • Performance was evaluated using standard metrics like precision, recall, and F1-score, and compared against BioBERT and PubMedBERT .

## **Results** ##
GPT-3.5-turbo achieved F1-scores ranging from 0.498 to 0.809, while GPT-4 achieved a highest F1-score of 0.84 .GPT models performed better on unmasked and expanded data versions compared to masked versions .For certain experiments, GPT's performance was comparable to BioBERT and PubMedBERT .GPT-4 generally outperformed GPT-3.5-turbo, particularly on EU-ADR, GAD dataset 1, and ChemProt .

## **Conclusion** ##
The study successfully demonstrated the capability of GPT models (GPT-3.5-turbo and GPT-4) to perform biomedical relation extraction. It highlighted that GPT's performance is superior on unmasked and expanded data compared to masked data and that the models can achieve results comparable to specialized BERT-like models in some cases. The research provides a foundational understanding for using GPT for biomedical relation extraction.

## **Relevance to Our Team** ##
This research is highly relevant as it showcases the potential of large language models for complex biomedical NLP tasks. Understanding how GPT models perform with different data formats (masked vs. unmasked/expanded) and prompt engineering strategies can inform our team's approach to similar challenges. The findings suggest that fine-tuning GPT models or using zero-shot classification with embeddings could further enhance performance, providing clear directions for future work in leveraging LLMs for biomedical text processing.

Reference Link - https://pmc.ncbi.nlm.nih.gov/articles/PMC11141827/,
Year - 2024
Author - Jeffrey Zhang , Maxwell Wibert, et al.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# **Proof-of-concept study of a small language model chatbot for breast cancer decision support – a transparent, source-controlled, explainable and data-secure approach** #

## **Problem Statement** ##
Large Language Models (LLMs) offer promise for decision support in breast cancer care; however, their clinical use is restricted by concerns over source control, explainability of decision-making, and health data security. Small Language Models (SLMs) are being explored to address these challenges by providing transparent, source-controlled, explainable, and data-secure approaches.

## **Algorithms Used** ##
The study utilized an open-source SLM, specifically Mixtral 8×7B instruct, in an unquantified state. The technological design incorporates Retrieval-Augmented Generation (RAG) which introduces an upstream search engine to interact with a static information database, such as clinical guidelines . It employs a dual retrieval mechanism using AI-embedding techniques with cosine similarity and the BM25 algorithm, followed by a mutual re ranking module .

## **Datasets** ##
The models were evaluated using 20 fictional patient profiles that comprehensively represent the spectrum of breast carcinoma subtypes, adhering to the German Association of Gynecology and Obstetrics (DGGG) guideline (version 4.4, May 2021) . These profiles cover diverse immuno- and histopathological subtypes, as well as pre- and postmenopausal statuses.

## **Model Training and Testing** ##
Initial clinical accuracy was assessed by comparing the BC-SLM's treatment recommendations with those from a conventional multidisciplinary gynecological tumor board (considered the gold standard) . The BC-SLM was also compared against two publicly available LLMs, ChatGPT3.5 and 4.0. The study evaluated 100 binary treatment recommendations across five treatment modalities.

## **Results** ##
The BC-SLM achieved an overall concordance of 86% (κ=0.721, p<0.001) with the multidisciplinary tumor board, which is comparable to ChatGPT4 (90%, κ=0.820) and ChatGPT3.5 (83%, κ=0.661) . Specific concordance for the BC-SLM ranged from 65% to 100% across different treatment modalities .The BC-SLM demonstrated local functionality, adherence to guidelines, and provided referenced sections for its decision-making .

## **Conclusion** ##
The tailored BC-SLM shows promising initial clinical accuracy and technical functionality, offering a proof-of-concept for adapting SLMs to oncological guidelines. This approach ensures decision transparency, explainability, source control, and data security, marking a crucial step towards clinical validation and safe use of language models in clinical oncology .

## **Relevance to Our Team** ##
This study highlights the potential of SLMs, particularly with RAG, to address critical issues in clinical decision support like data security and explainability. The methodology of tailoring an open-source SLM to specific medical guidelines and achieving comparable accuracy to larger LLMs demonstrates a viable path for developing secure and transparent AI tools in healthcare. This is particularly relevant for teams focused on integrating AI into clinical workflows while maintaining high standards of data privacy and interpretability.

Reference Link -https://pmc.ncbi.nlm.nih.gov/articles/PMC11464535/#:~:text=Additionally%2C%20it%20achieves%20concordance%20levels,international%20diagnostic%20and%20treatment%20standards,
year - 2024
Author -Sebastian Griewing, Fabian Lechner ,et al

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# **Small language models learn enhanced reasoning skills from medical textbooks** #

## **Problem Statement** ##
Small Language Models (SLMs) face challenges in multi-step reasoning for complex medical tasks due to their limited parameters, despite their advantages in privacy and hardware constraints compared to Large Language Models (LLMs) . Existing medical SLMs often lack consistent reasoning abilities during pre-training, and current training methods are inefficient and yield limited improvements for medical reasoning.

## **Algorithms Used** ##
The study introduces Meerkat, a new family of medical SLMs, built upon state-of-the-art LMs like Mistral-7B and Llama-3-8B. The core algorithm involves an effective and efficient training method that extracts high-quality Chain-of-Thought (CoT) reasoning paths from medical textbooks and combines them with diverse instruction-following datasets.
GPT-4 was specifically used to generate CoT reasoning data from MedQA questions and medical textbooks.

## **Datasets** ##
The training dataset comprises 441K examples, including CoT reasoning paths extracted from 18 medical textbooks and diverse instruction-following datasets within the medical domain.
Key datasets include
    • MedQA-CoT (9.3K examples),
    • MedBooks-18-CoT (77.6K examples), and
    • MedMCQA,
    • LiveQA,
    • MedicationQA,
    • ChatDoctor-cleaned,
    • MedQA-dialog, and
    • MedInstruct-52K.
      
## **Model Training and Testing** ##
Fine-tuning was conducted on open-source SLMs using the curated dataset . The Meerkat models were initialised with Mistral-7B-v0.1 and Meta-Llama-3-8B-Instruct weights. The 7B model was trained for three epochs on eight A100 GPUs (approximately 1 day), and the 8B model on Google TPUs. Performance was tested across six exam datasets, including MedQA, USMLE, Medbullets-4/5, MedMCQA, and MMLU-Medical, and on NEJM Case Challenges.

## **Results** ##
Meerkat-7B and Meerkat-8B outperformed their counterparts by 22.3% and 10.6% across six exam datasets, respectively. Meerkat-7B was the first 7B model to exceed the USMLE passing threshold of 60%. Meerkat-8B improved scores on the NEJM Case Challenge from 13 to 20, surpassing the human score of 13.7 . Expert evaluations showed Meerkat-8B's superiority in completeness, factuality, clarity, and logical consistency.

## **Conclusion** ##
Meerkat models demonstrate robust reasoning capabilities, addressing the gap between performance and security for medical AI. The CoT fine-tuning approach, especially with textbook augmentation, is highly effective and efficient, enabling smaller models to tackle complex reasoning tasks . The models are suitable for on-premises deployment due to lower hardware requirements.

## **Relevance to Our Team** ##
This paper is highly relevant as it demonstrates an effective and efficient method for enhancing reasoning capabilities in SLMs for medical applications. The use of CoT reasoning paths from medical textbooks and diverse instruction-following datasets provides a robust framework for developing medical AI. The success of Meerkat models, particularly their ability to run on high-end PCs, makes them practical for deployment in various healthcare settings, aligning with the need for accessible and privacy-preserving AI solutions in medicine.

## **Open Questions** ##
1. What specific improvements are needed for performance?

2. How will reinforcement learning enhance medical SLMs?

3. What strategies address biases in medical AI?

Refernec Link - https://pmc.ncbi.nlm.nih.gov/articles/PMC12048634/#:~:text=Abstract,effective%20and%20efficient%20training%20method ,
Year - 2025 
Author - Hyunjae Kim , Hyeon Hwang, et al.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------
