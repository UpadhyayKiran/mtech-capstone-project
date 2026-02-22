Title: Summarization and Simplification of Medical Articles using Natural Language Processing
Problem Statement: The paper addresses the challenge of improving health literacy by easing access to complex healthcare information by summarising medical texts and simplifying them lexically by translating specific medical terminology to laymen’s terms. 
Algorithms Used: Used 4 pretrained transformer-based models - ALBERT, DistilBERT, SciBERT, GPT-2 for extracting summaries from articles and another pretrained model - en_ner_bionlp13cg_md for Named Entity Recognition of the medical terms. Used Lemmatization for each medical entity and finally Web Scraping to generate a simplified meaning.
Datasets: Dataset of 400 medical articles taken from the Cochrane Database of Systematic Reviews (CDSR).
Model Training and Testing: In generated summary, the medical entities present in the summary are highlighted in green and their respective meaning is displayed to the user when he hovers over the highlighted word. ROUGE i.e. Recall-Oriented Understudy for Gisting Evaluation metric has been used to evaluate the summaries produced by the models.
Results: The compression rate of the models is 40%. Below figure shows a comparative analysis of the ROUGE scores obtained by the four chosen pretrained models.
 
Conclusions: Authors employ an extractive text summarization approach using ALBERT. Lexical simplification of the summary is done using Named Entity Recognition along with simplifying the complex words through web scraping.
Open Questions: The paper suggests future work on improving the paragraph summaries and identification of non-medical complex words and medical abbreviations.
Relevance to Our Team: The evaluations into the various transformer based models can guide our team in selecting appropriate models for text summarization which can help clinical researchers to quickly navigate and review documents.
Title: Extracting Health Evidence Information from Biomedical Literature using LLMs
Problem Statement: This article addresses the challenge of bridging the gap between research findings and real-world healthcare applications by exploring LLMs to enhance medical practice efficiency and advance evidence based medicine.
Algorithms Used:
- INSTRUCTOR and OpenAI for embeddings
- FAISS for storing vector embeddings in a knowledge base
- PICO Extraction Algorithm(User-Defined)
- Stuff for document processing
- Streamlit Framework to design an interface for user engagement
- LangChain for summarising complex PDFs
- RAG-based pipeline
- RAGAs for evaluation of retriever and LLMs
- OpenAI LLMs: GPT-3.5 turbo, GPT-4, GPT-4 turbo, and GPT-4o to generate responses

Datasets: 
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3952010/
https://link.springer.com/article/10.1208/s12249-021-02058-y 
https://www.thelancet.com/journals/landia/article/PIIS2213-8587(22)00387-4/abstract 
https://onlinelibrary.wiley.com/doi/full/10.1002/pst.2020 
https://www.sciencedirect.com/science/article/pii/S0753332223014488 

Model Training and Testing: Overall, 12 PICO queries were generated from the documents. These queries were then passed to each LLM to extract evidence using the PICO framework and answer the queries with the extracted evidence.
Results: The average performance of each LLM is detailed in below figure:
 
Conclusions: 
-	LLMs like GPT-4 and GPT-4 Turbo can effectively handle PICO-based queries in systematic medical reviews. 
-	The choice of embeddings significantly influences performance.
Open Questions: The predefined limits on context retrieval can result in incomplete information. Future work should aim to increase the context size to take full advantage of models like GPT-4 Turbo, even though this may come with higher costs which can be addressed by their fine-tuning.
Relevance to Our Team: This article is very relevant for our project as it caters to all the aspects of our objective and presents some challenges which we can work on.
